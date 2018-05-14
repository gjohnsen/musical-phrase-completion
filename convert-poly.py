from __future__ import print_function
import argparse as argp

## Usage: python convert-poly.py -f <filepath> [-d to include duration] > outputfile.txt

def retrieveOptions():
    parser = argp.ArgumentParser()
    parser.add_argument(
        "-d",
        action='store_true',
        dest="duration"
    )

    parser.add_argument(
        "-f",
        type=str,
        required=True,
        dest="dataFile"
    )

    return parser.parse_args()

def prune(line, duration):
    if len(line) > 2:
        line2 = line[:2]
        if duration:
            line2 = line2 + [line[-1]]
        return line2

    else:
        line2 = [line[0]]
        if duration:
            line2 = line2 + [line[-1]]
        return line2

def convert(dataFile, duration):
    with open(dataFile) as f:
        for f0 in f.readlines():
            f0 = f0.strip()
            f0 = f0.split(' ')
            f0 = [x.split('.') for x in f0]
            f0 = [prune(x, duration) for x in f0]
            f0 = ['.'.join(x) for x in f0]
            f0 = ' '.join(f0)
            print(f0)

if __name__ == "__main__":
    args = retrieveOptions()
    convert(args.dataFile, args.duration)
