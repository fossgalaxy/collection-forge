# Forgejo Runner

Deploy a runner capable of running containerised tasks from Forgejo instances.

At present, this role is quite basic, in future we plan to extend it to have
additional features (such as registering the runner automatically).

## Example usage

The role currently does not register the runner with Forgejo directly. You will need to do
this using the Forgejo web interface (eg, http://code.example.com/admin/actions).

Forgejo Runner will need Podman installed on the host alongside the runner - the role will not care
how this is accomplished (the example below uses our infra role).

```
- hosts: builder.example.com
  roles:
    - role: fossgalaxy.infra.container_host
    - role: fossgalaxy.forge.forgejo_runner
      vars:
        forgejo_runner_connection_url: "https://code.example.com"
        forgejo_runner_connection_uuid: uuid-from-forgejo
        forgejo_runner_connection_token: token-from-forgejo
  tags:
    - setup
```
```
