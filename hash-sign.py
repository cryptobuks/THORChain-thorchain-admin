import glob
import hashlib
import os.path

targetdirectory = 'C:/Users/ron/Documents/FilesToHash/*'
hasharray = []
signaturetext = """The following hashes have been signed for verification using THORCHAIN-ADMIN GPG keys
located on the profile at https://github.com/thorchain-admin
SHA256 Hashes\n
"""
stringhashes = ""

filenames = glob.glob(targetdirectory)

for filename in filenames:
    with open(filename, 'rb') as inputfile:
        data = inputfile.read()
        hasharray.append(os.path.basename(inputfile.name) +" "+ hashlib.sha256(data).hexdigest())

for hashes in hasharray:
    stringhashes += hashes+ " \n"
    pass


print(signaturetext + stringhashes)
