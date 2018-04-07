from pprint import pprint
from fbrecog import FBRecog
from datetime import datetime
import threading
import time
import sys
import cv2


def network_request(url):
	recog = FBRecog(access_token, cookie, fb_dtsg)
	print(recog.recognize(url))

def open_cv_stuff(url):
	print(url)

class myThread (threading.Thread):
	def __init__(self, threadID, name,url):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.url = url
	def run(self):
		print(self.url)
		network_request(self.url)

class myThread2 (threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		thread1 = myThread(1, "Thread-1", path)
		open_cv_stuff(self.name)
		cam = cv2.VideoCapture(0)
		while (True): 
			ret, frame = cam.read()
			cv2.imshow("Feed",frame)



path = 'avatar.jpg' # Insert your image file path here
path2 = '2.jpg' # Insert your image file path here
access_token = 'EAACEdEose0cBADl6njtO2ZBDyWPJq3ZCSdn72ZCTfortNae5ZC2DCk61b6Bl5YkUFcc984ZA1ZCeUCsj6tZBkSgRe1TIwFRZCA0jXFBtGkVIqg1YzJFRUZBZAyctR1bIzdDVC4R0ARfJMq4T4zmOa7q7ceHctQ4ZBBbv1XRtFu9RBvIF5LiiHwODyuWyfkwJsr5uYQZD' # Insert your access token obtained from Graph API explorer here
cookie = "sb=FXmrWAzGR6faGm5pne_Y4Qja; datr=CnmrWDxTCp3uhpim6UHlzvRT; c_user=1338030897; xs=81%3AzOfqaK_OFCGSWw%3A2%3A1487632661%3A19927%3A3051; fr=057IJjBsVIsC3a3V1.AWWF2Bg6-XF42dxtrf_TA_RSqR4.BYq1Rn.LZ.Fq5.0.0.Bax_o9.AWXzNMtE; act=1523055167822%2F2; presence=EDvF3EtimeF1523055217EuserFA21338030897A2EstateFDutF1523055217605CEchFDp_5f1338030897F2CC; wd=751x855"
fb_dtsg = 'AQGFgFEQDRRP:AQGdHLSt7675' # Insert the fb_dtsg parameter obtained from Form Data here.
#capture an image

# Instantiate the recog class


thread2 = myThread2(2, "Thread-2")

thread2.start()

thread2.join()
print("done")