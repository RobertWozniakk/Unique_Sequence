import os.path

cd = os.path.dirname(os.path.abspath(r'C:\Users\grzyb\PycharmProjects\Projekt_Jezyki_Skryptowe\output\out.txt'))
open(os.path.join(cd,r'C:\Users\grzyb\PycharmProjects\Projekt_Jezyki_Skryptowe\output\out.txt'))
with open(r'C:\Users\grzyb\PycharmProjects\Projekt_Jezyki_Skryptowe\input\in.txt',"r") as file:
    n = file.read()
s = ""
final=""
for i in range(int(n)*3):
    if bin(i).count(("1"))%2==0:
        s+="0"
    else:
        s+="1"
s = s.replace("11","a")
s = s.replace("1","b")
s = s.replace("00","c")
s = s.replace("0","")
if(int(n)<=0):
    print(0)
    outputfile = open(r'C:\Users\grzyb\PycharmProjects\Projekt_Jezyki_Skryptowe\output\out.txt',"w")
    outputfile.write(str(0))
if(int(n)==1):
    print("a")
    print(1)
    outputfile = open(r'C:\Users\grzyb\PycharmProjects\Projekt_Jezyki_Skryptowe\output\out.txt', "w")
    outputfile.write("a " + str(1))
if(int(n)==2):
    print("ab")
    print(2)
    outputfile = open(r'C:\Users\grzyb\PycharmProjects\Projekt_Jezyki_Skryptowe\output\out.txt', "w")
    outputfile.write("ab " + str(2))
if(int(n)==3):
    print("aba")
    print(2)
    outputfile = open(r'C:\Users\grzyb\PycharmProjects\Projekt_Jezyki_Skryptowe\output\out.txt', "w")
    outputfile.write("aba " + str(2))
if(int(n)>=4):
    for i in range(int(n)):
        final+=s[i]
    print(final)
    print(3)
    outputfile = open(r'C:\Users\grzyb\PycharmProjects\Projekt_Jezyki_Skryptowe\output\out.txt', "w")
    outputfile.write(f"{final} " + str(3))