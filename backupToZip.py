#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1
    
    # Create the ZIP file.
    print('Creating %s...' %(zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Wlak the entire folder tree and compress the files in each folder.
    for folderName, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' %(folderName))
        # Add the current folder to the ZIP file
        backupZip.write(folderName)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(folderName, filename))
    backupZip.close()
    print('Done.')

backupToZip('C:\\Users\\tylerhardy\\Developer\\testBackup\\')