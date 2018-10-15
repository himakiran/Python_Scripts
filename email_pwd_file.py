#!/usr/bin/python3

# This file takes a email-pass file the kind found in pastebin regularly 
# and scrapes it to either find an email of interest/ check which are the most
# used passwords.

# The input file should be of the format email:password . The linux cmd 
# tail -n +10 pw.txt > pw1.txt can remove top 10 lines of pw.txt
import collections as cols
fdesc=open("email_pass.txt","r")
email_pwd_dict={}
passwds=[]
for each in fdesc:
	email_pwd=each.split(":")
	try:
		email=email_pwd[0]
		pwd=email_pwd[1]
		#remove newline char from pwd
		pwd=pwd[:len(pwd)-1]
		email_pwd_dict[email]=pwd
		passwds.append(pwd)
	except Exception as e:
		print(e)
passwd_counter = cols.Counter(passwds)
for each in passwd_counter.most_common(10):
	print(each)
print("Total No of passwords is ",len(passwds))
fdesc.close()