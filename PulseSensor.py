import serial
import matplotlib.pyplot as plt
from tkinter import *

def drawGraph (drawList):
    plt.cla()
    s = []
    for i in range(50):
        s.append(50)

    x = range(50)
    plt.ion()
    ax = plt.gca()
    plt.cla()
    ax.bar(x, s, align='edge', color = drawList)  
    ax.set_xticks(x)
    ax.set_xticklabels(range(0,50,10))
    plt.axis('off')
    plt.pause(0.1)
    plt.draw()
    plt.ioff()
    plt.show()

def readFromArd(event):
    ser = serial.Serial('COM3', 115200)

    fileIBI = open('IBI.txt', 'w')
    fileIBI.close()

    valueListIBI = []
    drawList = []

    while True :

        listIndex = 0

        while (listIndex != 50):

            valueIBI = str( ser.readline() )
            lenLine = len(valueIBI)
            valueListIBI.append(valueIBI[2:(lenLine-5)])

            if 0 <= int(valueListIBI[listIndex], 10) <= 349:
                drawList.append(str('brown'))
            if 350 <= int(valueListIBI[listIndex], 10) <= 499:
                drawList.append(str('red'))
            if 500 <= int(valueListIBI[listIndex], 10) <= 579:
                drawList.append(str('orange'))
            if 580 <= int(valueListIBI[listIndex],10) <= 649:
                drawList.append(str('yellow'))
            if 650 <= int(valueListIBI[listIndex], 10) <= 799:
                drawList.append(str('green'))
            if 800 <= int(valueListIBI[listIndex], 10) <= 949:
                drawList.append('cyan')
            if 959 <= int(valueListIBI[listIndex], 10) <= 1099:
                drawList.append('blue')
            if 1100 <= int(valueListIBI[listIndex], 10) <= 5000:
                drawList.append('violet')
            print (drawList)

            with open('IBI.txt', 'a') as fileIBI:
                fileIBI.write( str(valueListIBI[listIndex]) )
                fileIBI.write(' ')

            listIndex += 1

            if listIndex == 50:
                with open('IBI.txt', 'a') as fileIBI:
                    fileIBI.write('\n')

        else:
            drawGraph(drawList)

            valueListIBI.clear()
            drawList.clear()


root=Tk()
root.title('PulseSensor')
root.geometry('200x150+300+225')

label1 = Label(root, text = 'Добро пожаловать')
label1.pack()
button1 = Button(root, text = 'Запуск', width = 10, height = 2, bg = 'Grey', fg = 'black', font = 'arial 14')
button1.pack()
button1.bind('<Button-1>', readFromArd)

root.mainloop()

