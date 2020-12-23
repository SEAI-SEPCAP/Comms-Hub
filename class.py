#! /usr/bin/python3 -u

import sys
import sms
import kbhit

def receiveMessage(kb):
    line = [kb.getch(), kb.getch()]
    
    if not line:
        return None
    
    return sms.lineToMessage(line)

def main():
    print("Class")

    kb = kbhit.KBHit()
    
    while 1:
        message = receiveMessage(kb)

        if message is not None:
            address, mtype, data = sms.decodeMessage(message)
            print(address, mtype, data)
        else:
            print("None")


if __name__ == "__main__":
    main()
