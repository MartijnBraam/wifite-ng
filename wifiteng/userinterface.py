import abc
import tty
import sys
import termios
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
        pass

    def error(self, message):
        pass

    def success(self, message):
        pass

    def warning(self, message):
        pass

    def menu(self, title, choises):
        print(Color.WHITE + " --------[ " + Color.GREEN + title + Color.WHITE + " ]--------")
        for index, choise in enumerate(choises):
            print(" {}. {}".format(index + 1, choise))
        print(" --------{}--------".format("-" * (len(title) + 4)))
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
            return self.menu(title, choises)
        else:
            return choises[int(keypress[0:1])]