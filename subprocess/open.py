#!/usr/bin/env python3

import time
import subprocess


def open_program(path_name):

    return subprocess.Popen(path_name)

def close_program(p):
    p.terminate()

#p=open_program(["linuxcnc", " /home/john/linuxcnc/configs/sim.axis/axis.ini"])
p=open_program("linuxcnc")
time.sleep(30)
close_program(p)

