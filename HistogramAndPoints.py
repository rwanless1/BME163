import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse


plt.style.use('BME163')

parser = argparse.ArgumentParser()
'''Adds parser argumentation'''
parser.add_argument('--outputFile','-o',default='Wanless_Ryan_BME163_Assignment_Week2.png',type=str,action='store',help='output file goes here')
parser.add_argument('--inputFile', '-i', default='/Users/ryanwanless/Documents/Bme163/BME163_Input_Data_1.txt',type=str,action='store', help = 'input file here')
#input file, have default input
#open file



args = parser.parse_args()

outFile = args.outputFile
inFile = args.inputFile

#print(inFile)



"""Sets the dimensions of the figure and the panel"""
figureWidth = 2
figureHeight = 2

plt.figure(figsize = (figureWidth,figureHeight))

mainPanel1Width = 1
mainPanel1Height = 1

mainPanel2Width = 1
mainPanel2Height = 1

sidePanel1Width = 0.25
sidePanel1Heigth = 1

sidePanel2Width = 0.25
sidePanel2Heigth = 1

topPanel1Width = 1
topPanel1DWidth = 0.25

topPanel2Width = 1
topPanel2DWidth = 0.25
#open path to file
#-i intput argparse


                  #left,bottom, width, height the division is so that you can
                  #define the panel in inches, that is why you
                  #devide by figue width

"""Sets the position of the pannels on the figure"""
mainpanel1 = plt.axes([0.7/figureWidth, 0.3/figureHeight, mainPanel1Width/figureWidth, mainPanel1Height/figureHeight])

mainpanel2 = plt.axes([2.7/figureWidth, 0.3/figureHeight, mainPanel2Width/figureWidth, mainPanel2Height/figureHeight])

sidepanel1 = plt.axes([0.38/figureWidth, 0.3/figureHeight, sidePanel1Width/figureWidth, sidePanel1Heigth/figureHeight])

topPanel1 = plt.axes([0.7/figureWidth, 1.37/figureHeight, topPanel1Width/figureWidth, topPanel1DWidth/figureHeight])

sidepanel2 = plt.axes([2.38/figureWidth, 0.3/figureHeight, sidePanel2Width/figureWidth, sidePanel2Heigth/figureHeight])

topPanel2 = plt.axes([2.7/figureWidth, 1.37/figureHeight, topPanel2Width/figureWidth, topPanel2DWidth/figureHeight])





"""Sets the x and y limits and the tickmarks"""
mainpanel1.set_xlim(0,15,5)
mainpanel1.set_ylim(0,15)

mainpanel2.set_xlim(0,15,5)
mainpanel2.set_ylim(0,20)

mainpanel1.set_yticks([])
mainpanel2.set_yticks([])

topPanel1.set_xlim(0,15)
topPanel1.set_ylim(0,20)

topPanel2.set_xlim(0,15)
topPanel2.set_ylim(0,20)

sidepanel1.set_xlim(20,0)
sidepanel1.set_ylim(0,15,5)

sidepanel2.set_xlim(20,0)
sidepanel2.set_ylim(0,15,5)

topPanel1.set_xticks([])
topPanel2.set_xticks([])

'''Opens and parses the data from the input and converts them to log to normalize data'''

in_fh=open(inFile,'r')

xvalues = []
yvalues = []
for line in in_fh:
    xvalues.append(np.log2(float(line.rstrip().split('\t')[1]) + 1))

    yvalues.append(np.log2(float(line.rstrip().split('\t')[2]) + 1))


in_fh.close()

'''plot the histograms in the side and top panels'''


bins = np.arange(0,16,0.5)

xhisto,bins = np.histogram(yvalues,bins)

for i in range(0,len(xhisto),1):
    left=bins[i]
    bottom=0
    width=bins[i+1]-left
    height=np.log2(xhisto[i]+1)
    rectangle = mplpatches.Rectangle([bottom,left],height,width,
    facecolor=(88/255,85/255,120/255),
    edgecolor='black',
    linewidth=0.3)
    sidepanel1.add_patch(rectangle)

xhisto,bins = np.histogram(xvalues,bins)

for i in range(0,len(xhisto),1):
    left=bins[i]
    bottom=0
    width=bins[i+1]-left
    height=np.log2(xhisto[i]+1)
    rectangle = mplpatches.Rectangle([left,bottom],width,height,
    facecolor=(120/255,172/255,145/255),
    edgecolor='black',
    linewidth=0.3)
    topPanel1.add_patch(rectangle)

'''plot the main pannel with the x and y values'''
mainpanel1.plot(xvalues,yvalues,
    marker='o',
    markerfacecolor=(248/255,174/255,51/255),
    markeredgewidth=0,
    markersize=1.425,
    color='black',
    linewidth=0,
    alpha=0.05,
    )






plt.savefig(outFile, dpi=600)
