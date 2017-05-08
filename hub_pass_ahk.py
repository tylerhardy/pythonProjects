#! python3
"""
Generate ahk password files for dis and hub, and append with current semester passwords.
"""
import os, sys


try:
    # Validate inputs
    if len(sys.argv) != 4:
        raise Exception('Incorrect number of arguments passed.')
    sys.argv[1] = sys.argv[1].lower()
    if sys.argv[1].isalpha() == False or sys.argv[1] not in ['fall', 'spring', 'summer']:
        raise Exception('First argument must be name of semester (fall, spring, summer).')
    if (sys.argv[2].isdecimal() == False) or (len(sys.argv[2]) != 4):
        raise Exception('Second argument must be name of year (2017, 2018, etc...).')
    if sys.argv[3][-4::] != '.csv':
        raise Exception('Last argument must be a valid CSV file.')

    # Directory variables
    root_dir = "\\\\jarvis\\scripts$\\TERM_Passwords"
    base_dir = "\\\\jarvis\\scripts$\\TERM_Passwords\\AHK"
    working_dir = "\\\\jarvis\\scripts$\\TERM_Passwords\\AHK\\{0}_{1}".format(sys.argv[1], sys.argv[2])

    # Check if base_dir exists, creates if not.
    if os.path.exists(base_dir) == False:
        print("Creating [{0}] directory.".format(base_dir))
        os.makedirs(base_dir)
        os.chdir(base_dir)
    else:
        os.chdir(base_dir)

    # Check if working_dir exists, creates if not.
    if os.path.exists(working_dir) == False:
        print("Creating [{0}] directory.".format(working_dir))
        os.makedirs(working_dir)
        os.chdir(working_dir)
    else:
        os.chdir(working_dir)
    
    # Input csv file for passwords
    if os.path.isfile("{0}\\{1}".format(root_dir, sys.argv[3])) == False:
        raise Exception("The password does not exists in the [{0}] directory.".format(root_dir))
    password_file = open("{0}\\{1}".format(root_dir, sys.argv[3]))
    password_list = password_file.read().strip().split('\n')
    semester_passwords = {}
    print()
    for i in password_list:
        k, v = i.split('-,')
        semester_passwords[k]=v

    # Create 16 files for disabilities
    print("Creating Disability's password files.")
    dis_count = 0
    for dis_Num in range(len(password_list)):
        dis_File = open("dis_pass_{0}_{1}_{2}.ahk".format(sys.argv[1], sys.argv[2], dis_Num+1), 'w')

        # Append each file with corisponding week password
        dis_ahk = open("{0}\\dis_ahk.txt".format(root_dir))
        dis_ahk_content = dis_ahk.read()
        dis_ahk_content = dis_ahk_content.replace('Password1', semester_passwords['Week 1']).replace('PasswordWeek', semester_passwords['Week {0}'.format(dis_Num+1)])
        dis_File.write(dis_ahk_content)
        dis_File.close()
        dis_count += 1
    print("Done. {0} Disability password files generated.".format(str(dis_count)))

    # Create 16 files for dev math hub
    print("Creating Hub's password files.")
    hub_count = 0
    for hub_Num in range(len(password_list)):
        hub_File = open("pass_{0}_{1}_{2}.ahk".format(sys.argv[1], sys.argv[2], hub_Num+1), 'w')

        # Append each file with corisponding week password
        hub_ahk = open("{0}\\hub_ahk.txt".format(root_dir))
        hub_ahk_content = hub_ahk.read()
        hub_ahk_content = hub_ahk_content.replace('Password1', semester_passwords['Week 1']).replace('PasswordWeek', semester_passwords['Week {0}'.format(hub_Num+1)])
        hub_File.write(hub_ahk_content)
        hub_File.close()
        hub_count += 1
    print("Done. {0} Hub password files generated.".format(str(hub_count)))

    print("Script completed!")

except Exception as err:
    print('An exception occured: {0}'.format(str(err)))