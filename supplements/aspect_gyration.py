import math
from squid import structures, utils


def get_rg(mol):

    (c_x, c_y, c_z) = mol.get_center_of_mass()
    rx_2 = 0
    ry_2 = 0
    rz_2 = 0
    mol_wt = 0
    for atom in mol.atoms:
        m_i = units.elem_weight(atom.element)
        mol_wt += m_i 
        (x_i, y_i, z_i) = atom.flatten()
        rx_2 += m_i*((x_i-c_x)**2)
        ry_2 += m_i*((y_i-c_y)**2)
        rz_2 += m_i*((z_i-c_z)**2)
        
    rg = math.sqrt((rx_2 + ry_2 + rz_2)/mol_wt)

    return rg

def ellipsoid(frame):
	
	(A,c) = geometry.mvee(frame, tol = 0.01)
	(U, Q, V) = np.linalg.svd(A)
	vol  = (4/3.) * np.pi * np.sqrt(1/np.product(Q))
	
	return Q

def get_aspect_ratio(frames):
    
    aspect_ratio = []
    for f in frames: 
        abc = 1/(np.sqrt(ellipsoid(f)))
        aspect_ratio.append(max(abc)/min(abc))

    return aspect_ratio
