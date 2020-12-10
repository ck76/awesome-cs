#!/bin/sh

#for file in `find ./ -name "*.java"`;
for file in $./*;
do
echo convering : $file
iconv -f GBK -t utf-8 $file > $file.t
mv $file.t $file
done
echo DONE