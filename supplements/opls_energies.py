import numpy as np

def get_dihedral_energy(coeffs):
    
    theta = [float(i) for i in range(0, 370, 10)]
    
    energy_values = []
    
    for angle in theta:
        energy_point = coeffs[0]*(1+np.cos(np.radians(angle))) + coeffs[1]*(1-np.cos(np.radians(2*angle))) +  coeffs[2]*(1+np.cos(np.radians(angle)))
        energy_values.append(energy_point)

    return (energy_values, theta)

