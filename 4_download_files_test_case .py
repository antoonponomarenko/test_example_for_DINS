import unittest
from ftplib import FTP
import os

test_file_name = '2MB.zip'
dir_for_download = './'

ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()

local_file_name = os.path.join(dir_for_download, test_file_name)
lf = open(local_file_name, "wb")
ftp.retrbinary("RETR " + test_file_name, lf.write, 8*1024)
lf.close()
result = os.path.exists(test_file_name)
file = open(test_file_name)
file.close()

class Download_file_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = result
        expected_result = True
        self.assertEqual(actual_result, expected_result, )

if __name__ == '__main__':
    unittest.main()

ftp.quit()









