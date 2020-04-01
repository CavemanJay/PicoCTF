folder=/home/jay/CTF/PicoCTF/2019/unzip/output/
mkdir -p $folder
cd $folder
rm *
wget https://2019shell1.picoctf.com/static/37762a7e5774d7d6c1bc79e8e1758ef9/flag.zip
unzip flag.zip
eog flag.png