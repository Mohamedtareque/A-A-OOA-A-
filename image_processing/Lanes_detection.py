import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import itemfreq
import math 
from numpy import zeros, newaxis
from numpy import linalg as LA




	
# # #------------------ image part ----------------------
# # image = cv2.imread("test_image.jpg",0)#Screen Shot 2019-06-28 at 12.32.50 AM
# # copy_image = np.copy(image)
# # cv2.imshow('res',copy_image)

# # height = copy_image.shape[0]
# # print(height)
def region_of_interest(image):
 	height = image.shape[0]
 	width  = image.shape[1]
 	polygons = np.array([
 	 	[(200,height),(1000,height),(700,550),(550,550)]
 	 	])
 	mask = np.zeros_like(image) 
 	cv2.fillPoly(mask,polygons,255)
 	masked_image = cv2.bitwise_and(image,mask)
 	return masked_image


def canny(frame):
	gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY )
	blur = cv2.GaussianBlur(gray,(5,5),0)
	canny = cv2.Canny(blur,50,150)
	return canny
# # #----------------- mouse event -----------------------
# # # clicked = False
# # # def onMouse(event, x, y, flags, param):
# # #     global clicked
# # #     if event == cv2.EVENT_LBUTTONUP:
# # #         clicked = True

# ----------------- video part ------------------------
#cap = cv2.VideoCapture("Lane Detection Test Video 01.mp4")#Lane Detection Test Video 01
#cv2.setMouseCallback('camera', onMouse)
#ret, frame = cap.read()
x_org = 214
y_org = 700

def display_lines(image,lines):
	line_image = np.zeros_like(image)
	if lines is not None :
		for line in lines :
			x1, y1, x2, y2 = line.reshape(4)
			cv2.line(line_image, (x1, y1), (x2,y2), (40,255,0), 10)
	return line_image


def find_lanes(frame):
	line_image = np.zeros_like(frame)
	canny_img = canny(frame)
	cropped_img = region_of_interest(canny_img)
	lines = cv2.HoughLinesP(cropped_img,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5) 
	print (lines)
	line_image = np.zeros_like(frame)
	if lines is not None :
		for line in range(0, len(lines)):#range(0, len(lines))
			for x1,y1,x2,y2 in lines[line]:
				p1 = (x1, y1)
				p2 = (x2, y2)
				org = (x_org, y_org)
				p1 = np.asarray(p1)
				p2 = np.asarray(p2)
				org = np.asarray(org)
				distance = LA.norm(np.cross(np.array(p2)-np.array(p1), np.array(p1)-np.array(org)))/LA.norm(np.array(p2)-np.array(p1))
				# print(distance)
				if (distance < 400 ):#(distance < 380 and distance > 220) or (distance <100 and distance >50)
					line_img = display_lines(frame,lines)
					combo_image = cv2.addWeighted(frame, 0.8, line_img, 1 , 1)
					print(line_img)
					#cv2.line(frame,(x1,y1),(x2,y2),(200,255,0),6)
				# cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)
				else:
					line_img = display_lines(frame,lines)
					combo_image = cv2.addWeighted(frame, 0.8, line_img, 1 , 1)

				# print (distance)
	else:
		combo_image = cv2.addWeighted(frame, 0.8, line_image, 1 , 1)

	return combo_image


# image = cv2.imread("test_image.jpg",0)#Screen Shot 2019-06-28 at 12.32.50 AM
# copy_image = np.copy(image)
# lanes = find_lanes(copy_image)
# cv2.imshow('res',copy_image)

cap = cv2.VideoCapture("Lane Detection Test Video 01.mp4")#Lane Detection Test Video 01
while (cap.isOpened()):
	_, frame = cap.read( )
	lanes = find_lanes(frame)
	cv2.imshow('result',lanes) 
	# plt.imshow(lanes) 
	# plt.show()
	cv2.waitKey(1)
	#print(canny_image)
cap.release()
cv2.destroyAllWindows()
# # #----------------- output -------------------------------
# # # cv2.waitKey(0)
# # #print (copy_image)

# #!/usr/local/bin/python3
# # -*- coding: utf-8 -*-
# from __future__ import division
# import time
# #from moviepy.editor import VideoFileClip
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import numpy as np
# import random
# #np.set_printoptions(threshold='nan')
# import argparse
# import math
# import cv2
# import pylab  
# from PIL import Image
# from scipy.misc import imsave

# ##
# # @Author David Awad
# # Detection.py, traces and identifies lane
# # markings in an image or .mp4 video
# # usage: detection.py [-h] [-f FILE] [-v VIDEO]


# def region_of_interest(img, vertices):
#     #defining a blank mask to start with
#     mask = np.zeros_like(img)
    
#     if len(img.shape) > 2:
#         channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
#         ignore_mask_color = (255,) * channel_count
#     else:
#         ignore_mask_color = 255

#     cv2.fillPoly(mask, vertices, ignore_mask_color)
#     masked_image = cv2.bitwise_and(img, mask)
#     return masked_image


# def get_keypoints(img,lines):
#     slopeleft=999
#     sloperight=999
#     slopemedian=999
#     listpoints=['n','n','n','n','n','n','n','n']
#     listmedianpoints=['n','n','n','n']   
#     medianlist=[]
# #    print lines
#     lines = lines.reshape(lines.shape[1], lines.shape[2])
# #    print lines
# #    print lines.shape
# #    print 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'
#     while True:
#         flag=False
#         for i in range(lines.shape[0]):
# #            print i
# #            print lines[i]
#             if (lines[i][0]<=(img.shape[1]/2)<=lines[i][2])or(lines[i][0]>=(img.shape[1]/2)>=lines[i][2]):
#                 medianlist.append(lines[i])
#                 lines=np.delete(lines,i,0)
#                 flag=True
# #                print 'remove'
#                 break
#         if flag==False:
#             break
# #    print lines
# #    print medianlist
    
#     medianfinal=[]
    
#     mediancount=len(medianlist)
# #    print mediancount
#     if mediancount>0:
#         for i in range(mediancount):
#             eachmedian=medianlist[i]
#             tempslopemedian=math.fabs((eachmedian[1]-eachmedian[3])/(eachmedian[0]-eachmedian[2]))
#             smedian=math.atan(tempslopemedian)*180.0/math.pi
#             if smedian>70:
#                 medianfinal.append(eachmedian)
#         if len(medianfinal)>0:
#             X1=0
#             Y1=0
#             X2=0
#             Y2=0
#             for i in range(len(medianfinal)):
#                 X1+=medianfinal[i][0]
#                 Y1+=medianfinal[i][1]
#                 X2+=medianfinal[i][2]
#                 Y2+=medianfinal[i][3]
#             listmedianpoints[0]=X1/len(medianfinal)
#             listmedianpoints[1]=Y1/len(medianfinal)
#             listmedianpoints[2]=X2/len(medianfinal)
#             listmedianpoints[3]=Y2/len(medianfinal)
#             tempslopemedian=math.fabs((listmedianpoints[3]-listmedianpoints[1])/(listmedianpoints[2]-listmedianpoints[0]))
#             slopemedian=math.atan(tempslopemedian)*180.0/math.pi

# #    print 'ggggggggggggg'
#     lines = lines[~np.isnan(lines) & ~np.isinf(lines)]
#     lines.shape = (lines.shape[0]//2,2)  
#     right_linesTest = np.array(list(filter(lambda x: x[0] >= (img.shape[1]/2), lines)))
#     q=0
#     w=0
#     e=0
#     r=0
#     c=0
#     listtt=[]
#     for x1,y1 in right_linesTest:
#         c=c+1
#         if(c==1): 
#             q=x1
#             w=y1 
#             continue
#         if(c==2):
#             e=x1
#             r=y1
#             c=0
#             ss=(r-w)*1.0/(e-q)
#             ss=math.atan(ss)*180.0/math.pi
#             listtt.append(ss)
# #            print ss

#     right_linesTest2=right_linesTest.tolist()
# #    print right_linesTest2
#     liOK=[]
#     c=0
#     for slo in listtt:
#         if(slo<=15):
#             liOK.append(c)
#         c=c+1
 
#     count=0        
#     for c in liOK:
#         del right_linesTest2[(c-count)*2]
#         del right_linesTest2[(c-count)*2]
#         count=count+1

#     left_linesTest = np.array(list(filter(lambda x: x[0] < (img.shape[1]/2), lines)))
#     q=0
#     w=0
#     e=0
#     r=0
#     c=0
#     listtt=[]
#     for x1,y1 in left_linesTest:
#         c=c+1
#         if(c==1): 
#             q=x1
#             w=y1 
#             continue
#         if(c==2):
#             e=x1
#             r=y1
#             c=0
#             ss=(r-w)*1.0/(e-q)
#             ss=math.atan(ss)*180.0/math.pi
#             listtt.append(ss)


#     left_linesTest2=left_linesTest.tolist()
# #    print left_linesTest2
#     liOK=[]
#     c=0
#     for slo in listtt:
#         if(slo>=-15):
# #            print c
#             liOK.append(c)
#         c=c+1

    
#     count=0        
#     for c in liOK:
#         del left_linesTest2[(c-count)*2]
#         del left_linesTest2[(c-count)*2]
#         count=count+1


#     left=np.asarray(left_linesTest2)

#     if(len(left_linesTest2)!=0):
#         listtemp1=[]
#         listtemp2=[0,0,0,0]
#         count=left.shape[0]/2
# #        print count
# #        print 'lefttttggggggggggggggggggg'
#         for i in range(left.shape[0]):

#             listtemp1.append(left[i][0])
#             listtemp1.append(left[i][1])
#             if len(listtemp1)==4:
#                 listtemp2[0]+=listtemp1[0] if listtemp1[0]>listtemp1[2] else listtemp1[2]
#                 listtemp2[1]+=listtemp1[0] if listtemp1[0]<listtemp1[2] else listtemp1[2]
#                 listtemp2[2]+=listtemp1[1] if listtemp1[1]>listtemp1[3] else listtemp1[3]
#                 listtemp2[3]+=listtemp1[1] if listtemp1[1]<listtemp1[3] else listtemp1[3]
#                 listtemp1=[]
#         max_left_x, min_left_x,max_left_y, min_left_y=listtemp2[0]*1.0/count,listtemp2[1]*1.0/count,listtemp2[2]*1.0/count,listtemp2[3]*1.0/count       
                  
# #            max_left_x, max_left_y = left.max(axis=0)
# #            min_left_x, min_left_y = left.min(axis=0)
#         tempslopeleft=math.fabs((max_left_y-min_left_y)/(min_left_x-max_left_x))
#         sleft=math.atan(tempslopeleft)*180.0/math.pi
#         if math.fabs(sleft)>20:
#             longleft=math.pow(max_left_y-min_left_y,2)+math.pow(max_left_x- min_left_x,2)
#             if math.sqrt(longleft)<120:
#                 listpoints[0]=max_left_x
#                 listpoints[1]=min_left_y
#                 listpoints[2]=min_left_x
#                 listpoints[3]=max_left_y
#                 slopeleft=sleft


#     right=np.asarray(right_linesTest2)


#     if(len(right_linesTest2)!=0): 
#         listtemp1=[]
#         listtemp2=[0,0,0,0]
# #        print right
# #        print right.shape
#         count=right.shape[0]/2
#         for i in range(right.shape[0]):
# #            print right[i]
#             listtemp1.append(right[i][0])
#             listtemp1.append(right[i][1])
#             if len(listtemp1)==4:
#                 listtemp2[0]+=listtemp1[0] if listtemp1[0]>listtemp1[2] else listtemp1[2]
#                 listtemp2[1]+=listtemp1[0] if listtemp1[0]<listtemp1[2] else listtemp1[2]
#                 listtemp2[2]+=listtemp1[1] if listtemp1[1]>listtemp1[3] else listtemp1[3]
#                 listtemp2[3]+=listtemp1[1] if listtemp1[1]<listtemp1[3] else listtemp1[3]
#                 listtemp1=[]
# #                print 'dddddddddd'
# #                print listtemp2
#         max_right_x, min_right_x,max_right_y, min_right_y=listtemp2[0]*1.0/count,listtemp2[1]*1.0/count,listtemp2[2]*1.0/count,listtemp2[3]*1.0/count  
# #        print max_right_x, min_right_x,max_right_y, min_right_y
# #            max_right_x, max_right_y = right.max(axis=0)
# #            min_right_x, min_right_y = right.min(axis=0)
#         tempsloperight=math.fabs((max_right_y-min_right_y)/(max_right_x-min_right_x))
#         sright=math.atan(tempsloperight)*180.0/math.pi
#         if math.fabs(sright)>20:
#             longright=math.pow(max_right_y-min_right_y,2)+math.pow(max_right_x- min_right_x,2)
#             if math.sqrt(longright)<120:                
#                 listpoints[4]=max_right_x
#                 listpoints[5]=max_right_y
#                 listpoints[6]=min_right_x
#                 listpoints[7]=min_right_y
#                 sloperight=sright
# #            sloperight=(min_right_y-max_right_y)/(min_right_x-max_right_x)  
#     return listpoints,slopeleft,sloperight,listmedianpoints,slopemedian    



# def get_finalpointsslope(img,lines,previouslistpoints,previousslopeleft,previoussloperight):
#     newlistpoints,newslopeleft,newsloperight,newmedianpoints,newslopemedian=get_keypoints(img,lines)
#     finalslopeleft=999
#     finalsloperight=999
#     finallistpoints=['n','n','n','n','n','n','n','n']
#     if newslopemedian !=999:
#         if newslopeleft!=999 and newsloperight==999:
#                 finalslopeleft=newslopemedian
#                 finallistpoints[0]=newmedianpoints[0]
#                 finallistpoints[1]=newmedianpoints[1]
#                 finallistpoints[2]=newmedianpoints[2]
#                 finallistpoints[3]=newmedianpoints[3]
#                 finallistpoints[4]=int(finallistpoints[2]+(25*57/1.8))
#                 finallistpoints[5]=finallistpoints[3]
#                 finallistpoints[6]=int(finallistpoints[0]+(25*51.5/1.8))
#                 finallistpoints[7]=finallistpoints[1]
#                 tempsloperight=math.fabs((finallistpoints[7]-finallistpoints[5])*1.0/(finallistpoints[6]- finallistpoints[4]))
#                 finalsloperight=math.atan(tempsloperight)*180.0/math.pi
# #                finalslopeleft=newslopeleft
# #                finallistpoints[0]=newlistpoints[0]
# #                finallistpoints[1]=newlistpoints[1]
# #                finallistpoints[2]=newlistpoints[2]
# #                finallistpoints[3]=newlistpoints[3]
# #                finallistpoints[4]=newmedianpoints[0]
# #                finallistpoints[5]=newmedianpoints[1]
# #                finallistpoints[6]=newmedianpoints[2]
# #                finallistpoints[7]=newmedianpoints[3]
# #                finalsloperight=newslopemedian
#         elif newsloperight!=999 and newslopeleft==999:
#                 finalsloperight=newslopemedian
#                 finallistpoints[4]=newmedianpoints[0]
#                 finallistpoints[5]=newmedianpoints[1]
#                 finallistpoints[6]=newmedianpoints[2]
#                 finallistpoints[7]=newmedianpoints[3]
#                 finallistpoints[0]=int(finallistpoints[6]-(25*51.5/1.8))
#                 finallistpoints[1]=finallistpoints[7]
#                 finallistpoints[2]=int(finallistpoints[4]-(25*57/1.8))
#                 finallistpoints[3]=finallistpoints[5]
#                 tempslopeleft=math.fabs((finallistpoints[3]-finallistpoints[1])*1.0/(finallistpoints[2]- finallistpoints[0]))
#                 finalslopeleft=math.atan(tempslopeleft)*180.0/math.pi      
# #                finalsloperight=newsloperight
# #                finallistpoints[4]=newlistpoints[4]
# #                finallistpoints[5]=newlistpoints[5]
# #                finallistpoints[6]=newlistpoints[6]
# #                finallistpoints[7]=newlistpoints[7]
# #                finallistpoints[0]=newmedianpoints[0]
# #                finallistpoints[1]=newmedianpoints[1]
# #                finallistpoints[2]=newmedianpoints[2]
# #                finallistpoints[3]=newmedianpoints[3]
# #                finalslopeleft=newslopemedian
#     else:
#         flag=False             
#         if newslopeleft!=999 and newsloperight==999:
# #                disprenow=math.fabs(((newlistpoints[0]+newlistpoints[2])/2.0)-((previouslistpoints[0]+previouslistpoints[2])/2.0))
# #                print '11111111111'
# #                print disprenow
# #                if disprenow<150:
#                     flag=True
#                     finalslopeleft=newslopeleft
#                     finallistpoints[0]=newlistpoints[0]
#                     finallistpoints[1]=newlistpoints[1]
#                     finallistpoints[2]=newlistpoints[2]
#                     finallistpoints[3]=newlistpoints[3]
#                     finallistpoints[4]=int(newlistpoints[2]+(25*57/1.8))
#                     finallistpoints[5]=newlistpoints[3]
#                     finallistpoints[6]=int(newlistpoints[0]+(25*51.5/1.8))
#                     finallistpoints[7]=newlistpoints[1]
#                     tempsloperight=math.fabs((finallistpoints[7]-finallistpoints[5])*1.0/(finallistpoints[6]- finallistpoints[4]))
#                     finalsloperight=math.atan(tempsloperight)*180.0/math.pi
#         elif newsloperight!=999 and newslopeleft==999:
# #                disprenow=math.fabs(((newlistpoints[4]+newlistpoints[6])/2.0)-((previouslistpoints[4]+previouslistpoints[6])/2.0))
# #                print '2222222222'
# #                print disprenow
# #                if disprenow<150:
#                     flag=True
#                     finalsloperight=newsloperight
#                     finallistpoints[4]=newlistpoints[4]
#                     finallistpoints[5]=newlistpoints[5]
#                     finallistpoints[6]=newlistpoints[6]
#                     finallistpoints[7]=newlistpoints[7]
#                     finallistpoints[0]=int(newlistpoints[6]-(25*51.5/1.8))
#                     finallistpoints[1]=newlistpoints[7]
#                     finallistpoints[2]=int(newlistpoints[4]-(25*57/1.8))
#                     finallistpoints[3]=newlistpoints[5]
#                     tempslopeleft=math.fabs((finallistpoints[3]-finallistpoints[1])*1.0/(finallistpoints[2]- finallistpoints[0]))
#                     finalslopeleft=math.atan(tempslopeleft)*180.0/math.pi       
#         elif newsloperight!=999 and newslopeleft!=999:
# #                if previouslistpoints[0]!='n' and previouslistpoints[4]!='n':
# #                    disprenowleft=math.fabs(((newlistpoints[0]+newlistpoints[2])/2.0)-((previouslistpoints[0]+previouslistpoints[2])/2.0))
# #                    disprenowright=math.fabs(((newlistpoints[4]+newlistpoints[6])/2.0)-((previouslistpoints[4]+previouslistpoints[6])/2.0))
# #                else:
# #                    disprenowleft=0
# #                    disprenowright=0
#                 dis=math.fabs(((newlistpoints[0]+newlistpoints[2])/2.0)-((newlistpoints[4]+newlistpoints[6])/2.0))
# #                print '44444444444'
# #                print disprenowleft
# #                print disprenowright
# #                if dis>500 and disprenowleft<150 and disprenowright<150: 
# #                print 'qqqdis'
# #                print dis
#                 if dis>650:

#                     flag=True
#                     finalslopeleft=newslopeleft
#                     finalsloperight=newsloperight
#                     finallistpoints[0]=newlistpoints[0]
#                     finallistpoints[1]=newlistpoints[1]
#                     finallistpoints[2]=newlistpoints[2]
#                     finallistpoints[3]=newlistpoints[3]
#                     finallistpoints[4]=newlistpoints[4]
#                     finallistpoints[5]=newlistpoints[5]
#                     finallistpoints[6]=newlistpoints[6]
#                     finallistpoints[7]=newlistpoints[7]
#         if flag==False:
#             finalslopeleft=previousslopeleft
#             finalsloperight=previoussloperight
#             finallistpoints[0]=previouslistpoints[0]
#             finallistpoints[1]=previouslistpoints[1]
#             finallistpoints[2]=previouslistpoints[2]
#             finallistpoints[3]=previouslistpoints[3]
#             finallistpoints[4]=previouslistpoints[4]
#             finallistpoints[5]=previouslistpoints[5]
#             finallistpoints[6]=previouslistpoints[6]
#             finallistpoints[7]=previouslistpoints[7]
#     return finallistpoints,finalslopeleft,finalsloperight,newmedianpoints,newslopemedian
        

# def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
#     """
#     `img` should be the output of a Canny transform.
#     Returns an image with hough lines drawn.
#     """
#     lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)   
# #    print 'bbbbbb'
# #    print lines
# #    print 'ggggg'       
#     if lines is None:
#         return 'NoLines'
#     else:
#         return lines


# # Takes in a single frame or an image and returns a marked image
# def mark_lanes(image):
#     gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
#     # Define a kernel size and apply Gaussian smoothing
#     kernel_size = 3
#     blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

    

#     # Define our parameters for Canny and apply
#     low_threshold = 40
#     high_threshold = 60
#     edges_img = cv2.Canny(np.uint8(blur_gray), low_threshold, high_threshold)

    
#     vertices = np.array([[(550, 900),
#                           (550,850),
#                           (1450,850),
#                           (1450, 900) ]],
#                           dtype=np.int32)


#     masked_edges = region_of_interest(edges_img, vertices )
    


#     # Define the Hough transform parameters
#     rho             = 2           # distance resolution in pixels of the Hough grid
#     theta           = np.pi/180   # angular resolution in radians of the Hough grid
#     threshold       = 30       # minimum number of votes (intersections in Hough grid cell)
#     min_line_length = 20       # minimum number of pixels making up a line
#     max_line_gap    = 15       # maximum gap in pixels between connectable line segments

#     line_image = hough_lines(masked_edges, rho, theta, threshold, min_line_length, max_line_gap)
    
#     return line_image



# #def read_image_for_marking(img_filepath):
# def read_image_for_marking(image):
#     marked_lanes = mark_lanes(image)

#     # show the image to plotter and then save it to a file
#     plt.imshow(marked_lanes)
#     plt.savefig('262626_output.png')

# disleftList=[]
# disrightList=[]

# def lane_Chage(image,disX,leftORright,Flag,previousdisX):
# #    detectionError=False
#     if leftORright==True:
#         disList=disleftList
#     else:
#         disList=disrightList
#     if previousdisX>120:
#         disList=[]
#     if disX<120:
#         disList.append(disX)
#         if len(disList)>=3:
#             if leftORright:
# #                print '进入左侧变道区域！'
#                 font1=cv2.cv.InitFont(cv2.FONT_HERSHEY_SIMPLEX, 3, 3, 0, 3, 8)
#                 cv2.cv.PutText(cv2.cv.fromarray(image), "Prepare for turning LEFT!", (300,500), font1, (255,255,0))
#             else:
# #                print '进入右侧变道区域'
#                 font1=cv2.cv.InitFont(cv2.FONT_HERSHEY_SIMPLEX, 3, 3, 0, 3, 8)
#                 cv2.cv.PutText(cv2.cv.fromarray(image), "Prepare for turning RIGHT!", (300,500), font1, (255,255,0))
#     elif disX>400 and len(disList)>=3:
#         if leftORright:
# #            print '向左变道成功！'
#             font1=cv2.cv.InitFont(cv2.FONT_HERSHEY_SIMPLEX, 3, 3, 0, 3, 8)
#             cv2.cv.PutText(cv2.cv.fromarray(image), "turn LEFT, SUCCESS!", (300,500), font1, (255,12,8))
#         else:
# #            print '向右变道成功！'
#             font1=cv2.cv.InitFont(cv2.FONT_HERSHEY_SIMPLEX, 3, 3, 0, 3, 8)
#             cv2.cv.PutText(cv2.cv.fromarray(image), "turn RIGHT, SUCCESS!", (300,500), font1, (255,12,8))
#         disList=[]

#     return disX,Flag

        


# if __name__ == "__main__":
#      input_name = 'test.mp4'
#      cap = cv2.VideoCapture(input_name)
#      if False == cap.isOpened():  
#          print 'open video failed'  
#      else:  
#          print 'open video succeeded'
     
#      previousslopeleft=999
#      previoussloperight=999
#      previouslistpoints=['n','n','n','n','n','n','n','n']
#      newslopemedian=999
#      newmedianpoints=['n','n','n','n']
#      n=0
#      tupletemp=()
#      stdx=960
#      FlagLeft=False
#      FlagRight=False
#      previousdisleft=0
#      previousdisright=0
# #     start=time.clock()
#      while (cap.isOpened()):
# #         end=time.clock()
# #         if end-start>=1:
# #             print n
# #             time.sleep(6666)
#          _, frame = cap.read()
#          n=n+1
# #         print '第'+str(n)+'帧'
#          cv2.namedWindow("result",cv2.WINDOW_NORMAL);  
#          newlines=mark_lanes(frame)

#          if newlines!='NoLines':
#              previouslistpoints,previousslopeleft,previoussloperight,newmedianpoints,newslopemedian=get_finalpointsslope(frame,newlines,previouslistpoints,previousslopeleft,previoussloperight)
# #         print previousslopeleftT
# #         print previoussloperightT
# #         print previouslistpointsT

#          cv2.imshow('result',frame)
#          if previousslopeleft!=999 and previoussloperight!=999:
# #             dis=math.fabs(((previouslistpoints[0]+previouslistpoints[2])/2.0)-((previouslistpoints[4]+previouslistpoints[6])/2.0))
# #             print '距离 '+str(dis)
#              disleft=math.fabs(960-(previouslistpoints[0]+previouslistpoints[2])/2.0)
#              disright=math.fabs(previouslistpoints[4]+previouslistpoints[6])/2.0-960
#              if n==1:
#                  previousdisleft=disleft
#                  previousdisright=disright
#              previousdisleft,FlagLeft=lane_Chage(frame,disleft,True,FlagLeft,previousdisleft)
#              previousdisright,FlagRight=lane_Chage(frame,disright,False,FlagRight,previousdisright)
#              font1=cv2.cv.InitFont(cv2.FONT_HERSHEY_SIMPLEX, 2, 2, 0, 2, 8)
#              cv2.cv.PutText(cv2.cv.fromarray(frame),"DISleft:"+str(int(disleft))+"  DISright:"+str(int(disright)), (500,800), font1, (0,0,0))  

  
        
#          if previousslopeleft!=999:
#              cv2.line(frame, (int(previouslistpoints[0]), int(previouslistpoints[1])), (int(previouslistpoints[2]), int(previouslistpoints[3])),[255, 255, 255], 18)
# #             longleft=math.pow(previouslistpoints[0]-previouslistpoints[2],2)+math.pow(previouslistpoints[1]-previouslistpoints[3],2)
# #             print "right:  "+str(math.sqrt(longleft))
#          if previoussloperight!=999:
#              cv2.line(frame, (int(previouslistpoints[4]), int(previouslistpoints[5])), (int(previouslistpoints[6]), int(previouslistpoints[7])),[255, 40, 100], 18)
# #             longright=math.pow(previouslistpoints[6]-previouslistpoints[4],2)+math.pow(previouslistpoints[5]-previouslistpoints[7],2)
# #             print "left:  "+str(math.sqrt(longright))
#          if newslopemedian!=999:
#             cv2.line(frame, (int(newmedianpoints[0]), int(newmedianpoints[1])), (int(newmedianpoints[2]), int(newmedianpoints[3])),[25, 40, 100], 4)
            
#          cv2.imshow('result',frame)   
# #         cv2.waitKey(0)
#          if cv2.waitKey(1) & 0xFF == ord('s'):
#              cv2.waitKey(0)
#          if cv2.waitKey(1) & 0xFF == ord('q'):
#              break
 
