#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import fcntl
import termios

class set_raw_mode():
    def __enter__(self):
        self.fno = fno = sys.stdin.fileno()

        # 現在の設定を保存
        self.termios = termios.tcgetattr(fno)
        self.fcntl = fcntl.fcntl(fno, fcntl.F_GETFL)

        # stdinのエコー無効、カノニカルモード無効
        attr = termios.tcgetattr(fno)
        attr[3] &= ~termios.ECHO & ~termios.ICANON # & ~termios.ISIG
        termios.tcsetattr(fno, termios.TCSANOW, attr)

        # stdinをNONBLOCKに設定
        fcntl.fcntl(fno, fcntl.F_SETFL, self.fcntl | os.O_NONBLOCK)

    def __exit__(self, *args):
        termios.tcsetattr(self.fno, termios.TCSANOW, self.termios)
        fcntl.fcntl(self.fno, fcntl.F_SETFL, self.fcntl)

def scankey():
    # キーを取得
    s = ''
    c = sys.stdin.read(8)
    while c:
        s += c
        c = sys.stdin.read(8)
    return s

def getkey():
    with set_raw_mode():
        return scankey()

if __name__ == "__main__":
    with set_raw_mode():
        while 1:
            key = scankey()
            # enterで終了、キー入力があれば表示
            if key == '\n':
                break
            elif key:
                print(repr(key))

