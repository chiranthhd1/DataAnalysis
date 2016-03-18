""" Framework for getting filetype-specific metadat
instatntiate appropriate class wiyh filename , returned object acts like a dictionary with key-value pairs for each piece of metadata.

	import fileinfo
	info = fileinfo.MP3FileInfo("/music/1.mp4")
	print "\\n ".join(["%s=%s" % (k,v) for k,v in info.items()])
	
	or use 
	Or use listDirectory function to get info on all files in a directory.
for info in fileinfo.listDirectory("/music/ap/", [".mp3"]):
...
Framework can be extended by adding classes for particular file types, e.g.
HTMLFileInfo, MPGFileInfo, DOCFileInfo. Each class is completely responsible for
parsing its files appropriately; see MP3FileInfo for example.
"""

import os
import sys

from UserDict import UserDict

def stripnulls(data):
	"strip whitespace and nulls"
	return data.replace("\00","").strip()
	
class FileInfo(UserDict):
	"store file metadata"
	def __init__(self,filename=name):
		UserDict.__init__(self)
		self["name"] = filename

class MP3FileInfo(Fileinfo):
	"store ID3v1.0MP3 tags"
	tagDataMap = {	"title" : (3,33,stripnulls),
			"artist" : (3,63,stripnulls),
			"album" : (63,93,stripnulls),
			"year" : (93,97,stripnulls),
			"comment" : (97,120,stripnulls),
			"genre" : (127,128,ord),}

def __parse(self,filename):
	"parse ID3v1,0 tages from MP4 file"
	self.clear()
	try:
		fsock = open(filename, "rb",n)
		try:
			fsock.seek(-128,2)
			tagdata = fsock.read(128)
		finally:
			fsock.close()
		if tagdata[:3] == "TAG":
			for tag. (start,end,parseFunc)in self.tagDataMap.items():
				self[tag] = parseFunc(tagdata[start:end])
		except IOError:
			pass


























