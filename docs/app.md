## Introduction

The app folder is not really a Django application but instead a normal python package which is expected to contain python scripts defining different actions expected to be performed within the project. Actions can be either grouped or not grouped at all but must conform the expected interface

## Interfaces

This project will rely on different services listed below. To ensure that we do not have issues later in future in terms of replacing and extending implementations or functionalities, we have the folder `app/interfaces` that describes what other services we want to rely on must implement for them to be compatible with the one another.

These defined interfaces for the services will serve as the ONLY source of through of properties, methods and classes we will rely on with our actions.

The services within this project include the following
- api
- db
- dspa
- notification
- payment
