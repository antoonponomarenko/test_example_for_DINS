import unittest
from ftplib import FTP

name_of_test_file = '1GB.zip'

ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()
list_files_names = list(filter(lambda name: name[-4:]== '.zip', ftp.nlst()))
result = False
try:
    if name_of_test_file in list_files_names:
        ftp.delete(name_of_test_file)
except:
    result = True

list_files_names = list(filter(lambda name: name[-4:]== '.zip', ftp.nlst()))

if name_of_test_file not in list_files_names:
    result = False


class Deleted_files_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = result
        expected_result = True

        self.assertEqual(actual_result, expected_result, 'step 1')

if __name__ == '__main__':
    unittest.main()

ftp.quit()









