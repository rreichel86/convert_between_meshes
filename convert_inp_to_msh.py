import sys
from os.path import exists

from collections import namedtuple
from helper_functions import node_prop, element_prop, read_from_inp, write_to_msh

input_filename = ""
output_filename = ""

if len(sys.argv) == 2:
    input_filename = sys.argv[1]
    file_exists = exists(input_filename)
    if not file_exists:
        print(f'The file {input_filename} does not exist!')
        exit(1)
    output_filename = input_filename.replace(".inp",".msh")
else:
    print("No file specified!")
    exit(1)


list_of_nodes = []
list_of_elements = []

list_of_nodes, list_of_elements = read_from_inp(input_filename, list_of_nodes, list_of_elements)
write_to_msh(output_filename, list_of_nodes, list_of_elements)
