import abc
import tty
import sys
import termios
import datetime
from wifiteng.helpers import Color


class BaseUserInterface(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def bootsplash(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def info(self, message):
        raise NotImplementedError()

    @abc.abstractmethod
    def warning(self, message):
        raise NotImplementedError()

    @abc.abstractmethod
    def error(self, message):
        raise NotImplementedError()

    @abc.abstractmethod
    def success(self, message):
        raise NotImplementedError()

    @abc.abstractmethod
    def menu(self, title, choises):
        raise NotImplementedError()


class TerminalUserInterface(BaseUserInterface):

    def __init__(self):
        pass

    def bootsplash(self):
        print()
        print(Color.GREEN + "  .;'                     `;,    ")
        print(Color.GREEN + " .;'  ,;'             `;,  `;,   " + Color.GREEN+"WiFite-ng")
        print(Color.GREEN + ".;'  ,;'  ,;'     `;,  `;,  `;,  ")
        print(Color.GREEN + "::   ::   :   " + Color.WHITE + "( )" + Color.GREEN + "   :   ::   ::  " + Color.WHITE +
              "automated wireless auditor")
        print(Color.GREEN + "':.  ':.  ':. " + Color.WHITE + "/_\\" + Color.GREEN + " ,:'  ,:'  ,:'  ")
        print(Color.GREEN + " ':.  ':.    " + Color.WHITE + "/___\\" + Color.GREEN + "    ,:'  ,:'   " + Color.WHITE +
              "designed for Linux")
        print(Color.GREEN + "  ':.       " + Color.WHITE + "/_____\\" + Color.GREEN + "      ,:'     ")
        print(Color.GREEN + "           " + Color.WHITE + "/       \\" + Color.GREEN + "             ")
        print(Color.WHITE)

    def info(self, message):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print("[{}] {}".format(now, message))

    def error(self, message):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print("[{}] {}{}{}".format(now, Color.RED, message, Color.WHITE))

    def success(self, message):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print("[{}] {}{}{}".format(now, Color.GREEN, message, Color.WHITE))

    def warning(self, message):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print("[{}] {}{}{}".format(now, Color.YELLOW, message, Color.WHITE))

    def menu(self, title, choises):
        print(Color.WHITE + "           --------[ " + Color.GREEN + title + Color.WHITE + " ]--------")
        for index, choise in enumerate(choises):
            print("           {}. {}".format(index + 1, choise))
        print("           --------{}--------".format("-" * (len(title) + 4)))
        stdin = sys.stdin.fileno()
        old_setting = termios.tcgetattr(stdin)
        try:
            tty.setraw(stdin)
            keypress = sys.stdin.read(1)
        except IOError:
            keypress = input()
        finally:
            termios.tcsetattr(stdin, termios.TCSADRAIN, old_setting)

        if not int(keypress) in range(1, len(choises)):
            self.warning("Invalid key pressed.")
            return self.menu(title, choises)
        else:
            self.info(choises[int(keypress[0:1])])
            return choises[int(keypress[0:1])]

    def table(self, columns, data):
        lengths = []
        temp_merge = data[:]
        temp_merge.append(columns)
        for row in temp_merge:
            for index, field in enumerate(row):
                if len(lengths) < index + 1:
                    lengths.append(len(field))
                else:
                    if len(field) > lengths[index]:
                        lengths[index] = len(field)

        format_part = []
        for length in lengths:
            format_part.append(" {!s:<" + str(length) + "} ")
        format_str = str("|".join(format_part))
        format_str = (" " * 11) + format_str
        total_width = sum(lengths) + len(lengths) * 3 - 1
        print(format_str.format(*columns))
        print(" " * 11 + "-" * total_width)
        for row in data:
            print(format_str.format(*row))