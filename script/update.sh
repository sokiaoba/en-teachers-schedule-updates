#!/bin/sh

HERE=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
python $HERE/../lib/Main.py
