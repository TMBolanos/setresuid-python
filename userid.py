import os, pwd, grp
from pwd import getpwnam as idnum
from grp import getgrnam as giddnum

user=pwd.getpwuid( os.getuid() ).pw_name
setting=os.setresuid(33,33,33)

print ("Id number is: " + str(idnum('mario').pw_uid))
print("User is: " + user)
print setting

