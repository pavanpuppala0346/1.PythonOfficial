import argparse

#### Introducing Positional arguments

# parser = argparse.ArgumentParser()
# print(parser)
# print(parser.parse_args())

# usage: arg_parse.py [-h] echo
# arg_parse.py: error: the following arguments are required: echo

# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()
# print(args)


# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print(args.echo)

# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number",
                    # type=int)
# args = parser.parse_args()
# print(args.square**2)


#### Introducing Optional arguments
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")