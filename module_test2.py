#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import lib.module as Module
from multiprocessing import Manager, Value, Process
from ctypes import c_char_p
import time
import keyboard
import getch

# def keyInput(gl_curr_key):
def keyInput(gl_curr_key):
    while True:
        # if keyboard.is_pressed('q'):
        if keyboard.is_pressed(' '):
           gl_curr_key.value = "piyo"

def Print(gl_curr_key):
    while 1:
        time.sleep(1)
        print(gl_curr_key.value)

if __name__ == "__main__":
    manager = Manager()
    # gl_curr_key = Value(c_char_p, "hoge")
    gl_curr_key = manager.Value(c_char_p, "hoge")
    input_process = Process(target=keyInput, args=[gl_curr_key, ])
    print_process = Process(target=Print, args=[gl_curr_key, ])
    
    input_process.start()
    print_process.start()

    input_process.join()
    print_process.join()

    # keyInput()
    

