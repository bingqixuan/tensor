from tensorflow import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = keras.models.load_model('1MaxValue.h5')
print(model.predict([1.1333]))
