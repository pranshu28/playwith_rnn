from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint

class rnn(object):
	def __init__(self, inp, X,y,layer1=256, dropout=0.5,epochs = 100,batch=128,optimizer = 'rmsprop'):
		self.model = Sequential()
		self.filename = inp+'.hdf5'
		self.layer1 = layer1
		self.dropout = dropout
		self.optimizer = optimizer
		self.batch = batch
		self.epochs = epochs
		self.X = X
		self.y = y

	def get_model(self):
		return self.model

	#model
	def define(self):
		self.model.add(LSTM(self.layer1, return_sequences=True,input_shape=(self.X.shape[1], self.X.shape[2])))
		self.model.add(Dropout(self.dropout))
		self.model.add(LSTM(self.layer1))
		self.model.add(Dropout(self.dropout))
		self.model.add(LSTM(self.layer1))
		self.model.add(Dropout(self.dropout))
		self.model.add(Dense(self.y.shape[1]))
		self.model.add(Activation('softmax'))
		self.model.compile(loss='categorical_crossentropy', optimizer=self.optimizer)
		self.model.summary()

	def train(self):
		checkpoint = ModelCheckpoint(self.filename, monitor='loss', verbose=1, save_best_only=True, mode='min')
		callbacks_list = [checkpoint]
		self.model.fit(self.X, self.y,batch_size=self.batch,epochs=self.epochs,verbose=2,callbacks=callbacks_list)

	def load(self):
		self.model.load_weights(self.filename)

