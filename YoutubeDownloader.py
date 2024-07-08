from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_Video(url, save_path):
     """""
     Function that get an url from a yt video,
     download that video in high resolution and 
     save the user path where store the video
     """""
     
     try:
        
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension= "mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded succesfully! ")
            
     except Exception as error:
        print(error)
          
def open_file_dialog():
     
    folder = filedialog.askdirectory()
    if folder:
       print(f"Selected folder: {folder}")
    return folder
     
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
     
video_url = input("Please enter a url from a Youtube video: ")
save_directory = open_file_dialog()

 if save_directory:
       download_Video(video_url, save_directory)
       
 else:
       print("Invalid location, please try again")
