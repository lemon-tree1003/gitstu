import argparse
import sys

parser = argparse.ArgumentParser(description="just testing")

# parser.add_argument("integer_exam", nargs=1, default=100, help="a integer")
# parser.add_argument("filename",  dest='hahah' ,default='abc.txt', help="a file")
#
# parser.add_argument("--rate",type=float, default=0.01, help="initial rate")
# parser.add_argument("--step", type=int, default=2000, help="max")


aa = parser.parse_args(sys.argv[1:])

print(aa.hahah)

