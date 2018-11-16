'''
Auther: Abudlmalk Alomran
Subtitle Matcher
Quick Subtitle sorter, Scan for current file in the direcotry with the cosen format, a viedo format and a subtitle format , 
scan directory and store into two list and rename the subtitle titles with the new one.

'''
import os
List_old=[]
List_new=[]
#VID_format=".mlv"
#sub_format=".srt"
print("Subtitle Matcher")
A_dot="."
VID_format=A_dot+input("Please Enter The  Video Extension Ex: mkv,mp4 : ")
sub_format=A_dot+input("Please Enter the Subtitle Extension Ex: srt,txt : ")
x=0
for root, dirs, files in os.walk("."): #scan for files
    for filename in files:
        	if sub_format in str(filename): #if has .srt store in list
        		List_old.append(filename)
        		
        	if VID_format in str(filename): #if has .mkv store in a difrent list
        		List_new.append(filename)
        	
for i in range(0,len(List_old)):
	try:
		os.rename(List_old[i],List_new[i][0:len(List_new[i])-4]+sub_format)
		#print((List_old[i],List_new[i][0:len(List_new[i])-4]+sub_format))
		
	except Exception  as e:
		print(e)
		
x=input("SSS")
