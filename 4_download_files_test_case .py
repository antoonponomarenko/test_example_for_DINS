import unittest
from ftplib import FTP


ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()
list_files_names = list(filter(lambda name: name[-4:]== '.zip', ftp.nlst()))


'''
class Coonection_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = sorted(list_files_names)
        expected_result = sorted([
    
])
        self.assertEqual(actual_result, expected_result, 'step 1')

if __name__ == '__main__':
    unittest.main()

ftp.quit()

'''







