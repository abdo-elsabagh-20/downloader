from tkinter import *
from tkinter import messagebox
from yt_dlp import YoutubeDL

# Function For Hight_Quality
def hight_Quality():
    try:
        url = myentry.get()
        ydl_opts = {
            'format': 'best'
            ,'merge_output_format':'mp4'
            ,'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", "Hight Quality Video Has Been Downloaded")
    except Exception as e:
        messagebox.showerror("Error", "Error To Download Hight Quality Video")

# Function For Low_Quality
def Low_Quality():
    try:
        url = myentry.get()
        ydl_opts = {
            'format': 'worst',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", "Low Quality Video Has Been Downloaded")
    except Exception as e:
        messagebox.showerror("Error", "Error To Download Low Quality Video")

# Function For Audio
def Audio():
    try:
        url = myentry.get()
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", " Audio Has Been Downloaded")
    except Exception as e:
        messagebox.showerror("Error", "Error To Download Audio")

root = Tk()
root.geometry("500x300")
root.title("Youtube Downloader")
root.configure(bg="grey")

mylabel = Label(root, text="Enter Link To Download:", font="Tahoma 25", bg="grey", fg="black")
mylabel.pack()

myentry = Entry(root, width="35", font="Tahoma 15")
myentry.pack(pady="15")

high = Button(root, text="High Quality", bg="black", fg="white", font="Tahoma 15", command=hight_Quality)
high.pack(pady="10")
high.place(x=65,y=150)

low = Button(root, text="Low Quality", bg="black", fg="white", font="Tahoma 15", command=Low_Quality)
low.pack(pady="10")
low.place(x=215,y=150)

audio = Button(root, text="Audio", bg="black", fg="white", font="Tahoma 15", command=Audio)
audio.pack(pady="10")
audio.place(x=365,y=150)

root.mainloop()
