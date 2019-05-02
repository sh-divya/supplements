from supplements.generator import helper

class system_opls_lammps(object):
    
    def __init__(self, molGen_object_list, packmol_coords_file, system_dimensions, opls_file_path ):

        self.molecule_list = molGen_object_list[:]
        self.packmol_coords = packmol_coords_file
        self.dims = [-system_dimensions/(2.0), system_dimensions/(2.0), -system_dimensions/(2.0), system_dimensions/(2.0), -system_dimensions/(2.0), system_dimensions/(2.0)]
        self.helper_obj = helper.helper(opls_file_path)
        self.vdw, self.bond, self.angle, self.torsion, self.charge = self.helper_obj.readOPLS()

    def generate_parameter_objects(self, molGen_objects_for_paras)
