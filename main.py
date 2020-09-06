import numpy as np
import shutil
from tkinter import *
from tkinter import ttk


alphabet = ["А","Б","В","Г","Д","Е","Ё","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"," ",",","-","?",".","!","(",")","«","»",'"',"0","1","2","3","4","5","6","7","8","9"]

def kript(key):
    text = read('Text.txt')
    line = makeKriptAlphabet(key)
    text = text.upper()
    row = []
    column = []
    finaltext = ""
    for i in range(len(text)):
        Begram = text[2*i:2*(i+1)]
        for i in Begram:
            temp = line.find(i)
            row.append(temp//6)
            column.append(temp%6)
    for i in range(0, len(row)-2, 2):
        if (column[i] == column[i+1]):
            if(row[i]+1<9):
                    l1 = line[(row[i]+1)*6 + column[i]]
            else:
                l1 = line[column[i]]
            if (row[i+1] + 1 < 9):
                l2 = line[(row[i+1] + 1) * 6 + column[i+1]]
            else:
                l2 = line[column[i+1]]
            finaltext = finaltext + l1 + l2
        else:
            if(row[i] == row[i+1]):
                if (column[i]+1<6):
                    l1 =  line[row[i]*6 + (column[i]+1)]
                else:
                    l1 = line[row[i]]
                if (column[i+1]+1<6):
                    l2 =  line[row[i+1]*6 + (column[i+1]+1)]
                else:
                    l2 = line[row[i+1]]
                finaltext = finaltext + l1 + l2
            else:
                l1 = line[row[i]*6 + column[i+1]]
                l2 = line[row[i+1]*6+column[i]]
                finaltext = finaltext + l1 + l2
    write('Kripto.txt', finaltext)

def dekript(key):
    kod = read('Kripto.txt')
    line = makeKriptAlphabet(key)
    kod = kod.upper()
    row = []
    column = []
    finaltext = ""
    for i in range(len(kod)):
        Begram = kod[2 * i:2 * (i + 1)]
        for i in Begram:
            temp = line.find(i)
            row.append(temp // 6)
            column.append(temp % 6)
    for i in range(0, len(row) - 2, 2):
        if (column[i] == column[i+1]):
            if(row[i]-1>=0):
                    l1 = line[(row[i]-1)*6 + column[i]]
            else:
                l1 = line[8*6 + column[i]]
            if (row[i+1] - 1 >= 0):
                l2 = line[(row[i+1] - 1) * 6 + column[i-1]]
            else:
                l2 = line[8*6 + column[i+1]]
            finaltext = finaltext + l1 + l2
        else:
            if(row[i] == row[i+1]):
                if (column[i]-1>=0):
                    l1 =  line[row[i]*6 + (column[i]-1)]
                else:
                    l1 = line[row[i] + 6]
                if (column[i+1]-1>=0):
                    l2 =  line[row[i+1]*6 + (column[i+1]-1)]
                else:
                    l2 = line[row[i+1]+6]
                finaltext = finaltext + l1 + l2
            else:
                l1 = line[row[i]*6 + column[i+1]]
                l2 = line[row[i+1]*6+column[i]]
                finaltext = finaltext + l1 + l2
    write('Text.txt', finaltext)




def read(file):
    f = open(file, 'r', encoding='UTF-8')
    a = f.read()
    #print(a)
    f.close()
    return a

def write(file, text):
    f = open(file, 'w', encoding='UTF-8')
    f.write(text)
    f.close()

def makeKriptAlphabet(key):
    key.upper()
    table = []
    line = ""
    for i in key:
        if (line.find(i) == -1):
            line = line + i
    line = line.upper()
    for i in alphabet:
        if (line.find(i) == -1):
            line = line + i
    # for i in range(0, 6):
    #     table.append(line[6*i:6*(i+1)])
    # table[5] = table[5] + " ,-"
    return line


root = Tk()
root.title("Машина Шифрования")
if("a" == "A"):
    print("+")

Label(root, text = "Ключ").grid(row = 1, column = 0)
Key = Entry(root, width = 15)
Key.grid(row = 1, column = 1)
print(len(alphabet))
Button(root, text = "Шифровать", width = 10, command = lambda: kript(Key.get())).grid(row = 2, column = 0, pady = 5, padx = 5)
Button(root, text = "Дешифровать", width = 10, command = lambda: dekript(Key.get())).grid(row = 2, column = 1, pady = 5, padx = 5)
root.mainloop()