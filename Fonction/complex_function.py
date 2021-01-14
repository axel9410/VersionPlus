from Fonction import basic_function
import semver
import getopt
import os


def extract_init_locations(package_locations, file_location):
    init_locations = [file_location]
    indent = 0
    while indent < len(package_locations):
        files = basic_function.extract_directory_files(package_locations[indent])
        file_name = basic_function.extract_file_name(files)
        file_location = basic_function.create_file_location(package_locations[indent], file_name)
        init_locations.append(file_location)
        indent = indent + 1
    return init_locations


def init_versions_upper(init_locations):
    indent = 0
    while indent < len(init_locations):

        all_lines = basic_function.read_lines(init_locations[indent])

        version_line_number = basic_function.find_version_line_number(all_lines)

        version_line = all_lines[version_line_number]

        version_number = basic_function.extract_version_number(version_line)

        new_version = basic_function.version_patch_upper(version_number)

        new_version_line = basic_function.create_new_version_line(new_version)

        all_lines = basic_function.replace_version_line(new_version_line, all_lines, version_line_number)

        basic_function.rewrite_module(init_locations[indent], all_lines)

        print("\n For ", init_locations[indent], " :")
        print("old version : ", version_number)
        print("new version : ", new_version)

        indent = indent + 1
