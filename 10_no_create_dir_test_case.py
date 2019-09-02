import unittest
from ftplib import FTP

name_of_test_dir = 'upload'

ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()
list_dir_names = list(filter(lambda name: name[-4:]!= '.zip', ftp.nlst()))
result = False
try:
    if name_of_test_dir in list_dir_names:
        ftp.delete(name_of_test_dir)
except:
    result = True

list_dir_names = list(filter(lambda name: name[-4:]== '.zip', ftp.nlst()))

if name_of_test_dir in list_dir_names:
    result = False


class Deleted_dir_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = result
        expected_result = True

        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()

ftp.quit()









