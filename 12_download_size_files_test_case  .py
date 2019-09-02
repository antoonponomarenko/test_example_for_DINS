import unittest
from ftplib import FTP
import os

test_file_name = '2MB.zip'
expect_result = 2097152
dir_for_download = '.'

ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()

local_file_name = os.path.join(dir_for_download, test_file_name)
lf = open(local_file_name, "wb")
ftp.retrbinary("RETR " + test_file_name, lf.write, 8*1024)
lf.close()

size_download_file = os.stat(test_file_name).st_size


class Download_file_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = size_download_file
        expected_result = expect_result
        self.assertEqual(actual_result, expected_result, )

if __name__ == '__main__':
    unittest.main()

ftp.quit()
