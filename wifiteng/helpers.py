import subprocess


class Color(object):
    GRAY = "\033[1;30m"
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    RESET = "\033[0m"


class ShellTool(object):

    def call_and_communicate(self, command, timeout=None):
        # Create subprocess and connect stdout and stderr to pipe
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            # Run command until it exits or the timeout (if set) expires
            (stdout, stderr) = proc.communicate(timeout=timeout)

            # Return all information
            return proc.returncode, stdout, stderr
        except subprocess.TimeoutExpired:
            # Cleanup after timeout expires and then bubble the exception up
            proc.kill()
            raise