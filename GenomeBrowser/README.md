This python program is a genome browswer in matplotlip :) 

This program uses two files one a psl file that has been uploaded and the other is a gencode gencode.vM12.annotation.gtf file
which is to large to be uploaded but can be found here for download https://www.gencodegenes.org/mouse/release_M12.html

to uploadfiles use argparser:

input: 

-i 'BME163_Input_Data_6.psl' 

-c 'gencode.vM12.annotation.gtf'

output: 

-o 'yournamefilehere'



You can change which region of the genome you want to view in argparser

example: 

-c 'chr7:45232000-45241000'



