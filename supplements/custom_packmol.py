from squid import files, structures, sysconst
import os

def custom_packmol_coords(packmol_custom_string):
    
    temp = open('temp.inp', 'a')
    temp.write(packmol_custom_string)
    temp.close()

    packmol_string_list = [line for line in packmol_custom_string.split('\n')]
    packmol_string_list = ' '.join(packmol_string_list)
    packmol_string_list = packmol_string_list.split(' ')
    packmol_output = [packmol_string_list[i+1] for i, word in enumerate(packmol_string_list) if word == 'output'][0]
    os.system(('rm ') + packmol_output)

    temp_file_path = os.path.abspath('temp.inp')
    os.system(sysconst.packmol_path + ' < ' + temp_file_path)
    packmol_coords = open(packmol_output).read()

    os.system('rm temp.inp')
    os.system(('rm ' + packmol_output))

    return packmol_coords
