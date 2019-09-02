import unittest
from ftplib import FTP


ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()
list_files_names = list(filter(lambda name: name[-4:]== '.zip', ftp.nlst()))
start_path = '.'
list_of_size = []

for file in list_files_names:
    list_of_size.append(ftp.size(file))


class Size_of_files_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = sorted(list_of_size)
        expected_result = sorted([
            1073741824000,
            107374182400,
            102400,
            104857600,
            10737418240,
            10485760,
            1073741824,
            1024,
            1048576,
            209715200,
            20971520,
            2097152,
            3145728,
            524288000,
            53687091200,
            52428800,
            524288,
            5242880])

        self.assertEqual(actual_result, expected_result,'file size matches')

if __name__ == '__main__':
    unittest.main()

ftp.quit()