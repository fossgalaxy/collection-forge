# Database Integration

The playbook can manage a (postgres) database for you using our infrastructure roles. You don't have to have deployed our postgres server role to use this feature.

## Key Variables

Note the defaults provided below assume `forgeo_service` has its default value (`forgejo`). If this is not the case any default value below will replace `forgejo` with whatever that has been set to.

| name | default | description |
| ---- | ------- | ----------- |
| `forgejo_db` | true | Should the role manage the database? |
| `forgejo_db_name` | forgejo | The postgres database name |
| `forgejo_db_owner` | forgejo_admin | The account which will manage the database |
| `forgejo_db_user` | forgejo_app | The account which will be used for database connections |
| `forgejo_db_pw` | N/A | The password for the `db_user` account |
| `forgejo_db_remote` | true | Should a HBA rule be added for the user account? |

Note that the playbook seperates out the 'owner' and 'user' roles. This is to allow for restricted permissions for the account which connects to the database. If these roles do not exist, they will be created by the Ansible role.

`forgejo_secret_db_password` is the name of the variable containing the Podman secret which will be used to store the admin password (exposed to the container as a container secret). Defaults to `forgejo_db_pass`.
