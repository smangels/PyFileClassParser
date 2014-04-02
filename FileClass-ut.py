import unittest
import random

from FileClass import FileClass

class TestSequence(unittest.TestCase):

	def setUp(self):
		self.analysis = FileClass('unittest')
		self.analysis.clear()

	def tearDown(self):
		del self.analysis

	def test_emptyWhenConstructed(self):

		self.assertEqual(len(self.analysis.getFiles()), 0)


	def test_addOneElement(self):

		# 'files = ['FileClass.py', 'FileClass-ut.py']'
		self.analysis.insertFile('FileClass.py')

		# expected: existing files are ignored
		self.assertEqual(len(self.analysis.getFiles()), 1)


	def test_doubledItemIgnored(self):

		# 'files = ['FileClass.py', 'FileClass-ut.py']'
		self.analysis.insertFile('FileClass.py')

		# expected: existing files are ignored
		self.assertEqual(len(self.analysis.getFiles()), 1)

		self.analysis.insertFile('FileClass.py')

		self.assertEqual(len(self.analysis.getFiles()), 1)


	def test_NoItemsWhenCleared(self):

		self.analysis.insertFile('FileClass.py')

		# expected: existing files are ignored
		self.assertEqual(len(self.analysis.getFiles()), 1)

		self.analysis.clear()

		self.assertEqual(len(self.analysis.getFiles()), 0)

	def test_AddExtension(self):

		self.assertTrue(self.analysis.addExtension('.cc'))

		self.assertEqual(['.cc'], self.analysis.getExtensions())

		self.assertTrue(self.analysis.addExtension('.cc'))

		self.assertEqual(['.cc'], self.analysis.getExtensions())

		self.assertTrue(self.analysis.addExtension('.C'))

		self.assertEqual(['.cc', '.C'], self.analysis.getExtensions())

	def test_AddExtensionList(self):

		self.assertEqual([], self.analysis.getExtensions())

		self.assertTrue(self.analysis.addExtension(['.cc', '.C', '.cc']))

		# doubled entries are ignored
		self.assertEqual(['.cc', '.C'], self.analysis.getExtensions())

	def test_FileNotMatchingExtension(self):

		self.assertTrue(self.analysis.addExtension(['.cc', '.C', '.cc']))

		self.assertFalse(self.analysis.insertFile('FileClass.py'))

		self.assertEqual(len(self.analysis.getFiles()), 0)

		self.assertEqual(self.analysis.getFiles(), [])

	def test_TestAddingMatchingFile(self):

		self.assertTrue(self.analysis.addExtension(['.py', '.sh']))

		self.assertTrue(self.analysis.insertFile('FileClass.py'))

		self.assertEqual(len(self.analysis.getFiles()), 1)

		self.assertEqual(self.analysis.getFiles(), ['FileClass.py'])

		self.assertTrue(self.analysis.insertFile('test-run-all.sh'))

		self.assertEqual(len(self.analysis.getFiles()), 2)

		self.assertEqual(self.analysis.getFiles(), ['FileClass.py', 'test-run-all.sh'])


	def test_AddingNonExistingFileCausesFalse(self):

		self.assertTrue(self.analysis.addExtension(['.py', '.sh']))

		self.assertFalse(self.analysis.insertFile('FileClasses.py'))


	def test_FileIsAlwaysAddedEvenWithoutExtensions(self):

		self.assertTrue(self.analysis.insertFile('FileClass.py'))

	def test_IncompleteExtensionNotExcepted(self):

		self.assertTrue(self.analysis.addExtension(['.py', '.sh']))

		self.assertFalse(self.analysis.insertFile('FileClasses.p'))

		self.assertEqual(len(self.analysis.getFiles()), 0)

		self.assertFalse(self.analysis.insertFile('FileClasses.pyc'))

		self.assertEqual(len(self.analysis.getFiles()), 0)

if __name__ == "__main__":
    unittest.main()
