# 0616  from   http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL5175
## probe ID to gene name , select NM, NR gene ....and probe ID pair

import re
import os
import matplotlib.pyplot
import numpy

FA=[]
with open("1000ENSG") as f:
 with open('firstL_ENSG') as g:
  with open("ENSG_out.txt", "w") as text_file:
   # with open("GSE_output", "w") as text_file:
    for lineg, line in zip(g, f):
    #for lineg in g.readlines():
            text_file.write("\n")
            text_file.write(str(lineg).rstrip() + "\t")
   # for line in f.readlines():
         #line in f.readlines():
            line = line.strip()
            line = line.split('\t')

            if re.findall("NR_\d+", str(line)) or re.findall("NM_\d+",str(line)):
                NR =set(re.findall("NR_\d+", str(line)))
                NM = set(re.findall("NM_\d+", str(line)))
               # print(NR)
               # print(NM)
                NM_NR= NR.union(NM)
                text_file.write(','.join(NM_NR)+"\t")
            else :
                text_file.write(".\t")
                #print (set(NM_NR))

                ## should initialize  HSB_list ,and region_list outside
            if re.findall(":ENSG\d+", str(line)):
                ENSG=set( re.findall("ENSG\d+", str(line)))
                text_file.write(','.join(ENSG)+"\t")
            else:
                text_file.write(".\t")

               # print (set(ENSG))

          # #      probeID_list = line.split('\t')
           #  re.match(":ENSG\d+", line)


           # pat = '[ENSG0-9]+'

           # print(  type( re.findall(pat, line)))
