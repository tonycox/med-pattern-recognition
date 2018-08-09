#!/bin/sh

gcc main.c -ansi -Wall -O2 -D_LARGEFILE64_SOURCE -D_LARGEFILE_SOURCE -o nk2edf

mkdir ../build
mv nk2edf ../build
