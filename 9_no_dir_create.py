import unittest
from ftplib import FTP


test_dir = 'my_test_dir'

ftp = FTP('speedtest.tele2.net')
status_connection = ftp.login()
list_of_dir = list(filter(lambda name: name[-4:] != '.zip', ftp.nlst()))
print(list_of_dir)
result = False
if test_dir not in list_of_dir:

    try:
        ftp.mkd(test_dir)
    except:
        result = True
list_of_dir = list(filter(lambda name: name[-4:] != '.zip', ftp.nlst()))

if test_dir in list_of_dir:
    result = False


class No_create_dir_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = result
        expected_result = True
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()

ftp.quit()