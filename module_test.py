#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import lib.module as Module

import os
import sys
import fcntl
import termios

if __name__ == "__main__":
    
    with Module.set_raw_mode():
        while 1:
            key = Module.scankey()
            # enterで終了、キー入力があれば表示
            if key == '\n':
                break
            elif key:
                print(repr(key))

