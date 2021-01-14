import Fonction.basic_function as basic_function
import semver
import getopt
import os
import sys

command = sys.argv
directory_location = basic_function.extract_directory_location(command)
test = os.path.isdir(directory_location)

print(test)