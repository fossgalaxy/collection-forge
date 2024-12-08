Forgejo (FOSS Galaxy)
=========

An ansible role for deploying Forgejo, based around podman and postgres.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

This role assumes you have the following already:

* Podman server
* Postgresql Server

For our purposes, we deploy postgres on the host and access it from the container. If you are not doing this
you will need to set up a postgres container and alter the `fg_forgejo_db` variables accordingly. The
playbook can also manage the user and database (assuming the 'postgres on host' setup) - if you are
not doing this turn the db management feature off.

Role Variables
--------------

There are variables which must be set for this playbook to work correctly:

```
fg_forgejo_db_password: db_password
fg_forgejo_domain: domain name

# secrets
fg_forgejo_secret_key: secret key
fg_forgejo_internal_token: token
fg_forgejo_jwt_lfs: jwt token
fg_forgejo_jwt_oauth: jwt token
```

There are also variables to customise how forgejo is deployed. The customisation directory is deployed into
`srv` so files can be added there as needed (this playbook can copy them across for you as well).

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

MIT

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
