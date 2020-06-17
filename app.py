# _*_ coding: utf8 _*_
import os
import sys

from abase.baseapp import runserver

if __name__ == '__main__':
    if sys.argv[1] == 'runserver':
        if len(sys.argv) == 3:
            host = 'localhost'
            port = sys.argv[2]
        else:
            host = sys.argv[2]
            port = sys.argv[3]
        runserver(host, port)





















