# Woodpecker Integration

This playbook can deploy and integrate woodpecker into Forgejo, there are a few things to be aware of:

## Agent Key

Woodpecker needs a shared secret for registering instance-level runners. You can set this to a suitable
value using:

```
woodpecker_server_agent_key: key-goes-here
```

The official [woodpecker documentation](https://woodpecker-ci.org/docs/administration/deployment-methods/docker-compose) recommends using this command: `openssl rand -hex 32`

## Database password

The default database values will deploy the database alongside the forgejo one. You will need to provide
a suitable password for the account however:

```
woodpecker_server_db_password: "password_here"
```

A reasonably long random string is fine. The playbook will store this in a podman secret.

## Forgejo Connection

Woodpecker assumes that there is a Forge it can use. This playbook is geared around forgejo, so that's the
one it will try to configure. However, this means you need to setup an oauth application.

### As a user application

If you plan to let the playbook manage the oauth application. You will need to generate an access token for
the API using the web interface ( `user/settings/applications` ) - it requires `user` access at least.

```
woodpecker_server_forgejo_token: <user token here>
```

When the playbook is run, it uses this token to fetch the oauth client ID and ensure that the oauth
application exists.

In the future, we might be able to automate the token-fetching process, but it's manual for now. The
oauth application will be registered if it does not exist, and the podman secret for the application
will be set. The playbook will not store the oauth details using this method.

If you need to regenerate the oauth token and secret for some reason, you can do this by setting:

```
woodpecker_server_forgejo_regenerate: true
```

### As an instance application

Forgejo also supports registering oauth tokens at the server level. Unfortunately, the API doens't have
methods for managing this, so as far as I know it needs to be done in the web ui in the `/admin/applications`
page.

Once you have created the application you can use the following variables to configure the connection:

```
woodpecker_server_forgejo_client: client-id-here
woodpecker_server_forgejo_secret: client-secret-here
```

Note forgejo oauth client ids are long strings with dashes in them, not the friendly name you input.

## Admin access

You can define users who should be admins upon login by providing a list of account names, for example:

```
woodpecker_server_admins:
  - testadmin
```
