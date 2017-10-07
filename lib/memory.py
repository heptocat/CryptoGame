import sys, os
class Memory:
	def save(ID, text, filename):
		file = open(filename, 'w')
		line = ID + ':' + text + '/n'
		Memory.deleteLine(ID)
		file.write(line)
		file.close()
		
	def deleteLine(searchID, filename):
		file = open(filename, 'w')
		for line in file:
			ID = ''
			found_ID = False
			new_line = ''
		
			if line == '\n':					# ignore empty lines
				continue
	
	
			for char in line:
				if found_ID:
					new_line = new_line + char
				elif not char == ':':
					ID = ID + char
				elif char == ':':
					found_ID = True
	

			if ID != searchID:
				file.write(ID + ':' + new_line)
		file.close()

	def loadB(searchID, filename):
		text = Memory.load(searchID, filename)
		if text == 'True':
			output = True
		elif text == 'False':
			output = False
		else:
			output = text
		return output

	def load(searchID, filename):
		file = open(filename, 'r')
		for line in file:
			output = ''
			ID = ''
			found_ID = False
			new_line = ''
		
			if line == '\n':					# ignore empty lines
				continue
	
			line = line[0:-1]					# remove line breaks that are automatically added at the end of lines (\n)
	
	
			for char in line:
				if found_ID:
					new_line = new_line + char
				elif not char == ':':
					ID = ID + char
				elif char == ':':
					found_ID = True
	

			if ID == searchID:

				output = new_line
				
				break
		file.close()
		return output

	def kill(filename):
		file = open(filename, 'r')
		file.truncate()
