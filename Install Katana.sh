sudo apt update
sudo apt-get install python3
sudo apt-get install -y python-tk tk-dev libffi-dev libssl-dev pandoc \
        libgmp3-dev libzbar-dev tesseract-ocr xsel libpoppler-cpp-dev libmpc-dev \
        libdbus-glib-1-dev ruby libenchant-dev apktool nodejs groff binwalk \
        foremost tcpflow poppler-utils exiftool steghide stegsnow bison ffmpeg \
        libgd-dev less
mkdir -p ~/repos/
cd ~/repos
git clone https://github.com/JohnHammond/katana.git
cd katana/
python3 -m venv env
source env/bin/activate
python setup.py install
