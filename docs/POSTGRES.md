## Postgres setup

First, install postgresql. A guide on how to do this can be found [here](https://dev.to/sfpear/install-and-use-postgres-in-wsl-423d). After postgresql has been installed and is running, follow this guide for the proper setup.

- Open a postgres shell
```console
$ sudo -su postgres psql
```

- Create a user
```console
postgres=# CREATE USER username WITH ENCRYPTED PASSWORD 'password';
```

- Create a database, for the owner, use the user you just created
```console
postgres=# CREATE DATABASE dbname OWNER username;
```

- Make sure the user has the correct permissions on the database
```console
postgres=# GRANT ALL PRIVILEGES ON DATABASE dbname TO username;
```

That's all, the rest of the database will be taken care of by django migrations.