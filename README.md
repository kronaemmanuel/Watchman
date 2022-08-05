# Watchman

Watchman is a Django application to track the in/out timings of Arbisoft office
employees. It is a simple project built to test Django Custom Management
Commands
with the following requirements:

- Write a Django Managment Command that will run and store records in the
  database:
    - Inserts Dummy Users in the database
    - Store 100 PST date times in a separate table
        - Run a scheduled Cron Job, that will run after every 5 minutes
            - Crob Job will update 10 date times to UTC
            - Once date times are converted to UTC, it will start converting
              date times to UTC

## Quickstart

The project is setup with [Docker](https://docs.docker.com/get-docker/). Make
sure you have `docker compose` available in your terminal. Run

```commandline
docker compose build
```

```commandline
docker compose up
```

The app should start running at `0.0.0.0:8000`
