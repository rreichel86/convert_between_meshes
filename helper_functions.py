from collections import namedtuple

node_prop = namedtuple('node_prop',['id','x_coord','y_coord','z_coord'])
element_prop = namedtuple('element_prop',['id', 'node_ids'])


def read_from_inp(input_filename, list_of_nodes, list_of_elements):
    with open(input_filename) as file_data:
        for line in file_data:
            if line[0] != '*':
                split_line = line.strip().split(",")
                split_line = list(map(str.strip, split_line))
                if len(split_line) == 4:
                    node_id = int(split_line[0])
                    node_coords = list(map(float, split_line[1:]))
                    node = node_prop(node_id, *node_coords)
                    list_of_nodes.append(node)
                elif len(split_line) == 9:
                    elmt_id, *lst_node_ids = map(int, split_line)
                    elmt = element_prop(elmt_id, lst_node_ids)
                    list_of_elements.append(elmt)

    return list_of_nodes, list_of_elements


def read_from_dat(input_filename, list_of_nodes, list_of_elements):
    with open(input_filename) as file_data:
        first_line = file_data.readline()
        number_of_vertices, _ = map(int,first_line.split(" "))
    
        # first number_of_vertices lines
        for _ in range(0,number_of_vertices):
            next_line = file_data.readline()
            split_line = next_line.strip().split(" ")

            node_id = int(split_line[0])
            node_coords = list(map(float, split_line[1:]))
            node = node_prop(node_id, *node_coords)
            list_of_nodes.append(node)


        elmt_id = 0
        for next_line in file_data:
            split_line = next_line.strip().split(" ")
            if int(split_line[1]) == 308:
                elmt_id += 1
                _, _, *lst_node_ids = map(int, split_line)
                elmt = element_prop(elmt_id, lst_node_ids)
                list_of_elements.append(elmt)
                
    return list_of_nodes, list_of_elements
            
 
def write_to_msh(output_filename, list_of_nodes, list_of_elements):            
    with open(output_filename, 'w') as f:
        f.write(f'$MeshFormat\n2.2 0 8\n$EndMeshFormat\n')
        f.write(f'$Nodes\n')
        f.write("{}\n".format(len(list_of_nodes)))
        for node in list_of_nodes:
            f.write("{:d}  {:f}  {:f}  {:f}\n".format(*node))
        f.write(f'$EndNodes\n')
    
        f.write(f'$Elements\n')
        f.write("{}\n".format(len(list_of_elements)))
        for elmt in list_of_elements:
            f.write("{:d} 5 1 1 {:d} {:d} {:d} {:d} {:d} {:d} {:d} {:d}\n".format(elmt.id, *elmt.node_ids))
        f.write(f'$EndElements\n')   
        
