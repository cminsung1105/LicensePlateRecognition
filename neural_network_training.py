import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

# Load data set
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize data set to 0-to-1 range
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# Create a model and add layers
model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3), activation="relu"))
model.add(Conv2D(32, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same', activation="relu"))
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))

# Compile the model
model.compile(
	loss='categorical_crossentropy',
	optimizer="adam",
	metrics=['accuracy']
)

# Train the model
model.fit(
	x_train,
	y_train,
	# batch_size: how many images to feed in nn at once during training
	# Too high: take too long Too high: run out of memory. typically 32 ~ 128
	batch_size=32,
	# epochs: how many times go through training data set during training process
	# 1 full pass through entire data set = 1 epoch
	# higher: longer training process. eventually at some point additional training won't help anymore
	# large datasets require less epochs
	epochs=300,
	# test data: what data to use to validate training
	validation_data=(x_test, y_test),
	# randomize order (default is already True btw)
	shuffle=True
)
