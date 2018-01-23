
from unittest import TestCase
from unique_file_identifier import *

class Test_minimal_identifying_path(TestCase):

	def test_directory_identifier_null(self):
		path = 'arst/qwfp'
		paths = []
		result = minimal_identifying_path(path, paths)
		self.assertEqual(result, [])

	def test_directory_identifier_with_namesake(self):
		path = 'arst/qwfp'
		paths = ['arst/arst/qwfp']
		result = minimal_identifying_path(path, paths)
		self.assertEqual(result, ['arst'])

class Test_minimal_identifying_path_from_lists(TestCase):

	def test_minimal_identifying_path_only_file(self):
		path = ['arst', 'qwfp', 'name']
		paths = []
		result = minimal_identifying_path_from_lists(path, paths)
		self.assertEqual(result, [])

	def test_minimal_identifying_path_with_unrelated_files(self):
		path = ['arst', 'qwfp', 'name']
		paths = [['arst', 'qwfp', 'file2'], ['arst', 'yul', 'zxcv']]
		result = minimal_identifying_path_from_lists(path, paths)
		self.assertEqual(result, [])

	def test_minimal_identifying_path_namesake_at_same_level(self):
		path = ['arst', 'qwfp', 'name']
		paths = [['arst', 'zxcv', 'name']]
		result = minimal_identifying_path_from_lists(path, paths)
		self.assertEqual(result, ['qwfp'])

	def test_minimal_identifying_path_namesake_inside_duplicate_folders(self):
		path = ['arst', 'qwfp', 'name']
		paths = [['arst', 'qwfp', 'qwfp', 'name']]
		result = minimal_identifying_path_from_lists(path, paths)
		self.assertEqual(result, ['qwfp'])

	def test_minimal_identifying_path_file_inside_duplicate_folders(self):
		path = ['arst', 'qwfp', 'qwfp', 'name']
		paths = [['arst', 'qwfp', 'name']]
		result = minimal_identifying_path_from_lists(path, paths)
		self.assertEqual(result, ['qwfp', 'qwfp'])

	def test_minimal_identifying_path_file_deep_inside_duplicate_folders(self):
		path = ['arst', 'qwfp', 'qwfp', 'qwfp', 'name']
		paths = [['arst', 'qwfp', 'name']]
		result = minimal_identifying_path_from_lists(path, paths)
		self.assertEqual(result, ['qwfp', 'qwfp', 'qwfp'])

	def test_minimal_identifying_path_file_deep_inside(self):
		path = ['arst', 'qwfp', 'arst', 'yul', 'name']
		paths = [['arst', 'qwfp', 'name']]
		result = minimal_identifying_path_from_lists(path, paths)
		self.assertEqual(result, ['qwfp', 'arst', 'yul'])

	def test_minimal_identifying_path_namesakes_deep(self):
		path = ['arst', 'qwfp', 'name']
		paths = [['arst', 'qwfp', 'arst', 'yul', 'name'], ['brst', 'qwfp', 'riste', 'name']]
		result = minimal_identifying_path_from_lists(path, paths)
		self.assertEqual(result, ['arst', 'qwfp'])



