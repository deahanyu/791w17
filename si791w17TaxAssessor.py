import re
import myfunc

############################################################################################################
#########################     Week 1     ###################################################################
############################################################################################################
##---------------Please comment out below if you want to run this week's code.---------------##

# with open('University_of_Michigan_TaxAssessor_001.txt','r') as ta1:
# 	c=0
# 	dd={}
# 	for i in ta1.readlines():
# 		if len(myfunc.adjustObj(i)) not in dd:
# 			dd[len(myfunc.adjustObj(i))]=c
# 		c+=1
# 	print dd
# with open('University_of_Michigan_TaxAssessor_002.txt','r') as ta2:
# 	c=0
# 	dd={}
# 	for i in ta2.readlines():
# 		if len(myfunc.adjustObj(i)) not in dd:
# 			dd[len(myfunc.adjustObj(i))]=c
# 		c+=1
# 	print dd



############################################################################################################
#########################     Week 2     ###################################################################
############################################################################################################

#####################################################################################################
################               Saving an original version as CSV file                ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# #Getting each column's information from REALTYTRAC DLP 3.0 Assessor NO Geo Layout.xlsx
# eachColumnSpace = myfunc.columnInformation('REALTYTRAC DLP 3.0 Assessor NO Geo Layout.csv')

# myfunc.forRecorderOrTaxAssessorCSV('University_of_Michigan_TaxAssessor_001.txt',['TaxAssessor1a','TaxAssessor1b','TaxAssessor1c'],eachColumnSpace)
# myfunc.forRecorderOrTaxAssessorCSV('University_of_Michigan_TaxAssessor_002.txt',['TaxAssessor2a','TaxAssessor2b','TaxAssessor2c'],eachColumnSpace)

#####################################################################################################
#####################################################################################################

#####################################################################################################
################            Checking if data has right number of records             ################
##---------------DO NOT COMMENT OUT THIS CODE BELOW UNLESS YOU WANT TO RUN IT AGAIN ---------------##

# for i in ['TaxAssessor1a','TaxAssessor1b','TaxAssessor1c','TaxAssessor2a','TaxAssessor2b','TaxAssessor2c']:
# 	if i =='TaxAssessor1a':
# 		subs = myfunc.checkingRecords(i,col=6,dd={})
# 	else:
# 		final = myfunc.checkingRecords(i,col=6,dd=subs)
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

#####################################################################################################
#####################################################################################################

