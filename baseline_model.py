import pandas as pd

#from keras.models import Model
#from keras.layers import Input, Dense, Dropout, Flatten
#from keras.layers.convolutional import Convolution1D, MaxPooling1D

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
import gc


INPUT_FILE = 'data.csv'
data = pd.read_csv(INPUT_FILE) #nrows=20)

sentences = data['code'].values.astype('U')
y = data['interesting'].values

del data
gc.collect()

sentences_train, sentences_test, y_train, y_test = train_test_split(
   sentences, y, test_size=0.25, random_state=1000)

vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)

X_train = vectorizer.transform(sentences_train)
X_test  = vectorizer.transform(sentences_test)

classifier = SGDClassifier(loss="log")
batch_size = 200
for i in xrange(0, len(X_train), batch_size):
   classifier.partial_fit(X_train[i:i+batch_size], y_train[i:i+batch_size])
   
score = classifier.score(X_test, y_test)

print("Accuracy:", score)

# print(data)
# print(sentences)
# print(y)