import unittest
from ftplib import FTP


ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()
count_files = len(list(filter(lambda name: name[-4:]== '.zip', ftp.nlst())))


class Count_files_case(unittest.TestCase):
    def test_connection(self):
        actual_result = count_files
        expected_result = 18
        self.assertEqual(actual_result, expected_result, 'step 1')

if __name__ == '__main__':
    unittest.main()

ftp.quit()


