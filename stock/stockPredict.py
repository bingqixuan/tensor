from tensorflow import keras
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# model = keras.models.load_model('9MaxValue.h5')
# print(model.predict([0.3111]))

model = keras.models.load_model('1KLowValue.h5')
k = np.array([[0.2097], [29.77]]).T
print(model.predict(k))
