import numpy as np 
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from random import randint

<<<<<<< HEAD
inp = 'train_names.txt'
=======
inp = 'name.txt'
>>>>>>> 73a3153bae6376b85f64baf4521fe91c108c1acf
with open(inp) as f:
    content = f.readlines()
content = [x.lower() for x in content]

vocab = ''
for i in content:
	vocab+=str(i).lower()
vocab = sorted(list(set(vocab)))
vocab = vocab[vocab.index('a'):]
vocab.append(('\n'))
vocab_indices = dict((c, i) for i, c in enumerate(vocab))
indices_vocab = dict((i, c) for i, c in enumerate(vocab))

<<<<<<< HEAD
def sample(preds, temperature=1):
	preds = np.asarray(preds[0]).astype('float64')
	preds = np.log(preds) / temperature
	exp_preds = np.exp(preds)
	preds = exp_preds / np.sum(exp_preds)
	probas = np.random.multinomial(1, preds, 1)
	return np.argmax(probas)

def exists(new):
	for j in content:
		if i==j[:-1]:
			return True
	return False

=======
>>>>>>> 73a3153bae6376b85f64baf4521fe91c108c1acf
seq = randint(1,6)
dataX = []
dataY = []
for x,word in enumerate(content):
	for i in range(0, len(word) - seq, 1):
		seq_in = word[i:i + seq]
		seq_out = word[i + seq]
		dataX.append([vocab_indices[char] for char in seq_in])
		dataY.append(vocab_indices[seq_out])

n_patterns = len(dataX)
X = np.reshape(dataX, (n_patterns, seq, 1))
X = X / float(len(vocab))
y = np_utils.to_categorical(dataY)
model = Sequential()

<<<<<<< HEAD
=======
#RNN model
>>>>>>> 73a3153bae6376b85f64baf4521fe91c108c1acf
model.add(LSTM(256, return_sequences=True,input_shape=(X.shape[1], X.shape[2])))
model.add(LSTM(256))
model.add(Dense(y.shape[1]))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
model.summary()

<<<<<<< HEAD
=======
# Comment is when trained
>>>>>>> 73a3153bae6376b85f64baf4521fe91c108c1acf
filepath='nn.hdf5'
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
model.fit(X, y,batch_size=128,epochs=10,verbose=2,callbacks=callbacks_list)

<<<<<<< HEAD

filename = 'nn.hdf5'
model.load_weights(filename)
=======
filename = 'nn.hdf5'
model.load_weights(filename)

def sample(preds, temperature=1):
	preds = np.asarray(preds[0]).astype('float64')
	preds = np.log(preds) / temperature
	exp_preds = np.exp(preds)
	preds = exp_preds / np.sum(exp_preds)
	probas = np.random.multinomial(1, preds, 1)
	return np.argmax(probas)

>>>>>>> 73a3153bae6376b85f64baf4521fe91c108c1acf
final=[]
for temp in [.5,.8,.1,1.2]:
	j=1
	while(j<=500):
		new=[]
		word = content[randint(0, len(content)-1)][:seq]
		for k in word[-seq:]:
			new.append(vocab_indices[k])
		try:
			for t in range(10):
				x = np.reshape(new, (1, seq, 1))
				x = x / float(len(vocab))
				preds = model.predict(x, verbose=2)
				word+=indices_vocab[sample(preds,temp)]
				new=[]
				for k in word[-seq:]:
					new.append(vocab_indices[k])
				if word[-1] == '\n':
					word=word.strip()
					word.replace('\n','')
					break
			if (len(word)>seq and len(word)>=2) and word not in final:
				final.append(word.capitalize())
		except:
			0
		j+=1

<<<<<<< HEAD
open("temp_output.txt", 'w').close()
new_text = open("temp_output.txt", "w")
for i in sorted(final):
	new_text.write(i.replace('\n','')+'\n')
new_text.close()
=======
open("New Names.txt", 'w').close()
new_text = open("New Names.txt", "w")
for i in sorted(final):
	new_text.write(i.replace('\n','')+'\n')
new_text.close()
>>>>>>> 73a3153bae6376b85f64baf4521fe91c108c1acf
