#from sqlalchemy import create_engine
import datetime
import shutil
import pandas as pd
from os.path import join as pjoin
from subprocess import PIPE, run
import matplotlib.pyplot as plt
import subprocess, sys, os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter import messagebox
import ffmpeg
from tktooltip import ToolTip
import zipfile
import threading

#set the window and lable frames

class Fxg(Tk):
    def __init__(self):
        super(Fxg, self).__init__()
        
        self.title("ToolBox")
        self.minsize(250, 180)
        self.BEncode()
        self.BRaudio()
        self.fixMoov()
        self.setEncode()
        self.sufex_Encode()
        self.frame_Encode()
        self.bit_Encode()
        self.imagePerFrame()
        self.frameCunt()
        self.releace()
        self.version_number()
        self.Exit()
        self.Unzip()
        self.Frstlast()
        self.PST_Value()
        self.PST_rep()
        self.Creat_folderB()
        
        
#set the buttons
        
    def  BEncode(self):
        
        t1 = threading.Thread(target=self.reEncode) #set up threading 
        self.BEncode = ttk.Button(width = 16,text = "Re Enecode" ,command = t1.start) # push botton to start funtion
        self.BEncode.grid(column = 1, row = 1) # set button position 
        ToolTip(self.BEncode, msg="Start to Re-encode video") # set tooltip info 
        

    def BRaudio(self):
        t2 = threading.Thread(target=self.removeAduio) #set up threading 
        self.BRaudio = ttk.Button(width = 16,text = "Remove Audio",command = t2.start) # push botton to start funtion
        self.BRaudio.grid(column = 1, row = 2)# set button position 
        ToolTip(self.BRaudio, msg="Remove audio from file")# set tooltip info 

    def fixMoov(self):
        t3 = threading.Thread(target=self.fixmoov)#set up threading 
        self.fixMoov = ttk.Button(width = 16,text = "Fix Moov Atom",command = t3.start)# push botton to start funtion
        self.fixMoov.grid(column = 1, row = 3)# set button position 
        ToolTip(self.fixMoov, msg="repaire missing moov atoms")# set tooltip info 
        
    def setEncode(self):
        t4 = threading.Thread(target=self.setencode)#set up threading 
        self.setEncode = ttk.Button(width = 16,text = "Set Encode",command = t4.start)# push botton to start funtion
        self.setEncode.grid(column = 1, row = 4)# set button position 
        ToolTip(self.setEncode , msg="Set Encode") # set tooltip info 
        

    def imagePerFrame(self):
        t5 = threading.Thread(target=self.framePer)#set up threading 
        self.imagePerFrame = ttk.Button(width = 16,text = "Img Per Frame ",command = t5.start)# push botton to start funtion
        self.imagePerFrame.grid(column = 2, row = 1)# set button position 
        ToolTip(self.imagePerFrame , msg="extra img per frame")# set tooltip info 

    def frameCunt(self):
        t6 = threading.Thread(target=self.framecount) #set up threading 
        self.framecunt = ttk.Button(width = 16,text = "Frame Count ",command = t6.start)# push botton to start funtion
        self.framecunt.grid(column = 2, row = 2)# set button position 
        ToolTip(self.framecunt, msg="Cuts first and last frame of videos")# set tooltip info 

    def releace(self):
        t7 = threading.Thread(target=self.release) #set up threading
        self.releace = ttk.Button(width = 16,text = "Release ",command = t7.start)# push botton to start funtion
        self.releace.grid(column = 2, row = 3)# set button position 
        ToolTip(self.releace, msg="Run though the releace checks")# set tooltip info 

    def Unzip(self):
        t8 = threading.Thread(target=self.Unzipfile) #set up threading
        self.unzip = ttk.Button(width = 16,text = "Unzip ",command = t8.start)# push botton to start funtion
        self.unzip.grid(column = 2, row = 4)# set button position 
        ToolTip(self.unzip, msg="Unzips Visualsoft zip file")# set tooltip info 

    def Frstlast(self):
        t9 = threading.Thread(target=self.Cutfirstlast) #set up threading
        self.frstlast = ttk.Button(width = 16,text = "Cut F/L frame ",command = t9.start)# push botton to start funtion
        self.frstlast.grid(column = 1, row = 5)# set button position 
        ToolTip(self.frstlast, msg="Cuts first and last frame of videos")# set tooltip info 
        
    def PST_rep(self):
        t10 = threading.Thread(target=self.pstEncode) #set up threading
        self.PST_rep = ttk.Button(width = 16,text = "PST repair ",command = t10.start)# push botton to start funtion
        self.PST_rep.grid(column = 2, row = 5)# set button position 
        ToolTip(self.PST_rep, msg="repare video withe PTS")# set tooltip info

    def Creat_folderB(self):
        t11 = threading.Thread(target=self.Creat_folder) #set up threading
        self.exit = ttk.Button(width = 16,text = "Create Folder ",command = t11.start)# push botton to start funtion
        self.exit.grid(column = 1, row = 7)# set button position
        ToolTip(self.exit, msg="Create folders form list")# set tooltip info 
        

    def Exit(self):
        t12 = threading.Thread(target=self.OSExit) #set up threading
        self.exit = ttk.Button(width = 16,text = "Exit ",command = t12.start)# push botton to start funtion
        self.exit.grid(column = 2, row = 7)# set button position 
        ToolTip(self.exit, msg="Close application")# set tooltip info 


        
    #Set the combo and entry boxs

    def  sufex_Encode(self):
         
         self.sufex_Encode = ttk.Combobox(width=8, state='readonly')
         self.sufex_Encode['values']=(".mp4", ".mpg", ".asf") 
         self.sufex_Encode.grid(column = 3, row = 1)# set position 
         self.sufex_Encode.set(".mp4")# Set defual vlaue
         ToolTip(self.sufex_Encode, msg="Select Sufix")# set tooltip info 

         
         
    def  frame_Encode(self):
        
         self.frame_Encode = ttk.Combobox(width=8, state='readonly')
         self.frame_Encode['values']=("25", "29.92", "30", "60") 
         self.frame_Encode.grid(column = 3, row = 2)# set position 
         self.frame_Encode.set("25") # Set defual vlaue
         ToolTip(self.frame_Encode, msg="Select FrameRate")# set tooltip info 

         
    def  bit_Encode(self):
        
         self.bit_Encode = ttk.Combobox(width=8, state='readonly')
         self.bit_Encode['values']=("1", "2", "3", "4","5","6",) 
         self.bit_Encode.grid(column = 3, row = 3)# set position 
         self.bit_Encode.set("1")# Set defual vlaue
         ToolTip(self.bit_Encode, msg="Select BitRate")# set tooltip info 

    def version_number(self):
         self.version_number = ttk.Entry(width=11) 
         self.version_number.grid(column = 3, row = 4)# set position 
         self.version_number.insert(END,"11")# Set defual vlaue
         ToolTip(self.version_number, msg="Type version number")# set tooltip info 
         
    def PST_Value(self):
        self.PST_Value = ttk.Entry(width=11) 
        self.PST_Value.grid(column = 3, row = 5)# set position 
        self.PST_Value.insert(END,"0.50")# Set defual vlaue
        ToolTip(self.PST_Value, msg="Type pst value")     # set tooltip info                         

###~~set the action of each button~~###

    #Rencode video withe same settings
    def reEncode(self): 
    
        folder_selected = filedialog.askdirectory(title="Select folder with files for re-encode")
        
        try:
            sufxset = self.sufex_Encode.get()
        except ValueError:
            messagebox.showinfo("failed to get sufix")
        self.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        self.progress.grid( column = 1, row = 9)

        try:
            os.chdir(folder_selected)
        except ValueError:
            messagebox.showinfo("failed to get folder")

        dest1 = folder_selected + r"/ffmpeg.exe"
        src_path1 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\ffmpeg.exe"
        shutil.copy(src_path1, dest1)
           
        for item in os.listdir(folder_selected):
            
            # loop through items in dir
            if item.endswith(sufxset): # check for extension
                 try:
                     self.update_idletasks()
                     self.progress['value'] += 30
                     file_name = item # get full path of files
                     re = "ffmpeg -fflags +genpts -y -i " + file_name + " -c:v copy -c:a copy new" + file_name
                     subprocess.call(re, shell=True)
                 except ValueError:
                    messagebox.showinfo('Failed to reencode (tool box)','Video Failed')
        
        self.progress.destroy()
        os.remove("ffmpeg.exe")
    # Remove audio from files leaveing a .mp3 file and a mute video     
    def removeAduio(self):
        folder_selected = filedialog.askdirectory(title="Selcte folder with file to have audio removed")
        sufx = self.sufex_Encode.get()
        self.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        self.progress.grid( column = 1, row = 9)
        os.chdir(folder_selected)

        dest1 = folder_selected + r"/ffmpeg.exe"
        src_path1 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\ffmpeg.exe"
        shutil.copy(src_path1, dest1)
        

        for item in os.listdir(folder_selected):
            if item.endswith(sufx): # check for extension
                self.update_idletasks()
                self.progress['value'] += 30
                file_name = item # get full path of files
                check = "ffmpeg -i " + file_name + " -c copy -an  quite"+ file_name
                extract = "ffmpeg -i " + file_name + " -vn -acodec copy " +"just" + file_name
                subprocess.call(check, shell=True)
                self.progress['value'] += 30
                subprocess.call(extract, shell=True)
                


        self.progress.destroy()
        os.remove("ffmpeg.exe")

    def fixmoov(self):
        os.system('cls')
        sufx = ".mp4"
        folder_selected = filedialog.askdirectory(title="Select folder with damaged files") #dmaged files location
        NameOfRef = filedialog.askopenfilename(title="Select folder good ref files")# selcte ref file
        # Copy untrunk file to folder
        #------------------------------
        
        # set destnation for untrunk files
        dest1 = folder_selected + r"/untrunc.exe"
        dest2 = folder_selected + r"/AVCODEC-57.DLL"
        dest3 = folder_selected + r"/AVFORMAT-57.DLL"
        dest4 = folder_selected + r"/AVUTIL-55.DLL"
        dest5 = folder_selected + r"/LIBGCC_S_SEH-1.DLL"
        dest6 = folder_selected + r"/LIBSTDC++-6.DLL"
        dest7 = folder_selected + r"/LIBWINPTHREAD-1.DLL"
        dest8 = folder_selected + r"/SWRESAMPLE-2.DLL"
        
         
        # set the source path for the untrunk files
        src_path1 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\untrunc.exe"
        src_path2 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\AVCODEC-57.DLL"
        src_path3 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\AVFORMAT-57.DLL"
        src_path4 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\AVUTIL-55.DLL"
        src_path5 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\LIBGCC_S_SEH-1.DLL"
        src_path6 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\LIBSTDC++-6.DLL"
        src_path7 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\LIBWINPTHREAD-1.DLL"
        src_path8 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\SWRESAMPLE-2.DLL"
        
        
        # copy the files
        shutil.copy(src_path1, dest1)
        shutil.copy(src_path2, dest2)
        shutil.copy(src_path3, dest3)
        shutil.copy(src_path4, dest4)
        shutil.copy(src_path5, dest5)
        shutil.copy(src_path6, dest6)
        shutil.copy(src_path7, dest7)
        shutil.copy(src_path8, dest8)
       
        #--------------------------------
        
        
        
        
        
        self.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        self.progress.grid( column = 1, row = 9)
        self.update_idletasks()
        self.progress['value'] += 30
    
        
        os.chdir(folder_selected)
        self.progress['value'] += 30
        for item in os.listdir(folder_selected):
            
            if item.endswith(sufx):
            
                self.progress['value'] += 30
                repair = "untrunc.exe " + NameOfRef + " " + item
            
                self.progress['value'] += 50
                subprocess.call(repair, shell=True)
            


        os.remove("untrunc.exe")
        os.remove("AVCODEC-57.DLL")
        os.remove("AVUTIL-55.DLL")
        os.remove("AVFORMAT-57.DLL")
        os.remove("LIBGCC_S_SEH-1.DLL")
        os.remove("LIBSTDC++-6.DLL")
        os.remove("LIBWINPTHREAD-1.DLL")
        os.remove("SWRESAMPLE-2.DLL")

        RemoveRef = NameOfRef + "_fixed.mp4"
    
        dirnameref, filenameref = os.path.split(NameOfRef)
       
        for i in os.listdir(folder_selected):
            
            if i == filenameref:
                os.remove(RemoveRef)
            elif i == NameOfRef:
                os.remove(NameOfRef)

            else:
                self.progress.destroy()
    
            
        self.progress.destroy()
                

    def setencode(self):
        folder_selected = filedialog.askdirectory(title="Select folder with files for reencode")
        sufxset = self.sufex_Encode.get()
        bit = self.bit_Encode.get()
        frame= self.frame_Encode.get()
        self.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        self.progress.grid( column = 1, row = 9)
        os.chdir(folder_selected)

        dest1 = folder_selected + r"/ffmpeg.exe"
        src_path1 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\ffmpeg.exe"
        shutil.copy(src_path1, dest1)

        
           
        for item in os.listdir(folder_selected):
            
            # loop through items in dir
            try:
                if item.endswith(sufxset): # check for extension
                    self.update_idletasks()
                    self.progress['value'] += 30
                    file_name = item # get full path of files
                    re = "ffmpeg -fflags +genpts -y -i " + file_name + " -r "+frame+" new" + file_name
                    subprocess.call(re, shell=True)
            
                    
            except ValueError:
                messagebox.showinfo("failed to re-encode")
            
        self.progress.destroy()
        self.re.destroy()
        os.remove("ffmpeg.exe")

    def framePer(self):
        
        os.system('cls')
        dir_name = filedialog.askdirectory(title="Select folder to have fames extracted")
        extension = self.sufex_Encode.get()
        os.chdir(dir_name)
        self.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        self.progress.grid( column = 1, row = 9)

        dest1 = dir_name + r"/ffmpeg.exe"
        src_path1 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\ffmpeg.exe"
        shutil.copy(src_path1, dest1)
        
        for item in os.listdir(dir_name): # loop through items in dir
            if item.endswith(extension): # check for extension
                self.update_idletasks()
                print(item)
                self.progress['value'] += 30
                file_name = item # get full path of files
                new_name = file_name[:file_name.rfind("@")] # remove @ from name
                re = "ffmpeg -i " + file_name + " "+new_name+"_" + "%04d-CH.png"
                subprocess.call(re, shell=True)
                
        self.progress.destroy()
        os.remove("ffmpeg.exe")

    def framecount(self):
        os.system('cls')
        dir_name = filedialog.askdirectory(title="select the folder where videos to take frame count" )
        extension = self.sufex_Encode.get()
        os.chdir(dir_name)

        dest1 = dir_name + r"/MediaInfo.exe"
        src_path1 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\MediaInfo.exe"
        shutil.copy(src_path1, dest1)
        
        for item in os.listdir(dir_name): # loop through items in dir
            if item.endswith(extension): # check for extension
                
                file_name = item # get full path of files
                re = "MediaInfo --Output=Video;%FrameCount% " + file_name
                ro = "MediaInfo --Output=Video;%Duration/String3% " + file_name
                Fresult = run(re , stdout=PIPE, stderr=PIPE, universal_newlines=True)
                Dresult = run(ro , stdout=PIPE, stderr=PIPE, universal_newlines=True)
                frameC = (Fresult.stdout)  
                messagebox.showinfo(item, "Frame count " + Fresult.stdout + " Avag time " + Dresult.stdout)

        os.remove("MediaInfo.exe")
        
                
    def release(self):
           #set list
        toDo = ["All tests have been past in testing spreadsheet","Release signed off by Mark or Bill?","Release installer built day of release?",
     "Installer tested All applications run, Help file OK, PDFs OK and marked off in testpad.","Check that the version number is correct on the splash screen/about box"," Does a Freash install work.",
     "Does installing over the top of old version work?","Installers for Suite and Review placed in Installations folder on W drive",
     "Previous installers moved to “Installers Superseded” folder.","What’s New file updated on the W drive","What's new use to create Knowledgebase?",
        "What's new use to create Email to clients?","Publish Knowledgebase?","Whats New file attached to Knowledgebase article Whats New File The Latest Updates","Update manuals on Knowledgebase",
        "Publish News article","Update Email list","Complete mail merge to clients","Place release.txt in the w drive"]

        ydate = datetime.date.today() #get date
        dir_name = 'C:\\Users\\douglas.smart\\Desktop\\10.New_Release\\'
        verson = self.version_number.get()
        filepath = pjoin(dir_name+str(ydate)+ "_"+ str(verson)+"_release.txt")
    
        file = open(filepath,"w")#create file
        
        file.close()#close file
        for i in toDo: #loop thouhg list and write output to file
            test = messagebox.askquestion("input",i)
            file = open(filepath,"a")
            #done = input('Yes/No ')
            if test == "yes":
                file.write(i + ">> " + "Yes" +"\r\n")
            elif test == "y":
                file.write(i + ">> " + "Yes" +"\r\n")
            else:
                file.write(i + ">> " + "no" +"\r\n")
        file.write("completed" +" "+ str(ydate) + " " + "by Douglas D Smart")
        file.close()

    def Unzipfile(self):
        os.system('cls')
        dir_name = filedialog.askdirectory()
        os.chdir(dir_name)# change directory from working dir to dir with files
        self.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        self.progress.grid( column = 1, row = 9)

        for item in os.listdir(dir_name): # loop through items in dir
          self.update_idletasks()
          self.progress['value'] += 5
    
          if item.endswith(extension): # check for ".zip" extension
             file_name = os.path.abspath(item) # get full path of files
             zip_ref = zipfile.ZipFile(file_name) # create zipfile object
             zip_ref.extractall(dir_name, pwd = password.encode('cp850','replace'))
             menu.update_idletasks()
             menu.progress['value'] += 5
             zip_ref.close() # close file
             menu.progress['value'] += 5
             os.remove(file_name) # delete zipped file
            
        self.progress.destroy()

    def Cutfirstlast(self):
        os.system('cls')
        dir_name = filedialog.askdirectory(title= "Select folder to have fames cut")
        extension = self.sufex_Encode.get()
        os.chdir(dir_name)
        self.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        self.progress.grid( column = 1, row = 9)

        dest1 = dir_name + r"/ffmpeg.exe"
        src_path1 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\ffmpeg.exe"
        shutil.copy(src_path1, dest1)
        
        for item in os.listdir(dir_name): # loop through items in dir
            if item.endswith(extension):# check for extension
                self.update_idletasks()
                self.progress['value'] += 30
                file_name = item # get full path of files
                new_name = file_name[:file_name.rfind("@")]
                
                re = "ffmpeg -i " + file_name+ " -vf scale=iw*sar:ih,setsar=1 -vframes 1 "+new_name+"first.png"
                do = "ffmpeg -sseof -2 -i " + file_name + " -vf scale=iw*sar:ih,setsar=1 -update 1 -q:v 1 " +new_name+ "last.png"

                    
                subprocess.call(re, shell=True)
                subprocess.call(do, shell=True)
                
                    
                
        self.progress.destroy()
        os.remove("ffmpeg.exe")
    

    def pstEncode(self):
        folder_selected = filedialog.askdirectory(title="Select folder with files for renacode with pts")
        sufxset = self.sufex_Encode.get()
        Pst= self.PST_Value.get()
        self.progress = Progressbar(orient=HORIZONTAL,length=100,  mode='indeterminate')
        self.progress.grid( column = 1, row = 9)
        os.chdir(folder_selected)

        dest1 = folder_selected + r"/ffmpeg.exe"
        src_path1 = r"C:\Users\douglas.smart\Desktop\4.FFMPEG\moov_atom\ffmpeg.exe"
        shutil.copy(src_path1, dest1)
           
        for item in os.listdir(folder_selected):
            
            # loop through items in dir
            if item.endswith(sufxset): # check for extension
                self.update_idletasks()
                self.progress['value'] += 30
                file_name = item # get full path of files
                re = "ffmpeg -fflags +genpts -y -i " + file_name + " -c:a copy -filter:v setpts="+Pst+"*PTS " "_"+file_name
                subprocess.call(re, shell=True)

        self.progress.destroy()
        os.remove("ffmpeg.exe")


    def Creat_folder(self):
         
        try:
            list = filedialog.askopenfilename(filetypes=[("text file", "*.txt")])
        except ValueError:
            raise messagebox.showinfo("Failed to create folders")

        try:
            with open(list) as file:
                names = file.read().splitlines()
        except FileNotFoundError:
            messagebox.showinfo (" Error", "No file selctected")
            sys.exit()
             
        input_folder = filedialog.askdirectory()
        try:
            os.chdir(input_folder)
        except OSError:
            messagebox.showinfo("Error","No Folder selected")
            sys.exit()
            
        try:
             for name in names:
                 if not os.path.exists(name):
                     os.makedirs(name)
                     print(f"Folder '{name}' created.")
                 else:
                     print(f"Folder '{name}' already exists.")
        except ValueError:
            messagebox.showinfo("Error","Failed to create folders")

        print("Folders created successfully.")

        
            
         

    def OSExit(self):
        self.destroy()
        self.quit()
                

fxg = Fxg()
fxg.mainloop()
