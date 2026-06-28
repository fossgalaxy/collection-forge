# Forgejo

[Forgejo](https://forgejo.org/) is a FOSS development forge with a feature set and appearance close to GitHub.

## Database Setup

Although the playbook can manage the database creation for you, you need to provide a suitable password
for the database account:

```yaml
# assumed to be running on container host by default
#forgejo_db_host: "host.containers.internal"
forgejo_db_password: 
```

Note: the assumption is that a postgres server is available (ie, via another role). Internally we use our
infra playbooks to do this.

## Secrets

You must provide the usual suite of forgejo secrets for the playbook:

```yaml
# forgejo generate secret SECRET_KEY
forgejo_secretkey: 
# forgejo generate secret INTERNAL_TOKEN
forgejo_internal_token: 

# forgejo generate secret JWT_SECRET (twice)
forgejo_jwt_oauth: 
forgejo_jwt_lfs: 
```

In the future, I'm hopeful the playbook might be able to do this for you, but it's a manual process for the
time being. Setting these rather than let forgejo generate them on first runs is important as we rebuild the
configuration file if the playbook options change.

## User Logins

The playbook disables the 'install' script in the web browser, although it can provision an account for you.

```yaml
# default user account name is ansible
forgejo_admin_user: ansible
forgejo_admin_pw:
```

### SSO (OpenID connect)
The playbook is designed to be usable with OpenID connect SSO providers (ie, keycloak).
You can provision your own oid values and provide the secret to the playbook, or you can
use the keycloak integration to provision the client for you.

```yaml
# replace realm_name with your realm name
forgejo_oid_meta_url: https://auth.example.com/realms/realm_name/.well-known/openid-configuration

# user provided oid values
#forgejo_oid_provider_name: freeipa
#forgejo_oid_client:
#forgejo_oid_secret:

# if using internal certs, uncomment the following line to inject the FreeIPA CA cert from the host
# forgejo_inject_cert: true
```
