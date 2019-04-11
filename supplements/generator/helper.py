import os

class helper(object):

	def __init__(self, opls_path):

		self.oplsObj = open(opls_path)

	def readCML(self, cml_file):

		flag = False
		count = 0
		allBonds = []

		objCML = open(cml_file)

		for line in objCML:

			data = line.split()

			if flag:
				try:
					count += 1
					temp = data[1].split('=')
					#print(temp[1])
					atom1 = temp[1][2:]
					atom2 = data[2][1:-1]
					#print(atom1, atom2)
					allBonds.append([count, 1, int(atom1), int(atom2)])

				except IndexError:
					break

			if data[0] == '<bondArray>':

				flag = True

			if data[0] == '/bondArray':
				flag = False

		return allBonds

	def readOPLS(self):

		epsSig = []
		bondPara = []
		anglePara = []
		dihedPara = []
		chargeDict = {}

		for line in self.oplsObj:

			temp = line.split()
			try:
				if temp[0] == 'vdw':
					epsSig.append([int(temp[1]), float(temp[2]), float(temp[3])])
				if temp[0] == 'bond':
					bondPara.append([int(temp[1]), int(temp[2]), float(temp[3]), float(temp[4])])
				if temp[0] == 'angle':
					anglePara.append([int(temp[1]), int(temp[2]), int(temp[3]), float(temp[4]), float(temp[5])])
				if temp[0] == 'torsion' or temp[0] == '#torsion':
					dihedPara.append([int(temp[1]), int(temp[2]), int(temp[3]), int(temp[4]), float(temp[5]), float(temp[8]), float(temp[11])])
				if temp[0] == 'charge':
					chargeDict[int(temp[1])] = float(temp[2])
			except IndexError:
				pass

		return (epsSig, bondPara, anglePara, dihedPara, chargeDict)
