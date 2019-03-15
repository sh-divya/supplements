class paraGen(object):

	def __init__(self, molAtomList, molBonds, molAngles, molDiheds, IDDict):

		self.bonds = molBonds[:]
		self.angles = molAngles[:]
		self.diheds = molDiheds[:]
		self.atoms = molAtomList[:]
		self.atomIDs = IDDict
		self.bondTypes = []
		self.angleTypes = []
		self.dihedTypes = []

	def bondTypeGen(self, bondtypelist):

		tempBondTypes = []
		temp1 = []
		temp3 = []
		t3 = []

		#for thing in self.atoms:
			#print(thing) 

		for b in self.bonds:
			#print(b)
			atom1 = self.atoms[b[2]-1][2]
			atom2 = self.atoms[b[3]-1][2]
			#print([atom1, atom2])
			t1 = [self.atomIDs[atom1][1], self.atomIDs[atom2][1]]
			t2 = [t1[1], t1[0]]
			#print(t1)
			if t1 in temp1 or t2 in temp1:
				pass
			else:
				temp1.append(t1)
				t3.append([t1[0], t1[1], atom1, atom2])

		#print(t3)

		for b in bondtypelist:
			temp3.append([b[0], b[1]])

		for t in temp1:
			ts1 = [t[0], t[1]]
			ts2 = [t[1], t[0]]
			try:
				if ts1 in temp3:
					i = temp3.index(ts1)
				else:
					i = temp3.index(ts2)
				j = bondtypelist[i]
				tempBondTypes.append([0, j[2], j[3], j[0], j[1]])

			except ValueError:
				pass

		count = 1

		for b in tempBondTypes:

			self.bondTypes.append([count, b[1], b[2], b[3], b[4]])
			count = count + 1

	def angleTypeGen(self, angleTypeList):

		oplsTypes = []
		tempAllAngles = angleTypeList[:]
		#print(len(angleTypeList))
		#print(len(tempAllAngles))

		for ang in angleTypeList:
			tempAllAngles.append([ang[2], ang[1], ang[0], ang[3], ang[4]])

		#print(len(tempAllAngles))

		for ang in tempAllAngles:
			oplsTypes.append([ang[0], ang[1], ang[2]])

		no_duplicates = []

		for ang in self.angles:
			a1 = self.atoms[ang[2]-1][2]
			a2 = self.atoms[ang[3]-1][2]
			a3 = self.atoms[ang[4]-1][2]
			t1 = [self.atomIDs[a1][1], self.atomIDs[a2][1], self.atomIDs[a3][1]]
			t2 = [t1[2], t1[1], t1[0]]
			if t1 in no_duplicates:
				pass
			elif t2 in no_duplicates:
				pass
			else:
				no_duplicates.append(t1)

		#for n in no_duplicates:
			#print(n)

		temp_final_angles = []

		for ang in no_duplicates:
			if ang in oplsTypes:
				i = oplsTypes.index(ang)
				j = tempAllAngles[i]
				temp_final_angles.append([0, j[3], j[4], j[0], j[1], j[2]])
			else:
				temp_final_angles.append([0, 0, 0, ang[0], ang[1], ang[2]])

			#print(temp_final_angles[-1])

		count = 1

		for a in temp_final_angles:
			self.angleTypes.append([count, a[1], a[2], a[3], a[4], a[5]])
			count= count + 1
			#print(self.angleTypes[-1])

	def dihedTypeGen(self, dihedTypeList):

		oplsTypes = []
		tempAlldiheds = dihedTypeList[:]

		for dih in dihedTypeList:
			#print(dih)
			tempAlldiheds.append([dih[3], dih[2], dih[1], dih[0], dih[4], dih[5], dih[6]])

		for dih in tempAlldiheds:
			oplsTypes.append([dih[0], dih[1], dih[2], dih[3]])

		no_duplicates = []

		for dih in self.diheds:
			a1 = self.atoms[dih[2]-1][2]
			a2 = self.atoms[dih[3]-1][2]
			a3 = self.atoms[dih[4]-1][2]
			a4 = self.atoms[dih[5]-1][2]
			t1 = [self.atomIDs[a1][1], self.atomIDs[a2][1], self.atomIDs[a3][1], self.atomIDs[a4][1]]
			t2 = [t1[3], t1[2], t1[1], t1[0]]
			if t1 in no_duplicates:
				pass
			elif t2 in no_duplicates:
				pass
			else:
				no_duplicates.append(t1)
		#print(len(no_duplicates))
		temp_final_diheds = []

		for dih in no_duplicates:
			flag = False
			for d in oplsTypes:
				if flag:
					break
				if dih[0] == d[0] and dih[1] == d[1] and dih[2] == d[2] and dih[3] == d[3]:
					i = oplsTypes.index(d)
					j = tempAlldiheds[i]
					temp_final_diheds.append([0, j[4], j[5], j[6], j[0], j[1], j[2], j[3]])
					flag = True
				elif dih[3] == d[0] and dih[2] == d[1] and dih[1] == d[2] and dih[0] == d[3]:
					i = oplsTypes.index(d)
					j = tempAlldiheds[i]
					temp_final_diheds.append([0, j[4], j[5], j[6], j[0], j[1], j[2], j[3]])
					flag = True

			if not flag:
				temp_final_diheds.append([0, 0, 0, 0, dih[0], dih[1], dih[2], dih[3]])
				#print(temp_final_diheds[-1])

		'''for dih in no_duplicates:
			if dih in oplsTypes:
				i = oplsTypes.index(dih)
				j = tempAlldiheds[i]
				#print(j)
				temp_final_diheds.append([0, j[4], j[5], j[6], j[0], j[1], j[2], j[3]])
			else:
				temp_final_diheds.append([0, 0, 0, 0, j[0], j[1], j[2], j[3]])
				print(temp_final_diheds[-1])'''


		#print(len(temp_final_diheds))
		count = 1

		for d in temp_final_diheds:
			self.dihedTypes.append([count, d[1], d[2], d[3], d[4], d[5], d[6], d[7]])
			#print(self.dihedTypes[-1])
			count = count + 1

	def getBondTypes(self):

		return self.bondTypes

	def getAngleTypes(self):

		return self.angleTypes

	def getDihedTypes(self):

		return self.dihedTypes

