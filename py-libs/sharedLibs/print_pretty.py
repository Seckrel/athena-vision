import sys


def print_red_error(text, file=sys.stderr):
    '''
    Displays error message in red
    @params
        text: error message to be displayed
        file: file like object to be used
    '''

    print(f"\033[91m Error:\033[00m {text}", file=file)


def print_blue_info(text):
    '''
    Displays info message in blue
    @params
        text: info message to be displayed
    '''

    print(f"\033[94m Info:\033[00m {text}")
