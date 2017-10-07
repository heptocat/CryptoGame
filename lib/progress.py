
progressDict = {'name': "unnamed", 'bi_bob': 0, 'bi_pickle': 0, 'bi_library': 1}

def setProgress(kind, status):
	global progressDict
	progressDict[kind] = status
def getProgress(kind):
	global progressDict
	return progressDict[kind]
	

