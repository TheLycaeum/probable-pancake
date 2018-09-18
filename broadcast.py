#!/usr/bin/env python3

import sys

def return_msg_from_cmdline():
    message = sys.argv[1]
    return message

def main():
    print(return_msg_from_cmdline())



if __name__ == "__main__":
    main()
