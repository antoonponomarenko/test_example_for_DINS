from ftplib import FTP
import os.path
ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()
print(status_connection)
path = '.'
#num_files= len( [ f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) ] )
print(os.listdir(ftp))
print(num_files)

