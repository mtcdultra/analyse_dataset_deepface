import os
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers import Dense, Dropout, Flatten
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

num_classes = 7
batch_size = 256
epochs = 10
dimension_1 = 300
dimension_2 = 300

##################### TEST VALUES #####################
path_csv_file = '/Users/mtcd/Downloads/MEAD_DATASET/mead_60/mead_csv_frames_60_300x300.csv'
path_save_model = '/Users/mtcd/Downloads/MEAD_DATASET/mead_60'
model_name_file = 'model_60_300x300.h5'
model_weight_name_file = 'model_weights_60_300x300.h5'

#path_csv_file = '/Users/mtcd/Downloads/mead_20221220/mead_csv_frames_20221220.csv'
#path_save_model = '/Users/mtcd/Downloads/mead_20221220'
#model_name_file = 'model_weights'
#model_name_file = model_name_file + '.h5'
#######################################################

#######################################################
#path_csv_file = input('Type the csv file: ')
#path_save_model = input('Type the path to save de trained model file: ')
#model_name_file = input('Name the model file (recomended: model_weights): ')
#model_name_file = model_name_file + '.h5'
#######################################################

with open(path_csv_file) as f:

    content = f.readlines()

lines = np.array(content)

num_of_instances = lines.size
print('number of instances: ', num_of_instances)
print('instance length: ', len(lines[1].split(',')[1].split(' ')))

# initialize trainset and test set
x_train, y_train, x_test, y_test = [], [], [], []

for index in range(1, num_of_instances):
    try:
        emotion, img, usage = lines[index].split(',')
        val = img.split(' ')
        pixels = np.array(val, 'float32')
        emotion = keras.utils.to_categorical(emotion, num_classes)

        if 'Training' in usage:
            y_train.append(emotion)
            x_train.append(pixels)
        elif 'Test' in usage:
        #elif 'PublicTest' in usage:
            y_test.append(emotion)
            x_test.append(pixels)
    except:
        print('', end='')

x_train = np.array(x_train, 'float32')
y_train = np.array(y_train, 'float32')
x_test = np.array(x_test, 'float32')
y_test = np.array(y_test, 'float32')

x_train /= 255   # normalize inputs between [0, 1]
x_test /= 255

x_train = x_train.reshape(x_train.shape[0], dimension_1, dimension_2, 1)
x_train = x_train.astype('float32')

x_test = x_test.reshape(x_test.shape[0], dimension_1, dimension_2, 1)
x_test = x_test.astype('float32')

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

def meu_modelo():
    # construct CNN structure
    model = Sequential()

    # 1st convolution layer
    #model.add(Conv2D(64,(5, 5),activation='relu',input_shape=(dimension_1, dimension_2, 1)))
    #model.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))

    # 2nd convolution layer
    #model.add(Conv2D(64, (3, 3), activation='relu'))
    #model.add(Conv2D(64, (3, 3), activation='relu'))
    #model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

    # 3rd convolution layer
    #model.add(Conv2D(128, (3, 3), activation='relu'))
    #model.add(Conv2D(128, (3, 3), activation='relu'))
    #model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

    #model.add(Flatten())

    # fully connected neural networks
    #model.add(Dense(1024, activation='relu'))
    #model.add(Dropout(0.2))
    #model.add(Dense(1024, activation='relu'))
    #model.add(Dropout(0.2))

    #model.add(Dense(num_classes, activation='softmax'))

    model= Sequential()
    model.add(Conv2D(32,kernel_size=(5,5),input_shape=(dimension_1,dimension_1,1),activation='relu'))
    #model.add(Conv2D(64,(5, 5),activation='relu',input_shape=(dimension_1, dimension_2, 1)))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(128,activation='relu'))
    model.add(Dense(num_classes,activation='softmax'))

    #gen = ImageDataGenerator()
    #gen.fit(x_train)
    #train_generator = gen.flow(x_train, y_train, batch_size=batch_size)
    
    model.compile(
        loss='categorical_crossentropy',
        optimizer=keras.optimizers.Adam(),
        metrics=['accuracy']
    )
    
    #checkpoint = ModelCheckpoint(
    #    os.path.join(path_save_model, model_name_file),
    #    monitor='val_accuracy',
    #    save_weights_only=True,
    #    mode='max',
    #    verbose=1,
    #)

    return model

modelo = meu_modelo()
print(modelo.summary())

history = modelo.fit(x_train, y_train, epochs=epochs)


modelo.save(os.path.join(path_save_model, model_name_file))
modelo.save_weights(os.path.join(path_save_model, model_weight_name_file))
#model.fit(x_train, y_train, epochs=epochs) 
##model.fit(train_generator,steps_per_epoch=batch_size, epochs=epochs) 
#model.save_weights(os.path.join(path_save_model, model_name_file))

# Evaluation
train_score = modelo.evaluate(x_train, y_train, verbose=0)
print('Train loss:', train_score[0])
print('Train accuracy:', 100*train_score[1])
 
test_score = modelo.evaluate(x_test, y_test, verbose=0)
print('Test loss:', test_score[0])
print('Test accuracy:', 100*test_score[1])

# Evaluation
#train_score = model.evaluate(x_train, y_train, verbose=0)
#print('Train loss:', train_score[0])
#print('Train accuracy:', 100*train_score[1])
 
#test_score = model.evaluate(x_test, y_test, verbose=0)
#print('Test loss:', test_score[0])
#print('Test accuracy:', 100*test_score[1])

#print(model.summary())

## Mostrar histórico de treinamento
def grafico():
    plt.figure(1)
    plt.plot(history.history['loss'])
    #plt.plot(history.history['val_loss'])
    plt.legend(['training','validation'])
    plt.title('loss')
    plt.xlabel('epoch')
    plt.figure(2)
    plt.plot(history.history['accuracy'])
    #plt.plot(history.history['val_accuracy'])
    plt.legend(['training','validation'])
    plt.title('Acurracy')
    plt.xlabel('epoch')
    plt.show()
    score =modelo.evaluate(x_test,y_test,verbose=0)
    print('Test Score:',score[0])
    print('Test Accuracy:',score[1])