import re
import itertools
import datetime
import sqlite3 as sqlite
import requests 
import urllib2
import json
import os
import traceback
import pandas as pd
import numpy as np
from inflation_calc.inflation import Inflation

# #This is for txt -> multiple csv files 
# #and multiple csv files -> one big files
# def columnInformation(csvFileFullName,k):
# 	#Getting each column's information from csvFileFullName
# 	#k==0 for Forclosure 
# 	#k==1 for Recorder
# 	#k==2 for TaxAssessor
# 	with open(csvFileFullName,'r') as fl:
# 		if k==0:
# 				#fl.readlines() or .read() gives one big string, so we are going to seperate by '\n'
# 				of=fl.read().splitlines()[2:69] #first 2 lines are unnecessary and we only need upto line 69.
# 		elif k==1:
# 			of1=fl.read().splitlines()[2:47] #first 2 lines are unnecessary and we only need upto line 47.
# 			with open(csvFileFullName,'r') as fl:
# 				of2=fl.read().splitlines()[64:108] 
# 			of=of1+of2
# 		else:
# 			of=fl.read().splitlines()[2:185] #first 2 lines are unnecessary and we only need upto line
# 	z=[re.search(r'[0-9].*[0-9],',i).group().split(',')[:-1] for i in of]
# 	z=zip(*z)
# 	#z[0] is column number
# 	#z[1] is headers
# 	#z[-1] is amount space that each column has.
# 	return z

# def makingSingleFileForEach():
# 	recorderFileList=['UMichRecorder1a.csv','UMichRecorder1b.csv','UMichRecorder1c.csv','UMichRecorder2a.csv','UMichRecorder2b.csv','UMichRecorder2c.csv','UMichRecorder3a.csv','UMichRecorder3b.csv','UMichRecorder3c.csv']
# 	taxAsseossorFileList=['UMichTaxAssessor1a.csv','UMichTaxAssessor1b.csv','UMichTaxAssessor1c.csv','UMichTaxAssessor2a.csv','UMichTaxAssessor2b.csv','UMichTaxAssessor2c.csv']
# 	keysList=['1a','1b','1c','2a','2b','2c','3a','3b','3c']
# 	with open('UMichTaxAssessor_Total.csv','w') as wo:
# 		with open('UMichTaxAssessor1a.csv','r') as rc:
# 			for i in rc.readlines():
# 				wo.write(i)
# 		for i in range(5):
# 			with open(taxAsseossorFileList[i+1],'r') as rc:
# 				for j in rc.readlines()[1:]:
# 					wo.write(j)
# 	with open('UmichRecorder_Total.csv','w') as wo:
# 		with open('UMichRecorder1a.csv','r') as rc:
# 			for i in rc.readlines():
# 				wo.write(i)
# 		for i in range(8):
# 			with open(recorderFileList[i+1],'r') as rc:
# 				for j in rc.readlines()[1:]:
# 					wo.write(j)
# 	return 'Done'

# def makingTxtfile(rrr,www,hhh,c):
# 	#rrr = CSV full file name
# 	#www = name textfile
# 	#hhh = headers
# 	#c==0 for Forclosure 
# 	#c==1 for Recorder
# 	#c==2 for TaxAssessor

# 	#Getting each column's information from csvFileFullName
# 	with open(rrr,'r') as fl:
# 		if c==0:
# 				#fl.readlines() or .read() gives one big string, so we are going to seperate by '\n'
# 				of=fl.read().splitlines()[2:69] #first 2 lines are unnecessary and we only need upto line 69.
# 		elif c==1:
# 			of1=fl.read().splitlines()[2:64] #first 2 lines are unnecessary and we only need upto line 47.
# 			with open(rrr,'r') as fl:
# 				of2=fl.read().splitlines()[64:108] 
# 			s=''
# 			for i in of1[45:]:
# 				s+=i
# 			of1[44]=of1[44]+s
# 			of=of1[:45]+of2
# 		else:
# 			of=fl.read().splitlines()[2:185]
# 	with open('UMich'+www+'.txt','w') as wo:
# 		ck=0
# 		for i in of:
# 			if re.search(r'(Yes|No)(.*)',i):
# 				k = re.search(r'(Yes|No)(.*)',i).group(2)[1:]
# 				if re.search(r'\s{2,}',k):
# 					gone = re.search(r'\s{2,}',k).group()
# 					k = k.replace(gone,'')
# 			else: 
# 				k = ''
# 			wo.write("\n".join([hhh[ck],'\t'+k])+'\n\n\n')
# 			ck+=1
# 	return 'DONE'

# def checkingRecords(k,col,dd):
# 	#imput: k = each file's unique name, col=column number, dd=dictionary
# 	with open('UMich'+k+'.csv') as dk:
# 		for i in dk.readlines()[1:]:
# 			if i.split(',')[col].lower() in dd:
# 				dd[i.split(',')[col].lower()]+=1
# 			else:
# 				dd[i.split(',')[col].lower()]=1
# 	return dd

# def forRecorderOrTaxAssessorCSV(rrr,www,columnInformation):
# 	eachColumnSpace=[int(i) for i in columnInformation[-1]]
# 	#rrr is file to read, www is a list of file names (3), eachcolumnspace is each column information 
# 	with open(rrr,'r') as rc:
# 		totalNumberOfRows=len(rc.readlines())
# 	remainder=totalNumberOfRows%3
# 	totalNum=totalNumberOfRows-remainder
# 	oneChunk=totalNum/3
# 	splitFiles=[oneChunk,2*oneChunk]#we only need to check 2 points to split them into 3 parts

# 	with open(rrr,'r') as rc:
# 		with open('UMich'+www[0]+'.csv','w') as wo:
# 			wo.write(','.join(columnInformation[1])+'\n')
# 			for i in rc.readlines()[0:splitFiles[0]]:
# 				eachList=[]
# 				for j in eachColumnSpace:
# 					eachList.append(i[:j])
# 					i = i[j:]
# 				#Last element of eachList is '\r\n'
# 				eachList=eachList[:-1]
# 				#We want to grab only data only or empty variable
# 				eachList=[re.search(r'([^\s].*[^\s]|[^\s])|[ ]+', i).group() for i in eachList]
# 				#For empty variables, we are replacing spaces with '' none. 
# 				for i in range(len(eachList)):
# 					if re.search(r'^\s+', eachList[i]):
# 						eachList[i]=eachList[i].replace(' ','')
# 				#Replacing commas with '' none. 
# 				eachList=[i.replace(',','') for i in eachList]
# 				wo.write(",".join(eachList)+'\n')

# 	with open(rrr,'r') as rc:
# 		with open('UMich'+www[1]+'.csv','w') as wo:
# 			wo.write(','.join(columnInformation[1])+'\n')
# 			for i in rc.readlines()[splitFiles[0]:splitFiles[1]]:
# 				eachList=[]
# 				for j in eachColumnSpace:
# 					eachList.append(i[:j])
# 					i = i[j:]
# 				#Last element of eachList is '\r\n'
# 				eachList=eachList[:-1]
# 				#We want to grab only data only or empty variable
# 				eachList=[re.search(r'([^\s].*[^\s]|[^\s])|[ ]+', i).group() for i in eachList]
# 				#For empty variables, we are replacing spaces with '' none. 
# 				for i in range(len(eachList)):
# 					if re.search(r'^\s+', eachList[i]):
# 						eachList[i]=eachList[i].replace(' ','')
# 				#Replacing commas with '' none. 
# 				eachList=[i.replace(',','') for i in eachList]
# 				wo.write(",".join(eachList)+'\n')

# 	with open(rrr,'r') as rc:
# 		with open('UMich'+www[2]+'.csv','w') as wo:
# 			wo.write(','.join(columnInformation[1])+'\n')
# 			for i in rc.readlines()[splitFiles[1]:]:
# 				eachList=[]
# 				for j in eachColumnSpace:
# 					eachList.append(i[:j])
# 					i = i[j:]
# 				#Last element of eachList is '\r\n'
# 				eachList=eachList[:-1]
# 				#We want to grab only data only or empty variable
# 				eachList=[re.search(r'([^\s].*[^\s]|[^\s])|[ ]+', i).group() for i in eachList]
# 				#For empty variables, we are replacing spaces with '' none. 
# 				for i in range(len(eachList)):
# 					if re.search(r'^\s+', eachList[i]):
# 						eachList[i]=eachList[i].replace(' ','')
# 				#Replacing commas with '' none. 
# 				eachList=[i.replace(',','') for i in eachList]
# 				wo.write(",".join(eachList)+'\n')
# 	return "Done"

# def onlyForeclosureCSV(rrr,www,columnInformation):
# 	eachColumnSpace=[int(i) for i in columnInformation[-1]]
# 	#rrr is file to read, www is a file that we want to write, eachColumnSpace is each column information 
# 	with open(rrr,'r') as fc:
# 		with open(www,'w') as wo:
# 			wo.write(','.join(columnInformation[1])+'\n')
# 			for i in fc.readlines():
# 				eachList=[]
# 				for j in eachColumnSpace:
# 					eachList.append(i[:j])
# 					i = i[j:]
# 				#Last element of eachList is '\r\n'
# 				eachList=eachList[:-1]
# 				#We want to grab only data only or empty variable
# 				eachList=[re.search(r'([^\s].*[^\s]|[^\s])|[ ]+', i).group() for i in eachList]
# 				#For empty variables, we are replacing spaces with '' none. 
# 				for i in range(len(eachList)):
# 					if re.search(r'^\s+', eachList[i]):
# 						eachList[i]=eachList[i].replace(' ','')
# 				#Replacing commas with '' none. 
# 				eachList=[i.replace(',','') for i in eachList]
# 				wo.write(",".join(eachList)+'\n')
# 	return "Done"

# #This is for sqlite.
# def makingListForACertainColumn_Integer(fullName,listOfIndexNumb):
# 	#fullName:file full name
# 	#listOfIndexNumb: list of index number
# 	#returns a single list contains len(listOfIndexNumb) number of tuples
# 	with open(fullName,'r') as fl:
# 		ff=fl.readlines()
# 	return [tuple(map(lambda j: int(i.split(',')[j]) if len(i.split(',')[j])!=0 else 0, listOfIndexNumb)) for i in ff[1:]]
# #This is for sqlite.
# def makingListForACertainColumn_Text(fullName,listOfIndexNumb):
# 	#fullName:file full name
# 	#listOfIndexNumb: list of index number
# 	#returns a single list contains len(listOfIndexNumb) number of tuples
# 	with open(fullName,'r') as fl:
# 		ff=fl.readlines()
# 	return [tuple(map(lambda j: i.split(',')[j], listOfIndexNumb)) for i in ff[1:]]

def gettingCensusTract(directory_k,k,starting=0,anyAdditionalName=''):
	#directory_k is a string ex) 'Mar/subfiles'
	#k is a list, contain how many files you want to request data 
	#starting is an integer (a starting index number)
	#anyAdditionalName is a string for file name 
	print os.listdir(directory_k)[k[0]:k[1]]
	for filename in os.listdir(directory_k)[k[0]:k[1]]:
		print filename
		print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
		dict_id_coordinates={}
		dict_id_row={}
		rowNumber=1
		dict_id_propertyValues={}
		with open(directory_k+filename,'r') as ck:
			ck=ck.readlines()
		for i in ck[1:]:
			z=i.replace('\r\n','').replace('\n','').split(',')
			dict_id_row[z[1]]=[rowNumber]
			rowNumber+=1
			dict_id_propertyValues[z[1]]=(z[6],z[7])
			dict_id_coordinates[z[1]]=(z[-1],z[-2])
		base='http://data.fcc.gov/api/block/2010/find'
		ak= open('Zip_Year_Tract_'+anyName+filename,'w')
		ak.write('Tract,Zip,Year,saPropertyId,Val_ass,Val_market\n')
		c=1
		#for i in sorted(dict_id_coordinates.keys()):
		for i in dict_id_coordinates:
			if c>starting:
				zipp=ck[dict_id_row[i][0]].split(',')[4]#zip
				yearr=ck[dict_id_row[i][0]].split(',')[5]#year
				#Getting tract information for each housing unit
				option={'latitude': float(dict_id_coordinates[i][0]),'longitude':float(dict_id_coordinates[i][1])}
				tractt=re.search(r'<Block FIPS="([0-9]{11})',requests.get(url=base, params=option).text).group(1)
				val1=dict_id_propertyValues[i][0]
				val2=dict_id_propertyValues[i][1]		
				ak.write("{},{},{},{},{},{}\n".format(tractt,zipp,yearr,i,val1,val2))
				print c,len(ck)
			c+=1
		ak.close()
	return 'Done'

def mergingCensusTractFiles(k,fileName):
	#k is an integer, either 0 or 1 due to having 'DS_...' file
	#fileName is a string ex) 'homeValues.txt'
 	initialOne = pd.read_csv('Mar/pct/'+os.listdir('Mar/pct')[k])
	#print initialOne.columns.to_series().groupby(initialOne.dtypes).groups
	for i in os.listdir('Mar/pct')[k+1:]:
		each=pd.read_csv('Mar/pct/'+i)
		initialOne = initialOne.append(pd.DataFrame(data = each), ignore_index=True)
	initialOne = initialOne[initialOne.Zip != 0.0]
	colls=['Zip','Year','saPropertyId','Val_ass','Val_market']

	initialOne[colls]=initialOne[colls].applymap(np.int64)
	initialOne.to_csv('Mar/pct/'+fileName,index=False)
	return 'Done'

def usingInflationAPI(fileName,whereToSave):
	#fileName is a string ex) 'homeValues.txt'
	#whereToSave is a string ex) 'Mar/NE_PropertyValues.txt'

	# Create a new Inflation instance
	inflation = Inflation()
	infla={}
	# How many US $ would I need in 2015 to pay for what cost $1 in eachYear
	for i in range(11):
		eachYear=i+2004
		infla[eachYear]=inflation.inflate(1, datetime.date(2015,1,1), datetime.date(eachYear,1,1), 'United States')
	print infla
	dfp=pd.read_csv('Mar/pct/'+fileName)

	dfp=dfp.sort(['Zip','Tract','Year'])
	dfp=dfp.reset_index(drop=True)
	dfp=dfp.rename(columns = {'Tract':'GEOID10','Val_ass':'VAL_ASS','Val_market':'VAL_MARKET','saPropertyId':'PROPERTY_ID','Zip':'ZIP','Year':'YEAR'})

	dfp['VAL_ASS_15']=0.0
	dfp['VAL_MARKET_15']=0.0

	for i in infla:	
		print i
		dfp.ix[dfp['YEAR']==i,'VAL_ASS_15'] = dfp.ix[dfp['YEAR']==i,'VAL_ASS'] * infla[i]
		dfp.ix[dfp['YEAR']==i,'VAL_MARKET_15'] = dfp.ix[dfp['YEAR']==i,'VAL_MARKET'] * infla[i]

	dfp = dfp[dfp['GEOID10'].astype(str).str.startswith('26')]
	dfp['GEOID10']=dfp['GEOID10'].astype(int)
	dfp.to_csv(whereToSave,index=False)
	return 'Done'




# ############################################################################################################
# #########################     Step 1     ###################################################################
# ############################################################################################################

# ################     Creating UMichForeclosure_Total.csv, UMichRecorder_Total.csv, UMichTaxAssessor_Total.c
# ################     From original REALTYTRAC txt files

# #######Foreclosure
# #Getting each column's information from REALTYTRAC DLP 3.0 Foreclosure Layout.xlsx
# eachColumn = columnInformation('REALTYTRAC DLP 3.0 Foreclosure Layout.csv',0)
# ignoreMe = onlyForeclosureCSV('University_of_Michigan_Foreclosure_001.txt','UMichForeclosure_Total.csv',eachColumn)

# #######Recorder
# #Getting each column's information from REALTYTRAC DLP 3.0 Recorder Layout.xlsx
# eachColumn = columnInformation('REALTYTRAC DLP 3.0 Recorder Layout.csv',1)
# ignoreMe = forRecorderOrTaxAssessorCSV('University_of_Michigan_Recorder_001.txt',['Recorder1a','Recorder1b','Recorder1c'],eachColumn)
# ignoreMe = forRecorderOrTaxAssessorCSV('University_of_Michigan_Recorder_002.txt',['Recorder2a','Recorder2b','Recorder2c'],eachColumn)
# ignoreMe = forRecorderOrTaxAssessorCSV('University_of_Michigan_Recorder_003.txt',['Recorder3a','Recorder3b','Recorder3c'],eachColumn)

# #######TaxAssessor
# #Getting each column's information from REALTYTRAC DLP 3.0 Assessor NO Geo Layout.xlsx
# eachColumn = columnInformation('REALTYTRAC DLP 3.0 Assessor NO Geo Layout.csv',2)
# ignoreMe = forRecorderOrTaxAssessorCSV('University_of_Michigan_TaxAssessor_001.txt',['TaxAssessor1a','TaxAssessor1b','TaxAssessor1c'],eachColumn)
# ignoreMe = forRecorderOrTaxAssessorCSV('University_of_Michigan_TaxAssessor_002.txt',['TaxAssessor2a','TaxAssessor2b','TaxAssessor2c'],eachColumn)

# #making UmichRecorder_Total +UmichTaxAssessor_Total file.
# ignoreMe = makingSingleFileForEach()

# ################     Checking if data has right number of records           

# #######Foreclosure
# kk = checkingRecords('Foreclosure',col=6,dd={})
# print sum(kk.values())
# print sorted(kk.items(), key= lambda x: x[0])
# #Total: 429875
# #[('genesee', 31185)
# #('lapeer', 4885), 
# #('livingston', 7556), 
# # ('macomb', 60447), 
# # ('monroe', 7582), 
# # ('oakland', 73751), 
# # ('saint clair', 9886), 
# # ('washtenaw', 13098), 
# # ('wayne', 221197)]

# #######Recorder
# lr = ['Recorder'+j for j in ['1a','1b','1c','2a','2b','2c','3a','3b','3c']]
# for i in lr:
# 	if i =='Recorder1a':
# 		subs = checkingRecords(i,col=7,dd={})
# 	else:
# 		final = checkingRecords(i,col=7,dd=subs)
# 		subs = final
# print sum(final.values())
# print sorted(final.items(), key= lambda x: x[0])
# # Total: 7056997
# # [('genesee', 427178), 
# # ('lapeer', 58920), 
# # ('livingston', 349521), 
# # ('macomb', 774258), 
# # ('monroe', 111704), 
# # ('oakland', 2186468), 
# # ('st. clair', 125686), 
# # ('washtenaw', 479496), 
# # ('wayne', 2543766)]

# #######TaxAssessor
# lta = ['TaxAssessor'+j for j in ['1a','1b','1c','2a','2b','2c']]
# for i in lta:
# 	if i =='TaxAssessor1a':
# 		subs = checkingRecords(i,col=6,dd={})
# 	else:
# 		final = checkingRecords(i,col=6,dd=subs)
# 		subs = final
# print sum(final.values())
# print sorted(final.items(), key= lambda x: x[0])
# # Total: 2290956
# # [('genesee', 195890), 
# # ('lapeer', 44837), 
# # ('livingston', 90088), 
# # ('macomb', 330502), 
# # ('monroe', 75122), 
# # ('oakland', 485889), 
# # ('saint clair', 82512), 
# # ('washtenaw', 146519), 
# # ('wayne', 839597)]





# ############################################################################################################
# #########################     Step 2     ###################################################################
# ############################################################################################################

# ################     Txt file for the column information(description)      

# #Getting each column's information from REALTYTRAC DLP 3.0 Foreclosure Layout.xlsx
# eachColumn = columnInformation('REALTYTRAC DLP 3.0 Foreclosure Layout.csv',0)
# headers = eachColumn[1]#headers
# ignoreMe = makingTxtfile('REALTYTRAC DLP 3.0 Foreclosure Layout.csv','ForeclosureLayout',headers,0)

# #######Recorder
# #Getting each column's information from REALTYTRAC DLP 3.0 Recorder Layout.xlsx
# eachColumn = columnInformation('REALTYTRAC DLP 3.0 Recorder Layout.csv',1)
# headers = eachColumn[1]#headers
# ignoreMe = makingTxtfile('REALTYTRAC DLP 3.0 Recorder Layout.csv','RecorderLayout',headers,1)

# #######TaxAssessor
# #Getting each column's information from REALTYTRAC DLP 3.0 Assessor NO Geo Layout.xlsx
# eachColumn = columnInformation('REALTYTRAC DLP 3.0 Assessor NO Geo Layout.csv',2)
# headers = eachColumn[1]#headers
# ignoreMe = makingTxtfile('REALTYTRAC DLP 3.0 Assessor NO Geo Layout.csv','TaxAssessorLayout',headers,2)

# ################     Checking 'unique Id' that represents each row 	      
# #Only for Foreclosure data
# with open('UmichForeclosure_Total.csv','r') as fc1:
# 	fc1=fc1.readlines()[1:]
# dd={}
# for i in fc1:
# 	#9th element is 'unique id'
# 	if i.split(',')[8] not in dd:
# 		dd[i.split(',')[8]]=1
# 	else:
# 		dd[i.split(',')[8]]+=1
# print len(fc1) 		  #429587
# print len(dd.keys())    #429587





# ############################################################################################################
# #########################     Step 3     ###################################################################
# ############################################################################################################

# ###############   Making databases to look up index(row) numbers

# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# #0 saPropetyID , 7 srUniqueID
# UMF=makingListForACertainColumn_Integer('UmichForeclosure_Total.csv',[0,7])
# print '1 / 3 completion'
# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# #0 saPropetyID , 171 srUniqueID
# UMTA=makingListForACertainColumn_Integer('UMichTaxAssessor_Total.csv',[0,171])
# print '2 / 3 completion'
# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# #0 srUniqueID, 1 saPropetyID 
# UMR=makingListForACertainColumn_Integer('UMichRecorder_Total.csv',[0,1])
# print '3 / 3 completion'
# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# with sqlite.connect(r'db_saPropertyID_srUniqueID.db') as con: 
# 	cur = con.cursor()
# 	cur.execute("DROP TABLE IF EXISTS f")
# 	cur.execute("CREATE TABLE f (row INTEGER PRIMARY KEY,  saPropertyID int, srUniqueID int)")
# 	cur.executemany("INSERT INTO f (saPropertyID,srUniqueID) VALUES (?,?)", UMF)
# 	con.commit()
# 	cur.execute("DROP TABLE IF EXISTS ta")
# 	cur.execute("CREATE TABLE ta (row INTEGER PRIMARY KEY,  saPropertyID int, srUniqueID int)")
# 	cur.executemany("INSERT INTO ta (saPropertyID, srUniqueID) VALUES (?,?)", UMTA)
# 	con.commit()
# 	cur.execute("DROP TABLE IF EXISTS r")
# 	cur.execute("CREATE TABLE r (row INTEGER PRIMARY KEY,  srUniqueID int, saPropertyID int)")
# 	cur.executemany("INSERT INTO r (srUniqueID,saPropertyID) VALUES (?,?)", UMR)
# 	con.commit()
	
# ################    Database exploratory

# with sqlite.connect(r'db_saPropertyID_srUniqueID.db') as con: 
# 	cur = con.cursor()
# 	To see how many of them do not contain 0
# 	check01=cur.execute("SELECT f.row,f.srUniqueID FROM f WHERE f.srUniqueID!=0")
# 	print len(check01.fetchall())#0
# 	check02=cur.execute("SELECT r.row,r.saPropertyID FROM r WHERE r.saPropertyID!=0")
# 	print len(check02.fetchall())#7056997
# 	#one way checking f.row r.row with saPropertyID

# 	#Double counting (because properties have been reported more than once)
# 	check1=cur.execute("SELECT f.row,r.row FROM f JOIN r ON (f.saPropertyID = r.saPropertyID ) WHERE r.saPropertyID!=0 ORDER BY f.row,r.row")
# 	print len(check1.fetchall())#2,645,169

# 	#two way checking with ta table
# 	check2=cur.execute("SELECT f.row,r.row FROM ta JOIN r JOIN f ON (f.saPropertyID = ta.saPropertyID and ta.srUniqueID = r.srUniqueID) ORDER BY f.row,r.row")
# 	print len(check2.fetchall())#384,446

# 	#Below is unique case for each property where we used GROUP BY METHOD 

# 	#one way checking
# 	selection1=cur.execute("SELECT f.row, r.row FROM f JOIN r ON (f.saPropertyID = r.saPropertyID ) WHERE r.saPropertyID!=0 GROUP BY f.saPropertyID ORDER BY f.row,r.row")
# 	print len(check1.fetchall())#251,755

#	#two way checking using fc table with saPropertyID
#	selection21=cur.execute("SELECT f.row, r.row, ta.row FROM f JOIN r JOIN ta ON (f.saPropertyID = r.saPropertyID and f.saPropertyID = ta.saPropertyID ) WHERE r.saPropertyID!=0 GROUP BY f.saPropertyID ORDER BY f.row,r.row,ta.row")
#	print len(selection21.fetchall())#251,755

# 	# two way checking using r table
# 	selection22=cur.execute("SELECT f.row, r.row, ta.row  FROM f JOIN r JOIN ta ON (f.saPropertyID = r.saPropertyID and r.srUniqueID = ta.srUniqueID ) WHERE r.saPropertyID!=0 GROUP BY f.saPropertyID ORDER BY f.row,r.row,ta.row ")
# 	print len(selection21.fetchall())#228,464

# 	#two way checking using ta table
# 	selection23=cur.execute("SELECT f.row,r.row,  ta.row  FROM f JOIN r JOIN ta ON (f.saPropertyID = ta.saPropertyID and ta.srUniqueID = r.srUniqueID) WHERE ta.saPropertyID!=0 and ta.srUniqueID!=0 GROUP BY f.saPropertyID ORDER BY f.row,r.row,ta.row ")
# 	print len(selection22.fetchall())#228,461

	


# ################  Making 3 csv files for forclosure and recorder using selection21   ################

# #Using selection21
# with sqlite.connect(r'db_saPropertyID_srUniqueID.db') as con: 
# 	cur = con.cursor()
# 	selection21=cur.execute("SELECT f.row, r.row, ta.row FROM f JOIN r JOIN ta ON (f.saPropertyID = r.saPropertyID and f.saPropertyID = ta.saPropertyID ) WHERE r.saPropertyID!=0 GROUP BY f.saPropertyID ORDER BY f.row,r.row,ta.row")
# 	selection21Inds = zip(*selection21.fetchall())

# with open('JanFeb/UMichForeclosure_Total.csv','r') as fc:
# 	fc=fc.readlines()
# 	with open('JanFeb/selection21Foreclosure.csv','w') as wo:
# 		wo.write(fc[0])
# 		for i in map(lambda j: fc[j], selection21Inds[0]):
# 			wo.write(i)
# with open('JanFeb/UMichRecorder_Total.csv','r') as fc:
# 	fc=fc.readlines()
# 	with open('JanFeb/selection21Recorder.csv','w') as wo:
# 		wo.write(fc[0])
# 		for i in map(lambda j: fc[j], selection21Inds[1]):
# 			wo.write(i)
# with open('JanFeb/UMichTaxAssessor_Total.csv','r') as fc:
# 	fc=fc.readlines()
# 	with open('JanFeb/selection21TaxAssessor.csv','w') as wo:
# 		wo.write(fc[0])
# 		for i in map(lambda j: fc[j], selection21Inds[2]):
# 			wo.write(i)
# print 'Done!'




# ############################################################################################################
# #########################     Step 4     ###################################################################
# ############################################################################################################

# ###############   Creating CSV file for foreclosure properties address
# with open('JanFeb/selection21Foreclosure.csv','r') as fc1:
# 	fc1=fc1.readlines()[1:]
# with open('JanFeb/selection21Recorder.csv','r') as fc2:
# 	fc2=fc2.readlines()[1:]
# with open('JanFeb/selection21TaxAssessor.csv','r') as fc3:
# 	fc3=fc3.readlines()[1:]

# print len(fc1),len(fc2),len(fc3)

# with open('JanFeb/selection21ForeclosureAddress.csv','w') as wo:
# 	wo.write('SA_PROPERTY_ID,SR_SITE_ADDR_RAW,FT_SITE_CITY,FT_SITE_STATE,FT_SITE_ZIP,SA_VAL_ASS,SA_VAL_MARKET\n')
# 	for i in range(len(fc1)):
# 		k=fc1[i].split(',')
# 		a=[k[0]]
# 		b=[fc2[i].split(',')[9]]
# 		c=map(lambda j: k[j], [55,56,57])
# 		d=[fc3[i].split(',')[85]]
# 		e=[fc3[i].split(',')[95]]
# 		wo.write(",".join(a+b+c+d+e)+'\n')
# print 'Done!'




# ################Removing empty addresses
# #about 15000 were removed, 237541 left
# with open('JanFeb/selection21ForeclosureAddress.csv','r') as kw:
# 	kw=kw.readlines()
# listOfAddresses=[i[0] for i in [map(lambda j: i.split(',')[j] if len(i.split(',')[j])!=0 else '', [1]) for i in kw]]
# listOfEmptyAddressIndex=[i for i in range(len(listOfAddresses)) if len(listOfAddresses[i])==0]
# for i in listOfEmptyAddressIndex[::-1]: #reverse the order so that we can safely delete all elements (order matters)
# 	del kw[i]	
# with open('JanFeb/selection21ForeclosureAddress.csv','w') as wo:
# 	for i in kw:
# 		wo.write(i)



# Then I geocoded all addresses and get the files in zip_coordinates file



################     Creating CSV contains zip,tract,year

# ###############This is to make sub csv files due to large amount
# #total of 237541 properties
# sfc=pd.read_csv('JanFeb/selection21Geocoded.txt')
# thisChunk=len(sfc.index)/5
# strt=len(sfc.index)/5
# init=0
# leftOver=len(sfc.index)%5
# for i in range(5):
# 	if i==4:
# 		sfc[init:thisChunk+leftOver+1].to_csv('JanFeb/subfiles/sfc'+str(i)+'.txt', encoding='utf-8',index=False)
# 	else:
# 		sfc[init:thisChunk].to_csv('JanFeb/subfiles/sfc'+str(i)+'.txt', encoding='utf-8',index=False)
# 		init=thisChunk
# 		thisChunk+=strt

# ###############Getting Census Tract using API
# #Id-row-number
# with open('JanFeb/selection21Foreclosure.csv','r') as fc1:
# 	fc1=fc1.readlines()
# dict_id_row={}
# rowNumber=1
# for i in fc1[1:]:
# 	dict_id_row[i.split(',')[0]]=[rowNumber]
# 	rowNumber+=1
# print os.listdir('JanFeb/subfiles')[5:6]
# for filename in os.listdir('JanFeb/subfiles')[5:6]:
# 	print filename
# 	print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# 	dict_id_coordinates={}
# 	dict_id_propertyValues={}
# 	with open('JanFeb/subfiles/'+filename,'r') as ck:
# 		ck=ck.readlines()
# 	for i in ck[1:]:
# 		z=i.replace('\r\n','').replace('\n','').split(',')
# 		dict_id_coordinates[z[3]]=(z[2],z[1])
# 		dict_id_propertyValues[z[3]]=(z[4],z[5])
# 	base='http://data.fcc.gov/api/block/2010/find'
# 	ak= open('Zip_Year_Tract_after8568'+filename,'w')
# 	ak.write('Tract,Zip,Year,saPropertyId,Val_ass,Val_market\n')
# 	c=1
# 	#for i in sorted(dict_id_coordinates.keys()):
# 	for i in dict_id_coordinates:
# 		if c>8568:
# 			zipp=fc1[dict_id_row[i][0]].split(',')[57]#zip
# 			yearr=fc1[dict_id_row[i][0]].split(',')[11][:4]#year
# 			#Getting tract information for each housing unit
# 			option={'latitude': float(dict_id_coordinates[i][0]),'longitude':float(dict_id_coordinates[i][1])}
# 			tractt=re.search(r'<Block FIPS="([0-9]{11})',requests.get(url=base, params=option).text).group(1)
# 			val1=dict_id_propertyValues[i][0]
# 			val2=dict_id_propertyValues[i][1]		
# 			ak.write("{},{},{},{},{},{}\n".format(tractt,zipp,yearr,i,val1,val2))
# 			print c,len(ck)
# 		c+=1
# 	ak.close()
# ################ Merging subfiles into one 
# print os.listdir('zip_year_tract')
# listOfFiles=os.listdir('zip_year_tract')
# with open("Mar/Zip_Year_Tract_Id.txt",'w') as dk:
# 	for i in range(len(listOfFiles)):
# 		if i!='.DS_Store':
# 			if i==1:
# 				kk = open("zip_year_tract/"+listOfFiles[i],'r')
# 				for j in kk.readlines():
# 						dk.write(j)
# 				kk.close()
# 			else:
# 				kk = open("zip_year_tract/"+listOfFiles[i],'r')
# 				for j in kk.readlines()[1:]:
# 						dk.write(j)
# 				kk.close()

# ################     Creating CSV contains County_Zip_TractLevel_totalNumbers
# with open('JanFeb/selection21Foreclosure.csv','r') as fc1:
# 	dict_countyCode_countyName={}
# 	for i in fc1.readlines()[1:]:
# 		if i.split(',')[5] not in dict_countyCode_countyName:
# 			dict_countyCode_countyName[i.split(',')[5]]=i.split(',')[3]
# print '1/3'
# with open("Mar/Zip_Year_Tract_Id.txt",'r') as sk:
# 	sk=sk.readlines()
# dict_countyCode_tract={}
# dict_tract_totalNumbs={}
# dict_tract_dict_year_count={}
# dict_tract_zip={}
# dict_zip_tract={}
# howManydifferentYear=[]
# for i in sk[1:]:
# 	countyCo=i.replace('\n','').split(',')[0][2:5]
# 	thisOne=i.replace('\n','').split(',')[0]
# 	zipp=i.replace('\n','').split(',')[1]
# 	years=i.replace('\n','').split(',')[2]
# 	if zipp not in dict_zip_tract:
# 		dict_zip_tract[zipp]=[thisOne]
# 	else:
# 		if thisOne not in dict_zip_tract[zipp]:
# 			dict_zip_tract[zipp].append(thisOne)

# 	if countyCo not in dict_countyCode_tract:
# 		dict_countyCode_tract[countyCo]=[thisOne]
# 	else:
# 		if thisOne not in dict_countyCode_tract[countyCo]:
# 			dict_countyCode_tract[countyCo].append(thisOne)
# 	if thisOne not in dict_tract_totalNumbs:
# 		dict_tract_totalNumbs[thisOne]=1
# 	else:
# 		dict_tract_totalNumbs[thisOne]+=1
# 	if thisOne not in dict_tract_dict_year_count:
# 		dict_tract_dict_year_count[thisOne]={}
# 		dict_tract_dict_year_count[thisOne][years]=1
# 	else:
# 		if years not in dict_tract_dict_year_count[thisOne]:
# 			dict_tract_dict_year_count[thisOne][years]=1
# 		else:
# 			dict_tract_dict_year_count[thisOne][years]+=1
# 	if years not in howManydifferentYear:
# 		howManydifferentYear.append(years)
# 	if thisOne not in dict_tract_zip:
# 		dict_tract_zip[thisOne]=zipp
# print '2/3'
# with open('Mar/County_Zip_TractLevel_totalNumbers.txt', 'w') as writeIt:
# 	writeIt.write('County,Zipcode,Id2,Total,F2004,F2005,F2006,F2007,F2008,F2009,F2010,F2011,F2012,F2013,F2014,F2015\n')
# 	for i in dict_countyCode_countyName:
# 		countyName=dict_countyCode_countyName[i]
# 		listOfTractCode=sorted(dict_countyCode_tract[i])
# 		totalnumbs=0
# 		eachyeartotal={}
# 		for eachTract in listOfTractCode:
# 			zipp=dict_tract_zip[eachTract]
# 			eachTotal=dict_tract_totalNumbs[eachTract]
# 			totalnumbs+=eachTotal
# 			writeIt.write('{},{},{},{},'.format(countyName,zipp,eachTract,eachTotal))
# 			for eachYear in sorted(howManydifferentYear):
# 				if eachYear=='2015':
# 					try:
# 						writeIt.write('{}\n'.format(dict_tract_dict_year_count[eachTract][eachYear]))
# 					except:
# 						writeIt.write('0\n')
# 				else:	
# 					try:
# 						writeIt.write('{},'.format(dict_tract_dict_year_count[eachTract][eachYear]))
# 					except:
# 						writeIt.write('0,')

# print '3/3'





# ###########################################################################################################
# ########################     Step 5     ###################################################################
# ###########################################################################################################

# #Creating FC rates 

# ################     Adding Mortgage numbers to County_Zip_TractLevel_totalNumbers.txt
# lookUp=[i for i in os.listdir('Mar') if 'totalNumbers.txt' in i][0]
# lookUp=pd.read_csv('Mar/'+lookUp)
# listOfeachFile=os.listdir('Mar/ACS')
# # lookUp = lookUp.loc[np.repeat(lookUp.index.values,6)]
# # createNewDf=lookUp[['Id2','County']]
# # yearss=[2010,2011,2012,2013,2014,2015]
# # createNewDf['Year']=yearss * (createNewDf.shape[0]/len(yearss))
# originalIndexNumber=len(lookUp.index)
# #'Id2','County','Year','Foreclosure','RealEstateOwned','Total'
# fYears=['F2010','F2011','F2012','F2013','F2014','F2015']
# onlyForOnce=0 #this is to make initinal dataframe
# newColumn1='Real_Estate_Owned'
# newColumn2='Total'
# for i in range(len(listOfeachFile)):
# 	#this is order of [2010,2011,2012,2013,2014,2015]
# 	print listOfeachFile[i]
# 	eachDf=pd.read_csv('Mar/ACS/'+listOfeachFile[i],header=None)
# 	eachDf.drop(eachDf.index[[0]],inplace=True)
# 	eachDf.rename(columns=eachDf.iloc[0],inplace=True)
# 	eachDf['Id2']=eachDf['Id2']
# 	thislookup=lookUp[['Id2','County']]
# 	thislookup['Year']=fYears[i][1:]
# 	thislookup['Foreclosure']=lookUp[fYears[i]]
# 	if onlyForOnce==0:
# 		onlyForOnce+=1
# 		#adding 'RealEstateOwned'
# 		br=False
# 		while br!=True:
# 			for col in range(len(eachDf.columns)):
# 				if 'Estimate; MORTGAGE STATUS' in eachDf.iloc[0,col] and 'Housing units with a mortgage' in eachDf.iloc[0,col]:
# 					thisColumn=eachDf.iloc[0,col]
# 					br=True
# 					# print eachDf.loc[eachDf['Id2']=='26163599000',thisColumn]
# 		eachDf[newColumn1]=eachDf[thisColumn]
# 		eachDf['Id2'] = pd.to_numeric(eachDf['Id2'], errors='coerce')
# 		thislookup1=pd.merge(thislookup, eachDf[['Id2',newColumn1]], left_on='Id2', right_on='Id2',  how='outer')
# 		thislookup1=thislookup1[:originalIndexNumber]
# 		#adding 'Total'
# 		thisColumn=eachDf.iloc[0,3]
# 		eachDf[newColumn2]=eachDf[thisColumn]
# 		thislookup1=pd.merge(thislookup1, eachDf[['Id2',newColumn2]], left_on='Id2', right_on='Id2',  how='outer')
# 		thislookup1=thislookup1[:originalIndexNumber]	

# 		# I will make chunk every loop and rbind the chunk after second loop
# 		#Id2, County year Foreclosures RealEstateOwned Total 
# 	else:
# 		br=False
# 		while br!=True:
# 			for col in range(len(eachDf.columns)):
# 				if 'Estimate; MORTGAGE STATUS' in eachDf.iloc[0,col] and 'Housing units with a mortgage' in eachDf.iloc[0,col]:
# 					thisColumn=eachDf.iloc[0,col]
# 					br=True
# 					# print eachDf.loc[eachDf['Id2']=='26163599000',thisColumn]
# 		eachDf[newColumn1]=eachDf[thisColumn]
# 		eachDf['Id2'] = pd.to_numeric(eachDf['Id2'], errors='coerce')
# 		thislookup11=pd.merge(thislookup, eachDf[['Id2',newColumn1]], left_on='Id2', right_on='Id2',  how='outer')
# 		thislookup11=thislookup11[:originalIndexNumber]
		
# 		thisColumn=eachDf.iloc[0,3]
# 		eachDf[newColumn2]=eachDf[thisColumn]
# 		thislookup11=pd.merge(thislookup11, eachDf[['Id2',newColumn2]], left_on='Id2', right_on='Id2',  how='outer')
# 		thislookup11=thislookup11[:originalIndexNumber]
# 		thislookup1 = thislookup1.append(thislookup11, ignore_index=True)

# thislookup1['Id2']=thislookup1['Id2'].astype(int)
# thislookup1['Foreclosure']=thislookup1['Foreclosure'].astype(int)
# thislookup1['Real_Estate_Owned_Rate']=thislookup1['Foreclosure']/thislookup1['Real_Estate_Owned'].astype(float)
# thislookup1['Overall_Rate']=thislookup1['Foreclosure']/thislookup1['Total'].astype(float)
# thislookup1=thislookup1.rename(columns = {'Id2':'GEOID10','Count':'COUNTY','Year':'YEAR','Foreclosure':'FORECLOSURE','Real_Estate_Owned':'REAL_ESTATE_OWNED','Total':'ALL_HOUSING','Real_Estate_Owned_Rate':'REAL_ESTATE_OWNED_RATE','Overall_Rate':'ALL_HOUSING_RATE'})
# thislookup1.to_csv('Mar/NE_ForeclosureRates.csv', encoding='utf-8',index=False)





# ###########################################################################################################
# ########################     Step 6     ###################################################################
# ###########################################################################################################

# #Creating all property values around 10 counties 

#-----------------------Ignore this part-----------------------------------------------
# ta=pd.read_csv('JanFeb/UMichTaxAssessor_Total.csv')

# print len(ta.index)
# print 'TAXYEAR'
# print ta.TAXYEAR.unique()
# print 'ASSR_YEAR'
# print ta.ASSR_YEAR.unique()
# print 'SA_APPRAISE_YR'
# print ta.SA_APPRAISE_YR.unique()
# print 'SA_YR_LAND_APPRAISE'
# print ta.SA_YR_LAND_APPRAISE.unique()
# print 'SA_TAX_YEAR_DELINQ'
# print ta.SA_TAX_YEAR_DELINQ.unique()
# print 'SA_YR_BLT'
# print ta.SA_YR_BLT.unique()
# print 'SA_YR_BLT_EFFECT'
# print ta.SA_YR_BLT_EFFECT.unique()
# print 'SA_PARCEL_NBR_CHANGE_YR'
# print ta.SA_PARCEL_NBR_CHANGE_YR.unique()
# print 'SA_YR_APN_ADDED'
# print ta.SA_YR_APN_ADDED.unique()

# rdd=pd.read_csv('JanFeb/UMichRecorder_Total.csv')

# #Example
# #s = pd.Series([0,1,2])
# #for i in s: 
# #    print (i)
# #0
# #1
# #2
# #type(rdd.SR_DATE_TRANSFER) -- series
# sdict={}
# for i in rdd.SR_DATE_TRANSFER:
# 	kk = str(i)
# 	if kk[:4] not in sdict:
# 		sdict[kk[:4]]=1
# print sdict.keys()
# sdict={}
# for i in rdd.SR_DATE_FILING:
# 	kk = str(i)
# 	if kk[:4] not in sdict:
# 		sdict[kk[:4]]=1
# print sdict.keys()

#----------------------------------------------------------------------



########## FIRST until line 947     AFter line 947, the code is same, but doing rest 1M data

# ta=pd.read_csv('JanFeb/UMichTaxAssessor_Total.csv')
# #SA_PROPERTY_ID, SR_UNIQUE_ID,SA_SITE_CITY,SA_SITE_STATE,SA_SITE_ZIP,TAXYEAR,SA_VAL_ASSD, SA_VAL_MARKET
# ta = ta[['SR_UNIQUE_ID','SA_PROPERTY_ID','SA_SITE_CITY','SA_SITE_STATE','SA_SITE_ZIP','TAXYEAR','SA_VAL_ASSD','SA_VAL_MARKET']]
# ta = ta[ta.SR_UNIQUE_ID != 0]
# ta = ta[ta.SR_UNIQUE_ID.notnull()]
# #Instead of checking TAXYEAR, SA_VAL_ASSD, and SA_VAL_MARKET, just checking SA_VAL_ASSD once
# ta = ta[ta.SA_VAL_ASSD.notnull()]

# rr=pd.read_csv('JanFeb/UmichRecorder_Total.csv')
#SR_UNIQUE_ID,SR_PROPERTY_ID, SR_SITE_ADDR_RAW
# rr = rr[['SR_UNIQUE_ID','SR_PROPERTY_ID','SR_SITE_ADDR_RAW']]
# rr = rr[rr.SR_UNIQUE_ID != 0]
# rr = rr[rr.SR_UNIQUE_ID.notnull()]
# #print len(rr.index)#7056997
# rr = rr[rr.SR_SITE_ADDR_RAW.notnull()]

# merged=pd.merge(ta, rr , on=['SR_UNIQUE_ID'],  how="outer")
# #print len(merged.index)#6248546
# #removing some rows once more 
# print len(rr.index)
# rr = rr[rr.SA_VAL_ASSD.notnull()]
# rr = rr[rr.SA_VAL_ASSD!=0]
# rr.to_csv('Mar/property_Complete.txt', encoding='utf-8',index=False)

# #steps for GEOCODING
# tt=pd.read_csv('Mar/property_Complete.txt')
# print len(tt.index)
# tt = tt[['SR_UNIQUE_ID','SA_PROPERTY_ID','SR_SITE_ADDR_RAW','SA_SITE_CITY','SA_SITE_STATE','SA_SITE_ZIP','SA_VAL_ASSD','SA_VAL_MARKET']]
# tt.to_csv('Mar/PropertyForGeocoding.csv', encoding='utf-8',index=False)

#after geocoding all properties (about 1,080,000)
###############This is to make sub csv files due to large amount
#total of 1,080,000 properties
# sfc=pd.read_csv('Mar/propertyGeocoded.txt')
# thisChunk=len(sfc.index)/10
# strt=len(sfc.index)/10
# init=0
# leftOver=len(sfc.index)%10
# for i in range(10):
# 	if i==9:
# 		sfc[init:thisChunk+leftOver+1].to_csv('Mar/subfiles/propertyGeocoded'+str(i)+'.txt', encoding='utf-8',index=False)
# 	else:
# 		sfc[init:thisChunk].to_csv('Mar/subfiles/propertyGeocoded'+str(i)+'.txt', encoding='utf-8',index=False)
# 		init=thisChunk
# 		thisChunk+=strt

# ###############Getting Census Tract using API
# #Id-row-number
# with open('Mar/property_Complete.txt','r') as fc1:
# 	fc1=fc1.readlines()
# dict_id_row={}
# rowNumber=1
# dict_id_propertyValues={}
# for i in fc1[1:]:
# 	z=i.replace('\r\n','').replace('\n','').split(',')
# 	dict_id_row[z[1]]=[rowNumber]
# 	rowNumber+=1
# 	dict_id_propertyValues[z[1]]=(z[6],z[7])
# #takes 10 hours for each file. 
#gettingCensusTract('Mar/subfiles',[1:10],starting=0,anyAdditionalName='')

# ################ Merging subfiles into one and deleting rows that are out of zipcode
# #Step1
# mergingCensusTractFiles(1,'homeValues.txt')

# #Step2
# usingInflationAPI('homeValues.txt','Mar/NE_PropertyValues.txt')

# #Step3
# dfp=pd.read_csv('Mar/NE_PropertyValues.txt')
# del dfp['PROPERTY_ID']
# del dfp['ZIP']
# dfp=dfp.groupby(['GEOID10','YEAR']).mean().reset_index()

# dfp.to_csv('Mar/NE_PropertyValues_mean.txt',index=False)

########## SECOND

ta=pd.read_csv('JanFeb/UMichTaxAssessor_Total.csv')
#SA_PROPERTY_ID, SR_UNIQUE_ID,SA_SITE_CITY,SA_SITE_STATE,SA_SITE_ZIP,TAXYEAR,SA_VAL_ASSD, SA_VAL_MARKET
ta = ta[['SR_UNIQUE_ID','SA_PROPERTY_ID','SA_SITE_CITY','SA_SITE_STATE','SA_SITE_ZIP','TAXYEAR','SA_VAL_ASSD','SA_VAL_MARKET']]
ta = ta.drop_duplicates(subset='SA_PROPERTY_ID', keep='first')
ta['key1'] = 1

dk=pd.read_csv('Mar/property_Complete.txt')
dk=dk[['SA_PROPERTY_ID']]

dk['key2'] = 1
print 'original length'
print len(ta.index)
df_1 = pd.merge(ta, dk, on=['SA_PROPERTY_ID'], how = 'left')

df_1 = df_1[~(df_1.key2 == df_1.key1)]
df_1 = df_1.drop(['key1','key2'], axis=1)

# df_1 = df_1.drop(['key1','key2','SA_PROPERTY_ID_y', 'SA_SITE_CITY_y', 'SA_SITE_STATE_y', 'SA_SITE_ZIP_y', 'TAXYEAR_y', 'SA_VAL_ASSD_y', 'SA_VAL_MARKET_y'], axis=1)
# df_1 = df_1.rename(columns={'SA_PROPERTY_ID_x': 'SA_PROPERTY_ID', 'SA_SITE_CITY_x': 'SA_SITE_CITY','SA_SITE_STATE_x':'SA_SITE_STATE','SA_SITE_ZIP_x':'SA_SITE_ZIP','TAXYEAR_x':'TAXYEAR','SA_VAL_ASSD_x':'SA_VAL_ASSD','SA_VAL_MARKET_x':'SA_VAL_MARKET'})
print len(dk.index)
print list(df_1)
print len(df_1.index)
rr=pd.read_csv('JanFeb/UmichRecorder_Total.csv')
rr = rr[['SR_UNIQUE_ID','SR_PROPERTY_ID','SR_SITE_ADDR_RAW']]
print 'rr length'
print len(rr.index)
rr = rr.drop_duplicates(subset='SR_PROPERTY_ID', keep='first')
print len(rr.index)
merged1 = pd.merge(df_1, rr , left_on='SA_PROPERTY_ID', right_on='SR_PROPERTY_ID', how="left")
#PROPERTY_ID's are all unique

merged1 = merged1[merged1.SR_SITE_ADDR_RAW.notnull()]
merged1 = merged1[merged1.SR_SITE_ADDR_RAW != 0]
merged1 = merged1[merged1.SA_VAL_ASSD.notnull()]
merged1 = merged1[merged1.SA_VAL_ASSD!=0]
print len(merged1.index)
print list(merged1)
merged1.to_csv('Mar/property_Complete_Rest.txt', encoding='utf-8',index=False)

##############This is to make sub csv files due to large amount
# #total of 559,000 properties
# sfc=pd.read_csv('Mar/propertyGeocoded_Rest.txt')
# thisChunk=len(sfc.index)/6
# strt=len(sfc.index)/6
# init=0
# leftOver=len(sfc.index)%6
# for i in range(6):
# 	if i==5:
# 		sfc[init:thisChunk+leftOver+1].to_csv('Mar/subfiles/propertyGeocoded'+str(i)+'.txt', encoding='utf-8',index=False)
# 	else:
# 		sfc[init:thisChunk].to_csv('Mar/subfiles/propertyGeocoded'+str(i)+'.txt', encoding='utf-8',index=False)
# 		init=thisChunk
# 		thisChunk+=strt

#steps for GEOCODING
# ###############Getting Census Tract using API
# #Id-row-number
# print os.listdir('Mar/subfiles')[6:7]
# for filename in os.listdir('Mar/subfiles')[6:7]:
# 	print filename
# 	print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# 	dict_id_coordinates={}
# 	dict_id_row={}
# 	rowNumber=1
# 	dict_id_propertyValues={}
# 	with open('Mar/subfiles/'+filename,'r') as ck:
# 		ck=ck.readlines()
# 	for i in ck[1:]:
# 		z=i.replace('\r\n','').replace('\n','').split(',')
# 		dict_id_row[z[1]]=[rowNumber]
# 		rowNumber+=1
# 		dict_id_propertyValues[z[1]]=(z[6],z[7])
# 		dict_id_coordinates[z[1]]=(z[-1],z[-2])
# 	base='http://data.fcc.gov/api/block/2010/find'
# 	ak= open('REST_Zip_Year_Tract_RRR23900'+filename,'w')
# 	ak.write('Tract,Zip,Year,saPropertyId,Val_ass,Val_market\n')
# 	c=1
# 	#for i in sorted(dict_id_coordinates.keys()):
# 	for i in dict_id_coordinates:
# 		if c>23900:
# 			zipp=ck[dict_id_row[i][0]].split(',')[4]#zip
# 			yearr=ck[dict_id_row[i][0]].split(',')[5]#year
# 			#Getting tract information for each housing unit
# 			option={'latitude': float(dict_id_coordinates[i][0]),'longitude':float(dict_id_coordinates[i][1])}
# 			tractt=re.search(r'<Block FIPS="([0-9]{11})',requests.get(url=base, params=option).text).group(1)
# 			val1=dict_id_propertyValues[i][0]
# 			val2=dict_id_propertyValues[i][1]		
# 			ak.write("{},{},{},{},{},{}\n".format(tractt,zipp,yearr,i,val1,val2))
# 			print c,len(ck)
# 		c+=1
# 	ak.close()

# ################ Merging subfiles into one and deleting rows that are out of zipcode

# #Step1
# initialOne = pd.read_csv('Mar/pct2/'+os.listdir('Mar/pct2')[0])
# #print initialOne.columns.to_series().groupby(initialOne.dtypes).groups

# for i in os.listdir('Mar/pct2')[1:]:
# 	each=pd.read_csv('Mar/pct2/'+i)
# 	initialOne = initialOne.append(pd.DataFrame(data = each), ignore_index=True)
# initialOne = initialOne[initialOne.Zip != 0.0]
# colls=['Zip','Year','saPropertyId','Val_ass','Val_market']

# initialOne[colls]=initialOne[colls].applymap(np.int64)
# initialOne.to_csv('Mar/pct2/homeValues2.txt',index=False)



# #Step2
# # Create a new Inflation instance
# inflation = Inflation()
# infla={}
# # How many US $ would I need in 2015 to pay for what cost $1 in eachYear
# for i in range(11):
# 	eachYear=i+2004
# 	infla[eachYear]=inflation.inflate(1, datetime.date(2015,1,1), datetime.date(eachYear,1,1), 'United States')
# print infla

# dfp=pd.read_csv('Mar/pct2/homeValues2.txt')

# dfp=dfp.sort(['Zip','Tract','Year'])
# dfp=dfp.reset_index(drop=True)
# dfp=dfp.rename(columns = {'Tract':'GEOID10','Val_ass':'VAL_ASS','Val_market':'VAL_MARKET','saPropertyId':'PROPERTY_ID','Zip':'ZIP','Year':'YEAR'})

# dfp['VAL_ASS_15']=0.0
# dfp['VAL_MARKET_15']=0.0

# for i in infla:	
# 	print i
# 	dfp.ix[dfp['YEAR']==i,'VAL_ASS_15'] = dfp.ix[dfp['YEAR']==i,'VAL_ASS'] * infla[i]
# 	dfp.ix[dfp['YEAR']==i,'VAL_MARKET_15'] = dfp.ix[dfp['YEAR']==i,'VAL_MARKET'] * infla[i]

# dfp = dfp[dfp['GEOID10'].astype(str).str.startswith('26')]
# dfp['GEOID10']=dfp['GEOID10'].astype(int)
# dfp.to_csv('Mar/NE_PropertyValues2.txt',index=False)



# ##########################actually you have to do this first 
# ########MERGING ALL GEOCODED CENSUS TRACT ID

# #Merging two files 
# initialOne = pd.read_csv('Mar/NE_PropertyValues.txt')
# #print initialOne.columns.to_series().groupby(initialOne.dtypes).groups

# each=pd.read_csv('Mar/NE_PropertyValues2.txt')

# initialOne = initialOne.append(pd.DataFrame(data = each), ignore_index=True)

# initialOne.to_csv('Mar/NE_PropertyValues_Final.txt',index=False)




# # #Step3
# dfp=pd.read_csv('Mar/NE_PropertyValues2.txt')
# del dfp['PROPERTY_ID']
# del dfp['ZIP']
# dfp=dfp.groupby(['GEOID10','YEAR']).mean().reset_index()

# dfp.to_csv('Mar/NE_PropertyValues_mean2.txt',index=False)



# #Merging two files 
# initialOne = pd.read_csv('Mar/NE_PropertyValues_mean.txt')
# #print initialOne.columns.to_series().groupby(initialOne.dtypes).groups

# each=pd.read_csv('Mar/NE_PropertyValues_mean2.txt')
# initialOne = initialOne.append(pd.DataFrame(data = each), ignore_index=True)

# initialOne.to_csv('Mar/NE_PropertyValues_mean_Final.txt',index=False)

# ################# Merging NE datasets
# #doing the rest of the data
# dd={'idd':['a','b','c','d','e'],'kk':[1,2,3,4,5]}
# kk={'idd':['a','x','y','z',],'kk':[1,2,3,4]}
# dd=pd.DataFrame(dd)
# kk=pd.DataFrame(kk)
# print dd
# print kk
# dd['key1']=1
# kk['key2']=1
# cc = pd.merge(dd, kk , on=['idd'], how="left")
# print cc
# print cc[~(cc.key1==cc.key2)]

# #final version of data 
# dfp=pd.read_csv('Mar/NE_PropertyValues_mean_Final.txt')
# dfp2=pd.read_csv('Mar/NE_ForeclosureRates.csv')
# dfp['key1']=1
# dfp['key2']=1

# dff=pd.merge(dfp2, dfp, on = ['GEOID10','YEAR'],  how='outer')
# dff=dff[dff.key1==dff.key2]
# del dff['key1']
# del dff['key2']
# dff.to_csv('Apr/NE_data22.csv',encoding='utf-8',index=False)








# ##########################
# ########macthing all the sales transactions property ID to Census tract

################# Merging NE datasets
#doing the rest of the data
# dd={'idd_a':['a','b','c','d','e','a','b','c'],'kk':[99,99,99,99,99,99,99,99]}
# kk={'idd_b':['a','b','c','y','z'],'kk':[88,88,88,88,88]}
# kk={'idd_b':['a','b','c','y','z','a'],'kk':[88,88,88,88,88,88]}
# dd=pd.DataFrame(dd)
# kk=pd.DataFrame(kk)
# print dd
# print kk
# dd['key1']=1
# kk['key2']=1
# cc = pd.merge(dd, kk , left_on='idd_a',right_on='idd_b', how="left")
# print cc

# cc = pd.merge(dd, kk , left_on='idd_a',right_on='idd_b', how="outer")
# print cc

# #Merging two files 

rr=pd.read_csv('JanFeb/UmichRecorder_Total.csv')
rr = rr[['SR_UNIQUE_ID','SR_PROPERTY_ID','SR_DATE_TRANSFER','SR_DATE_FILING','MM_FIPS_COUNTY_NAME']]
rr['SR_DATE_TRANSFER'] = rr['SR_DATE_TRANSFER'].map(lambda x: int(str(x)[:4]))
rr['SR_DATE_FILING'] = rr['SR_DATE_FILING'].map(lambda x: int(str(x)[:4]))
rr['que'] = np.where((rr['SR_DATE_TRANSFER'] == rr['SR_DATE_FILING']), 1, np.nan)
print 'rr length'
print len(rr.index)
kk = pd.read_csv('Mar/NE_PropertyValues_Final.txt')
kk = kk[['GEOID10','PROPERTY_ID','ZIP']]
kk = kk.drop_duplicates(subset='PROPERTY_ID', keep='first')#we assessed different years so we have some duplicates

rr['key1']=1
kk['key2']=1
merged1 = pd.merge(rr, kk , left_on='SR_PROPERTY_ID', right_on='PROPERTY_ID', how="left")
print len(merged1[merged1.key1==merged1.key2].index)
print len(merged1[~(merged1.key1==merged1.key2)].index)

mm=merged1[~(merged1.key1==merged1.key2)]
del mm['key1']
del mm['key2']

# del merged1['key1']
# del merged1['key2']
# #PROPERTY_ID's are all unique
# #merged1  --> columns would be : GEOID , 'SR_DATE_TRANSFER', 'SR_DATE_FLIING'
# #after merging 
# rr=pd.read_csv('Mar/ppp.txt')
# #changing yy/mm/dd to yy values
# print rr
# print rr[rr.que!=1]
# print rr.groupby('SR_PROPERTY_ID')['SR_DATE_TRANSFER'].nunique()
# print rr.groupby(['GEOID','YYYY']).count()
# zzz= rr.groupby(['GEOID','YYYY']).count().reset_index()
# print zzz
# zzz.to_csv('Mar/zzz.txt', encoding='utf-8',sep='\t',header=True,index=False)











