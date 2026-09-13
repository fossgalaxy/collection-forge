# Role for Deploying Penpot

[Penpot](https://penpot.app/) is a design platform for developing UX mockups and the like.

## Usage

```
- role: fossgalaxy.forge.penpot
  vars:
    penpot_domain: pulp.example.com
    penpot_db_host: "{{ homelab_database_primary }}"
    penpot_db_pw: "{{ vault_forgejo_admin_pw }}"
    penpot_secretkey: "{{ vault_forgejo_secretkey }}"
```

At present, this role should work but is has not been robustly tested in a range of environments.

### SSO Integration

SSO can be configured, the playbook has support for injecting a CA into the container
if you are using local PKI. Because this is a JVM app, the process for this is a little
complicated behind the scenes (so may be brittle).

```
# required if using self-signed certs...
# penpot_inject_cert: true

penpot_be_allowed_hosts: [ "idp.example.com" ]
penpot_oid: true
penpot_oid_displayname: "Homelab SSO"
penpot_oid_meta_url: "https://idp.example.com/realms/freeipa/"
penpot_oid_client: penpot
penpot_oid_secret: "{{ vault_penpot_oid_secret }}"
```
