"""
FileAnalysis is meant to scan a folder in the filesystem and count 
associate different file types to different classes. The module provides
statistics about:
 > total number of files per class
 > total size of files per class
 > maximum file size per class
 > minimum file size per class
 > average file size per class
"""


import os
import getpass
import re
from FileSize import FileSize
from FileClass import FileClass
from FileWalker import FileWalker
from Session import Session
AlreadyExists = 1

# scan a folder for files and present the results
# in a very neat way
# add interface in order to store the results into a database



class CodeAnalysis():
	"""Holds the results for a file analysis"""

	def __init__(self):
		self.folder = []
		self.db = {} # create a dictionary, file extensions to class names
		self.sessions = [] # list of sessions, stores files and statistics for a number of classes per session
		self.classes = [] # list of classes


	def folderAdd(self, folderObject):
		"""
			each time one adds a new FileWalker object it triggers 
			a new session that is stored using the unique FileWalker 
			name
		"""
		if isinstance(folderObject, FileWalker):
			
			# clone list of classes and create new
			thisSession = Session(folderObject.name, folderObject.path, self.classes)

			# iterate over all files
			thisSession.addFiles(folderObject)
			
			# append the completed session to the list
			self.sessions.append(thisSession)

			print "add Folder: %s" % folderObject.name

		else:
			return NotImplemented
		return True


	def extAdd(self, type, extension):
		self.classes.append(FileClass(type, list(extension)))

	def __str__(self):
		str = ""
		str += "File Analysis\n"
		for item in self.classes:
			str += " %s\n\n" % item
		return str

	def __typePrint(self):
		return


	def __folderPrint(self):
		for folder in self.folder:
			print " folder: %s" % folder
		return

