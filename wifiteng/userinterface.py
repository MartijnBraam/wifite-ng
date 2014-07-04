import abc
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
    def menu(self, choises):
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

    def menu(self, choises):
        pass