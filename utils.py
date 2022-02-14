from os import listdir
from os.path import isfile, join

def read_files():
    files = [f for f in listdir("input/") if isfile(join("input/", f))]
    print(",".join(files))
