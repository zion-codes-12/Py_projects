# GLORY TO GOD
# Project2: Parsing System Log and Analysis

# Project description: This project focuses on getting a system log file
# parsing its info Line by line 
# Getting a statistical Report using appropriate data structures 
# On the basis of users and errors 
# storing them in CSV files.


# Input is a system log file and output is a CSV file


# done by Chris Zionna A

import re
import csv
import operator

err={}
per_user={}

with open("syslog.log") as file:
    for i in file.readlines():
        istrip=i.strip()

        result=re.search(r"ubuntu\.local ticky: (ERROR|INFO) ([\[\'\w\[\#0-9\s\]]*) [(]([\w]*)[)]$",istrip)
        if result!=None:
            a=result.group(1)
            b=result.group(2)
            c=result.group(3)
            if c not in per_user.keys():
                per_user[c]={}
                per_user[c]["Username"]=c
                per_user[c]["INFO"]=0
                per_user[c]["ERROR"]=0
            if  a=="ERROR":
                err[b]=err.get(b,0)+1
                per_user[c]["ERROR"]+=1
            if  a=="INFO":
                per_user[c]["INFO"]+=1

err = dict(sorted(err.items(), key = operator.itemgetter(1), reverse = True))
per_user=dict(sorted(per_user.items()))

print(err)
print("\n\n\n")

print(per_user)
print("\n\n\n")

x=per_user.values()

field_names=["Username","INFO","ERROR"]
with open('user_statistics.csv',"w",newline='') as p_u:
    reader=csv.DictWriter(p_u,fieldnames=field_names)
    reader.writeheader()
    reader.writerows(x)
with open('user_statistics.csv',"r") as e:
    x=e.readlines()
    print(x)
    print("\n\n\n")
with open('error_message.csv',"w",newline='') as er:
    writer = csv.writer(er, delimiter = ",")
    writer.writerow(["Error","Count"])
    for key in err.keys():
        writer.writerow([key,err[key]])
with open('error_message.csv',"r") as e:
    Y=e.readlines()
    print(Y)

