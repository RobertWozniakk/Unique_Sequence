import os
from datetime import datetime
from os.path import exists

class HTMLCreator:
    def __init__(self):
        if exists("raport.html"):
            os.remove("raport.html")

        now = datetime.now()
        self.fulldate = now.strftime("%d-%m-%Y %H:%M:%S")
        self.css = open("style.css", "r")
        self.html = open("raport.html", "w")
        self.html.write(f"""<!DOCTYPE html>
            <html>
            <head>
                <title>Raport z dnia {self.fulldate}</title>
                <style>
                {self.css.read()}
                </style>
            </head>
            <body>
                <div class="container">
                <h1>Raport z dnia {self.fulldate}</h1>
                <table>
                <tr>
                    <th>Input</th>
                    <th>Output</th>
                </tr>\n""")

raport = HTMLCreator()

raport.html.write("<tr>")
inputfile = open(r'C:\Users\grzyb\PycharmProjects\Projekt_Jezyki_Skryptowe\input\in.txt',"r")
raport.html.write(f"<td>{inputfile.read()}</td>\n")

outputfile = open(r'C:\Users\grzyb\PycharmProjects\Projekt_Jezyki_Skryptowe\output\out.txt',"r")
raport.html.write(f"<td>{outputfile.read()}</td>\n")

raport.html.write("</tr>\n")

raport.html.write("</table>")
raport.html.write("</div>")
raport.html.write("</body>")
raport.html.write("</html>")
raport.html.close()