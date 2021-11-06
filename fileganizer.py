#=============AUTHOR=============#
"""
    Autor:      Víctor Velázquez Cid
    Versión:    Beta 1.0
    Ult. actualización: 10/1/21
    
    Blog:       liteshut.blogspot.com
    GitHub:     https://github.com/vvelc
    Contacto:   victorvelazquezcid@gmail.com
    
    Titulo:     Fileganizer

"""

#=============IMPORTS=============#
import os
import shutil
import time
import locale
from colored import color as c

#=============DATA=============#
opsy = os.name #Checks if the OS is Windows or Linux

#=============STRINGS=============#
inp = ">>"
fill = "█"

#=============FORMATS=============#
photo = ['AIS', 'BMP', 'BW', 'CDT', 'CDT', 'CGM', 'CMX', 'CPT', 'DCX', 'DIB', 'EMF', 'GBR',
         'GIF', 'ICO', 'IFF', 'ILBM', 'JFIF', 'JIF', 'JPE', 'JPEG', 'JPG', 'KDC', 'LBM', 
         'MAC', 'PAT', 'PCD', 'PCT', 'PCX', 'PIC', 'PICT', 'PNG', 'PNTG', 'PIX', 'PSD', 
         'PSP', 'QTI', 'QRIF', 'RGB', 'RGBA', 'RIF', 'RLE', 'SGI', 'TGA', 'TIF', 'TIFF', 
         'WMF', 'XCF']

video = ['ASF','AVI','BIK','DIV','DIVX','DVD','IVF','M1V','MOV','MOVIE','MP2V','MP4','MPA',
        'MPE','MPEG','MPG','MPV2','QT','QTL','RPM','SMK','WM','WOB']

audio = ['669','AIF','AIFC','AIFF','AMF','ASF','AU','AUDIOCD','CDA','CDDA','FAR','IT','ITZ',
        'LWV','MID','MIDI','MIZ','MP1','MP2','MP3','MTM','OGG','OGM','OKT','RA','RMI','SND',
        'STM','STZ','ULT','VOC','WAV','WAX','WMA','XM','XMZ']

document = ['CSV', 'DIF', 'DOC', 'DOCHTML', 'DOCX', 'DOT', 'DOTHTML', 'DQY', 'EXC', 'IDX', 
            'LOG', 'PDF', 'POT', 'POTHTML', 'PPA', 'PPS', 'PPT', 'PPTHTML', 'RTF', 'SCP', 
            'SDA', 'SDC', 'SDD', 'SDS', 'SDW', 'SFS', 'SGL', 'SMD', 'SMF', 'STC', 'STD', 
            'STI', 'STW', 'SXC', 'SXD', 'SXG', 'SXI', 'SXM', 'SXW', 'TXT', 'VOR', 'WBK', 
            'WIZ', 'WRI', 'WTX', 'XLA', 'XLB', 'XLB', 'XLD', 'XLK', 'XLL', 'XLS', 'XLSHTML', 
            'XLT', 'XLTHTML', 'XLV', 'XLW', 'XSL']

code = ['ACTION', 'ASHX', 'ASMX', 'ASP', 'ASPX', 'ASX', 'AXD', 'C', 'CFM', 'CLASS', 'CP',
         'CS', 'CSS', 'DO', 'HTM', 'HTML', 'JAR', 'JAV', 'JAVA', 'JHTML', 'JS', 'JSP', 
         'JSPX', 'KT', 'PL', 'PY', 'RB', 'RHTML', 'RSS', 'SHTML', 'SVG', 'SWF', 'VBS', 
         'WSS', 'XHTML', 'XML', 'YAWS']

compressed = ['ACE','ARJ','BZ','BZ2','CAB','GZ','HA','ISO','LHA','LZH','R00','R01','R03',
                'RAR','TAR','TBZ','TBZ2','TGZ','UU','UUE','XXE','ZIP','ZOO']

#=============FUNCTIONS=============#

def clear():
    #Clear the terminal
    global opsy
    os.system("cls" if opsy == "nt" else "clear")
    start()

def start():
    #Startup screen
    print(startm)
    print(options)

def selector():
    global inp
    opt = input("{} ".format(inp))
    return opt

def selected(opt):
    #Convert input to int
    try:
        opt = int(opt)
    except:
        print("Error: Invalid option")
        return
    
    #Option select
    if opt == 1:
        return auto("downloads")
    elif opt == 2:
        return auto("desktop")
    elif opt == 3:
        return manual()
    elif opt == 4:
        global opsy
        os.system("cls" if opsy == "nt" else "clear")
        return exit()
    else:
        print("Error: Invalid option")
        return

def auto(sel):
    global opsy

    #Get system language (Example: en, es)
    lang = locale.getdefaultlocale()[0][:2]

    if sel == "downloads":
        if opsy == "nt":
            path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
        else:
            #Returns path depending on your OS language. Windows doesn't need it
            if lang == "es":
                path = os.path.join(os.path.join(os.path.expanduser('~')), 'Descargas')
            elif lang == "en":
                path = os.path.join(os.path.join(os.path.expanduser('~')), 'Downloads')
            else:
                print("Error: This is not available for your OS language")
    else:
        if opsy == "nt":
            path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        else:
            if lang == "es":
                path = os.path.join(os.path.join(os.path.expanduser('~')), 'Escritorio')
            elif lang == "en":
                path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            else:
                print("Error: This is not available for your OS language")

    #Call the organizer with the path and name of the directory
    return organize(path, sel.capitalize())

def manual():
    print("Enter the {}directory path{}".format(c.GREEN,c.END))
    
    path = selector()

    #Check if directory exists
    if not os.path.exists(path):
        print("Error: Nonexistent directory")
        return
    
    invalidpath = ["/", "C:", "C:/", "C://", "/home", "/etc"]

    if path in invalidpath:
        print("Error: Invalid path")

    else:
        #Call the organizer with the path of the directory
        return organize(path,path)

def pbar(name=None):
    global fill
    for i in range(26):
        print("\r|{0}{1}| {2}%".format(fill*i, "-"*(25-i), i*4), end="")
        time.sleep(0.05)

        if i == 25:
            print("\n")
    if name:
        print("[{0}+{1}] Finished process at {0}{2}{1}".format(c.GREEN,c.END,name))

def organize(path,name):
    print("[{0}+{1}] Scanning directory...".format(c.GREEN,c.END))

    time.sleep(0.5)
    pbar()

    print("[{0}+{1}] Creating missing folders".format(c.GREEN,c.END))
    time.sleep(0.5)

    if not os.path.exists(path + "/Photos"):
        os.mkdir(path + "/Photos")
    
    if not os.path.exists(path + "/Videos"):
        os.mkdir(path + "/Videos")
    if not os.path.exists(path + "/Documents"):
        os.mkdir(path + "/Documents")
    if not os.path.exists(path + "/Compressed"):
        os.mkdir(path + "/Compressed")
    if not os.path.exists(path + "/Audio"):
        os.mkdir(path + "/Audio")
    if not os.path.exists(path + "/Code"):
        os.mkdir(path + "/Code")
    if not os.path.exists(path + "/Other"):
        os.mkdir(path + "/Other")
    
    pbar()

    print("[{0}+{1}] Scanning files...".format(c.GREEN,c.END))

    time.sleep(1.5)
    pbar()

    print("[{0}+{1}] Moving files...".format(c.GREEN,c.END))

    files = os.listdir(path)

    for f in files:
        #Skip folders
        if os.path.isdir("{}/".format(path)+f):
            continue
        
        #Get file name and extension
        _nam, ext = os.path.splitext(f)

        ext = ext.upper()[1:] #Convert extension from ".ext" to "EXT"

        if ext in photo:
            shutil.move(path+"/"+f,"{}/Photos/".format(path))
        elif ext in video:
            shutil.move(path+"/"+f,"{}/Videos/".format(path))
        elif ext in audio:
            shutil.move(path+"/"+f,"{}/Audio/".format(path))
        elif ext in document:
            shutil.move(path+"/"+f,"{}/Documents/".format(path))
        elif ext in code:
            shutil.move(path+"/"+f,"{}/Code/".format(path))
        elif ext in compressed:
            shutil.move(path+"/"+f,"{}/Compressed/".format(path))
        else:
            shutil.move(path+"/"+f,"{}/Other/".format(path))

    time.sleep(0.5)
    pbar()

#=============HOME=============#
startm = c.GREEN + """\
   ___ _ _                    _
  | __(_) |___ __ _ __ _ _ _ (_)______ _ _
  | _|| | / -_) _´ / _´ | ´ \| |_ / -_) ´_|
  |_| |_|_\___\__, \__,_|_||_|_|__\___|_|
              |___/""" + c.END + f"""

[{c.GREEN}+{c.END}] Author: Víctor Velázquez Cid
[{c.GREEN}+{c.END}] Version: Beta 1.0\
"""

options = """ 
Which {0}directory{1} do you want to {0}organize{1}?

[{0}1{1}] Downloads
[{0}2{1}] Desktop
[{0}3{1}] Manual path
[{0}4{1}] Exit
""".format(c.GREEN,c.END)

#=============SCRIPT=============#

clear()

while True:
    #pbar("Desktop")
    #"""
    opcion = selector()
    selected(opcion)

    input("Press any key to continue")

    clear()
    #"""
    #organize("/home/victor/Descargas","Descargas")
