#! /usr/bin/python3 -u

import sys
import sms

def main():
    if len(sys.argv) < 5:
        print("Not enough arguments", file=sys.stderr)
        #return 1
    
    HtC = open(sys.argv[1], "wb")
    #CtH = open(sys.argv[2], "rb")

    print("Hub")
    
    message = sms.encodeMessage(4, 9, 0x02)

    while 1:
        HtC.write(message)
    

if __name__ == "__main__":
    main()
