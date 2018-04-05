#!/bin/sh

Folder_A="../individual_stocks_5yr/"  
for file_a in ${Folder_A}/*; do  
    temp_file=`basename $file_a`  
    tail -9 $file_a > $temp_file
done   