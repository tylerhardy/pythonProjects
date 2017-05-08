#! python3
"""
Generate ahk password files for dis and hub, and append with current semester passwords.
"""
import os, sys

root_dir = "\\\\jarvis\\scripts$\\TERM_Passwords"
base_dir = "\\\\jarvis\\scripts$\\TERM_Passwords\\AHK"
working_dir = "\\\\jarvis\\scripts$\\TERM_Passwords\\AHK\\{0}_{1}".format(sys.argv[1], sys.argv[2])

# Parse Inputs
if len(sys.argv) == 4:
    if sys.argv[3][-4::] == '.csv':
        # Create Folder in netwokr share
        print("Starting directory [{0}]".format(os.getcwd()))
        print("Checking if [{0}] exists...".format(base_dir))
        if os.path.exists(base_dir) == False:
            print("...It does not exist, creating directory [\\AHK]")
            os.makedirs(base_dir)
            print("...Changing directory to [{0}]".format(base_dir))
            os.chdir(base_dir)
        else:
            print("[{0}] exists!".format(base_dir))
            print("...Changing directory to [{0}]".format(base_dir))
            os.chdir(base_dir)
        print("Checking if [{0}] exists...".format(working_dir))
        if os.path.exists(working_dir) == False:
            print("...It does not exist, creating directory [\\{0}_{1}]".format(sys.argv[1], sys.argv[2]))
            os.makedirs(working_dir)
            print("...Changing directory to [{0}]".format(working_dir))
            os.chdir(working_dir)
        else:
            print("[{0}] exists!".format(working_dir))
            print("...Changing directory to {0}".format(working_dir))
            os.chdir(working_dir)
        print("Working directory [{0}]".format(os.getcwd()))
        # Input csv file for passwords
        semester_passwords = {}
        if os.path.isfile("{0}\\{1}".format(root_dir, sys.argv[3])):
            print("The file [{0}] exists".format(sys.argv[3]))
        else:
            print("The file [{0}] doesn't exists".format(sys.argv[3]))
        password_file = open("{0}\\{1}".format(root_dir, sys.argv[3]))
        password_list = password_file.read().strip().split('\n')
        for i in password_list:
            print(i)
            k, v = i.split('-,')
            semester_passwords[k]=v
        # Create 16 files for disabilities
        print("Creating Disability's password files")
        for dis_Num in range(16):
            dis_File = open("dis_pass_{0}_{1}_{2}.ahk".format(sys.argv[1], sys.argv[2], dis_Num+1), 'w')
            # Append each file with corisponding week password
            dis_ahk = open("{0}\\dis_ahk.txt".format(root_dir))
            dis_ahk_content = dis_ahk.read()
            dis_ahk_content = dis_ahk_content.replace('Password1', semester_passwords['Week 1'])
            dis_ahk_content = dis_ahk_content.replace('PasswordWeek', semester_passwords['Week {0}'.format(dis_Num+1)])
            dis_File.write(dis_ahk_content)
            dis_File.close()
        # Create 16 files for dev math hub
        print("Creating Hub's password files")
        for hub_Num in range(16):
            hub_File = open("pass_{0}_{1}_{2}.ahk".format(sys.argv[1], sys.argv[2], hub_Num+1), 'w')
            # Append each file with corisponding week password
            hub_ahk = open("{0}\\hub_ahk.txt".format(root_dir))
            hub_ahk_content = hub_ahk.read()
            hub_ahk_content = hub_ahk_content.replace('Password1', semester_passwords['Week 1'])
            hub_ahk_content = hub_ahk_content.replace('PasswordWeek', semester_passwords['Week {0}'.format(hub_Num+1)])
            hub_File.write(hub_ahk_content)
            hub_File.close()
    else:
        print("Last arg must be a CSV file")
else:
    print("Incorrect number of arguments passed")
