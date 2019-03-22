from squid import structures

def isolate_atom_types(types, dump_obj, mol_len):
	
	count = 0
	atoms_list = []

	for line in dump_obj:
		words = line.split()

		if count == mol_len:
			yield atom_list
			count = 0
			atoms_list = []

		try:
			if int(words[0]) in types:
				atom_type = types[int(words[0])]
				x = float(words[1])
				y = float(words[2])
				z = float(words[3])
				count = count + 1
				atoms_list.append(structures.Atom(atom_type, x, y, z, index = count))
		except ValueError:
			pass