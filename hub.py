#! /usr/bin/python3 -u

import sys
from sms import SepcapMessagingSystem as SMS


def main():
    if len(sys.argv) < 5:
        print("Not enough arguments", file=sys.stderr)
        # return 1

    print("Hub")

    HubToClass = open(sys.argv[1], 'wb')
    ClassToHub = open(sys.argv[2], 'rb')
    HubToInterface = open(sys.argv[3], 'wb')
    InterfaceToHub = open(sys.argv[4], 'rb')

    std = SMS(sys.stdin, sys.stdout)
    classification = SMS(ClassToHub, HubToClass)

    while 1:
        classification.sentPacket(
            SMS.Address.Classification,
            SMS.Message.EmergencyStop.type,
            SMS.Message.EmergencyStop.Resume
        )

        if classification.isData():
            sys.stdout.write('HUB: ')
            address, mtype, data = classification.readPacket()
            sys.stdout.write(f'{address}, {mtype}, {data}\n')

        if std.isData():
            c = std.read()
            if c == '\x1b':         # x1b is ESC
                break


if __name__ == "__main__":
    main()
