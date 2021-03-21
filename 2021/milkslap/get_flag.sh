#!/bin/bash

[[ -f concat_v.png ]] || wget http://mercury.picoctf.net:29522/concat_v.png; zsteg concat_v.png | grep -oE "picoCTF{.*}"