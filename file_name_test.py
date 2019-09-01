from unittest import TestCase

from FTP_connection_test_case import FTP_connection_test_case


class File_name_test_case(FTP_connection_test_case):

    def get_list_files(self):
        list_files = self._connection.nlst()
        return list(filter(lambda name: name[-4 : ] == '.zip', list_files))

    def test_connection(self):
        actual_result = sorted(self.get_list_files())
        expected_result = sorted([
                            '100GB.zip',
                            '1000GB.zip',
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
        self.assertSequenceEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()


