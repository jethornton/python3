import os

# to test if a directory exists
os.path.exists(directory)

# to test if a file exists
os.path.isfile(filename)

# create directories when they don't exist
home = os.path.expanduser('~')
filename = os.path.join(home, "foo/bar/baz.txt")

# see if the directory exists, if not create it
if not os.path.exists(os.path.dirname(filename)):
	os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
	f.write("FOOBAR")

# get directory from full path
home = os.path.expanduser('~')
path = os.path.join(home, "foo/bar/baz.txt")
print(path)
print(os.path.dirname(path))


os.path.abspath(path)
/home/john/foo/bar/baz.txt

os.path.basename(path)
baz.txt

os.path.commonpath(paths)
os.path.commonprefix(list)
os.path.dirname(path)
/home/john/foo/bar

os.path.exists(path)
False

os.path.expanduser('~')
/home/john

os.path.getatime(path)
os.path.getmtime(path)
os.path.getctime(path)
os.path.getsize(path)
os.path.isabs(path)
os.path.isfile(path)
os.path.isdir(path)
os.path.islink(path)
os.path.ismount(path)
os.path.join(path, *paths)
os.path.split(path)
('/home/john/foo/bar', 'baz.txt')

os.path.splitext(path)
('/home/john/foo/bar/baz', '.txt')


