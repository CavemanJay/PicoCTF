#!/bin/zsh
rm -rf _dolls.jpg*
binwalk -q -e -M dolls.jpg 
cat **/*flag.txt
