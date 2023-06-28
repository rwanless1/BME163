import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

plt.style.use('BME163')

parser = argparse.ArgumentParser()

'''Adds parser argumentation'''
parser.add_argument('--outputFile','-o',default='Wanless_Ryan_BME163_Assignment_Week4.png',type=str,action='store',help='output file goes here')
parser.add_argument('--identFile', '-i', default='/Users/ryanwanless/Documents/Bme163/BME163_Input_Data_4.ident',type=str,action='store', help = 'input file here')
parser.add_argument('--covFile', '-c', default='/Users/ryanwanless/Documents/Bme163/BME163_Input_Data_4.cov',type=str,action='store', help = 'input file here')
parser.add_argument('--qualsFile', '-q', default='/Users/ryanwanless/Documents/Bme163/BME163_Input_Data_4.quals',type=str,action='store', help = 'input file here')

args = parser.parse_args()

outFile = args.outputFile
identityFile = args.identFile
covFile = args.covFile
qualsFile = args.qualsFile

"""Sets the dimensions of the figure and the panel"""
figureWidth = 4
figureHeight = 5

plt.figure(figsize = (figureWidth,figureHeight))

MainPanelWidth = 3
MainPanelHeight = 4

MainPanel = plt.axes([0.5/figureWidth, 0.65/figureHeight, MainPanelWidth/figureWidth, MainPanelHeight/figureHeight])

'''Sets the axis labels and points'''
MainPanel.set_ylabel('Subread Coverage')
MainPanel.set_xlabel('Identity (%)')

MainPanel.set_xlim(75, 100, 5)
MainPanel.set_ylim(0, 8)
MainPanel.set_yticks([ 1, 3, 5, 7])
MainPanel.set_yticklabels(['1-3', '4-6', '7-9', '>=10'])

'''parsing the data and creating dictionaries and lists'''
in_fh=open(covFile,'r')
barcodeCoverage = {}

for line in in_fh:
    row = line.rstrip().split('\t')
    barcode = row[0]
    coverage = int(row[1])
    barcodeCoverage[barcode] = coverage

in_fh=open(identityFile,'r')
barcodeIdentity = {}

for line in in_fh:
    row = line.rstrip().split('\t')
    barcode = row[0]
    identity = float(row[1])
    barcodeIdentity[barcode] = identity

groups = ['1-3', '4-6', '7-9','>=10' ]
xValues = {group:[] for group in groups}

for barcode, coverage in barcodeCoverage.items():
     x = barcodeIdentity[barcode]
     if coverage <= 3 :
         xValues['1-3'].append(x)

     elif coverage <= 6:
          xValues['4-6'].append(x)

     elif coverage <= 9:
          xValues['7-9'].append(x)

     else:
         xValues['>=10'].append(x)

def swarmplot(yPos, xValues, MainPanel, color):
    xmax =100
    xmin = 75
    width = 0.8
    ymin = 0
    ymax = 8
    xrange=xmax-xmin
    yrange=ymax-ymin
    markersize=1
    placedPoints=[]
    minDist=markersize/72 #how far the distance between the points
    shift=((minDist/20)*xrange)/MainPanelWidth
    for x1 in xValues:
        placed = False
        if len(placedPoints)==0:
            placedPoints.append((yPos, x1))
        else:
            nearPoints=[]
            for cords2 in placedPoints:
                x2,y2 = cords2[0], cords2[1]
                xdist = (np.abs(x1-x2)/xrange)*MainPanelWidth #converts the data space to visual space
                if xdist <= minDist:
                    nearPoints.append(cords2)

            if nearPoints:
                for move in np.arange(0,width,shift):
                    distList = {}
                    for multiplier in [1,-1]:
                        distList[multiplier] = []
                        y1 = yPos + move*multiplier
                        for cords2 in nearPoints:
                            x2,y2 = cords2[0], cords2[1]
                            xdist = (np.abs(x1-x2)/xrange)*MainPanelWidth
                            ydist = (np.abs(y1-y2)/yrange)*MainPanelHeight
                            distance = (xdist**2+ydist**2)**0.5
                            distList[multiplier].append(distance)

                    if min(distList[1]) > minDist or min(distList[-1]) > minDist:
                        placed = True
                        break

                if placed:
                    if min(distList[1]) > minDist:
                        placedPoints.append(((x1, yPos + move)))
                    elif min(distList[-1]) > minDist:
                        placedPoints.append((x1, yPos + (move * (-1))))

                else:
                    break
            else:
                placedPoints.append((x1, yPos))
    #print (placedPoints)
    for coords in placedPoints:
        x,y = coords[0],coords[1]
        MainPanel.plot(x,y,marker='o',mew=0, mfc=color,ms=markersize)



iBlue=(44/255,86/255,134/255)
iOrange=(230/255,87/255,43/255)
iYellow=(248/255,174/255,51/255)
iGreen=(32/255,100/255,113/255)
#print(xValues)
median1 = np.median(xValues['1-3'][:1000])
median2 = np.median(xValues['4-6'][:1000])
median3 = np.median(xValues['7-9'][:1000])
median4 = np.median(xValues['>=10'][:1000])

swarmplot(1, xValues['1-3'][:1000], MainPanel, iBlue)
plt.vlines(median1, ymin=0.2, ymax=1.8, colors='r', linewidth = 0.8)

swarmplot(3, xValues['4-6'][:1000], MainPanel, iGreen)
plt.vlines(median2, ymin=2.2, ymax=3.8, colors='r', linewidth = 0.8)

swarmplot(5, xValues['7-9'][:1000], MainPanel, iYellow)
plt.vlines(median3, ymin=4.2, ymax=5.8, colors='r', linewidth = 0.8)

swarmplot(7, xValues['>=10'][:1000], MainPanel, iOrange)
plt.vlines(median4, ymin=6.2, ymax=7.8, colors='r', linewidth = 0.8)








plt.savefig(outFile, dpi=600)
