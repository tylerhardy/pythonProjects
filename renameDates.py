#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY format.

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)(-|_|\.)?
    ((0|1)?\d)(-|_|\.)
    ((0|1|2|3)?\d)(-|_|\.)
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

# (.*?)((0|1)?\d)(-|_|\.)((0|1|2|3)?\d)(-|_|\.)((19|20)\d\d)(.*?)$

# TODO: Loop over the files in the working directory.
for oldFilename in os.listdir('.'):
    # print(oldFilename)
    mo = datePattern.search(oldFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    # print(mo.group())
    
    beforepart = mo.group(1)
    monthpart = mo.group(3)
    daypart = mo.group(6)
    yearpart = mo.group(9)
    afterpart = mo.group(11)

    if beforepart == None:
        beforepart = ''
    if afterpart == None:
        afterpart = ''

    # Form the European-style filename.
    if beforepart == '':
        newFilename = yearpart+'_'+monthpart+'_'+daypart+beforepart+afterpart
    else:
        newFilename = yearpart+'_'+monthpart+'_'+daypart+'_'+beforepart+afterpart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    oldFilename = os.path.join(absWorkingDir, oldFilename)
    newFilename = os.path.join(absWorkingDir, newFilename)

    # Rename the files.
    print('renaming "%s" to "%s"...' %(oldFilename, newFilename))
    # shutil.move(oldFilename, newFilename)

