#!/usr/bin/env python
import unittest
import clnzr

class TestClnzr(unittest.TestCase):

    def setUp(self):
        self.test_file = clnzr.retrieve_file('test.txt')

    def test_retrieve_file(self):
        self.assertIsNotNone(self.test_file)

    def test_getlines(self):
        self.test_list = clnzr.get_lines(self.test_file)
        self.assertIsNotNone(self.test_list)
        
    def tearDown(self):
        self.test_file.close()

if __name__ == "__main__":
    unittest.main()