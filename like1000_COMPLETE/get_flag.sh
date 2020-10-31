output_folder=output/
mkdir -p $output_folder
cd $output_folder
rm -f *
wget https://2019shell1.picoctf.com/static/8694f84879d3b7c0dcf775930f4665fc/1000.tar

for i in {1000..1}
do
   tar -xvf "$i.tar"
   rm "$i.tar"
done

rm filler.txt
eog flag.png