#! /usr/bin/python3 -u

import sys
import sms as SMS


def main():
    if len(sys.argv) < 5:
        print("Not enough arguments", file=sys.stderr)
        # return 1

    HtC = open(sys.argv[1], "wb")
    CtH = open(sys.argv[2], "r")

    print("Hub")

    stdin = SMS.SepcapMessagingSystem(sys.stdin)
    sms = SMS.SepcapMessagingSystem(CtH)

    byte = 0x02
    while 1:
        message = sms.encodeMessage(
            sms.Address.Classification,
            sms.Message.EmergencyStop.type,
            sms.Message.EmergencyStop.Resume
        )
        byte += 1
        if (byte >= 256):
            byte = 0x00
        HtC.write(message)

        if sms.isData():
            sys.stdout.write('HUB: ')
            while sms.isData():
                c = sms.read()
                sys.stdout.write(c)
                if c == '\n':         # x1b is ESC
                    break

        if stdin.isData():
            c = stdin.read()
            if c == '\x1b':         # x1b is ESC
                break


if __name__ == "__main__":
    main()
