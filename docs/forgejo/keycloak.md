# Keycloak Integration
Forgejo provides generic OpenID Connect provider support, this playbook extends this with
our privision roles for keycloak.

## Key concepts

There are three key terms which must be understood:

client_id
: What Forgejo calls itself to your provider (default: `forgejo`) - used as client id

provider_name
: What Forgejo knows keycloak as (default: `freeipa`) - used for redirect url, forgejo admin interface and UI elements

realm
: Where keycloak stores the users and clients (default: `freeipa`) - used for meta url

## Automatic Creation
If Keycloak has been created using the `fossgalaxy.infra` the role can auto-provision the keycloak client
with the recommended settings and create the authentication provider in Forgejo using `fossgalaxy.selfhosted.keycloak_client`.

If you provide the meta url but not the secret, forgejo will fetch it by default. You will need to provide:

```yaml
forgejo_oid_meta_url: https://auth.example.com/realms/realm_name/.well-known/openid-configuration
```

The playbook auto-detects provisioning urls if they are same ones the `fossgalaxy.selfhosted.keycloak` role uses, so if 
are using that role and have them set, it will 'just work'. If not, you should provide:

```yaml
# for auto-provisioning
keycloak_url: 'https://auth.example.com'
keycloak_auth_user: 'ansible'
keycloak_auth_password: '' # whatever the password is

# defaults (only need to provide if different
keycloak_client_id: 'admin-cli'
keycloak_auth_realm: 'master'
```

If you wish to change the defaults, the core variables to know about are:

```yaml
forgejo_keycloak_realm: freeipa #If your keycloak realm is not freeipa
forgejo_oid_provider_name: freeipa # If you want your provider to not be called 'freeipa'
```

## Manual Method

You can choose to manually create your Keycloak client then provide the OpenID secrets.

In the keycloak administration panel:

1. Go to manage -> Clients
2. Click 'Create Client'
3. Set the Client type to 'OpenID Connect'
4. Set the client ID (playbook assumes `forgejo` but can be overridden using `forgejo_oid_client`)
5. (name and description can be set but are optional)
6. Press Next
5. Turn on 'Client authentication'
6. Ensure 'Standard Flow' is checked (it is by default)
7. Leave other options as defaults
8. Press Next
9. Set `Root URL` to the URL to deployed forgejo (eg, `https://code.example.com`)
10. Set `Valid redirect URIs` to `https://code.example.com/realms/freeipa/.well-known/openid-configuration` (where `freeipa` is what the auth provider is called in Forgejo, defaults to `freeipa`)
11. Press Next

On the client details page, go to the `Credentials` tab:

1. Select `Client Id and Secret` as 'Client Authenticator' (the default)
2. Copy the `Client Secret` value - this is the value for `forgejo_oid_secret`

In your ansible vars, provide the following:

```yaml
# replace realm_name with your Keycloak realm name
forgejo_oid_meta_url: https://auth.example.com/realms/realm_name/.well-known/openid-configuration

forgejo_oid_provider_name: 'freeipa' # must match step 10
forgejo_oid_client: 'forgejo' # (or whatever you used in step 4)
forgejo_oid_secret: '' # value from `Client Secret`

# forgejo_inject_cert: true # if host is FreeIPA enrolled and using internal certs
```