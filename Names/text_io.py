import numpy as np 
from keras.utils import np_utils
# import sys

class inp(object):
	def __init__(self, inp='karpathy', seq=10):
		self.inp = inp
		self.seq = seq
		self.inpFile = self.inp+".txt"
		self.outFile = self.inp+"-out.txt"
		self.content = [x.lower() for x in open(self.inpFile).read()]
		self.vocab = sorted(list(set(self.content)))
		self.vocab_indices = dict((c, i) for i, c in enumerate(self.vocab))
		self.indices_vocab = dict((i, c) for i, c in enumerate(self.vocab))
		self.dataX = []
		self.dataY = []

	def get_content(self):
		return self.content

	def get_vocab(self):
		return self.vocab,self.vocab_indices,self.indices_vocab

	def text_seq(self):
		for i in range(0, len(self.content) - self.seq, 1):
			seq_in = self.content[i:i + self.seq]
			seq_out = self.content[i + self.seq]
			self.dataX.append([self.vocab_indices[word] for word in seq_in])
			self.dataY.append(self.vocab_indices[seq_out])

	def rnn_input(self):
		n_patterns = len(self.dataX)
		X = np.reshape(self.dataX, (n_patterns, self.seq, 1))
		X = X / float(len(self.vocab))
		y = np_utils.to_categorical(self.dataY)
		return X,y

	def save(self,new):
		with open(self.outFile, 'w') as f:
			f.write(new)
			f.close()