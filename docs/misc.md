## Library

A `project/lib` folder has been created to hold reusable codes for common or generic operations within the project. Note that codes that goes in this folder should be very independent from business logics or Django codes

## Other Services

For the other services namely `notification`, `payment` and `dspa`, the approach to take in ensuring replacability and maintainability will be discuss when implementations requires them.

## Docker compose bind mounts

Bind mount make sensewhen what's on the host is expected to overwrite what is in the container and not the other way round

## Docker compose bind mounts environment variables

Though some environment variables (ex. `DEBUG`, `SECRET_KEY` etc) have default values assigned to then in the codes making it unnecessary for us to declared here. However it is important we explicitly declare them here so we know all the required environment variables as we do not have anything like for instance env.sample

## Move commits to production repository

```bash
# Dev Repo  :>> Cinch API repository on Decadevs organization
# Prod Repo :>> Cinch API repository on DecagonHQ organization

# Ensure to be on the main branch of the prod repo before running
# any of the below commands

git checkout main

# Ensure the dev repo has been added as a remote to the
# prod repo with name dev-origin or you manually do it
# with the below command

git remote add dev-origin https://github.com/decadevs/cinch-api-dev

# Pull all changes from the main branch of the dev repo into the
# main branch of the prod repo

git pull dev-origin main

# Confirm that commit history on prod repo's main branch is exactly
# the same as that on the dev repo's main branch

git log

# Push all latest changes to upstream branch { main }

git push

```
