import tensorflow as tf

print("hello")
model = tf.keras.models.Sequential()
# Adds a densely-connected layer with 2 units to the model:
model.add(tf.keras.layers.Dense(2,input_shape=(2, 1)))
model.add(tf.keras.layers.Dense(6,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(2,activation=tf.nn.softmax))

model.compile(optimizer=tf.optimizers.RMSprop(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print("sucess")
