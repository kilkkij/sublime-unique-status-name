
import os
from unittest import TestCase
import unique_file_identifier

# class Test_in_same_branch(TestCase):
# 	def test_is_in_same_branch(self):
# 		self.assertEqual(0, 1)
# 	def test_not_in_same_branch(self):
# 		self.assertNotEqual(0, 0)

class Test_split_path(TestCase):
    def test_split_path(self):
    	sep = os.sep
    	folders = ['abc', 'dfg']
    	path = sep.join(folders)
    	split_string = unique_file_identifier.split_path(path)
    	self.assertEqual(split_string, folders)


