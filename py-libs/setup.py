import os
import curses
from sharedLibs.find import find_pipfile
from sharedLibs.print_pretty import print_blue_info


def ask_whether_to_install() -> bool:
    '''
    Ask users wether to install pip packages or not
    '''
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    screen.addstr('Do you want to install python packages(y/N): ')
    while True:
        char = screen.getch()
        print(type(char))
        if char in [ord('y'), ord('Y')]:
            return True
        else:
            return False


def main():
    setup_flag = ask_whether_to_install()

    if not setup_flag:
        print_blue_info(
            "\t\tIf you want to install in future\n\t\t`yarn pipenv install`")
        return

    os.chdir(find_pipfile())
    os.system("pipenv install")
    os.system("pipenv install django")


if __name__ == "__main__":
    main()
