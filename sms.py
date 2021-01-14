"""
SEPCAP Messaging System
"""

import select
import tty
import termios
import enum


class SepcapMessagingSystem(object):
    """
    docstring
    """

    stream = None
    old_settings = None

    class Address(enum.IntEnum):
        Broadcast = 0
        Individualization = 1
        Classification = 2
        Distribuition = 3
        Interface = 4

    class Message:

        class EmergencyStop(enum.IntEnum):
            type = 0
            Emergency = 0
            Resume = 1

        class NewCapsule(enum.IntEnum):
            type = 1

        class StartStop(enum.IntEnum):
            type = 2
            Stop = 0
            Start = 1

    def __init__(self, stream):
        self.stream = stream
        self.old_settings = termios.tcgetattr(self.stream)
        tty.setcbreak(self.stream.fileno())

    def __del__(self):
        termios.tcsetattr(self.stream, termios.TCSADRAIN, self.old_settings)

    def isData(self):
        return select.select([self.stream], [], [], 0) == ([self.stream], [], [])

    def read(self, n=1):
        return self.stream.read(n)

    def lineToMessage(self, line):
        return [i for i in list(line)]

    def getAddress(self, byte):
        return (byte & 0xF0) >> 4

    def getMessageType(self, byte):
        return byte & 0x0F

    def decodeMessage(self, message: list):
        return self.getAddress(message[0]), self.getMessageType(message[0]), message[1:]

    def encodeMessage(self, address: int, messageType: int, data: int):
        return bytes([(address << 4) + messageType, data])

    def readPacket(self):
        line = bytearray(self.read(2))
        message = self.lineToMessage(line)
        return self.decodeMessage(message)
