from ftplib import FTP_TLS
from datetime import datetime

start = datetime.now()
ftp = FTP_TLS('ecurep.mainz.de.ibm.com')
ftp.login('caomzh@cn.ibm.com','7ujm*IK<')

# Get All Files
files = ftp.nlst()

# Print out the files
for file in files:
	print("Downloading..." + file)
	# ftp.retrbinary("RETR " + file ,open("download/to/your/directory/" + file, 'wb').write)

ftp.close()

end = datetime.now()
diff = end - start
print('All files downloaded for ' + str(diff.seconds) + 's')