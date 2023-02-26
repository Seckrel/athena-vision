import sys
import os
from sharedLibs.find import find_pipfile, find_managepy
from sharedLibs.print_pretty import *


class DjangoStartAppException(Exception):
    pass


def decision_tree(argv) -> str:
    '''
        Choose proper command based on intruction and furthure paramater provided
        @params
            argv: sys.argv list
        @returns
            command in string datatype to be executed
    '''

    try:
        instruction: str = argv[1].lower()  # lower casing entire instruction
        command: str = "pipenv run python manage.py "

        single_parameter_instruction: bool = instruction == "runserver" or instruction == "makemigrations" or instruction == "migrate" or instruction == "collectstatic"

        if single_parameter_instruction:
            command += instruction

        elif instruction == "startapp":
            app_name: str = argv[2]

            # Throwing error if app name is not provided
            if app_name is None or app_name == "":
                raise DjangoStartAppException(
                    "manage.py startapp missing app name")

            command += f"{instruction} {app_name}"

        elif instruction == "startproject":
            project_name: str = argv[2]
            command = f"pipenv run django-admin startproject {project_name}"

            if project_name is None or project_name == "":
                raise DjangoStartAppException(
                    "django-admin startproject requires a proper name"
                )

    except IndexError:
        print_red_error(
            "Either no instruction provided with manage.py or no app name given for startapp instruction")
        print_blue_info(
            "Try using startapp <app-name>, makemigrations, runserver...")

        sys.exit(1)

    except DjangoStartAppException as e:
        print_red_error(e)

        print_blue_info(
            '''To start new app:
            yarn startapp my-app

            To start new project:
            yarn startproject mysite'''
        )
        sys.exit(1)

    return command


def exec_instruction(command: str, exec_dir) -> None:
    '''
        Executes command 
        @params
            command: command to be executed
            exec_dir: directory where command needs to be executed
    '''

    if exec_dir == None or exec_dir == "":
        print_red_error(
            "Directory to execute instruction cannot be None or empty")

    os.chdir(exec_dir)
    os.system(command=command)


def choose_py_dir(argv) -> str:
    '''
        Chooses appropriate directory
        @params
            argv: sys.argv list
        @returns
            relative directory to director where the command needs to be executed
    '''

    py_dir = find_pipfile()

    try:
        instruction = argv[1].lower()

        if instruction != "startproject":
            py_dir = find_managepy()

    except IndexError as e:
        print_red_error("No instruction provided")
        print_blue_info(
            "Try using yarn django <instruction>. Intruction includes startapp, runserver, makemigrations, migrate, collectstatic and startproject")

    return py_dir


def write_cmd(args):
    try:
        command: str = "pipenv run python manage.py "
        command += " ".join(args[1:])
        return command
    except DjangoStartAppException:
        print_red_error("Insturction error")


def main():
    # path to directory where command needs to be executed
    exec_dir = choose_py_dir(sys.argv)

    # command to be executed
    # command = decision_tree(sys.argv)
    command = write_cmd(sys.argv)
    exec_instruction(command, exec_dir)


if __name__ == '__main__':
    main()
