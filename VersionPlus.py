import Fonction.basic_function as basic_function
import Fonction.complex_function as complex_function
import sys


def main():
    command = sys.argv

    directory_location = basic_function.extract_directory_location(command)

    files = basic_function.extract_directory_files(directory_location)

    file_name = basic_function.extract_file_name(files)

    file_location = basic_function.create_file_location(directory_location, file_name)

    package_locations = basic_function.extract_packages(files, directory_location)

    init_locations = complex_function.extract_init_locations(package_locations, file_location)

    complex_function.init_versions_upper(init_locations)


main()
