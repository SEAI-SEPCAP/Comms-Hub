"""
SEPCAP Messaging System

Helper Functions
"""

def lineToMessage(line):
    return [ord(i) for i in list(line)]

def getAddress(byte):
    return (byte & 0xF0) >> 4

def getMessageType(byte):
    return byte & 0x0F

def decodeMessage(message: list):
    return getAddress(message[0]), getMessageType(message[0]), message[1:]

def encodeMessage(address, type, data):
    return bytes([(address << 4) + type, data])
