import unittest
from ftplib import FTP


ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()


class Coonection_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = status_connection[0:3]
        expected_result = '230'
        self.assertEqual(actual_result, expected_result, 'step 1')

if __name__ == '__main__':
    unittest.main()

ftp.quit()


