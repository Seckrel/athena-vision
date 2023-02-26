import os
import curses
from sharedLibs.find import find_pipfile
from sharedLibs.print_pretty import print_blue_info


def ask_whether_to_install() -> bool:
    '''
    Ask users wether to install pip packages or not
    '''
    ask_var: str = input('Do you want to install python packages(y/N): ')
    if (ask_var.lower() == 'y'):
        return True
    return False


def main():
    setup_flag = ask_whether_to_install()

    if not setup_flag:
        print_blue_info('''If you want to install in future
        `yarn pipenv install`''')
        return

    os.chdir(find_pipfile())
    os.system("pipenv install")
    os.system("pipenv install django")


if __name__ == "__main__":
    main()
