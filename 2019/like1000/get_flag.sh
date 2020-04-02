cd like1000
output_folder=output/
mkdir -p $output_folder
cd $output_folder
rm -f *

# for i in {1..1000}
for i in {1000..998}
do
   echo "Welcome $i times"
   pwd
done