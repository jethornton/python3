def update_config(file, section, option, value, comment: str = None):
	sectFound = False
	lineIdx = 0
	with open(file, 'r') as config:
		lines = config.readlines()
		lineCount = len(lines)
		for line in lines:
			lineIdx += 1
			if sectFound and line.startswith('['):  #next secion
				lineIdx += -1
				lines.insert(lineIdx, option + ' = ' + value)
				if comment is not None:
					lineIdx += 1
					lines.insert(lineIdx, option + ' = ' + comment)
				break
			elif sectFound and line.startswith(option + ' = '):
				lines.pop(lineIdx)
				lines.insert(lineIdx, option + ' = ' + value)
				if comment is not None:
					lineIdx += 1
					lines.insert(lineIdx, option + ' = ' + comment)
				break
			elif sectFound and lineIdx == lineCount:
				lineIdx += 1
				lines.insert(lineIdx, option + ' = ' + value + '\n')
				if comment is not None:
					lineIdx += 1
					lines.insert(lineIdx, comment + '\n')
				break
			if line.strip() == '[' + section + ']':
				sectFound = True
	with open(file, 'w') as cfgfile:
		cfgfile.writelines(lines)
		if sectFound == False:
			cfgfile.writelines('[' + section + ']\n' + option + ' = ' + value)
			if comment is not None:
				cfgfile.writelines(comment)



