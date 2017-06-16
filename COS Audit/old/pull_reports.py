#! Python3
import active_directory
computers = active_directory.AD_object ("LDAP://OU=sci,OU=acad,OU=emp,DC=ad,DC=weber,DC=edu")
for computer in computers.search (objectCategory='Computer'):
    print(computer)