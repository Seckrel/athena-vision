# Athena-Vision 👁️

## Table of Content
- [Introduction](#Introduction)
- [Project Structure](#Project-Structure)
- [How to Run](#How-to-run)
    - [Requirements](##Requirements)
    - [Initial Setup](##Initial-Setup)
- [Run Django Command](##Run-Django-Command)
- [Run Pipenv Command](##Run-Pipenv-Command)

# Introduction
Athena Vision aims to make cyber world of Twitter a little better. It provides ability to blur out hateful tweets, as well as perfoms multilingual sentiment analysis and topic analysis

# Project Structure
Monorepo created using nx tool. 
	|- Packages
		|- athena-vision-web -- react app
		|- athena-vision-api -- django backend
	|- py-libs -- custom library run django and pipenv from root dir

Rest of the structure is basic nx integrated repo structure (Learn more [here](https://nx.dev/getting-started/integrated-repo-tutorial)
# How to Run

## Requirements
Project requires:
- [node@16.13.0](https://nodejs.org/download/release/v16.1.0/)
- [python@3.10](https://www.python.org/downloads/release/python-3100/)
- [pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)

These three need to be already installed on the working machine

## Initial Setup
Install all packages:

    yarn install
    
   It will install all required node packages and python packages while cretaing virtual env using pipenv

# Run Django Command
Basic commands of Django can be run directly from root directory
- runserver
- makemigrations
- migrate
- collectstatic
- startapp
- startproject

Syntax:

    yarn django <command>

Example Codes

- `yarn django runserver`
- `yarn djagno startapp myapp`

# Run Pipenv Command
All pipenv commands can be run directly from root directory

Syntax

    yarn pipenv <flag/command>

Example

- `yarn pipenv --venv`
- `yarn pipenv lock --pre`
- `yarn pipenv install requests`
