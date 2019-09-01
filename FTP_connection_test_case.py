from ftplib import FTP
from unittest import TestCase

FTP_ADDRESS = 'speedtest.tele2.net'

class FTP_connection_test_case(TestCase):
    @classmethod
    def setUpClass(self):
        self._connection = FTP(FTP_ADDRESS)
        self._connection_status = self._connection.login()[0:3]

    @classmethod
    def tearDownClass(self):
        self._connection.quit()
