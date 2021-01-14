#! /usr/bin/python3 -u

import sys
from sms import SepcapMessagingSystem as SMS

def main():
    print("Class")

    sms = SMS(open(sys.argv[1], "rb"), open(sys.argv[2], "wb"))

    while 1:
        if sms.isData():
            address, mtype, data = sms.readPacket()
            sms.sentPacket(address, mtype, data)


if __name__ == "__main__":
    main()
