from squid import files, structures, sysconst
import os

def custom_packmol_coords(packmol_custom_string):
    
    packmol_string_list = packmol_custom_string.split('_').split('\n')
    packmol_output = [packmol_string_list[i+1] for i, word in enumerate(packmol_string_list) if words == 'output']

    temp = open('temp.inp', 'a')
    temp.write(packmol_custom_string)
    temp.close()

    temp_file_path = os.path.abspath('temp.inp')
    os.system(packmol_path + ' < ' + temp_file_path)
    packmol_coords = open(packmol_output).read()

    os.system('rm temp.inp')
    os.system(('rm ' + packmol_output))

    return packmol_coords
