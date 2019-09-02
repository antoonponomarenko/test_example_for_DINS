import unittest
import ftplib

name_of_test_file = 'README.md'




ftp = ftplib.FTP('speedtest.tele2.net')
status_connection = ftp.login()
list_files_names = list(filter(lambda name: name[-4:] == '.zip', ftp.nlst()))
if name_of_test_file not in list_files_names:

    result = False

    if name_of_test_file not in list_files_names:
        dir_for_download = './'
        ftp = ftplib.FTP('speedtest.tele2.net')
        status_connection = ftp.login()
        result = False
        try:
            file_to_upload = open(name_of_test_file, 'rb')
            ftp.storbinary('STOR ' + name_of_test_file, file_to_upload)
        except:
            result = True

    if name_of_test_file in list_files_names:
        result = False


    list_files_names = list(filter(lambda name: name[-4:]== '.zip', ftp.nlst()))
    if name_of_test_file in list_files_names:
        result = False
    else:
        result = True

class Deleted_files_test_case(unittest.TestCase):
    def test_connection(self):
        actual_result = result
        expected_result = True
        self.assertEqual(actual_result, expected_result, )

if __name__ == '__main__':
    unittest.main()

ftp.quit()