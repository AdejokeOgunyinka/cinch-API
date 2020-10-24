## Docker compose bind mounts

Bind mount only works well when what is on host is expected to overwrite what is in the container and not the other way round

## Docker compose bind mounts environment variables

Though some environment variables (ex. `DEBUG`, `SECRET_KEY` etc) have default values assigned to then in the codes making it unnecessary for us to declared here. However it is important we explicitly declare them here so we know all the required environment variables as we do not have anything like for instance env.sample

## About the tmp folder

This is a temporary folder for holding runtime generated files and folders of other services that are completely independent of the `api` service
