import fcntl
import termios
import sys
import os

def getkey():
    fno = sys.stdin.fileno()

    # get stdin-property.
    attr_old = termios.tcgetattr(fno)

    # disnable stdin-echo, disnable canonical mode.
    attr = termios.tcgetattr(fno)
    attr[3] = attr[3] & ~termios.ECHO & ~termios.ICANON # & ~termios.ISIG
    termios.tcsetattr(fno, termios.TCSADRAIN, attr)

    # set stdin to NONBLOCK.
    fcntl_old = fcntl.fcntl(fno, fcntl.F_GETFL)
    fcntl.fcntl(fno, fcntl.F_SETFL, fcntl_old | os.O_NONBLOCK)

    chr = 0

    try:
        # get key.
        c = sys.stdin.read(1)
        if len(c):
            while len(c):
                chr = (chr << 8) + ord(c)
                c = sys.stdin.read(1)
    finally:
        # reset stdin.
        fcntl.fcntl(fno, fcntl.F_SETFL, fcntl_old)
        termios.tcsetattr(fno, termios.TCSANOW, attr_old)

    return chr

if __name__ == "__main__":
    while 1:
        key = getkey()
        # end by enter-key, display if input key.
        if key == 10:
            break
        elif key:
            print(key)
