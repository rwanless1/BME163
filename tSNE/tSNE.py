
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse
from matplotlib.patheffects import withStroke

plt.style.use('BME163')

parser = argparse.ArgumentParser()
'''Adds parser argumentation'''
parser.add_argument('--outputFile','-o',default='Wanless_Ryan_BME163_Assignment_Week3.png',type=str,action='store',help='output file goes here')
parser.add_argument('--cellFile', '-c', default='/Users/ryanwanless/Documents/Bme163/BME163_Input_Data_Week3.celltype.tsv',type=str,action='store', help = 'input file here')
parser.add_argument('--positionFile', '-p', default='/Users/ryanwanless/Documents/Bme163/BME163_Input_Data_Week3.position.tsv',type=str,action='store', help = 'input file here')
args = parser.parse_args()

outFile = args.outputFile
cellFile = args.cellFile
positionFile = args.positionFile




"""Sets the dimensions of the figure and the panel"""
figureWidth = 4
figureHeight = 4

plt.figure(figsize = (figureWidth,figureHeight))

leftPanelWidth = 3
leftPanelHeight = 3

leftpanel = plt.axes([0.5/figureWidth, 0.5/figureHeight, leftPanelWidth/figureWidth, leftPanelHeight/figureHeight])
leftpanel.set_xlim(-30, 30)
leftpanel.set_ylim(-40, 30)
leftpanel.set_xlabel('tSNE 2')
leftpanel.set_ylabel('tSNE 1')
leftpanel.set_xticks([-30, -20, -10, 0, 10, 20, 30])
#leftpanel.set_yticks([]['test'])


#leftpanel.tick_params(bottom = True, labelbottom = True, left = True, labelleft = False, right = False, labelright = true, top = False, labeltop = False )
#leftpanel.set_xticks(['tSNE 2'])

'''parsing the data and creating dictionaries and lists'''
in_fh=open(cellFile,'r')
barcodeCelltype = {}
in_fh.readline()
for line in in_fh:
    row = line.rstrip().split('\t')
    celltype = row[1]
    barcode = row[2]
    barcodeCelltype[barcode] = celltype

in_fh=open(positionFile,'r')
positionCellx = {}
positionCelly = {}

for line in in_fh:
    row = line.rstrip().split()
    barcode = row[0]
    xPosition = float(row[1])
    yPosistion =float(row[2])
    positionCellx[barcode] = xPosition
    positionCelly[barcode] = yPosistion
xValues = {cellType:[] for cellType in set(barcodeCelltype.values())}
yValues = {cellType:[] for cellType in set(barcodeCelltype.values())}

#barcodes and cells
for barcode, cellType in barcodeCelltype.items():
    #cellType = barcodeCelltype[barcode]
    x = positionCellx[barcode]
    y = positionCelly[barcode]
    xValues[cellType].append(x)
    yValues[cellType].append(y)

'''plots the values of the different cell types'''
#leftpanel.plot(xValues['bCell'], yValues['bCell']), marker = 'o', markerfacecolor = (1,0,0),markeredgewidth=0, color = 'black', linewidth = 0)
leftpanel.plot(xValues['bCell'], yValues['bCell'], marker='o', markersize = 4, markerfacecolor=(239/255,99/255,59/255), markeredgewidth=0.1, color='black', linewidth=0)
leftpanel.plot(xValues['monocyte'], yValues['monocyte'], marker='o', markersize = 4, markerfacecolor=(56/255,66/255,156/255), markeredgewidth=0.1, color='black', linewidth=0)
leftpanel.plot(xValues['tCell'], yValues['tCell'], marker='o', markersize = 4, markerfacecolor=(0.5,0.5,0.5), markeredgewidth = 0.1, color='black', linewidth=0)

leftpanel.text((np.median(xValues['bCell'])), (np.median(yValues['bCell'])), 'bCell', fontsize = 8, color = 'black', style = 'normal', va = 'center', ha = 'center', path_effects=[withStroke(linewidth=1, foreground='white')])
leftpanel.text((np.median(xValues['monocyte'])), (np.median(yValues['monocyte'])), 'monocyte', fontsize = 8, color = 'black', style = 'normal', va = 'center', ha = 'center', path_effects=[withStroke(linewidth=1, foreground='white')])
leftpanel.text((np.median(xValues['tCell'])), (np.median(yValues['tCell'])), 'tCell', fontsize = 8, color = 'black', style = 'normal', va = 'center', ha = 'center', path_effects=[withStroke(linewidth=1, foreground='white')])







plt.savefig(outFile, dpi=600)
