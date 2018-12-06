# jupyterhub-deploy-docker

**See [original repository](https://github.com/jupyterhub/jupyterhub-deploy-docker).**

## Authenticator setup

This deployment uses GitLab OAuth to authenticate users.

- add variables to an `oauth.env` file in the `secrets` directory of this repository.
  You may need to create both the `secrets` directory and the `oauth.env` file.
  For example, add the following lines in the `oauth.env` file:

  `oauth.env` file

  ```env
  OAUTH_CLIENT_ID=<gitlab_client_id>
  OAUTH_CLIENT_SECRET=<gitlab_client_secret>
  OAUTH_CALLBACK_URL=http://<myaddress>:8001/hub/oauth_callback
  GITLAB_HOST=https://<gitlab_address>
  ```

  **Note:** The `oauth.env` file is a special file that Docker Compose uses
  to lookup environment variables. If you choose to place the GitHub
  OAuth application settings in this file, you should make sure that the
  file remains private (be careful to not commit the `oauth.env` file with
  these secrets to source control).

### GitLab OAuth Application

Create a [GitLab OAuth application](http://docs.gitlab.com/ce/integration/oauth_provider.html).

## Database setup

- add variables to an `postgres.env` file in the `secrets` directory of this repository.

  `postgres.env` file

  ```env
  POSTGRES_PASSWORD=mysecretpassword
  ```

## Build the JupyterHub Docker image

Finish configuring JupyterHub and then build the hub's Docker image. (We'll
build the Jupyter Notebook image in the next section.)

1. Configure `userlist`: Create a `userlist` file of authorized JupyterHub
   users. The list should contain GitHub usernames, and this file should
   designate at least one `admin` user. For instance, the example file below
   contains three users, `jtyberg`, `jenny`, and `guido`, and one designated
   administrator, `jtyberg`:

   `userlist` file

   ```plain
   jtyberg admin
   jenny
   guido
   ```

   The admin user will have the ability to add more users through JupyterHub's
   admin console.

1. Use [docker-compose](https://docs.docker.com/compose/reference/) to build
   the JupyterHub Docker image on the active Docker machine host by running
   the `make build` command:

   ```bash
   make build
   ```

## Spawner: Prepare the Jupyter Notebook Image

Build and tag the image using the `Dockerfile` in `notebook-with-gpu` directory.

```bash
cd notebook-with-gpu
docker build -t jupyterhub-gpu-notebook .
```

## Run JupyterHub

Run the JupyterHub container on the host.

To run the JupyterHub container in detached mode:

```bash
docker-compose up -d
```

Once the container is running, you should be able to access the JupyterHub console at

```plain
http://<myaddress>:8001
```

To bring down the JupyterHub container:

```bash
docker-compose down
```
