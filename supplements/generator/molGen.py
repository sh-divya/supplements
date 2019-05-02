class molGen(object):

	def __init__(self, sizeMol, number, IDdict, atomList = [], bondList = [], angleList = [], dihedList = []):

		self.atoms = atomList[:]
		self.bonds = bondList[:]
		self.angles = angleList[:]
		self.diheds = dihedList[:]
		self.size = sizeMol
		self.number = number
		self.atomIDs = IDdict

	def angleGen(self):

		angleCount = 0
		bondNum = self.bonds[-1][0]

		for i in range(bondNum - 1):

			for j in range(bondNum - i - 1):

				if self.bonds[i][2] == self.bonds[i+j+1][2]:
					angleCount += 1
					self.angles.append( [angleCount, 1, self.bonds[i][3], self.bonds[i][2], self.bonds[i+j+1][3]])

				if self.bonds[i][2] == self.bonds[i+j+1][3]:
					angleCount += 1
					self.angles.append( [angleCount, 1, self.bonds[i][3], self.bonds[i][2], self.bonds[i+j+1][2]])

				if self.bonds[i][3] == self.bonds[i+j+1][2]:
					angleCount += 1
					self.angles.append( [angleCount, 1, self.bonds[i][2], self.bonds[i][3], self.bonds[i+j+1][3]])
				if self.bonds[i][3] == self.bonds[i+j+1][3]:
					angleCount += 1
					self.angles.append( [angleCount, 1, self.bonds[i][2], self.bonds[i][3], self.bonds[i+j+1][2]])

	def dihedGen(self):

		if self.size < 5:
			pass
		else:

			dihedList = []
			dihedCount = 0

			bondNum = self.bonds[-1][0]
			angleNum = self.angles[-1][0]

			for i in range(bondNum):
				
				for j in range(angleNum):

					if self.bonds[i][2] == self.angles[j][2] and self.bonds[i][3] != self.angles[j][3]:
						dihedCount += 1
						dihedList.append( [dihedCount, 1, self.bonds[i][3], self.bonds[i][2], self.angles[j][3], self.angles[j][4] ])

					if self.bonds[i][2] == self.angles[j][4] and self.bonds[i][3] != self.angles[j][3]:
						dihedCount += 1
						dihedList.append( [dihedCount, 1, self.bonds[i][3], self.bonds[i][2], self.angles[j][3], self.angles[j][2] ])

					if self.bonds[i][3] == self.angles[j][2] and self.bonds[i][2] != self.angles[j][3]:
						dihedCount += 1
						dihedList.append( [dihedCount, 1, self.bonds[i][2], self.bonds[i][3], self.angles[j][3], self.angles[j][4] ])

					if self.bonds[i][3] == self.angles[j][4] and self.bonds[i][2] != self.angles[j][3]:
						dihedCount += 1
						dihedList.append( [dihedCount, 1, self.bonds[i][2], self.bonds[i][3], self.angles[j][3], self.angles[j][2] ])

			doubleCount = []
			count = 0
			
			for i in range(len(dihedList)):
				
				for j in range(len(dihedList)-i-1):
					
					if dihedList[i][2] == dihedList[j+i+1][5] and dihedList[i][3] == dihedList[j+i+1][4] and dihedList[i][4] == dihedList[j+i+1][3] and dihedList[i][5] == dihedList[j+i+1][2]:
						doubleCount.append(j+i+1)
			
			for i in range(len(dihedList)):

				if (i not in doubleCount):
					count += 1
					self.diheds.append(dihedList[i])
					self.diheds[-1][0] = count

	def setTypes(self, masterBonds, masterAngles, masterDiheds):

		for b in self.bonds:

			id1 = self.atoms[b[2]-1][2]
			id2 = self.atoms[b[3]-1][2]
			srID1 = self.atomIDs[id1][1]
			srID2 = self.atomIDs[id2][1]

			for b_m in masterBonds:

				if srID1 == b_m[3] and srID2 == b_m[4]:

					b[1] = b_m[0]

				elif srID1 == b_m[4] and srID2 == b_m[3]:

					b[1] = b_m[0]

		aLen = len(masterAngles)
		dLen = len(masterDiheds)

		for i in range(aLen):

			masterAngles.append([masterAngles[i][0], masterAngles[i][1], masterAngles[i][2], masterAngles[i][5], masterAngles[i][4], masterAngles[i][3]])

		for i in range(dLen):

			masterDiheds.append([masterDiheds[i][0], masterDiheds[i][1], masterDiheds[i][2], masterDiheds[i][3], masterDiheds[i][7], masterDiheds[i][6], masterDiheds[i][5], masterDiheds[i][4], masterDiheds[i][3]])

		for a in self.angles:

			id1 = self.atoms[a[2]-1][2]
			id2 = self.atoms[a[3]-1][2]
			id3 = self.atoms[a[4]-1][2]
			srID1 = self.atomIDs[id1][1]
			srID2 = self.atomIDs[id2][1]
			srID3 = self.atomIDs[id3][1]

			for a_m in masterAngles:

				if srID1 == a_m[3] and srID2 == a_m[4] and srID3 == a_m[5]:

					a[1] = a_m[0]

		for d in self.diheds:

			id1 = self.atoms[d[2]-1][2]
			id2 = self.atoms[d[3]-1][2]
			id3 = self.atoms[d[4]-1][2]
			id4 = self.atoms[d[5]-1][2]
			srID1 = self.atomIDs[id1][1]
			srID2 = self.atomIDs[id2][1]
			srID3 = self.atomIDs[id3][1]
			srID4 = self.atomIDs[id4][1]

			for d_m in masterDiheds:

				if srID1 == d_m[4] and srID2 == d_m[5] and srID3 == d_m[6] and srID4 == d_m[7]:

					d[1] = d_m[0]

	def readCoords(self, coordObj):

		temp = coordObj.readline()
		temp = coordObj.readline()

		for i in range(self.size):

			temp = coordObj.readline()
			toList = temp.split()
			self.atoms.append([i + 1, 1, 1, 0, float(toList[1]), float(toList[2]), float(toList[3])])

	def typeAndCharge(self, types, charge, IDdict):

		i = 0

		for ats in self.atoms:
			
			t = types[i]
			ats[2] = t
			lrID = IDdict[t][0]
			ats[3] = charge[lrID]
			i = i + 1

	def getNum(self):

		return self.number
	
	def getBonds(self):

		return self.bonds

	def getAtoms(self):

		return self.atoms

	def getAngles(self):

		return self.angles

	def getDiheds(self):

		return self.diheds


