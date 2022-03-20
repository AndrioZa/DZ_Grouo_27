import sys
import argparse

parser = argparse.ArgumentParser()
print(parser)
parser.add_argument("--name", type=str)
parser.add_argument("--age", type=int)

arg = parser.parse_args()

print("Name =", arg.name)
print("Age =", arg.age)