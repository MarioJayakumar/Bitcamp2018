from pprint import pprint
from fbrecog import FBRecog
from datetime import datetime
import threading
import time
import sys
import cv2
name_list = []


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
		try:
			network_request(self.url)
		except:
			print("Oops :(")




path = 'avatar.jpg' # Insert your image file path here
path2 = '2.jpg' # Insert your image file path here
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
access_token = 'EAACEdEose0cBAEjtg2nCsa8XkQwTh6QgQl85zuNvIajZCqY58i33LZBLuq8V9wosEiH6l8Ws3Oa6Rih3iWRHkdnChjeQcO6K1XGQSZB8HOMx8vLIh32ydNIShlmWknkHqrqVUdePcBssOZBwoxiCzNrljapfEZBqlm5Xyp7e8npl5rFhAZCVrHhHp6jKnJXYYZD' # Insert your access token obtained from Graph API explorer here
cookie = "sb=FXmrWAzGR6faGm5pne_Y4Qja; datr=CnmrWDxTCp3uhpim6UHlzvRT; c_user=1338030897; xs=81%3AzOfqaK_OFCGSWw%3A2%3A1487632661%3A19927%3A3051; fr=057IJjBsVIsC3a3V1.AWWF2Bg6-XF42dxtrf_TA_RSqR4.BYq1Rn.LZ.Fq5.0.0.Bax_o9.AWXzNMtE; act=1523055167822%2F2; presence=EDvF3EtimeF1523055217EuserFA21338030897A2EstateFDutF1523055217605CEchFDp_5f1338030897F2CC; wd=751x855"
fb_dtsg = 'AQGFgFEQDRRP:AQGdHLSt7675' # Insert the fb_dtsg parameter obtained from Form Data here.
#capture an image

# Instantiate the recog class


#thread2 = myThread2(2, "Thread-2")

cam = cv2.VideoCapture(0)

#thread1 = myThread(1, "Thread-1", path)
while(True):
	ret, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imwrite(path, frame)
	cv2.imshow("frame",frame)
	faces = face_cascade.detectMultiScale(gray, 1.3,5)
	if cv2.waitKey(1) & 0xFF == ord('p'):
		print("Starting Recognition!")
		thread1 = myThread(1, "Thread-1", path)
		thread1.start()
	print(name_list)
#thread1.start()
#thread1.join()

cam.release()
print("done")
cv2.destroyAllWindows()

