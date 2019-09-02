import unittest
from ftplib import FTP


ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()
list_dir_names = list(filter(lambda name: name[-4:]!= '.zip', ftp.nlst()))

class Coonection_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = sorted(list_dir_names)
        expected_result = sorted(['upload'])
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()

ftp.quit()
