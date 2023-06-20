import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

plt.style.use('BME163')

parser = argparse.ArgumentParser()


'''Adds parser argumentation'''
parser.add_argument('--outputFile','-o',default='Wanless_Ryan_BME163_Assignment_Week6.png',type=str,action='store',help='output file goes here')
parser.add_argument('--exp', '-e', default='/Users/ryanwanless/Documents/Bme163/BME163_Input_Data_Assignment6.exp',type=str,action='store', help = 'input file here')
parser.add_argument('--phase', '-p', default='/Users/ryanwanless/Documents/Bme163/BME163_Input_Data_Assignment6.phase',type=str,action='store', help = 'input file here')

args = parser.parse_args()

outFile = args.outputFile
expo = args.exp
phase = args.phase


"""Sets the dimensions of the figure and the panel"""
figureWidth = 5
figureHeight = 3

plt.figure(figsize = (figureWidth,figureHeight))

MainPanelWidth = 0.75
MainPanelHeight = 2.5

smallPanelWidth = 0.1
smallPanelHeight = 0.2

MainPanel = plt.axes([0.5/figureWidth, 0.3/figureHeight, MainPanelWidth/figureWidth, MainPanelHeight/figureHeight])

smallPanel = plt.axes([1.30/figureWidth, 1.45/figureHeight, smallPanelWidth/figureWidth, smallPanelHeight/figureHeight])

'''sets labels of pannels'''

smallPanel.set_xticks([])
smallPanel.set_yticks([])

MainPanel.set_ylabel('Number of genes')
MainPanel.set_xlabel('CT')

'''sets the x and y limits of pannels '''
smallPanel.set_ylim(0,101)
smallPanel.set_xlim(0,1)

MainPanel.set_xlim(0,24)

'''sets tickpmarks of panels'''
MainPanel.set_xticks([1.5, 4.5, 7.5, 10.5, 13.5, 16.5, 19.5, 22.5],['0','','6','','12','','18',''])

'''Creating the heatmap'''

viridis5 = (253/255, 231/255, 37/255)
viridis4 = (94/255, 201/255, 98/255)
viridis3 = (33/255, 145/255, 140/255)
viridis2 = (59/255, 82/255, 139/255)
viridis1 = (68/255, 1/255, 84/255)

R1=np.linspace(viridis1[0],viridis2[0],25)
R2=np.linspace(viridis2[0],viridis3[0],25)
R3=np.linspace(viridis3[0],viridis4[0],25)
R4=np.linspace(viridis4[0],viridis5[0],26)

G1=np.linspace(viridis1[1],viridis2[1],25)
G2=np.linspace(viridis2[1],viridis3[1],25)
G3=np.linspace(viridis3[1],viridis4[1],25)
G4=np.linspace(viridis4[1],viridis5[1],26)


B1=np.linspace(viridis1[2],viridis2[2],25)
B2=np.linspace(viridis2[2],viridis3[2],25)
B3=np.linspace(viridis3[2],viridis4[2],25)
B4=np.linspace(viridis4[2],viridis5[2],26)


R = list(R1)+list(R2)+list(R3)+list(R4)
G = list(G1)+list(G2)+list(G3)+list(G4)
B = list(B1)+list(B2)+list(B3)+list(B4)

'''parses through the two data files normalizes the data and plots them'''

in_fh=open(expo,'r')
barcodeExpression = {}
normalizedBarcodeExpression = {}
in_fh.readline()
for line in in_fh:
    row = line.rstrip().split('\t')
    expression = [float(x) for x in row[4:]]
    #print(expression)
    barcode = row[1]
    #print(barcode)
    barcodeExpression[barcode] = expression
    FPKMList = []
    for i in expression:
        norm_values=((i-min(expression))/(max(expression)-min(expression)))*100
        FPKMList.append(norm_values)
    normalizedBarcodeExpression[barcode] = FPKMList

#print(sortedBarcodeExpression)

MainPanel.set_ylim(0,len(normalizedBarcodeExpression))

in_fh=open(phase,'r')
barcodephase = {}
in_fh.readline()
for line in in_fh:
    row = line.rstrip().split('\t')
    phase = row[1]
    barcode = row[0]
    #print(barcode)
    barcodephase[barcode] = phase
    #print(barcodephase)
y = 0
for barcode, phase in sorted(barcodephase.items(), key=lambda x: -float(x[1])):
    #barcode = float(barcode)
    expressionnNorm = normalizedBarcodeExpression[barcode]
    for pos in range(0,len(expressionnNorm),1):
        x=expressionnNorm[pos]
        rectangle = mplpatches.Rectangle([pos*3,y], 3, 1, facecolor=(R[int(x)],G[int(x)],B[int(x)]), edgecolor='black', linewidth=0)
        MainPanel.add_patch(rectangle)
    y+=1









viridis5 = (253/255, 231/255, 37/255)
viridis4 = (94/255, 201/255, 98/255)
viridis3 = (33/255, 145/255, 140/255)
viridis2 = (59/255, 82/255, 139/255)
viridis1 = (68/255, 1/255, 84/255)

R1=np.linspace(viridis1[0],viridis2[0],25)
R2=np.linspace(viridis2[0],viridis3[0],25)
R3=np.linspace(viridis3[0],viridis4[0],25)
R4=np.linspace(viridis4[0],viridis5[0],26)

G1=np.linspace(viridis1[1],viridis2[1],25)
G2=np.linspace(viridis2[1],viridis3[1],25)
G3=np.linspace(viridis3[1],viridis4[1],25)
G4=np.linspace(viridis4[1],viridis5[1],26)


B1=np.linspace(viridis1[2],viridis2[2],25)
B2=np.linspace(viridis2[2],viridis3[2],25)
B3=np.linspace(viridis3[2],viridis4[2],25)
B4=np.linspace(viridis4[2],viridis5[2],26)


fullRList = list(R1)+list(R2)+list(R3)+list(R4)
fullGList = list(G1)+list(G2)+list(G3)+list(G4)
fullBList = list(B1)+list(B2)+list(B3)+list(B4)

smallPanel.yaxis.tick_right()  # Place ticks on the right side
smallPanel.yaxis.set_ticks([0.5, 100.5])
smallPanel.yaxis.set_ticklabels(['Min', 'Max'])





for ypos in range(0,101,1):
  rectangle = mplpatches.Rectangle([0,ypos],1,100,
  facecolor=(fullRList[ypos], fullGList[ypos], fullBList[ypos]),
  edgecolor='red',linewidth=0)
  smallPanel.add_patch(rectangle)













plt.savefig(outFile, dpi=600)
