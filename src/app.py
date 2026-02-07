from tkinter import *
from src.func import Func

class App:

    def __init__(self, root, resolucion, background, resizable):
        self.f = Func()
        self.f.set_interface(self)
        
        self.app = root
        self.app.title("ytDonwload")
        self.app.geometry(resolucion)
        self.bg = background

        if not resizable:
            self.app.resizable(False, False)

        self.app["background"] = self.bg

        self.create_folder_section()
        self.create_link_section()
        self.create_format_section()
        self.create_status_section()

    def create_folder_section(self):
        folder_frame = Frame(self.app, bg=self.bg)
        folder_frame.pack()

        folder_btn = Button(folder_frame, text="Folder", background="yellow", 
                            highlightbackground="yellow", command=self.f.AskDirectory,
                            fg="black")
        folder_btn.grid(row=0, column=1, padx=20, pady=20)

        self.folder_stat = Label(folder_frame, text="None", bg=self.bg, fg="white")
        self.folder_stat.grid(row=0, column=2, padx=20, pady=20)
    
    def create_link_section(self):
        link_frame = Frame(self.app, bg=self.bg)
        link_frame.pack()

        link_text = Label(link_frame, text="Link: ", bg=self.bg, fg="white")
        link_text.grid(row=0, column=0, padx=20, pady=20)
        
        self.link_entry = Entry(link_frame, highlightbackground=self.bg)
        self.link_entry.grid(row=0, column=1, padx=20, pady=20)
    
    def create_format_section(self):
        format_frame = Frame(self.app, bg=self.bg)
        format_frame.pack()

        self.format_mp4 = Button(format_frame, text="MP4", command=self.f.changeToMp4, 
                                 background="#007acc", highlightbackground="#007acc", fg="white")
        self.format_mp4.grid(row=0, column=0, padx=10, pady=20)
        
        self.format_mp3 = Button(format_frame, text="MP3", command=self.f.changeToMp3, 
                                 background="gray", highlightbackground="gray", fg="white")
        self.format_mp3.grid(row=0, column=1, padx=10, pady=20)
        
        self.format_convert = Button(format_frame, text="Start", background="green", 
                                     highlightbackground="green", fg="white",
                                     command=lambda: self.f.convert(self.link_entry.get()))
        self.format_convert.grid(row=0, column=2, padx=10, pady=20)
    
    def create_status_section(self):
        status_frame = Frame(self.app, bg=self.bg)
        status_frame.pack()

        self.status_text = Label(status_frame, text="Everything is good!", bg=self.bg, fg="white")
        self.status_text.grid(row=0, column=0, padx=20, pady=20)