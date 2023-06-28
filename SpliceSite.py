import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse
import matplotlib.image as mplimg
#import mappy

plt.style.use('BME163')

parser = argparse.ArgumentParser()

'''Adds parser argumentation'''
parser.add_argument('--outputFile','-o',default='Wanless_Ryan_BME163_Assignment_Week5.png',type=str,action='store',help='output file goes here')
parser.add_argument('--Splice_Seq', '-s', default='/Users/ryanwanless/Documents/Bme163/Splice_Sequences.fasta',type=str,action='store', help = 'input splice sequence file here')
parser.add_argument('--A_png', '-A', default='/Users/ryanwanless/Documents/Bme163/A.png',type=str,action='store', help = 'input A file here')
parser.add_argument('--T_png', '-T', default='/Users/ryanwanless/Documents/Bme163/T.png',type=str,action='store', help = 'input T file here')
parser.add_argument('--C_png', '-C', default='/Users/ryanwanless/Documents/Bme163/C.png',type=str,action='store', help = 'input C file here')
parser.add_argument('--G_png', '-G', default='/Users/ryanwanless/Documents/Bme163/G.png',type=str,action='store', help = 'input G file here')
args = parser.parse_args()

outFile = args.outputFile
Splice_Sequences = args.Splice_Seq
aPNG = args.A_png
tPNG = args.T_png
cPNG = args.C_png
gPNG = args.G_png

A=mplimg.imread(aPNG)
T=mplimg.imread(tPNG)
C=mplimg.imread(cPNG)
G=mplimg.imread(gPNG)

"""Sets the dimensions of the figure and the panel"""
figureWidth = 4
figureHeight = 1.5

plt.figure(figsize = (figureWidth,figureHeight))

leftPanelWidth = 1.5
leftPanelHeight = 0.5

rightPanelWidth = 1.5
rightPanelHeight = 0.5

leftPanel = plt.axes([0.5/figureWidth, 0.6/figureHeight, leftPanelWidth/figureWidth, leftPanelHeight/figureHeight])

rightPanel = plt.axes([2.2/figureWidth, 0.6/figureHeight, rightPanelWidth/figureWidth, rightPanelHeight/figureHeight])

leftPanel.axvline(x=10, color='black', linewidth = 0.5)
rightPanel.axvline(x=10, color='black', linewidth = 0.5 )
'''sets the x any y limits and the labels'''
rightPanel.set_yticks([])
leftPanel.set_yticks([])

#rightPanel.set_xlim(-10,10,5)
leftPanel.set_xlim(0,20,5)
#leftPanel.set_xticks([0,1,2,3,4])
leftPanel.set_xticklabels([-10,-5,0,5,10])

rightPanel.set_xlim(0,20,5)

rightPanel.set_xticklabels([-10,-5,0,5,10])

leftPanel.set_ylim(0,2)
rightPanel.set_ylim(0,2)

leftPanel.set_yticks([ 0,1,2])
leftPanel.set_yticklabels(['0', '1', '2'])

leftPanel.set_xlabel('Distance to\nSplice Site')
rightPanel.set_xlabel('Distance to\nSplice Site')

leftPanel.set_title("5'SS")
rightPanel.set_title("3'SS")

leftPanel.set_ylabel('Bits')

'''parses throught the data'''
in_fh=open(Splice_Sequences,'r')
seqDict = {}
sequence=''
for line in open(Splice_Sequences):
    if line.startswith('>'):
        if sequence:
            seqDict[name]=sequence
            sequence=''
        name=line[1:].strip().split()[0]
    else:
        sequence +=line.strip()

seq3 = []
seq5 = []
for name, sequence in seqDict.items():
    if name.startswith('3'):
        seq3.append(sequence)
    elif name.startswith('5'):
        seq5.append(sequence)
counts5 = [{'A': 0, 'C':0, 'G':0, 'T':0} for i in range(20)]
counts3 = [{'A': 0, 'C':0, 'G':0, 'T':0} for i in range(20)]

for sequence in seq5:
    for i,base in enumerate(sequence):
        counts5[i][base] += 1

for sequence in seq3:
    for i,base in enumerate(sequence):
        counts3[i][base] += 1

'''calculate the frequency of each base at each position and returns it as a dictionary '''

frequency5 = [{'A': 0, 'C':0, 'G':0, 'T':0} for i in range(20)]
frequency3 = [{'A': 0, 'C':0, 'G':0, 'T':0} for i in range(20)]

height3 = [{'A': 0, 'C':0, 'G':0, 'T':0} for i in range(20)]
height5 = [{'A': 0, 'C':0, 'G':0, 'T':0} for i in range(20)]

for dictionary in counts3:
    totalnuc3 = 0
    totalnuc3 = sum(dictionary.values())

for dictionary in counts5:
    totalnuc5 = 0
    totalnuc5 = sum(dictionary.values())

'''calculates height and position for 3' side'''
for i, dictionary in enumerate(counts3):
    Hi3 = 0
    #print(dictionary)
    for key,value in dictionary.items():
        freq3 = dictionary[key]
        freq3 = ((value)/(totalnuc3))
        frequency3[i][key]= freq3
#print (frequency3)
        Hi3 -= ((freq3)*(np.log2(freq3)))
        #print(Hi3)
    Ri3 = (2)-(Hi3)

    for key,value in dictionary.items():
        freq3 = dictionary[key]
        freq3 = value / totalnuc3
        height = ((Ri3) * (freq3))
        height3[i][key]= height


height3sorted = []

for ddic in height3:
    sorted_dict = {k: v for k, v in sorted(ddic.items(), key=lambda x:x[1])}
    height3sorted.append(sorted_dict)

for xpos, dictionary in enumerate(height3sorted):
    ycord = 0

    for nuc, height in dictionary.items():
        if nuc == 'A':
            rightPanel.imshow(A, extent = [xpos, xpos+1, ycord, height+ycord], aspect ='auto', origin = 'upper')
        elif nuc == 'C':
            rightPanel.imshow(C, extent = [xpos, xpos+1, ycord, height+ycord], aspect ='auto', origin = 'upper')
        elif nuc == 'G':
            rightPanel.imshow(G, extent = [xpos, xpos+1, ycord, height+ycord], aspect ='auto', origin = 'upper')
        elif nuc == 'T':
            rightPanel.imshow(T, extent = [xpos, xpos+1, ycord, height+ycord], aspect ='auto', origin = 'upper')

        ycord += height
'''calculates height and position for 3' side'''
for i, dictionary in enumerate(counts5):
    Hi5 = 0
    #print(dictionary)
    for key,value in dictionary.items():
        freq5 = dictionary[key]
        freq5 = value / totalnuc5
        frequency5[i][key]= freq5
#print (frequency3)
        Hi5 -= (freq5)*(np.log2(freq5))
        #print(Hi3)
    Ri5 = (2)-(Hi5)

    for key,value in dictionary.items():
        freq5 = dictionary[key]
        freq5 = value / totalnuc5
        height = ((Ri5) * (freq5))
        height5[i][key]= height


height5sorted = []

for ddic in height5:
    sorted_dict = {k: v for k, v in sorted(ddic.items(), key=lambda x:x[1])}
    height5sorted.append(sorted_dict)

for xpos, dictionary in enumerate(height5sorted):
    ycord = 0

    for nuc, height in dictionary.items():
        if nuc == 'A':
            leftPanel.imshow(A, extent = [xpos, xpos+1, ycord, height+ycord], aspect ='auto', origin = 'upper')
        elif nuc == 'C':
            leftPanel.imshow(C, extent = [xpos, xpos+1, ycord, height+ycord], aspect ='auto', origin = 'upper')
        elif nuc == 'G':
            leftPanel.imshow(G, extent = [xpos, xpos+1, ycord, height+ycord], aspect ='auto', origin = 'upper')
        elif nuc == 'T':
            leftPanel.imshow(T, extent = [xpos, xpos+1, ycord, height+ycord], aspect ='auto', origin = 'upper')

        ycord += height

#print (height3sorted)


        #height3list =


plt.savefig(outFile, dpi=600)
