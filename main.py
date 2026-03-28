from core.shell import Shell
from commandsignals.signal import listen_to_signint

if __name__ == '__main__':
    listen_to_signint()
    shell = Shell()
    shell.run()