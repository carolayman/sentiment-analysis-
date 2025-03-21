# -*- coding: utf-8 -*-
"""sentiment analysis .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b1XJ7RA96LFHJTevOzQCKl22ol7gDx9x
"""

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

texts = [
    'I love this movie', 'I hate this place', 'It is a great day', 'This is terrible',
    'The weather is amazing', 'I feel very happy today', 'This is the best thing ever',
    'I am so excited about this', 'The food tastes awful', 'I am disappointed with the service',
    'That was an incredible experience', 'I am feeling very sad', 'The view is breathtaking',
    'I cannot believe how bad this is', 'Absolutely fantastic!', 'What a waste of time',
    'I had a lot of fun', 'I am not happy with this', 'This made my day',
    'I will never come here again', 'Such a beautiful moment', 'This is just terrible',
    'I am beyond grateful', 'I am extremely frustrated', 'The staff was very helpful',
    'Worst decision I have ever made', 'I am loving every second of it',
    'This place is disgusting', 'I am so proud of myself', 'That was a horrible experience',
    'It is a dream come true', 'I am very upset', 'I cannot stop smiling',
    'Everything is perfect', 'I regret coming here', 'This is heaven',
    'I feel very uncomfortable', 'I am speechless, it was that good',
    'This is not what I expected', 'Amazing atmosphere', 'Completely unacceptable',
    'I feel relaxed and calm', 'I feel so angry', 'What a pleasant surprise',
    'It is so dirty here', 'I am feeling very peaceful', 'This was a big mistake',
    'Outstanding performance', 'I am shocked by the poor quality',
    'That was the best meal I have ever had', 'I wish I never saw that'
]

labels = [
    1, 0, 1, 0, 1, 1, 1, 1, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    1
]

tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
X_train = pad_sequences(sequences, maxlen=5)
y_train = np.array(labels)

model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=32, input_length=5))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=2)

text = input("Enter a text: ")
seq = tokenizer.texts_to_sequences([text])
X_test = pad_sequences(seq, maxlen=5)
prediction = model.predict(X_test)[0][0]

if prediction > 0.5:
    print("Positive")
else:
    print("Negative")