#! /usr/bin/python3 -u

import sys
import sms as SMS

def main():
    print("Class")

    sms = SMS.SepcapMessagingSystem(open(sys.argv[1], "rb"))
    CtH = open(sys.argv[2], "w")

    while 1:
        if sms.isData():
            address, mtype, data = sms.readPacket()
            print(f'Class: {address} {mtype} {data}', file=CtH)


if __name__ == "__main__":
    main()
