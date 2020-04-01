function DeleteImage(){
    rm -f buildings.png
}
cd what_lies_within
DeleteImage
wget -q https://2019shell1.picoctf.com/static/aec3861fc4d5bce4d39dc0db196426de/buildings.png 
zsteg -a buildings.png | grep -oE picoCTF{.*}
DeleteImage