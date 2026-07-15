Forgejo (FOSS Galaxy)
=========

An Ansible role for deploying Forgejo, based around Podman and PostgreSQL.

Requirements
------------

This role assumes you have the following already:

* Podman server
* PostgreSQL Server

For our purposes, we deploy PostgreSQL on the host and access it from the container. If you are not doing this
you will need to set up a PostgreSQL container and alter the `forgejo_db` variables accordingly. The
playbook can also manage the user and database (assuming the 'postgres on host' setup) - if you are
not doing this turn the db management feature off.

Role Variables
--------------

There are variables which must be set for this playbook to work correctly:

```
forgejo_db_password: db_password
forgejo_domain: domain name

# secrets
forgejo_secret_key: secret key
forgejo_internal_token: token
forgejo_jwt_lfs: jwt token
forgejo_jwt_oauth: jwt token
```

There are also variables to customise how Forgejo is deployed. The customisation directory is deployed into
`srv` so files can be added there as needed (this playbook can copy them across for you as well).

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: apps.example.com
  roles:
    - role: fossgalaxy.infra.container_host
    - role: fossgalaxy.forge.forgejo
      vars:
        forgejo_db_host: "psql.example.com"
        forgejo_db_pw: "{{ vault_forgejo_db_pw }}"
        forgejo_secretkey: "{{ vault_forgejo_secretkey }}"
        forgejo_internal_token: "{{ vault_forgejo_internal_token }}"
        forgejo_jwt_oauth: "{{ vault_forgejo_jwt_oauth }}"
        forgejo_jwt_lfs: "{{ vault_forgejo_jwt_lfs }}"
        forgejo_admin_pw: "{{ vault_forgejo_admin_pw }}"
        #forgejo_oid_meta_url: "{{ homelab_autodiscover_url }}"
        #forgejo_inject_cert: true
        #forgejo_oid_secret: "{{ vault_forgejo_oid_secret }}"
```

Note - you do not need to use our container host role if your host is already being managed as a Podman server some other way. The role will set up Forgejo using quadlets. You
may need to make changes to the bind mount locations if you do though.

License
-------

MIT

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
