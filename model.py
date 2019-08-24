import pandas as pd

from keras.models import Model
from keras.layers import Input, Dense, Dropout, Flatten
from keras.layers.convolutional import Convolution1D, MaxPooling1D

INPUT_FILE = 'data.csv'
data = pd.read_csv(INPUT_FILE)

print(data)