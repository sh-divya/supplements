import math
from squid import structures

def get_com(molecule, types):
    
    com_x = 0
    com_y = 0
    com_z = 0
    mol_wt = 0
    for atom in molecule:
        m_i = types[atom.element]
        mol_wt += m_i
        (x_i, y_i, z_i) = atom.flatten()
        com_x += m_i*x_i
        com_y += m_i*y_i
        com_z += m_i*z_i

    com_x = com_x/mol_wt
    com_y = com_y/mol_wt
    com_z = com_z/mol_wt

    return(com_x, com_y, com_z)
    
def get_rg(mol):

    (c_x, c_y, c_z) = get_com(mol)
    rx_2 = 0
    ry_2 = 0
    rz_2 = 0
    mol_wt = 0
    for atom in mol:
        m_i = types[atom.element]
        mol_wt += m_i 
        (x_i, y_i, z_i) = atom.flatten()
        rx_2 += m_i*((x_i-c_x)**2)
        ry_2 += m_i*((y_i-c_y)**2)
        rz_2 += m_i*((z_i-c_z)**2)
        
    rg = math.sqrt((rx_2 + ry_2 + rz_2)/mol_wt)

    return rg
