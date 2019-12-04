from tensorflow import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# model = keras.models.load_model('9MaxValue.h5')
# print(model.predict([0.3111]))

model = keras.models.load_model('7KLowValue.h5')
print(model.predict([0.2097, 29.77]))