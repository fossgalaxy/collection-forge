# Forgejo

Forgejo is a FOSS development forge with a feature set and apperance close to github.

## Database Setup

Although the playbook can manage the database creation for you, you need to provide a suitable password
for the database account:

```
fg_forgejo_db_password: "password_here"
```

## Secrets

You must provide the usual suite of forgejo secrets for the playbook:

```
fg_forgejo_secret_key: TODO
fg_forgejo_internal_token: TODO
fg_forgejo_jwt_lfs: TODO
fg_forgejo_jwt_oauth: TODO
```

In the future, I'm hopeful the playbook might be able to do this for you, but it's a manual process for the
time being. Setting these rather than let forgejo generate them on first runs is important as we rebuild the
configuration file if the playbook options change.

There are commands in the cli binary you can use to generate these:

```
forgejo generate secret SECRET_KEY
forgejo generate secret INTERNAL_TOKEN
forgejo generate secret JWT_SECRET # once for each _jwt_ value
```
