from random import randint
import numpy as np 


class output(object):
	def __init__(self,content,seq, words,temp):
		self.content = content
		self.seq = seq
		self.words = words
		self.start = randint(0, len(self.content)-1-self.seq)
		self.text = content[self.start:self.start+self.seq]
		self.temp = temp

	def sample(self,preds):
		preds = np.asarray(preds).astype('float64')
		preds = np.log(preds) / self.temp
		exp_preds = np.exp(preds)
		preds = exp_preds / np.sum(exp_preds)
		probas = np.random.multinomial(1, preds, 1)
		return np.argmax(probas)

	def generate(self,model,vocab,vocab_indices,indices_vocab):
		for it in range(self.words):
			new=[]
			new_word=[] 
			for k in self.text[-self.seq:]:
				new.append(vocab_indices[k])
			x = np.reshape(new, (1, self.seq, 1))
			x = x / float(len(vocab))
			preds = model.predict(x, verbose=2)[0]
			new_word += indices_vocab[self.sample(preds)]
			new_word = ''.join(new_word)
			self.text.append(new_word)
		return ''.join(self.text)