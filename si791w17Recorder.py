import re
import myfunc
import sqlite3 as sqlite

############################################################################################################
#########################     Week 1     ###################################################################
############################################################################################################
##---------------Please comment out below if you want to run this week's code.---------------##

#Already changed the format as 'Recorder1.txt', 'Recorder2.txt', and 'Recorder3.txt'. 









############################################################################################################
#########################     Week 2     ###################################################################
############################################################################################################

#####################################################################################################
################               Saving an original version as CSV file                ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# #Getting each column's information from REALTYTRAC DLP 3.0 Recorder Layout.xlsx
# eachColumn = myfunc.columnInformation('REALTYTRAC DLP 3.0 Recorder Layout.csv',1)

# myfunc.forRecorderOrTaxAssessorCSV('University_of_Michigan_Recorder_001.txt',['Recorder1a','Recorder1b','Recorder1c'],eachColumn)
# myfunc.forRecorderOrTaxAssessorCSV('University_of_Michigan_Recorder_002.txt',['Recorder2a','Recorder2b','Recorder2c'],eachColumn)
# myfunc.forRecorderOrTaxAssessorCSV('University_of_Michigan_Recorder_003.txt',['Recorder3a','Recorder3b','Recorder3c'],eachColumn)

#####################################################################################################
################            Checking if data has right number of records             ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# for i in ['Recorder1a','Recorder1b','Recorder1c','Recorder2a','Recorder2b','Recorder2c','Recorder3a','Recorder3b','Recorder3c']:
# 	if i =='Recorder1a':
# 		subs = myfunc.checkingRecords(i,col=7,dd={})
# 	else:
# 		final = myfunc.checkingRecords(i,col=7,dd=subs)
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










############################################################################################################
#########################     Week 3     ###################################################################
############################################################################################################

#####################################################################################################
################           Txt file for the column information - description         ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# #Getting each column's information from REALTYTRAC DLP 3.0 Recorder Layout.xlsx
# eachColumn = myfunc.columnInformation('REALTYTRAC DLP 3.0 Recorder Layout.csv',1)
# headers = eachColumn[1]#headers
# myfunc.makingTxtfile('REALTYTRAC DLP 3.0 Recorder Layout.csv','RecorderLayout',headers,1)



