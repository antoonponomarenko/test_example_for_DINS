import unittest
from ftplib import FTP


ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()
list_files_names = list(filter(lambda name: name[-4:]== '.zip', ftp.nlst()))



class Coonection_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = sorted(list_files_names)
        expected_result = sorted([
    '1000GB.zip',
    '100GB.zip',
    '100KB.zip',
    '100MB.zip',
    '10GB.zip',
    '10MB.zip',
    '1GB.zip',
    '1KB.zip',
    '1MB.zip',
    '200MB.zip',
    '20MB.zip',
    '2MB.zip',
    '3MB.zip',
    '500MB.zip',
    '50GB.zip',
    '50MB.zip',
    '512KB.zip',
    '5MB.zip'
])
        self.assertEqual(actual_result, expected_result, 'step 1')

if __name__ == '__main__':
    unittest.main()

ftp.quit()









