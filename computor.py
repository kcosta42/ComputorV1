#!/usr/bin/python3

import argparse
import computor.core as core

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("equation", type=str,
                      help="equation to resolve")
  args = parser.parse_args()
  core.resolve(args.equation)
