#! /usr/bin/python3 -u

import sys
import sms as SMS


def main():
    if len(sys.argv) < 5:
        print("Not enough arguments", file=sys.stderr)
        # return 1

    print("Hub")

    stdin = SMS.SepcapMessagingSystem(sys.stdin, sys.stdout)
    sms = SMS.SepcapMessagingSystem(open(sys.argv[2], "rb"), open(sys.argv[1], "wb"))

    while 1:
        sms.sentPacket(
            sms.Address.Classification,
            sms.Message.EmergencyStop.type,
            sms.Message.EmergencyStop.Resume
        )

        if sms.isData():
            sys.stdout.write('HUB: ')
            address, mtype, data = sms.readPacket()
            sys.stdout.write(f'{address}, {mtype}, {data}\n')

        if stdin.isData():
            c = stdin.read()
            if c == '\x1b':         # x1b is ESC
                break


if __name__ == "__main__":
    main()
