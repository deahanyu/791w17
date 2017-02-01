import re

########################################################################
########################################################################
#####################   Global Functions   #############################
########################################################################
########################################################################

########################################################################
#This is for txt -> multiple csv files 
#and multiple csv files -> one big files
def columnInformation(csvFileFullName,k):
	#Getting each column's information from csvFileFullName
	#k==0 for Forclosure 
	#k==1 for Recorder
	#k==2 for TaxAssessor
	with open(csvFileFullName,'r') as fl:
		if k==0:
				#fl.readlines() or .read() gives one big string, so we are going to seperate by '\n'
				of=fl.read().splitlines()[2:69] #first 2 lines are unnecessary and we only need upto line 69.
		elif k==1:
			of1=fl.read().splitlines()[2:47] #first 2 lines are unnecessary and we only need upto line 47.
			with open(csvFileFullName,'r') as fl:
				of2=fl.read().splitlines()[64:108] 
			of=of1+of2
		else:
			of=fl.read().splitlines()[2:185] #first 2 lines are unnecessary and we only need upto line
	z=[re.search(r'[0-9].*[0-9],',i).group().split(',')[:-1] for i in of]
	z=zip(*z)
	#z[0] is column number
	#z[1] is headers
	#z[-1] is amount space that each column has.
	return z

def makingSingleFileForEach():
	recorderFileList=['UMichRecorder1a.csv','UMichRecorder1b.csv','UMichRecorder1c.csv','UMichRecorder2a.csv','UMichRecorder2b.csv','UMichRecorder2c.csv','UMichRecorder3a.csv','UMichRecorder3b.csv','UMichRecorder3c.csv']
	taxAsseossorFileList=['UMichTaxAssessor1a.csv','UMichTaxAssessor1b.csv','UMichTaxAssessor1c.csv','UMichTaxAssessor2a.csv','UMichTaxAssessor2b.csv','UMichTaxAssessor2c.csv']
	keysList=['1a','1b','1c','2a','2b','2c','3a','3b','3c']
	with open('UMichTaxAssessor_Total.csv','w') as wo:
		with open('UMichTaxAssessor1a.csv','r') as rc:
			for i in rc.readlines():
				wo.write(i)
		for i in range(5):
			with open(taxAsseossorFileList[i+1],'r') as rc:
				for j in rc.readlines()[1:]:
					wo.write(j)
	with open('UmichRecorder_Total.csv','w') as wo:
		with open('UMichRecorder1a.csv','r') as rc:
			for i in rc.readlines():
				wo.write(i)
		for i in range(8):
			with open(recorderFileList[i+1],'r') as rc:
				for j in rc.readlines()[1:]:
					wo.write(j)
	return 'Done'

def makingTxtfile(rrr,www,hhh,c):
	#rrr = CSV full file name
	#www = name textfile
	#hhh = headers
	#c==0 for Forclosure 
	#c==1 for Recorder
	#c==2 for TaxAssessor

	#Getting each column's information from csvFileFullName
	with open(rrr,'r') as fl:
		if c==0:
				#fl.readlines() or .read() gives one big string, so we are going to seperate by '\n'
				of=fl.read().splitlines()[2:69] #first 2 lines are unnecessary and we only need upto line 69.
		elif c==1:
			of1=fl.read().splitlines()[2:64] #first 2 lines are unnecessary and we only need upto line 47.
			with open(rrr,'r') as fl:
				of2=fl.read().splitlines()[64:108] 
			s=''
			for i in of1[45:]:
				s+=i
			of1[44]=of1[44]+s
			of=of1[:45]+of2
		else:
			of=fl.read().splitlines()[2:185]
	with open('UMich'+www+'.txt','w') as wo:
		ck=0
		for i in of:
			if re.search(r'(Yes|No)(.*)',i):
				k = re.search(r'(Yes|No)(.*)',i).group(2)[1:]
				if re.search(r'\s{2,}',k):
					gone = re.search(r'\s{2,}',k).group()
					k = k.replace(gone,'')
			else: 
				k = ''
			wo.write("\n".join([hhh[ck],'\t'+k])+'\n\n\n')
			ck+=1
	return 'DONE'

def checkingRecords(k,col,dd):
	#imput: k = each file's unique name, col=column number, dd=dictionary
	with open('UMich'+k+'.csv') as dk:
		for i in dk.readlines()[1:]:
			if i.split(',')[col].lower() in dd:
				dd[i.split(',')[col].lower()]+=1
			else:
				dd[i.split(',')[col].lower()]=1
	return dd

def forRecorderOrTaxAssessorCSV(rrr,www,columnInformation):
	eachColumnSpace=[int(i) for i in columnInformation[-1]]
	#rrr is file to read, www is a list of file names (3), eachcolumnspace is each column information 
	with open(rrr,'r') as rc:
		totalNumberOfRows=len(rc.readlines())
	remainder=totalNumberOfRows%3
	totalNum=totalNumberOfRows-remainder
	oneChunk=totalNum/3
	splitFiles=[oneChunk,2*oneChunk]#we only need to check 2 points to split them into 3 parts

	with open(rrr,'r') as rc:
		with open('UMich'+www[0]+'.csv','w') as wo:
			wo.write(','.join(columnInformation[1])+'\n')
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
			wo.write(','.join(columnInformation[1])+'\n')
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
			wo.write(','.join(columnInformation[1])+'\n')
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
#This is for sqlite.
def makingListForACertainColumn_Integer(fullName,listOfIndexNumb):
	#fullName:file full name
	#listOfIndexNumb: list of index number
	#returns a single list contains len(listOfIndexNumb) number of tuples
	with open(fullName,'r') as fl:
		ff=fl.readlines()
	return [tuple(map(lambda j: int(i.split(',')[j]) if len(i.split(',')[j])!=0 else 0, listOfIndexNumb)) for i in ff[1:]]
def makingListForACertainColumn_Text(fullName,listOfIndexNumb):
	#fullName:file full name
	#listOfIndexNumb: list of index number
	#returns a single list contains len(listOfIndexNumb) number of tuples
	with open(fullName,'r') as fl:
		ff=fl.readlines()
	return [tuple(map(lambda j: i.split(',')[j], listOfIndexNumb)) for i in ff[1:]]







########################################################################
########################################################################
#####################      Foreclosure Only      ########################
########################################################################
########################################################################
def onlyForeclosureCSV(rrr,www,columnInformation):
	eachColumnSpace=[int(i) for i in columnInformation[-1]]
	#rrr is file to read, www is a file that we want to write, eachColumnSpace is each column information 
	with open(rrr,'r') as fc:
		with open(www,'w') as wo:
			wo.write(','.join(columnInformation[1])+'\n')
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
