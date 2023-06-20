import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

plt.style.use('BME163')

parser = argparse.ArgumentParser()


'''Adds parser argumentation'''
parser.add_argument('--outputFile','-o',default='Wanless_Ryan_BME163_Assignment_Final.png',type=str,action='store',help='output file goes here')
parser.add_argument('--psl', '-i', default='/Users/ryanwanless/Documents/Bme163/BME163_Input_Data_6.psl',type=str,action='store', help = 'input file here')
parser.add_argument('--gencode', '-g', default='/Users/ryanwanless/Documents/Bme163/gencode.vM12.annotation.gtf',type=str,action='store', help = 'input file here')
parser.add_argument('--chromosome', '-c', default='chr7:45232000-45241000',type=str,action='store', help = 'input file here')
#not sure how to change the chromosome paramaters   #set as chromosome


args = parser.parse_args()

outFile = args.outputFile
psl = args.psl
gtf = args.gencode
chr = args.chromosome


"""Sets the dimensions of the figure and the panel"""
figureWidth = 5
figureHeight = 5


plt.figure(figsize = (figureWidth,figureHeight))

topPanelWidth = 4
topPanelHeight = 1.5

middlePanelWidth = 4
middlePanelHeight = 1.5


bottomPanelWidth = 4
bottomPanelHeight = 1.5

topPanel = plt.axes([0.1/figureWidth, 3.3/figureHeight, topPanelWidth/figureWidth, topPanelHeight/figureHeight])
middlePanel = plt.axes([0.1/figureWidth, 1.7/figureHeight, middlePanelWidth/figureWidth, middlePanelHeight/figureHeight])
bottomPanel = plt.axes([0.1/figureWidth, 0.1/figureHeight, bottomPanelWidth/figureWidth, bottomPanelHeight/figureHeight])



'''sets tick marks for pannels'''

topPanel.set_xticks([])
topPanel.set_yticks([])

middlePanel.set_xticks([])
middlePanel.set_yticks([])

bottomPanel.set_xticks([])
bottomPanel.set_yticks([])



'''sorts and splits through the chromosome input for the argparser'''
#print(chr)
chr_parts = chr.split(':')
chromosomeNumber = chr_parts[0]
chromosomeCoordinates = chr_parts[1]
chr_range = chromosomeCoordinates.split('-')
chr_start = int(chr_range[0])
chr_end = int(chr_range[1])
iBlue = (88/255, 85/255, 120/255)
# print(chromosomeCoordinates)
#print(chr_range)
#print(chr_start)
# print(chr_end)
'''sets x and y values for panels'''
topPanel.set_xlim(chr_start, chr_end)
middlePanel.set_xlim(chr_start, chr_end)
bottomPanel.set_xlim(chr_start, chr_end)

'''parses through the psl file'''
pslDictionary = {}
pslPloting = []
with open(psl, 'r') as f:
    f.readline()
    for line in f:
        line=line.split('\t')
        chromosome=line[13]
        start=int(line[15])
        end=int(line[16])
        blockstarts=np.array(line[20].split(',')[:-1],dtype=int)
        blockwidths=np.array(line[18].split(',')[:-1],dtype=int)
        if chromosome == chromosomeNumber and (start >= chr_start and start <= chr_end) and (end >= chr_start and end <= chr_end):
            pslPloting.append([start, end, blockstarts, blockwidths, False])

sortPsl = sorted(pslPloting, key = lambda x:x[1])
for y in range (0, len(sortPsl), 1):
    edge = 0
    for values in sortPsl:
        left = values[0]
        right = values[1]
        if not values [4]:
            if left > edge:
                height = 0.05
                rectangle = mplpatches.Rectangle([left,y-(height/2)],right-left,height,facecolor= iBlue ,edgecolor='red',linewidth=0)
                middlePanel.add_patch(rectangle)
                height = 0.5
                for index in range (0, len(values[2]),1):
                    blockstart = values[2][index]
                    blockwidth = values[3][index]
                    rectangle = mplpatches.Rectangle([blockstart,y-(height/2)],blockwidth,height, facecolor= iBlue, edgecolor= iBlue,linewidth=0.05)
                    middlePanel.add_patch(rectangle)
                    for base in range(blockstart, (blockstart+blockwidth), 1):
                        if base in pslDictionary:
                            pslDictionary[base] += 1
                        else:
                            pslDictionary[base] = 1
                edge = right
                values[4] = True
                ymax = y
for bases, numbers in pslDictionary.items():
    bottom = 0
    height = numbers
    width = 1
    rectangle = rectangle = mplpatches.Rectangle([bases, bottom], width, height, facecolor = iBlue, edgecolor = 'black', linewidth = 0)
    bottomPanel.add_patch(rectangle)
    height=1


'''parses throught the gtf file and creates two dictionaries where the key is transcript id and the other exon or cds list'''
with open(gtf, 'r') as f:
    gftDictionaryCDS = {}
    gftDictionaryExon = {}
    #line = f.readlines()
    line=f.readline().split('\t')
    line=f.readline().split('\t')
    line=f.readline().split('\t')
    line=f.readline().split('\t')
    line=f.readline().split('\t')
    line=f.readline().split('\t')
    line=f.readline().split('\t')
     #row = line.rstrip().split('\t')
    #if not line.startswith('##'):
    for line in f:
        line=line.split('\t')
        chromosome=line[0]
        start= int(line[3])
        end=int(line[4])
        feature=line[2]
        if chromosome == chromosomeNumber:
            if feature in ['exon','CDS']:
                metaData=line[8].split('transcript_id')[1].split('"')[0]
                if (chromosome == chromosomeNumber) and (start >= chr_start and end <= chr_end):
                #if feature in ['exon','CDS']:
                    if metaData not in gftDictionaryExon:
                        gftDictionaryExon[metaData] = []
                    gftDictionaryExon[metaData].append((start,end,chromosome,feature))
                #print(gftDictionaryExon)

    for transcript,exons in gftDictionaryExon.items():
        #print(exons)
        startListsort = []
        endListsort = []
        for exon in exons:
            #print(exon)
            #print(exon[0])
            startListsort.append(exon[0])
            endListsort.append(exon[1])

        start=min(startListsort)
        #end2 = sorted(endListsort)
        end=max(endListsort)
                #endListsort = sorted(endListsort, key = max, reverse = True)

                #endListsort = sorted(endListsort, key = max, reverse = True)

                #min(startListsort)
            #print(endListsort)
            #print(startListsort)
             # start #min list
             # end # max list
              #chromosome
              #feature
                #gftDictionaryExon.append

        if chromosome == chromosomeNumber:
            if (start >= chr_start and start <= chr_end) or (end >= chr_start and end <= chr_end):
                gftDictionaryCDS[transcript].append((start,end))
                gftDictionaryExon[transcript].append((start,end))

zeroList = [0]*len(gftDictionaryExon)
ypos = 0
for i in gftDictionaryExon:
    findPosition = []
    for p in gftDictionaryExon[i]:
        for x in p[0:1]:
            findPosition.append(x)
    startP = min(findPosition)
    endP = max(findPosition)
    for j in range(len(zeroList)):
        if zeroList[j] < startP:
            break
    #print(j)
    #print(i)
    ypos = j + 1
    rectangle = mplpatches.Rectangle([startP, ypos - 0.025], endP -startP, 0.05,facecolor = 'grey', edgecolor = 'black', linewidth = 0.05)
    topPanel.add_patch(rectangle)
    for k in gftDictionaryExon[i]:
        blockstart = k[0]
        blockend = k[1]
        if k[2] == 'exon':
            height = 0.25
        if k[2]== 'CDS':
            height = 0.5
        rectangle = mplpatches.Rectangle([blockstart, ypos - (height/2)], blockend-blockstart, height, facecolor = 'grey', edgecolor = 'black', linewidth = 0.25)
        topPanel.add_patch(rectangle)
    zeroList[j] = endP


topPanel.set_ylim(-1,(ymax+1)*1.1)
middlePanel.set_ylim(-1,(ymax+1)*1.1 )
bottomPanel.set_ylim(-1,(ymax+1)*1.1)
#topPanel.set_ylim(-1,(145321394+1))
#print(endP)

                    #print(gftDictionaryCDS)
                    #



plt.savefig(outFile, dpi=2400)
