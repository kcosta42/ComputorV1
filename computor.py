import argparse
import computor.core as core

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("equation", type=str,
                      help="equation to resolve")
  parser.add_argument("-v", "--verbose", action="store_true",
                      help="Show additional output")
  parser.add_argument("-s", "--show", action="store_true",
                      help="Show the graph of the polynomial function")
  args = parser.parse_args()
  core.resolve(args.equation.strip(), args.verbose, args.show)
