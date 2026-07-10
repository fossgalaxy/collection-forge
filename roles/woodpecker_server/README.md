Woodpecker CI (FOSS Galaxy)
=========

An Ansible role for deploying Woodpecker CI, based around Podman and PostgreSQL.

Requirements
------------

This role assumes you have the following already:

* Podman server
* PostgreSQL Server

For our purposes, we deploy PostgreSQL on the host and access it from the container. If you are not doing this
you will need to set up a PostgreSQL container and alter the `fg_forgejo_db` variables accordingly. The
playbook can also manage the user and database (assuming the 'postgres on host' setup) - if you are
not doing this turn the db management feature off.

Role Variables
--------------

There are variables which must be set for this playbook to work correctly:

```

```

There are also variables to customise how Forgejo is deployed. The customisation directory is deployed into
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
