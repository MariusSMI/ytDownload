from tkinter import *
from tkinter import filedialog
import subprocess

# Global variables

path = ""
mp4 = True
mp3 = False

# Functions

def askDirectory():
    global path
    path = filedialog.askdirectory()
    folder_stat["text"] = path

def convert(link):
    global path, mp4, mp3
    status_text["text"] = "Everything is good!"
    if link != "":
        if mp4:
            result = subprocess.run(["yt-dlp", "-P", path, "-i", "-f" "best[height<=1080]", link])
            if result.returncode != 0:
                status_text["text"] = "Error. Put a valid link"
        if mp3:
            result = subprocess.run(["yt-dlp", "-P", path , "-i", "-x", "--audio-format", "mp3", link])
            if result.returncode != 0:
                status_text["text"] = "Error. Put a valid link"
    else:
        status_text["text"] = "Error. Put a valid link"

def changeToMp4():
    global mp4, mp3
    mp4 = True
    mp3 = False
    if mp4:
        format_mp4["background"] = "#007acc"
        format_mp4["highlightbackground"] = "#007acc"
        format_mp3["background"] = "gray"
        format_mp3["highlightbackground"] = "gray"

def changeToMp3():
    global mp4, mp3
    mp4 = False
    mp3 = True
    if mp3:
        format_mp4["background"] = "gray"
        format_mp4["highlightbackground"] = "gray"
        format_mp3["background"]="#007acc"
        format_mp3["highlightbackground"] = "#007acc"

root = Tk()
root.title("ytDonwload")
root.geometry("500x300")
root.resizable(False, False)
root["background"] = "#1e1e1e"

# Widgets and Frames

# 1
folder_frame = Frame(root)
folder_frame.pack()
folder_frame["background"] = "#1e1e1e"

folder_btn = Button(folder_frame, text=f"Folder", background="yellow", highlightbackground="yellow", command=askDirectory)
folder_btn.grid(row=0, column=1, padx=20, pady=20)
folder_stat = Label(folder_frame, text="None", highlightbackground="#1e1e1e")
folder_stat.grid(row=0, column=2, padx=20, pady=20)

# 2
link_frame = Frame(root)
link_frame.pack()
link_frame["background"]="#1e1e1e"

link_text = Label(link_frame, text=f"Link: ", highlightbackground="#1e1e1e")
link_text.grid(row=0, column=0, padx=20, pady=20)
link_entry = Entry(link_frame, highlightbackground="#1e1e1e")
link_entry.grid(row=0, column=1, padx=20, pady=20)

# 3
format_frame = Frame(root)
format_frame.pack()
format_frame["background"]="#1e1e1e"

format_mp4 = Button(format_frame, text=f"MP4", command=changeToMp4, background="#007acc", highlightbackground="#007acc")
format_mp4.grid(row=0, column=0, padx=10, pady=20)
format_mp3 = Button(format_frame, text=f"MP3", command=changeToMp3, background="gray", highlightbackground="gray")
format_mp3.grid(row=0, column=1, padx=10, pady=20)
format_convert = Button(format_frame, text=f"Start", background="green", highlightbackground="green", command=lambda: convert(link_entry.get()))
format_convert.grid(row=0, column=2, padx=10, pady=20)

# 4
status_frame = Frame(root)
status_frame.pack()
status_frame["background"] = "#1e1e1e"

status_text = Label(status_frame, text=f"Everything is good!", fg="#1e1e1e")
status_text.grid(row=0, column=0, padx=20, pady=20)

root.mainloop()
