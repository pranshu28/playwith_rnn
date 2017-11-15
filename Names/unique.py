inp = 'temp_output.txt'
with open(inp) as f:
    content = f.readlines()
    for i in content:
    	if i not in open('train_names.txt').read():
    		print i