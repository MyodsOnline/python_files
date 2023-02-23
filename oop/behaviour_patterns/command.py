import datetime
from abc import ABC, abstractmethod
from time import sleep


class CommandInvoker:

    def __init__(self):
        self._commands_list = []

    def store_command(self, command):
        self._commands_list.append(command)

    def execute(self):
        for command in self._commands_list:
            command.execute()


class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class Start(Command):
    def execute(self):
        self.receiver.start()


class Stop(Command):
    def execute(self):
        self.receiver.stop()


class Pause(Command):
    def execute(self):
        self.receiver.pause()


class CommandReceiver:
    def start(self):
        print(f'Start')

    def stop(self):
        print(f'Stop')

    def pause(self):
        sleep(2)
        print(f'Pause')


reciver = CommandReceiver()
strt = Start(reciver)
stp = Stop(reciver)
ps = Pause(reciver)

invoker = CommandInvoker()
invoker_list = [invoker.store_command(strt), invoker.store_command(stp), invoker.store_command(ps),
                 invoker.store_command(stp), invoker.store_command(strt), invoker.store_command(stp)]

invoker.execute()


###

class ICommand(ABC):
    """command interface, will imlplement all commands"""
    @abstractmethod
    def execute(self):
        """required execute method"""
        pass


class Invocler:
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f'Command [{command_name}] is not recognised')


class Receiver:
    def run_command_1(self):
        print(f'Executing Command 1')

    def run_command_2(self):
        print(f'Executing Command 2')


class Command_1(ICommand):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.run_command_1()


class Command_2(ICommand):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.run_command_2()


# Create a receiver
iReceiver = Receiver()
# Create Commands
iCommand1 = Command_1(iReceiver)
iCommand2 = Command_2(iReceiver)
# Register commands with the invoker
iInvocler = Invocler()
iInvocler.register('1', iCommand1)
iInvocler.register('2', iCommand2)

iInvocler.execute('1')
iInvocler.execute('2')
iInvocler.execute('3')
iInvocler.execute('1')
iInvocler.execute('2')


###

class ABCSwitch(ABC):
    @abstractmethod
    def execute(self):
        pass


class Switch:
    """The invoker class"""
    def __init__(self):
        self._commands = {}
        self._history = []

    def show_history(self):
        for row in self._history:
            print(f'{datetime.datetime.now().strftime("%H:%M:%S")}: {row}', end='; ')

    def register(self, cmd_name, cmd):
        self._commands[cmd_name] = cmd

    def execute(self, cmd):
        if cmd in self._commands.keys():
            self._commands[cmd].execute()
            self._history.append(cmd)
        else:
            print(f'Command [{cmd}] is not recognised')


class SwitchOnCommand(ABCSwitch):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.switch_on()


class SwitchOffCommand(ABCSwitch):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.switch_off()


class Light:
    """The Receiver"""
    def switch_on(self):
        print('Light is on')

    def switch_off(self):
        print('Light is off')


LIGHT = Light()
ON = SwitchOnCommand(LIGHT)
OFF = SwitchOffCommand(LIGHT)

SWITCH = Switch()
SWITCH.register('ON', ON)
SWITCH.register('OFF', OFF)

SWITCH.execute('ON')
SWITCH.execute('OFF')
SWITCH.execute('ON')
SWITCH.execute('OFF')

SWITCH.show_history()
