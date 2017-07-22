import numpy as np 
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from random import randint
from keras.utils import np_utils

inp = 'train_text.txt'

with open(inp) as f:
    content = f.read().lower()

vocab = sorted(list(set(content)))
vocab_indices = dict((c, i) for i, c in enumerate(vocab))
indices_vocab = dict((i, c) for i, c in enumerate(vocab))

seq = 50
dataX = []
dataY = []
for i in range(0, len(content) - seq, 1):
	seq_in = content[i:i + seq]
	seq_out = content[i + seq]
	dataX.append([vocab_indices[char] for char in seq_in])
	dataY.append(vocab_indices[seq_out])

n_patterns = len(dataX)
X = np.reshape(dataX, (n_patterns, seq, 1))
X = X / float(len(vocab))
y = np_utils.to_categorical(dataY)

model = Sequential()
model.add(LSTM(256, return_sequences=True,input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1]))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
model.summary()

filepath='nn.hdf5'
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
model.fit(X, y,batch_size=128,epochs=10,verbose=2,callbacks=callbacks_list)

filename = 'nn.hdf5'
model.load_weights(filename)

def sample(preds, temperature=1):
	preds = np.asarray(preds).astype('float64')
	preds = np.log(preds) / temperature
	exp_preds = np.exp(preds)
	preds = exp_preds / np.sum(exp_preds)
	probas = np.random.multinomial(1, preds, 1)
	return np.argmax(probas)

start = randint(0, len(content)-1-seq)
text = content[start:start+seq]
for it in range(400):
	new=[]
	for k in text[-seq:]:
		new.append(vocab_indices[k])
	x = np.reshape(new, (1, seq, 1))
	x = x / float(len(vocab))
	preds = model.predict(x, verbose=2)[0]
	text+=indices_vocab[sample(preds,1)]
		
open("temp_output.txt", 'w').close()
new_text = open("temp_output.txt", "w")
for i in sorted(text):
	new_text.write(i.replace('\n','')+'\n')
new_text.close()
