import re
import myfunc

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
# eachColumnSpace = myfunc.columnInformation('REALTYTRAC DLP 3.0 Foreclosure Layout.csv')

# myfunc.onlyForeclosureCSV('University_of_Michigan_Foreclosure_001.txt','UMichForeclosure.csv',eachColumnSpace)

#####################################################################################################
#####################################################################################################

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

#####################################################################################################
#####################################################################################################

