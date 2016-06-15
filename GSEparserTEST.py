# get sample ID according info :  1. brain region 2. time slot

import re
import os
import matplotlib.pyplot
import numpy

# initialize list
NCX_index=[]
HIP_index=[]
AMY_index=[]
VF_index =[]
DIE_index =[]
URL_index=[]

region_list=[]
HSB_list=[]
stage_list=[]

## sort ID by time slot

# retreive value of
NCX_value=[]
HIP_value=[]
AMY_value=[]
VF_value=[]
DIE_value =[]
URL_value=[]

probe_num=0
probe_num2=0
probe_mat = []
probe_mat_stage=[]

# whole list

with open("601") as f:
  with open("GSE_output", "w") as text_file:

   for line in f.readlines():

     line = line.strip()
    ## should initialize  HSB_list ,and region_list outside
     if re.match("HSB", line):
        HSB_list = line.split('\t')
     if re.match("\w{3}",line) and (re.match("HSB", line)==None):
        region_list = line.split('\t')
     if re.match("^[0-9]{1,2}",line):
        stage_list = line.split('\t')
        print (stage_list)

print(region_list.count("A1C") + region_list.count("AMY"))
print(len(region_list))
print(len(stage_list))
print(len(HSB_list))

## len HSB, stage ,region ==1340
# align all three list in one array
list= []

##################################################################################
#use  region cluster HSBID, 11 NCX, 5 other
#NCX:    OFC, DFC, VFC, MFC, M1C, S1C, IPC,A1C, STC, ITC , V1C
#
#range(len()), start from 0
################################
# use dictionary implementation
################################
# keys = ['a', 'b', 'c']
#>>> values = [1, 2, 3]
#>>> dictionary = dict(zip(keys, values))
#>>> print dictionary
#{'a': 1, 'b': 2, 'c': 3}
for i in range(len(region_list)):
    if (region_list[i] == "OFC" or region_list[i] == "DFC" or region_list[i] == "VFC" or region_list[i] == "MFC"
        or region_list[i] == "M1C" or region_list[i] == " S1C" or region_list[i] == "IPC" or region_list[i] == "A1C"
        or region_list[i] == " STC" or region_list[i] == "ITC" or region_list[i] == "V1C"):
        NCX_index.append(i)

    if (region_list[i] == "HIP"):
        HIP_index.append(i)
    if (region_list[i] == "AMY"):
        AMY_index.append(i)
    if (region_list[i] == "MGE" or region_list[i] == "LGE" or region_list[i] == "CGE" or region_list[i] == "STR"):
        VF_index.append(i)
    if (region_list[i] == "DTH" or region_list[i] == "MD"):
        DIE_index.append(i)

    if (region_list[i] == "CBC"):
        URL_index.append(i)

NCX_stage = []

for i in range(len(NCX_index)):
    NCX_stage.append(stage_list[NCX_index[i]])
    # print(NCX_stage)
    # NCX index, stage > dictionary , sort stage then output NCX index
    #  for NCX_stage,NCX_index in zip(NCX_stage,NCX_index):
    dictNCX = {key: value for key, value in zip(NCX_index, NCX_stage)}
    dictNCX2 = {key: value for key, value in zip(NCX_index, NCX_stage)}
    # QQQ  zip must in iteration for ????
  #  print(dictNCX2)
    #  print (NCX_tage," ", NCX_index)
    # test = sorted(dictNCX.items(), key=lambda (NCX_index,NCX_stage): (NCX_stage,NCX_index))
# ######################################
 #   print("\n")
    # Use the __getitem__ method as the key function
    test2 = sorted(dictNCX, key=dictNCX.__getitem__)
    # test2 return a list !!!!!!!!!!!!!
    # In order of sorted values: [1, 2, 3, 4]
    # test2  has NCX stage sorting get key(NCX index) but the sorting start from 10-15,1-9
   # print(test2)
    #print(type(test2))

with open("2000SubGSE") as GSE_f:
    for Gline in GSE_f:
        if not Gline.startswith("!"):
            Gline = Gline.strip()
            temp = Gline.split('\t')
           # print(len(temp))
           # temp[0] is probe ID
            temp1=temp[1:]
           #print(temp1)

            if len(temp1) == 1340:
                probe_mat.append([])

          # probe matrix_ NCX part
                for i in range(len(NCX_index)):
                    # print(temp[NCX_index[i]+1])
                    probe_mat[probe_num].append(temp1[NCX_index[i] ])
                probe_num += 1
               # print(probe_num)
                for i in range(len(test2)):
                    probe_mat_stage[probe_num_2].append(temp1[test2[i]])
                probe_num_2 += 1
# print(probe_mat)
#########sort by time
#time 0f NCX, same index

#### create a new matrix for NCX data

############################################
#print (len(dictNCX))
#dictNCX= sorted(dictNCX.values())
#dictNCX= sorted(dictNCX.items(),key=lambda x:x[1])
#d = sorted(dictNCX, key = dictNCX.get())

#for id in d:
 #   text = data[id]
#after sorting , output is a list?
#print(dictNCX.get())
#sorted(data.items(), key=lambda x:x[1])
#print dictNCX.key
print ("\n")
#print (dictNCX)
#746

#print(dictNCX())
################################
# use dictionary implementation
################################
# keys = ['a', 'b', 'c']
#>>> values = [1, 2, 3]
#>>> dictionary = dict(zip(keys, values))
#>>> print dictionary
#{'a': 1, 'b': 2, 'c': 3}

################################################################################
import matplotlib.pyplot
import numpy
######plot
#
# intensity= numpy.array(probe_mat[1:][:])
# print (intensity)
# print("\n")
# intensity=numpy.sort(intensity, axis=None)
# print (intensity)
#
# # plot the data in to pcolormesh
# matplotlib.pyplot.pcolormesh(intensity)
# #colorbar to show intensity scale
# matplotlib.pyplot.colorbar()
# matplotlib.pyplot.show()

# nba_norm = (nba - nba.mean()) / (nba.max() - nba.min())
# # Sort data according to Points, lowest to highest
# # This was just a design choice made by Yau
# nba_sort = nba_norm.sort('PTS',ascending=True, inplace=True)
#
# # Plot it out
# fig, ax = plt.subplots()
# heatmap = ax.pcolor(nba_sort, cmap=plt.cm.Blues, alpha=0.8)

