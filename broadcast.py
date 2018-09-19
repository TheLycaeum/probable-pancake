#!/usr/bin/env python3

import sys
import dispatcher



def return_msg_from_cmdline():
    message = sys.argv[1]
    return message


if __name__ == '__main__':
    dispatcher.main(return_msg_from_cmdline())
