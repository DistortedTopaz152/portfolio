import datetime
import sys


def display_options(options):
    index = 1
    for option in options:
        print(str.format('{}......{}', index, option))
        index += 1
    while True:
        choice = input('pick an number between 1 and' + str(len(options)) + ":")
        if choice.isnumeric():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return choice
            else:
                print('Not an option')
        else:
            print('Not an option')


def get_good_name(question):
    while True:
        name = input(question)
        if name.isnumeric == False:
            if len(name) >= 1:
                print("Invalid name")
        else:
            return name


def get_a_number(question, low, high):
    while True:
        number = input(question)
        if number.isnumeric():
            number = int(number)
            if low <= number <= high:
                return number
            else:
                print("Invalid number")


def open_file(file_name, mode):
    """open and return a file with the given permissions"""
    try:
        file = open("assets/test_files/" + file_name, mode)
    except IOError as e:
        print("Unable to open file", file_name, "ending program.\n", e)
        try:
            time = datetime.now()
            error_time = time.strftime("%m/%d/%y %H:%M$S")
            file = open("assets/error_log/error_log.txt", "a")
            file.write(str(e) + " " + str(error_time + " " + "\n"))
            input("\n\nPress enter to exit")
            # noinspection PyStatementEffect
            sys.exit
        except:
            # noinspection PyStatementEffect
            sys.exit


def ask_yes_no(question):
    """ask yes no questions"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = Score()
        self.isAlive = True
        self.lives = 3


class Score(object):
    def __init__(self):
        self.score = 0

    def and_to_score(self, points):
        self.score += points

    def take_from_score(self, points):
        self.score -= points
        if self.score < 0:
            self.score = 0



if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit")