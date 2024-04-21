import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("name", type=str, help="Your name")
parser.add_argument("age", type=int, nargs="?", help="Your age")
parser.add_argument("-m", "--is-main-character", action="store_true", help="The person is the main character")

# Parse the arguments
args = parser.parse_args()

# Use the parsed arguments
if args.age is not None:
    print(f"Now that you are {args.age}, I can reveal your true nature")
print(f"You're a hazard {args.name}")

if args.is_main_character:
    print("Also, here's a pile of cash")
