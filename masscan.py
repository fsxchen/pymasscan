#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: masscan.py
Description: 
Created_Time: 2016-10-19 15:41:07
Last modified: 2017-05-22 14时22分37秒
'''

_author = 'arron'
_email = 'fsxchen@gmail.com'

import os
import subprocess
from datetime import datetime


s = subprocess.Popen("which masscan", shell=True, stdout=subprocess.PIPE)
s_path, _ = s.communicate()

MASSCAN = s_path.decode("utf-8").strip("\n")

def masscan(target, port):
    filename = "{datetime}_{port}.json".format(datetime=datetime.now().strftime("%Y%m%d%H%M%S"),
            port=port)
    CMD = "{masscan} {target} -p{port} --banners --output-format json --output-filename {filename}".format(
            masscan=MASSCAN, target=target, port=port, filename=filename)
    s = subprocess.Popen(CMD, shell=True, stdout=subprocess.PIPE)
    s.wait()
    print CMD

if __name__ == "__main__":
    target_list = []
    with open(filename) as fd:
        for l in fd:
            target_list.append(l.strip())
    import sys
    port = sys.argv[1]
    masscan(",".join(target_list), port)


