from tensorflow.keras.models import load_model

#if input_ticker == "TSLA":
model = load_model('test_tsla_model.h5')

print(model.summary())