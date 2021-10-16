"""import requests
from bs4 import BeautifulSoup

# specify the URL of the archive here
archive_url = "https://www.youtube.com/playlist?list=PLEbnTDJUr_IeMn2sPHXPVkvSkU_tGNF58"

def get_video_links():
	
	# create response object
	r = requests.get(archive_url)
	
	# create beautiful-soup object
	soup = BeautifulSoup(r.content,'html5lib')
	
	# find all links on web-page
	links = soup.findAll('a')

	# filter the link sending with .mp4
	video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]

	return video_links


def download_video_series(video_links):

	for link in video_links:

		'''iterate through all links in video_links
		and download them one by one'''
		
		# obtain filename by splitting url and getting
		# last string
		file_name = link.split('/')[-1]

		print( "Downloading file:%s"%file_name)
		
		# create response object
		r = requests.get(link, stream = True)
		
		# download started
		with open(file_name, 'wb') as f:
			for chunk in r.iter_content(chunk_size = 1024*1024):
				if chunk:
					f.write(chunk)
		
		print( "%s downloaded!\n"%file_name )

	print ("All videos downloaded!")
	return


if __name__ == "__main__":

	# getting all video links
	video_links = get_video_links()

	# download all videos
	download_video_series(video_links)
"""

"""
# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():

	head_label = Label(root, text="YouTube Video Downloader Using Tkinter",
					padx=15,
					pady=15,
					font="SegoeUI 14",
					bg="palegreen1",
					fg="red")
	head_label.grid(row=1,
					column=1,
					pady=10,
					padx=5,
					columnspan=3)

	link_label = Label(root,
					text="YouTube link :",
					bg="salmon",
					pady=5,
					padx=5)
	link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)

	root.linkText = Entry(root,
						width=35,
						textvariable=video_Link,
						font="Arial 14")
	root.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)


	destination_label = Label(root,
							text="Destination :",
							bg="salmon",
							pady=5,
							padx=9)
	destination_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


	root.destinationText = Entry(root,
								width=27,
								textvariable=download_Path,
								font="Arial 14")
	root.destinationText.grid(row=3,
							column=1,
							pady=5,
							padx=5)


	browse_B = Button(root,
					text="Browse",
					command=Browse,
					width=10,
					bg="bisque",
					relief=GROOVE)
	browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)

	Download_B = Button(root,
						text="Download Video",
						command=Download,
						width=20,
						bg="thistle1",
						pady=10,
						padx=15,
						relief=GROOVE,
						font="Georgia, 13")
	Download_B.grid(row=4,
					column=1,
					pady=20,
					padx=20)


# Defining Browse() to select a
# destination folder to save the video

def Browse():
	# Presenting user with a pop-up for
	# directory selection. initialdir
	# argument is optional Retrieving the
	# user-input destination directory and
	# storing it in downloadDirectory
	download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")

	# Displaying the directory in the directory
	# textbox
	download_Path.set(download_Directory)

# Defining Download() to download the video


def Download():

	# getting user-input Youtube Link
	Youtube_link = video_Link.get()

	# select the optimal location for
	# saving file's
	download_Folder = download_Path.get()

	# Creating object of YouTube()
	getVideo = YouTube(Youtube_link)

	# Getting all the available streams of the
	# youtube video and selecting the first
	# from the
	videoStream = getVideo.streams.first()

	# Downloading the video to destination
	# directory
	videoStream.download(download_Folder)

	# Displaying the message
	messagebox.showinfo("SUCCESSFULLY",
						"DOWNLOADED AND SAVED IN\n"
						+ download_Folder)


# Creating object of tk class
root = tk.Tk()

# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="PaleGreen1")

# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()"""


"""
from pytube import YouTube

# where to save
SAVE_PATH = "E:/" #to_do

# link of the video to be downloaded
# opening the file
link=open('links_file.txt','r')

for i in link:
	try:
		
		# object creation using YouTube
		# which was imported in the beginning
		yt = YouTube(i)
	except:
		
		#to handle exception
		print("Connection Error")
	
	#filters out all the files with "mp4" extension
	mp4files = yt.filter('mp4')
	
	# get the video with the extension and
	# resolution passed in the get() function
	d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
	try:
		
		# downloading the video
		d_video.download(SAVE_PATH)
	except:
		print("Some Error!")
print('Task Completed!')"""

"""
from pytube import YouTube

#where to save
SAVE_PATH = "E:/" #to_do

#link of the video to be downloaded
link=["https://www.youtube.com/playlist?list=PLEbnTDJUr_IeMn2sPHXPVkvSkU_tGNF58"
	]

for i in link:
	try:
		
		# object creation using YouTube
		# which was imported in the beginning
		yt = YouTube(i)
	except:
		
		#to handle exception
		print("Connection Error")
	
	#filters out all the files with "mp4" extension
	mp4files = yt.filter('mp4')

	# get the video with the extension and
	# resolution passed in the get() function
	d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
	try:
		# downloading the video
		d_video.download(SAVE_PATH)
	except:
		print("Some Error!")
print('Task Completed!')

"""

"""from pytube import YouTube
YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt.streams
... .filter(progressive=True, file_extension='mp4')
... .order_by('resolution')
... .desc()
... .first()
... .download()"""


