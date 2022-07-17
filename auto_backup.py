"""
This is a simple script that will copy files located in a source directory ("src") to a destination directory ("dst").  Instructions on how to run the script regulary using Windows Task Scheduler can be found at <https://datatofish.com/python-script-windows-scheduler/>
"""

import shutil
import datetime as dt

current_datetime = dt.datetime.now() 
filename_datetime = current_datetime.strftime("%b%d%Y_%H.%M.%S")
src = 'C:/source_file_location'
dst = 'Z:/Backup Files/backup_files_{}'.format(filename_datetime) #date and time are added to avoid duplicate file names
shutil.copytree(src=src,dst=dst)