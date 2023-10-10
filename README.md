# CapX

# Project Title: Bug Management Dashboard

Bug management dashboard is developed as part of the [microtasks](https://phabricator.wikimedia.org/T346641) assigned on Wikimedia Phabricator. Django and SQLite are used for building this dashboard.

## Features

- **User Authentication**: Access to the dashboard is limited to registered and authenticated users. A username and password are required for login.

- **Leaderboard**: A list of users who have resolved the most bugs is displayed, fostering a friendly competition amongst users.

- **Add New Bug**: New bugs encountered can be reported by users. Details about the bug, including its description, severity, and steps to reproduce it, can be added.

- **Find All Bugs**: All reported bugs are listed. This list can be browsed to understand the current issues.

## Setup

The following steps are needed to run this project on a local machine:

1. The repository needs to be cloned from GitHub.
2. A virtual environment should be set up and the dependencies listed in the `requirements.txt` file should be installed.
3. The Django server should be run.

Here are the detailed steps:

```bash

# Clone the repository
git clone https://github.com/axif0/CapX.git

# Navigate into the cloned repository
cd CapX/core

# Set up virtual environment (Windows)
python -m venv env

# Set up virtual environment (Unix/MacOS)
python3 -m venv env

# Activate the virtual environment
# Windows
./env/Scripts/activate

# Unix/MacOS
source env/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Run the Django server
python manage.py runserver
```

Now, `http://localhost:8000` should be navigated to in the browser to view the project.

## Screenshots

Screenshots of the features are provided for a better understanding of the project. They should be referred to while exploring the project.

## Contributions

The tasks completed for this project are as follows:

- [T347253](https://phabricator.wikimedia.org/T347253): A Django project with an app called bug is created.
- [T347254](https://phabricator.wikimedia.org/T347254): A SQLite database is set up and models for the bug app are created.
- [T347255](https://phabricator.wikimedia.org/T347255): Views and templates for registering and viewing a bug and listing all bugs are created.
- [T347256](https://phabricator.wikimedia.org/T347256): User authentication is implemented.

## Acknowledgements

This project was developed as part of the Wikimedia microtasks assigned on Phabricator. The tasks were aimed at getting familiar with the basic structure of the development of the Capacity Exchange platform. The project has been committed to GitHub as per the guidelines provided in the tasks [stackoverflow.com](https://phabricator.wikimedia.org/T347253), [markdown.land](https://phabricator.wikimedia.org/T347255).

## License

The MIT License is used for this project. 


