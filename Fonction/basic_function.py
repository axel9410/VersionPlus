import semver
import getopt
import os


def extract_directory_location(command):
    command = getopt.getopt(command[1:], '-a')
    directory_location = command[1][0]
    return directory_location


def extract_directory_files(directory_location):
    directory_files = os.listdir(directory_location)
    return directory_files


def extract_file_name(files):
    for file in files:
        if "__init__" in file:
            file_name = file

    return file_name


def create_file_location(directory_location, file_name):
    file_location = os.path.join(directory_location, file_name)

    return file_location


def extract_packages(directory_files, directory_location):
    package_locations = []
    indent = 0
    while indent < len(directory_files):
        file_location = os.path.join(directory_location, directory_files[indent])

        if os.path.isdir(file_location):
            package_locations.append(file_location)
        indent = indent + 1
    return package_locations


def read_lines(file_location):
    file = open(file_location)
    all_lines = file.readlines()
    file.close()
    return all_lines


def find_version_line_number(all_lines):
    number_line = 0
    version_line_number = 0

    for line in all_lines:

        if "__version__ =" in line:
            version_line_number = number_line

        number_line = number_line + 1
    return version_line_number


def extract_version_number(version_line):
    version_lines = version_line.split("'")
    version_number = version_lines[1]
    return version_number


def version_patch_upper(version_number):
    __version__ = semver.VersionInfo.parse(version_number)
    new_version = __version__.bump_patch()
    return new_version


def create_new_version_line(new_version):
    new_version_line = "__version__ = semver.VersionInfo.parse('" + str(new_version) + "') \n"
    return new_version_line


def replace_version_line(new_line, all_lines, version_line_number):
    all_lines[version_line_number] = new_line
    return all_lines


def rewrite_module(file_location, all_lines):
    file = open(file_location, "w")
    file.writelines(all_lines)
    file.close()
