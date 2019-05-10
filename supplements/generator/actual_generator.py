from supplements.generator import helper
from supplements.generator import paraGen

class system_opls_lammps(object):
    
    def __init__(self, molGen_object_list, packmol_coords_file, system_dimensions, opls_file_path ):

        self.molecule_list = molGen_object_list[:]
        self.packmol_coords = packmol_coords_file
        self.dims = [-system_dimensions/(2.0), system_dimensions/(2.0), -system_dimensions/(2.0), system_dimensions/(2.0), -system_dimensions/(2.0), system_dimensions/(2.0)]
        self.helper_obj = helper.helper(opls_file_path)
        self.vdw, self.bond, self.angle, self.torsion, self.charge = self.helper_obj.readOPLS()

    def generate_parameter_objects(self, molGen_objects_for_paras, dictionary_with_atom_ids):
        
        self.para_objects = []

        for molecule in molGen_objects_for_paras:

            self.para_objects.append(paraGen.paraGen(molecule.getAtoms(), molecule.getBonds(), molecule.getAngles(), molecule.getDiheds(), atomIDs))

        for para in para_objects;
            para.bondTypegen(self.bond)
            para.angleTypeGen(self.angle)
            para.dihedTypeGen(self.torsion)

    def create_master_lists():

        self.masterBonds = []
        self.masterAngles = []
        self.masterDiheds = []

        bcount = 1
        acount = 1
        dcount = 1
        
        for obj in self.pata_objects:
            
            for b in obj.getBondTypes:
                self.master
