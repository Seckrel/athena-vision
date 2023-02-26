import sys
import os
from sharedLibs.find import find_pipfile, find_managepy
from sharedLibs.print_pretty import *


class DjangoStartAppException(Exception):
    pass


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
