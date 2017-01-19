import re

########################################################################
########################################################################
#####################   Global Functions   #############################
########################################################################
########################################################################

def adjustObj(ss):
	#Object = each row
	#if there is space in a given column(field), we want to replace it without space 
	#so that we can parse it with spaces later
    #this function does removing Multiple Spaces And replace any comma with a space 
    #because we will be make CSV file at the end.
    r = re.split(r'\s{2,}',ss)
    if r[0]=='':
        del r[0]
    if r[-1]=='':
    	del r[-1]
    return [i.replace(',',' ') for i in r]


########################################################################
########################################################################
#####################      Forclosure Only      ########################
########################################################################
########################################################################
def adjustForeclosureObj(ss):
	#if there is space in a given column(field), we want to replace it without space so that we can parse it with spaces later
    #this function does removing Multiple Spaces And Commas and seperates. . .
    r = re.split(r'\s{2,}',ss)
    #re.split(r'\s{2,}',ss) this function sometimes can have '' at the begining or end 
    #so we want to delete it 
    if r[0]=='':
        del r[0]
    if r[-1]=='':
    	del r[-1]
    #From the initial data set, I figured 
    if re.search(r'[0-9.]+ [a-zA-z]+',r[8]):
        firstName=re.search(r'[a-zA-z]+',r[8]).group()
        inds=len(firstName)+1
        r[8]=r[8][:-6]
        r=r[:9]+[firstName]+r[9:]

    return [i.replace(',',' ') for i in r]

def foreclosureStandardizeObj(objList):
	#Basically I eyeballed and checked differences betweeen 15 columns to 16 columns
	#Then, I was able to 
	#each object has different number of fields so we need to equalize the number of fields
	a = objList
	if len(a)==22:
		a=a[:17]+['','']+a[17:]#**24
		a=a[:19]+['']+a[19:]#25
		a=a[:20]+['','']+a[20:]#**27
	elif len(a)==25:
		a=a[:12]+['']+a[12:]#26
		a=a+['']#27
	elif len(a)==15:
		a=a+['']#16
		a=a[:9]+['']+a[9:]#17
		a=a[:13]+['']+a[13:]#18
		a=a[:8]+['']+a[8:]#19
		a=a[:11]+['']+a[11:]#20
		a=a[:12]+['']+a[12:]#21
		a=a[:17]+['','']+a[17:]#**23
		a=a[:19]+['']+a[19:]#24
		a=a[:20]+['','']+a[20:]#26
		a=a+['']#27
	elif len(a)==16:
		a=a[:9]+['']+a[9:]#17
		a=a[:13]+['']+a[13:]#18
		a=a[:8]+['']+a[8:]#19
		a=a[:11]+['']+a[11:]#20
		a=a[:12]+['']+a[12:]#21
		a=a[:17]+['','']+a[17:]#**23
		a=a[:19]+['']+a[19:]#24
		a=a[:20]+['','']+a[20:]#26
		a=a+['']#27
	elif len(a)==17:
		a=a[:13]+['']+a[13:]#18
		a=a[:8]+['']+a[8:]#19
		a=a[:11]+['']+a[11:]#20
		a=a[:12]+['']+a[12:]#21
		a=a[:17]+['','']+a[17:]#**23
		a=a[:19]+['']+a[19:]#24
		a=a[:20]+['','']+a[20:]#26
		a=a+['']#27
	elif len(a)==18:
		a=a[:8]+['']+a[8:]#19
		a=a[:11]+['']+a[11:]#20
		a=a[:12]+['']+a[12:]#21
		a=a[:17]+['','']+a[17:]#**23
		a=a[:19]+['']+a[19:]#24
		a=a[:20]+['','']+a[20:]#26
		a=a+['']#27
	elif len(a)==19:
		a=a[:11]+['']+a[11:]#20
		a=a[:12]+['']+a[12:]#21
		a=a[:17]+['','']+a[17:]#**23
		a=a[:19]+['']+a[19:]#24
		a=a[:20]+['','']+a[20:]#26
		a=a+['']#27
	elif len(a)==20:
		a=a[:12]+['']+a[12:]#21
		a=a[:17]+['','']+a[17:]#**23
		a=a[:19]+['']+a[19:]#24
		a=a[:20]+['','']+a[20:]#26
		a=a+['']#27
	elif len(a)==21:
		a=a[:17]+['','']+a[17:]#**23
		a=a[:19]+['']+a[19:]#24
		a=a[:20]+['','']+a[20:]#26
		a=a+['']#27
	elif len(a)==23:
		a=a[:19]+['']+a[19:]#24
		a=a[:20]+['','']+a[20:]#26
		a=a+['']#27
	elif len(a)==24:
		a=a[:20]+['','']+a[20:]#26
		a=a+['']#27
	elif len(a)==26:
	    a=a+['']
	return a
 


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
