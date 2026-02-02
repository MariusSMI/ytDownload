from tkinter import *

# Global variables



# Functions



root = Tk()
root.title("ytDonwload")
root.geometry("420x540")

# Widgets and Frames

folder_frame = Frame(root)
folder_frame.pack()

folder_text = Label(folder_frame, text=f"Directory:").grid(row=0, column=0, padx=20, pady=20)
folder_stat = Label(folder_frame, text=f"Null").grid(row=0, column=1, padx=20, pady=20)
folder_btn = Button(folder_frame, text=f"Change").grid(row=0, column=2, padx=20, pady=20)

link_frame = Frame(root)
link_frame.pack()

link_text = Label(link_frame, text=f"Link: ").grid(row=0, column=0, padx=20, pady=20)
link_entry = Entry(link_frame).grid(row=0, column=1, padx=20, pady=20)

format_frame = Frame(root)
format_frame.pack()

format_mp4 = Button(format_frame, text=f"MP4", background="red").grid(row=0, column=0, padx=20, pady=20)
format_mp3 = Button(format_frame).grid(row=0, column=1, padx=20, pady=20)
format_convert = Button(format_frame).grid(row=0, column=2, padx=20, pady=20)
format_single = Button(format_frame).grid(row=0, column=3, padx=20, pady=20)
format_playlist = Button(format_frame).grid(row=0, column=4, padx=20, pady=20)

status_frame = Frame(root)
status_frame.pack()



root.mainloop()
