##
# Execute command in podman container
# Based on https://github.com/containers/ansible-podman-collections/blob/main/plugins/module_utils/podman/common.py
# GPL v3.0+
##

from __future__ import absolute_import, division, print_function
__metaclass__ = type

FORGEJO_EXE_PATH = "/app/gitea/forgejo-cli"
TOKEN_TYPES = set(["INTERNAL_TOKEN", "JWT_SECRET", "LFS_JWT_SECRET", "SECRET_KEY"])

#"podman exec --user 1000 -it forgejo /app/gitea/forgejo-cli help"

import re

def run_forgejo_cli(module, args=[], executable='podman', container="forgejo", user_id=1000, expected_rc=0, ignore_errors=False):
    """Execute a command using the forgejo CLI"""

    command = [ executable,
                "exec",
                "--user", str(user_id),
                "-it", container,
                FORGEJO_EXE_PATH
               ]

    # command arguments
    if args is not None:
        command.extend(args)

    # execute commands
    rc, out, err = module.run_command(command)
    if not ignore_errors and rc != expected_rc:
        module.fail_json(
                msg='Failed to run "{args}" [exit={rc}]: {out} {err}'.format(args=" ".join(args), rc=rc, err=err, out=out))

    # return outputs
    return rc, out, err


def generate_token(module, token_type):
    """Generate a secret token using the executable."""

    # validate the token type
    if token_type not in TOKEN_TYPES:
        return None

    rc, token_str, err = run_forgejo_cli(module, args=["generate", "secret", token_type])
    return token_str


def create_ldap(module, hostname, search_base,
                *,
                port = 636,

                security_protocol="starttls",

                # user filter
                user_filter="(&(objectClass=posixAccount)(|(uid=%[1]s)(mail=%[1]s)))",

                # bind account
                bind_dn=None,
                bind_pass=None,

                # FreeIPA defaults
                attr_username="uid",
                attr_email="mail",
                attr_firstname="givenName",
                attr_surname="sn",

                # FreeIPA settings
                name="freeipa" ):
    """Create LDAP connection."""
    args = [
        "--name", name,
        "--host", hostname,
        "--port", str(port),
        "--user-search-base", search_base,

        # user filters
        "--user-filter", user_filter,
        "--security-protocol", security_protocol,

        # ldap attributes
        "--username-attribute", attr_username,
        "--email-attribute", attr_email,
        "--firstname-attribute", attr_firstname,
        "--surname-attribute", attr_surname
    ]

    if bind_dn:
        args += ["--bind-dn", bind_dn, "--bind-password", bind_pass]

    rc, out, err = run_forgejo_cli(module, args=["admin", "auth", "add-ldap"] + args)
    return {}


def get_auth_sources(module): 
    rc, out, err = run_forgejo_cli(module, args=["admin", "auth", "list"])

    sources = []
    for line in out.split("\n"):
        parts = line.split("\t")
        sources.append(parts)

    return sources


def create_user(module, username, email, password=None, admin=True):
    """Create a user account using the command line."""
    args = [
            "--username", username,
            "--email", email
    ]

    # handle password
    if password is None:
        args.append("--random-password")
    else:
        args += ["--password", password]
        
    # handle admin
    if admin:
        args.append("--admin")

    rc, out, err = run_forgejo_cli(module, args=["admin", "user", "create"] + args)
    
    # return code 1 = error
    if rc == 1:
        if out.contains('Command error: CreateUser: user already exists'):
            return {
                    'username': username,
                    'email': email,
                    'password': None,
                    'admin': admin,
                    'changed': True
            }
        return None

    # grab the password if we asked for a random password
    if password is None:
        m = re.search(r"generated random password is '(\w+)'", out)
        if m:
            password = m.group(1)

    # account details
    return {
        'username': username,
        'email': email,
        'password': password,
        'admin': admin,
        'changed': True
    }

