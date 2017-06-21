#!/usr/bin/env sh

echo testing pi.py
python pi.py -n 100

echo testing texturegen.py
python texturegen.py -o out.png --noshow -n 10 -b 1 -m rand3
python texturegen.py -o out2.png --noshow -n 100 -b 2 -m rand1

echo tests complete
