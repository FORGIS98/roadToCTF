import tarfile

i = 1000
while(i >= 0):
    f = str(i) + '.tar'
    tar = tarfile.open(f)
    tar.extractall()
    i -= 1

