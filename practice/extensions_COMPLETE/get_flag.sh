# eog https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt
# feh https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt

tesseract flag.txt out -l eng && cat out.txt | head -n 1 && rm out.txt