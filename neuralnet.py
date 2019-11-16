from keras.models import Sequential
from keras.layers import Dense
import keras.optimizers as optimizers
from keras.utils import to_categorical
import numpy


dataset = numpy.loadtxt("C:\CyKit-master\CyKit-master\Py3\eeg-emg-combined-final6-data.csv", delimiter=",")
X = dataset[:, 0:14]

Y = dataset[:, 15]


model=Sequential()
model.add(Dense(14, input_dim=14, activation='linear'))
model.add(Dense(4, activation='linear'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer=optimizers.Adam(), loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, Y, epochs=1000, batch_size=25)
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
model.save('my_model_update_modified_processed_emg_only.h5')