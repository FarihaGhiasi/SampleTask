# Sample Task (Dockerized PostgreSQL Database)

This repository contains the solution for an interview task that involves using Docker to set up two containers. The first container runs a PostgreSQL database with artificial data, and the second container is a Python service/script that accesses the PostgreSQL database, filters and deletes entries older than a specified date. In addition, a bash script is provided to automate the setup and execution of the entire process.

# Getting Started
To get started with this project, follow these steps:

Clone this repository to your local machine.

```bash
git clone https://github.com/FarihaGhiasi/SampleTask.git

```
## Project Structure

The project is structured as follows:

- `db.py`: Establishes a connection to the PostgreSQL database using SQLAlchemy.
- `main.py`: Defines a Python script that generates and manages data in the PostgreSQL database.
- `Dockerfile`: Configures the Docker container for the Python application.
- `docker-compose.yml`: Defines the services for the PostgreSQL database and the Python application.
- `docker-build-and-up.sh`: A bash script to automate the setup and execution of the Docker containers and data management process.

## Automated Setup with Bash Script

You can automate the setup and execution of the Docker containers and data management process using the provided bash script. Here's how to use it:


1. Open a terminal and navigate to the project directory.

2. Make the bash script (`docker_build_and_up.sh`) executable by running the following command:

```bash
chmod +x docker_build_and_up.sh

```



