from django.test import TestCase

class UploadTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)
        
        #Test: pdf-size < 10Mb; file is type PDF
