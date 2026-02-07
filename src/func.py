from tkinter import filedialog
import subprocess

class Func:
    def __init__(self):
        self.path = ""
        self.mp4 = True
        self.mp3 = False
        self.interface = None

    def set_interface(self, interface_instance):
        self.interface = interface_instance

    def AskDirectory(self):
        self.path = filedialog.askdirectory()
        if self.path:
            self.interface.folder_stat.config(text=self.path)

    def convert(self, link):
        if not self.path:
            self.interface.status_text.config(text="Error: Select a folder first")
            return

        self.interface.status_text.config(text="Downloading...")
        
        try:
            if self.mp4:
                cmd = ["yt-dlp", "-P", self.path, "-f", "best[height<=1080]", link]
            else:
                cmd = ["yt-dlp", "-P", self.path, "-x", "--audio-format", "mp3", link]
            
            result = subprocess.run(cmd, capture_output=True)
            
            if result.returncode == 0:
                self.interface.status_text.config(text="Done!")
            else:
                self.interface.status_text.config(text="Error: Invalid link")
        except Exception:
            self.interface.status_text.config(text="Error: yt-dlp not found")

    def changeToMp4(self):
        self.mp4 = True
        self.mp3 = False
        self.interface.format_mp4.config(bg="#007acc")
        self.interface.format_mp3.config(bg="gray")

    def changeToMp3(self):
        self.mp4 = False
        self.mp3 = True
        self.interface.format_mp4.config(bg="gray")
        self.interface.format_mp3.config(bg="#007acc")