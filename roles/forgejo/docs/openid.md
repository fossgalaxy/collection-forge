# OpenID Integration

This is still a little flakey, as it relies on running commands inside the running forgejo container using the forgejo command line. You can manage this yourself using the WebUI when you have an administrator account crated.

## Variables

| Name | Default | Description |
| ---- | ------- | ----------- |
| `forgejo_oid` | false (true if `meta_url` is set) | Should OpenID be enabled? |
| `forgejo_oid_provider_name` | forgejo | The provider name as it should appear in forgejo |
| `forgejo_oid_meta_url` | "" | The 'well-known' url for your IDP |
| `forgejo_oid_client` | forgejo | The client ID from the IDP |
| `forgejo_oid_secret` | `<undefined>` | The secret from the IDP |
| `forgejo_oid_register` | false (true if private instance) | Should logging in with OpenID without an account create one? |

## Keycloak Integration (recommended)
As the OpenID provider we use, Keycloak has special integrations with the playbook, it can integrate correctly.

| Name | Default | Description |
| ---- | ------- | ----------- |
| `forgejo_keycloak` | false (true if forgejo_oid_secret is no defined) | Should we manage the keycloak client? |
| `forgejo_keycloak_realm` | `freeipa` | The realm which the client should be added to. |

If the keycloak option is used, then the role will attempt to register and create the client, with the recommended configuration options. If the secret is not defined on the `appserver`, it will fetch the secret from `keycloak` then store it in the required secret.

### Manual configuration

NOTE: We will manage this for you if using the Keycloak integration.

If your Forgejo instance is at: `code.example.com`, then the admin page for managing authentication methods is at: https://code.example.com/admin/auths/

Authentication name is what `forgejo_oid_provider_name` auto-populates.

#### Setting up the keycloak client

The provider name (ie `forgejo_oid_provider_name`) is embedded in the return url. 

The redirect URL should be: `https://code.example.com/user/oauth2/PROVIDER_NAME/callback`

#### Discovery URL
If your Keycloak instance is deployed on `auth.example.com` and has the realm name `blarg` then this URL would be:

```https://auth.example.com/realms/blarg/.well-known/openid-configuration```

The recommended settings (from our perspective) is as follows:

| Name | Value | Reason |
| ---- | ----- | ------ |
| Skip local 2FA | true | Let keycloak manage 2FA |


