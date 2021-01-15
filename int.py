#! /usr/bin/python3 -u

import sys
from sms import SepcapMessagingSystem as SMS

def main():

    sms = SMS(open(sys.argv[1], "rb"), open(sys.argv[2], "wb"))

    print("Int")
    while 1:
        if sms.isData():
            address, mtype, data = sms.readPacket()
            print(f'Int: {address}, {mtype}, {data}')
            sms.sendPacket(SMS.Address.Individualization, mtype, data)


if __name__ == "__main__":
    main()
