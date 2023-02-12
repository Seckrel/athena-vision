import os
from sharedLibs.find import find_pipfile


def main():
    os.chdir(find_pipfile())
    os.system("pipenv install")
    os.system("pipenv install django")


if __name__ == "__main__":
    main()
