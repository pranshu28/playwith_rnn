from text_io import inp
from model import rnn
from generate import output
import sys

if __name__ == '__main__':
	
	text = sys.argv[1] if (len(sys.argv) > 1) else "karpathy"
	layer = 256
	drop = 0.5
	epochs = 100
	batch = 128
	optimizer = 'rmsprop'
	seq = 50
	new_words = 1000
	temperature = 1

	file = inp(text,seq)
	file.text_seq()
	x,y = file.rnn_input()

	rnn = rnn(text, x,y,layer1=layer, dropout=drop,epochs = epochs,batch=batch,optimizer = optimizer)
	rnn.define()
	rnn.load()
	# rnn.train()

	new = output(file.get_content(),seq=seq, words=new_words,temp=temperature)
	vocab,dict1,dict2 = file.get_vocab()
	new_text = new.generate(rnn.get_model(),vocab,dict1,dict2)

	# print new_text
	file.save(new_text)