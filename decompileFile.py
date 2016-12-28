import uncompyle6, os

os.chdir("You PY/PYC path")
with open("uncompiled file name","wb") as fileobj:
	uncompyle6.uncompyle_file("PYC file name",fileobj)