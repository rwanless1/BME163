import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

plt.style.use('BME163.mplstyle')

parser = argparse.ArgumentParser()

parser.add_argument('--outputFile','-o',default='Wanless_Ryan_BME163_Assignment_Week1.png',type=str,action='store',help='output file goes here')

args = parser.parse_args()

outFile = args.outputFile




figureWidth = 5
figureHeight = 2

plt.figure(figsize = (figureWidth,figureHeight))

panel1Width = 1
panel1Height = 1

panel2Width = 2
panel2Height = 1
                  #left,bottom, width, height the division is so that you can
                  #define the panel in inches, that is why you
                  #devide by figue width
panel1 = plt.axes([0.2/figureWidth, 0.2/figureHeight, panel1Width/figureWidth, panel1Height/figureHeight])
#this number you would do it bigger .3 and 1.8

panel2 = plt.axes([1.7/figureWidth, 0.2/figureHeight, panel2Width/figureWidth, panel2Height/figureHeight])

'''removing the tick marks for the rectagles '''
panel1.set_xticks([]) #removed ticks in the x axis
panel1.set_yticklabels([]) #removed labels in the x axis
panel1.set_xticklabels([])
panel1.set_yticks([])
panel1.set_xlim(-1,14) #to make the circle smaller
panel1.set_ylim(0,16) # to make the circle smaller

panel2.set_xticks([]) #removed ticks in the y axis
panel2.set_yticklabels([]) #removed labels in the y axis
panel2.set_xticklabels([])
panel2.set_yticks([])
panel2.set_ylim(-1,1)
panel2.set_ylim(-1,1)
panel2.set_xlim(0,101)

panel2.axhline(y=0, color='black', linewidth=0.75)
#panel2.hlines(0, -1, 1, linewidth=1, color='black')

'''creating the circle for first rectangle''' # i cannot shrink the size of the circle
CircleColors = [(225/255,13/255,50/255),(242/255,50/255,54/255), (239/255,99/255,59/255), (244/255,138/255,30/255), (248/255,177/255,61/255),
              (143/255,138/255,86/255), (32/255,100/255,113/255), (42/255,88/255,132/255), (56/255,66/255,156/255), (84/255,60/255,135/255),
              (110/255,57/255,115/255), (155/255,42/255,90/255)]

for i in range(1,13):
  xvalues = []
  yvalues = []


  for r in np.arange(0, 6.3, 0.001):
    x=np.cos(r) + i
    y=np.sin(r) + 8
    xvalues.append(x)
    yvalues.append(y)

  panel1.plot(xvalues, yvalues, marker='o', markerfacecolor=CircleColors[i-1], markeredgewidth=0, markersize=1,linewidth=0)

'''Creating the heatmaps for the second rectangle'''
viridis5 = (253/255, 231/255, 37/255)
viridis4 = (94/255, 201/255, 98/255)
viridis3 = (33/255, 145/255, 140/255)
viridis2 = (59/255, 82/255, 139/255)
viridis1 = (68/255, 1/255, 84/255)

plasma5 = (237/255, 252/255, 27/255)
plasma4 = (245/255, 135/255, 48/255)
plasma3 = (190/255, 48/255, 101/255)
plasma2 = (87/255, 0/255, 151/255)
plasma1 = (15/255, 0/255, 118/255)

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

R1P=np.linspace(plasma1[0],plasma2[0],25)
R2P=np.linspace(plasma2[0],plasma3[0],25)
R3P=np.linspace(plasma3[0],plasma4[0],25)
R4P=np.linspace(plasma4[0],plasma5[0],26)

G1P=np.linspace(plasma1[1],plasma2[1],25)
G2P=np.linspace(plasma2[1],plasma3[1],25)
G3P=np.linspace(plasma3[1],plasma4[1],25)
G4P=np.linspace(plasma4[1],plasma5[1],26)

B1P=np.linspace(plasma1[2],plasma2[2],25)
B2P=np.linspace(plasma2[2],plasma3[2],25)
B3P=np.linspace(plasma3[2],plasma4[2],25)
B4P=np.linspace(plasma4[2],plasma5[2],26)

fullRPList = list(R1P)+list(R2P)+list(R3P)+list(R4P)
fullGPList = list(G1P)+list(G2P)+list(G3P)+list(G4P)
fullBPList = list(B1P)+list(B2P)+list(B3P)+list(B4P)

#creates the heatmap for top part
for xpos in range(0,101,1):
  rectangle = mplpatches.Rectangle([xpos,0],1,-10,
  facecolor=(fullRList[xpos], fullGList[xpos], fullBList[xpos]),
  edgecolor='red',linewidth=0)
  panel2.add_patch(rectangle)

#creates the heatmap for the bottom part
for xpos in range(0,101,1):
  rectangle = mplpatches.Rectangle([xpos,0],1,10,
  facecolor=(fullRPList[xpos],fullGPList[xpos],fullBPList[xpos]),
  edgecolor='red',linewidth=0)
  panel2.add_patch(rectangle)



plt.savefig(outFile, dpi=600)
