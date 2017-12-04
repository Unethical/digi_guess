# Larger CNN for the MNIST Dataset
import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')


# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)


# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()


# reshape to be [samples][pixels][width][height]
num_pixels = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape(X_train.shape[0], 1, 28, 28).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28).astype('float32')


# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255


# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]


# Define the larger model
def larger_model():
    # create model
    model = Sequential()
    model.add(Conv2D(30, (5, 5), input_shape=(1, 28, 28), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(15, (3, 3,), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    # Complie model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def save_model(model, filename):
    model.save(filename)


# build the model
model = larger_model()
# fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=100)
# create model for single item
weights = model.get_weights()
single_model = larger_model()

single_model.set_weights(weights)
single_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the new model
# single_model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=1, batch_size=1)
# save the model to h5
save_model(single_model, "cnn_digit_clf.h5")
# Final evaluation of the model
scores = single_model.evaluate(X_test, y_test, batch_size=1, verbose=0)
print("Large CNN Error: %.2f%%" % (100-scores[1]*100))