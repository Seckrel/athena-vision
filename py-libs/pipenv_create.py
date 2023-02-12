import sys
import os
from sharedLibs.find import find_pipfile
from sharedLibs.print_pretty import print_red_error

PIP_DIR: str = find_pipfile()
PACKAGES_PATH: str = "packages"


def create_pipfile(argv) -> None:
    try:
        os.chdir(PACKAGES_PATH)
        pipenv_project_name: str = argv[1]
        os.system(f"mkdir {pipenv_project_name}")
        os.chdir(os.path.join(PACKAGES_PATH, pipenv_project_name))
        os.system("pipenv install")
    except IndexError:
        print_red_error("Sys.argv index error")


def execute_pipenv_cmd(argv) -> None:
    try:
        os.chdir(PIP_DIR)
        args: str = " ".join(argv[1:])
        os.system(f"pipenv {args}")
    except:
        print_red_error("Cannot execute pipenv command")


def main():
    argv: list = sys.argv

    if PIP_DIR == None:
        create_pipfile(argv)
    else:
        execute_pipenv_cmd(argv)


if __name__ == "__main__":
    main()
