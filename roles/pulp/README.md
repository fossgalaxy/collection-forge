# Role for Deploying Pulp

[Pulp](https://pulpproject.org/) is a very capable tool for hosting and caching packages in a range of different formats. Although 
Forgejo has this functionality now, this is an alternative which can be deployed stand-alone and has a
bit more of a history behind it.

## Usage

```
- role: fossgalaxy.forge.pulp
  vars:
    pulp_domain: pulp.example.com
    pulp_db_host: db01.example.com
    pulp_db_pw: db_password_here
    pulp_admin_password: admin_password_for_cli
    pulp_secretkey: django_style_secret_key
```

This role should be able to perform migrations and initial admin password setup. It will also generate certs for registry signing and so forth.

At present, this role should work but is has not been robustly tested in a range of environments.

## Limitations

### Multiple reverse proxies

At present, the role will deploy the pulp nginx (pulp-web) container which is then exposed via traefik.
It should be possible to avoid this 'double proxying' with some clever traefik config. There is a feature
flag for this, but it's not implemented yet.

### Limited error checking

There is extremely limited error checking in this role at present. This needs to be improved.

### No SSO support
pulp has limited documentation on SSO support, but they document SAML not OpenID Connect.
