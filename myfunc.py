import re

########################################################################
########################################################################
#####################   Global Functions   #############################
########################################################################
########################################################################

def columnInformation(csvFileFullName):
	#Getting each column's information from csvFileFullName
	with open(csvFileFullName,'r') as fl:
		#fl.readlines() or .read() gives one big string, so we are going to seperate by '\n'
		of=fl.read().splitlines()[2:69] #first 2 lines are unnecessary and we only need upto line 69.
	z=[re.search(r'[0-9].*[0-9],',i).group().split(',')[:-1] for i in of]
	z=zip(*z)
	#z[0] is column number
	#z[1] is headers
	#z[-1] is amount space that each column has.
	return [int(i) for i in z[-1]]

def checkingRecords(k,col,dd):
	#imput: k = each file's unique name, col=column number, dd=dictionary
	with open('UMich'+k+'.csv') as dk:
		for i in dk.readlines()[1:]:
			if i.split(',')[col].lower() in dd:
				dd[i.split(',')[col].lower()]+=1
			else:
				dd[i.split(',')[col].lower()]=1
	return dd

def forRecorderOrTaxAssessorCSV(rrr,www,eachColumnSpace):
	#rrr is file to read, www is a list of file names (3), eachcolumnspace is each column information 
	with open(rrr,'r') as rc:
		totalNumberOfRows=len(rc.readlines())
	remainder=totalNumberOfRows%3
	totalNum=totalNumberOfRows-remainder
	oneChunk=totalNum/3
	splitFiles=[oneChunk,2*oneChunk]#we only need to check 2 points to split them into 3 parts

	with open(rrr,'r') as rc:
		with open('UMich'+www[0]+'.csv','w') as wo:
			wo.write(','.join(z[1])+'\n')
			for i in rc.readlines()[0:splitFiles[0]]:
				eachList=[]
				for j in eachColumnSpace:
					eachList.append(i[:j])
					i = i[j:]
				#Last element of eachList is '\r\n'
				eachList=eachList[:-1]
				#We want to grab only data only or empty variable
				eachList=[re.search(r'([^\s].*[^\s]|[^\s])|[ ]+', i).group() for i in eachList]
				#For empty variables, we are replacing spaces with '' none. 
				for i in range(len(eachList)):
					if re.search(r'^\s+', eachList[i]):
						eachList[i]=eachList[i].replace(' ','')
				#Replacing commas with '' none. 
				eachList=[i.replace(',','') for i in eachList]
				wo.write(",".join(eachList)+'\n')

	with open(rrr,'r') as rc:
		with open('UMich'+www[1]+'.csv','w') as wo:
			wo.write(','.join(z[1])+'\n')
			for i in rc.readlines()[splitFiles[0]:splitFiles[1]]:
				eachList=[]
				for j in eachColumnSpace:
					eachList.append(i[:j])
					i = i[j:]
				#Last element of eachList is '\r\n'
				eachList=eachList[:-1]
				#We want to grab only data only or empty variable
				eachList=[re.search(r'([^\s].*[^\s]|[^\s])|[ ]+', i).group() for i in eachList]
				#For empty variables, we are replacing spaces with '' none. 
				for i in range(len(eachList)):
					if re.search(r'^\s+', eachList[i]):
						eachList[i]=eachList[i].replace(' ','')
				#Replacing commas with '' none. 
				eachList=[i.replace(',','') for i in eachList]
				wo.write(",".join(eachList)+'\n')

	with open(rrr,'r') as rc:
		with open('UMich'+www[2]+'.csv','w') as wo:
			wo.write(','.join(z[1])+'\n')
			for i in rc.readlines()[splitFiles[1]:]:
				eachList=[]
				for j in eachColumnSpace:
					eachList.append(i[:j])
					i = i[j:]
				#Last element of eachList is '\r\n'
				eachList=eachList[:-1]
				#We want to grab only data only or empty variable
				eachList=[re.search(r'([^\s].*[^\s]|[^\s])|[ ]+', i).group() for i in eachList]
				#For empty variables, we are replacing spaces with '' none. 
				for i in range(len(eachList)):
					if re.search(r'^\s+', eachList[i]):
						eachList[i]=eachList[i].replace(' ','')
				#Replacing commas with '' none. 
				eachList=[i.replace(',','') for i in eachList]
				wo.write(",".join(eachList)+'\n')
	return "Done"

########################################################################
########################################################################
#####################      Foreclosure Only      ########################
########################################################################
########################################################################
def onlyForeclosureCSV(rrr,www,eachColumnSpace):
	#rrr is file to read, www is a file that we want to write, eachColumnSpace is each column information 
	with open(rrr,'r') as fc:
		with open(www,'w') as wo:
			wo.write(','.join(z[1])+'\n')
			for i in fc.readlines():
				eachList=[]
				for j in eachColumnSpace:
					eachList.append(i[:j])
					i = i[j:]
				#Last element of eachList is '\r\n'
				eachList=eachList[:-1]
				#We want to grab only data only or empty variable
				eachList=[re.search(r'([^\s].*[^\s]|[^\s])|[ ]+', i).group() for i in eachList]
				#For empty variables, we are replacing spaces with '' none. 
				for i in range(len(eachList)):
					if re.search(r'^\s+', eachList[i]):
						eachList[i]=eachList[i].replace(' ','')
				#Replacing commas with '' none. 
				eachList=[i.replace(',','') for i in eachList]
				wo.write(",".join(eachList)+'\n')
	return "Done"

########################################################################
########################################################################
#####################       Recorder Only       ########################
########################################################################
########################################################################


########################################################################
########################################################################
#####################       Assessor Only       ########################
########################################################################
########################################################################
