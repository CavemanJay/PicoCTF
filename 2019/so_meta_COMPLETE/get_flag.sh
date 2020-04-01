folder=/home/jay/CTF/PicoCTF/2019/so_meta/
img_name=pico_img.png

function MethodOne(){
    identify -verbose $img_name | grep -oE picoCTF{.*}
}

function MethodTwo(){
    strings $img_name | grep -oE picoCTF{.*}
}

function DeleteImage(){
    rm -f $img_name
}

cd $folder
DeleteImage
wget -q https://2019shell1.picoctf.com/static/707dcf0533b53e911b2f7496ebdf9a72/pico_img.png
# MethodOne
MethodTwo
DeleteImage