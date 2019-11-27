from tensorflow import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = keras.models.load_model('3MaxValue.h5')
print(model.predict([0.3522]))
