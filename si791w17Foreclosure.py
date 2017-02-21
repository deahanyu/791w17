import re
import myfunc
import itertools
import datetime
import sqlite3 as sqlite

############################################################################################################
#########################     Week 1     ###################################################################
############################################################################################################
##---------------ignore code BELOW completely. NOT useful at all.---------------##
# with open('University_of_Michigan_Foreclosure_001.txt','r') as fc:
# 	with open('foreclosureOriginal.csv','w') as wo:
# 		wo.write('\n')
# 		for i in fc.readlines():
# 			k = myfunc.foreclosureStandardizeObj(myfunc.adjustForeclosureObj(i))
# 			wo.write(",".join(k)+'\n')
##---------------ignore code ABOVE completely. NOT useful at all.---------------##








############################################################################################################
#########################     Week 2     ###################################################################
############################################################################################################


#####################################################################################################
################               Saving an original version as CSV file                ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# #Getting each column's information from REALTYTRAC DLP 3.0 Foreclosure Layout.xlsx
# eachColumn = myfunc.columnInformation('REALTYTRAC DLP 3.0 Foreclosure Layout.csv',0)

# myfunc.onlyForeclosureCSV('University_of_Michigan_Foreclosure_001.txt','UMichForeclosure.csv',eachColumn)


#####################################################################################################
################            Checking if data has right number of records             ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# kk= myfunc.checkingRecords('Foreclosure',col=6,dd={})
# print sum(kk.values())
# print sorted(kk.items(), key= lambda x: x[0])
#	  
#	  #429875, Actual records: 429875
#     #[('genesee', 31185)
#     #('lapeer', 4885), 
#     #('livingston', 7556), 
#     # ('macomb', 60447), 
#     # ('monroe', 7582), 
#     # ('oakland', 73751), 
#     # ('saint clair', 9886), 
#     # ('washtenaw', 13098), 
#     # ('wayne', 221197)]











############################################################################################################
#########################     Week 3     ###################################################################
############################################################################################################


#####################################################################################################
################           Txt file for the column information - description         ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# #Getting each column's information from REALTYTRAC DLP 3.0 Foreclosure Layout.xlsx
# eachColumn = myfunc.columnInformation('REALTYTRAC DLP 3.0 Foreclosure Layout.csv',0)
# headers = eachColumn[1]#headers
# myfunc.makingTxtfile('REALTYTRAC DLP 3.0 Foreclosure Layout.csv','ForeclosureLayout',headers,0)

# #making UmichRecorder_Total +UmichTaxAssessor_Total file.
# myfunc.makingSingleFileForEach()


#####################################################################################################
################   			Checking 'unique Id' that represents each row 	         ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# with open('UmichForeclosure_Total.csv','r') as fc1:
# 	fc1=fc1.readlines()[1:]
# dd={}
# for i in fc1:
# 	if i.split(',')[8] not in dd:
# 		dd[i.split(',')[8]]=1
# 	else:
# 		dd[i.split(',')[8]]+=1
# print len(fc1) 		  #429587
# print len(dd.keys())    #429587



####################################################################################################
###############           Making databases to look up index(row) numbers            ################
#---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# #0 saPropetyID , 7 srUniqueID
# UMF=myfunc.makingListForACertainColumn_Integer('UmichForeclosure_Total.csv',[0,7])
# print '1 / 3 completion'
# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# #0 saPropetyID , 171 srUniqueID
# UMTA=myfunc.makingListForACertainColumn_Integer('UMichTaxAssessor_Total.csv',[0,171])
# print '2 / 3 completion'
# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# #0 srUniqueID, 1 saPropetyID 
# UMR=myfunc.makingListForACertainColumn_Integer('UMichRecorder_Total.csv',[0,1])
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
	
	

#####################################################################################################
################                 Database        exploratory                         ################
# ##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# with sqlite.connect(r'db_saPropertyID_srUniqueID.db') as con: 
# 	cur = con.cursor()
	# #To see how many of them do not contain 0
	# check01=cur.execute("SELECT f.row,f.srUniqueID FROM f WHERE f.srUniqueID!=0")
	# print len(check01.fetchall())#0
	# check02=cur.execute("SELECT r.row,r.saPropertyID FROM r WHERE r.saPropertyID!=0")
	# print len(check02.fetchall())#7056997
	# one way checking f.row r.row with saPropertyID

	# #Double counting issues because properties have been reported more than once
	# check1=cur.execute("SELECT f.row,r.row FROM f JOIN r ON (f.saPropertyID = r.saPropertyID ) WHERE r.saPropertyID!=0 ORDER BY f.row,r.row")
	# print len(check1.fetchall())#2,645,169
	# #two way checking with ta table
	# check2=cur.execute("SELECT f.row,r.row FROM ta JOIN r JOIN f ON (f.saPropertyID = ta.saPropertyID and ta.srUniqueID = r.srUniqueID) ORDER BY f.row,r.row")
	# print len(check2.fetchall())#384446

	# #Below is unique case for each property where we used GROUP BY METHOD 
	# #one way checking
	# selection1=cur.execute("SELECT f.row, r.row FROM f JOIN r ON (f.saPropertyID = r.saPropertyID ) WHERE r.saPropertyID!=0 GROUP BY f.saPropertyID ORDER BY f.row,r.row")
	# print len(check1.fetchall())#251755

	# ###My assumption is that check 21 and check 22 are same.
	# two way checking with ta table
	# selection21=cur.execute("SELECT f.row, r.row FROM f JOIN r JOIN ta ON (f.saPropertyID = r.saPropertyID and ta.srUniqueID = r.srUniqueID) WHERE r.saPropertyID!=0 GROUP BY f.saPropertyID ORDER BY f.row,r.row")
	# print len(selection21.fetchall())#228464
	# # #two way checking with ta table
	# # selection22=cur.execute("SELECT f.row,r.row FROM f JOIN r JOIN ta ON (f.saPropertyID = ta.saPropertyID and ta.srUniqueID = r.srUniqueID) WHERE ta.saPropertyID!=0 and ta.srUniqueID!=0 GROUP BY f.saPropertyID ORDER BY f.row,r.row")
	# # print len(selection22.fetchall())#228461

	# check1=cur.execute("SELECT f.row,r.row FROM f JOIN r JOIN ta ON (f.saPropertyID = r.saPropertyID and ta.srUniqueID = r.srUniqueID) WHERE r.saPropertyID!=0 ORDER BY f.row,r.row")
	# print len(check1.fetchall())#384455
	# 							 228464




#####################################################################################################
################  Making 2 csv files for forclosure and recorder using selection21   ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# #Using selection21
# with sqlite.connect(r'db_saPropertyID_srUniqueID.db') as con: 
# 	cur = con.cursor()
# 	selection21=cur.execute("SELECT f.row, r.row FROM f JOIN r JOIN ta ON (f.saPropertyID = r.saPropertyID and ta.srUniqueID = r.srUniqueID) WHERE r.saPropertyID!=0 GROUP BY f.saPropertyID ORDER BY f.row,r.row")
# 	selection21Inds = zip(*selection21.fetchall())
# with open('UMichForeclosure_Total.csv','r') as fc:
# 	fc=fc.readlines()
# 	with open('selection21Foreclosure.csv','w') as wo:
# 		wo.write(fc[0])
# 		for i in map(lambda j: fc[j], selection21Inds[0]):
# 			wo.write(i)
# with open('UMichRecorder_Total.csv','r') as fc:
# 	fc=fc.readlines()
# 	with open('selection21Recorder.csv','w') as wo:
# 		wo.write(fc[0])
# 		for i in map(lambda j: fc[j], selection21Inds[1]):
# 			wo.write(i)



#####################################################################################################
################        Making csv file for foreclosure properties address           ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# with open('selection21Foreclosure.csv','r') as fc1:
# 	fc1=fc1.readlines()[1:]
# with open('selection21Recorder.csv','r') as fc2:
# 	fc2=fc2.readlines()[1:]
# with open('selection21ForeclosureAddress.csv','w') as wo:
# 	wo.write('SA_PROPERTY_ID,SR_SITE_ADDR_RAW,FT_SITE_CITY,FT_SITE_STATE,FT_SITE_ZIP\n')
# 	for i in range(len(fc1)):
# 		k=fc1[i].split(',')
# 		a=[k[0]]
# 		b=[fc2[i].split(',')[9]]
# 		c=map(lambda j: k[j], [55,56,57])
# 		wo.write(",".join(a+b+c)+'\n')


############################################################################################################
#########################     Week 5     ###################################################################
############################################################################################################

####################################################################################################
################              Spliting Fourclosure Address data set by Zipcode               ################
# ##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# with open('selection21ForeclosureAddress.csv','r') as kw:
# 	kw=kw.readlines()

# listOfAddresses=[i[0] for i in [map(lambda j: i.split(',')[j] if len(i.split(',')[j])!=0 else '', [1]) for i in kw]]
# listOfEmptyAddressIndex=[i for i in range(len(listOfAddresses)) if len(listOfAddresses[i])==0]
# for i in listOfEmptyAddressIndex[::-1]: #reverse the order so that we can safely delete all elements (order matters)
# 	del kw[i]
# kw_data=sorted(kw[1:], key=lambda x : (x.split(',')[4],x.split(',')[2]))
# listOfZipcode=[i[0].replace('\n','') for i in [map(lambda j: i.split(',')[j] if len(i.split(',')[j])!=0 else '', [4]) for i in kw_data]]

# dict_Zip_Index={}
# for i in range(len(listOfZipcode)-1):
# 	i+=1
# 	if listOfZipcode[i] not in dict_Zip_Index:
# 		dict_Zip_Index[listOfZipcode[i]]=[i]
# 	else:
# 		dict_Zip_Index[listOfZipcode[i]]+=[i]

# dict_Zip3_Zip5={}
# for i in dict_Zip_Index:
# 	if i[:3] not in dict_Zip3_Zip5:
# 		dict_Zip3_Zip5[i[:3]]=[i]
# 	else:
# 		dict_Zip3_Zip5[i[:3]]+=[i]
# for i in dict_Zip3_Zip5:
# 	dict_Zip3_Zip5[i]=sorted(dict_Zip3_Zip5[i], key=lambda x : x)

# dict_Zip_Data={}
# for i in dict_Zip_Index:
# 	dict_Zip_Data[i]=[]
# 	for j in dict_Zip_Index[i]:
# 		dict_Zip_Data[i]+=[kw_data[j]]
# for i in dict_Zip_Data:
# 	dict_Zip_Data[i]=sorted(dict_Zip_Data[i], key=lambda x : (x.split(',')[4],x.split(',')[2]))

# for k in dict_Zip3_Zip5:
# 	names='ForeclosureAddress_'+k+'.csv'
# 	with open(names,'w') as zk:
# 		zk.write(kw[0])
# 		for i in dict_Zip3_Zip5[k]:
# 			for j in dict_Zip_Data[i]:
# 				zk.write(j)



