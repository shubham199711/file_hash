from hashlib import sha256
import os
import argparse

def getFileHash(fn):
    if os.path.exists(fn):
        with open(os.path.basename(fn),'r') as input_:
            file = ''.join(input_.readlines())
            return sha256(file.encode('UTF-8')).hexdigest()
    else:
        print("Error: File does not exists")


def checkFileHash(fn,providedHash):
    return getFileHash(fn) == providedHash


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True, help="file path")
    ap.add_argument("-c", "--check", required=False, help="sha256 hash value to be checked")
    args = vars(ap.parse_args())
    if args.get('check') is not None:
        print(checkFileHash(args.get('file'), args.get('check')))
    else:
        print(getFileHash(args.get('file')))

