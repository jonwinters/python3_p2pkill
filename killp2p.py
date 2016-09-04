#!/usr/bin/python3
import os
import sys
import time
#testCode
#print(os.system('tasklist | find "xxx.exe"'))###@@@
##@@@xxx.exe区分大小写



	
##error
class myError(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return self.value
		
def initFileLoad():
	##init
	f = open("foo.txt")            
	line = f.readline()  
	it={}           
	while line:  
		print(line)
		if (line.find(':')==-1):
			raise myError("can't find char :")
		it[line[0:line.find(':')]]=line[line.find(':')+1:]
		line = f.readline() 
	
	f.close()
	return it
		
def isProcessAlive(processName):
	return os.system('tasklist | find "'+processName+'"')
	##alive return 0
	##not alive return 1
def toKillProcess(processName):	
	os.system('TASKKILL /F /IM '+processName)
	if (isProcessAlive(processName)==0):
		print(processName+"still alive !")
		
def main():
	#init...
	try:
		it=initFileLoad()
	except IOError:
		print("can't open file!!")
		os._exit()
	except myError as e:
		print(e.value)
		os._exit()
	finally:
		# testPrint
		for k, v in it.items():
			print(k,v)
		#
	#init end..

	#start main loop
	while(1):
	##alive return 0
	##not alive return 1
		for mainProcess,childProcess in it.items():
			if( isProcessAlive(mainProcess) == 1):
				print("main process "+mainProcess+" is not alive!!")
				print("maybe we shoudl kill child process!")
				if(isProcessAlive(childProcess)==0):
					print(childProcess+" will be killed!")
					toKillProcess(childProcess)
				else:
					print("not find child process!")
		time.sleep(10)

##main
if __name__=='__main__':
	main()