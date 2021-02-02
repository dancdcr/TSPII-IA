#Entrenamiento para reconocimiento de imagenes con Keras y TensorFlow
#Alojamiento de la red neuronal para el sistema

import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator #Preprocesamiento de imagenes para el entrenamiento#Preprocesamiento de imagenes para el entrenamiento
#from tensorflow.python.keras import optimizers #Optimizador para el entrenamiento del algoritmo
from tensorflow.python.keras import optimizer_v2 #--------------> Cambio de implementacion por actualizacion de Tensorflow
from tensorflow.python.keras.models import Sequential #Libreria que nos permite hacer redes neuronales secuenciales, o sea con capas en orden
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation #Libreria con las funciones de transferencia, procesesamiento de imagenes y otras herramientas
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D #Capas donde haremos las convoluciones y maxpooling
from tensorflow.python.keras import backend as K #Si hay una sesion de Keras corriendo de fondo, lo va a cerrar

#Aqui la cierra, primero que nada
K.clear_session()

#Donde estan los datos
trainData = './data/entrenamiento'
validationData = './data/validacion'

#Parametrinis
epocas=5 #Veces a iterar en el set
lpx, apx = 150, 150 #Longitud del tamanio para las imagenes
batch = 32 #numero de imagenes que le mandaremos a procesar en cada paso
pasos = 20 #Cuantas veces se va a procesar la informacion en cada epoca
pasos_validacion = 300 #Se correran 300 pasos de validacion para ver que esta aprendiendo

filtrosConv1 = 32 #Filtros en cada convolucion (Profundidad de la imagen) ----> Checar
filtrosConv2 = 64
tamano_filtro1 = (3, 3) #Tamanio de los filtros ----> Checar
tamano_filtro2 = (2, 2)

poolsize = (2, 2) #Tamanio de los filtros en el pooling ---> Checar
clases = 3 #Al menos 3 clases: Automovil, Camion, Motocicleta
lr = 0.0004 #Learning rate. El alpha para el avance

#Preprocesamiento de imagenes

#Generador de las imagenes
entrenamiento_datagen = ImageDataGenerator(
    rescale=1. / 255, #Reescalamiento de imagenes de 0 a255, a 0 a 1
    shear_range=0.2, #Inclina un poco las imagenes siempre
    zoom_range=0.2,  #Hace zoom a algunas imagenes (20%)
    horizontal_flip=True) #Va a invertir las imagenes para distinguir direccionalidad

#Set de datos de prueba y validacion
test_datagen = ImageDataGenerator(rescale=1. / 255) #Unicamente reescalamiento. Las imagenes las tomara tal como aparecen en pantalla

#Ahora generamos las imagenes para el entrenamiento
entrenamiento_generador = entrenamiento_datagen.flow_from_directory(
    trainData, #Datos que usara. Las imagenes en las carpeta de entrenamiento
    target_size=(apx, lpx), #El tamanio definido antes
    batch_size=batch, #El batch size
    class_mode='categorical') #Etiquetas categoricas, o sea, el nombre en este caso

#Generamos los datos de validacion
validacion_generador = test_datagen.flow_from_directory(
    validationData, #Los datos que va a usar para el entrenamiento. Esto es, la carpeta de validacion
    target_size=(apx, lpx), #El tamanio que definimos
    batch_size=batch, #Cuantas va a procesar por paso
    class_mode='categorical') #Etiquetado categorico

#Comenzamos con la creacion de la red neuronal convolucional (CNN)
cnn = Sequential() #La red es secuencial. Tiene varias capas una luego de la otra
#Se agrega una capa convolusional 2D. Tiene los 32 filtros definidos anteriormente, con los valores del filtro 1, padding no se, la forma de la entrada (RGB), la funcion de activacion sera la relu
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, padding ="same", input_shape=(lpx, apx, 3), activation='relu'))
#Capa de pooling del tamanio antes mencionada
cnn.add(MaxPooling2D(pool_size=poolsize))

#Otra capa convolucional. Ahora con el filtro de 64 y las dimensiones antes mencionadas
cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding ="same"))
#Otra capa de maxpooling
cnn.add(MaxPooling2D(pool_size=poolsize))

#Aplanamos la imagen (convertimos la imagen a una sola dimension)
cnn.add(Flatten()) #Esto se refiere a convertir la imagen en un vector de valores, no en una matriz cuadrada
#Ahora lo mandamos a una capa de 256 neuronas con la funcion de activacion relu
cnn.add(Dense(256, activation='relu'))
#Aqui dice que vamos a quitarle el 50% de las neuronas para evitar el overfitting y encuentre caminos alternos de clasificacion
cnn.add(Dropout(0.5))
#El numero de neuronas de esta casa va a ser la de salida, que son el numero de clases. El softmax nos da las probabilidades de que sea cada una de las clases
cnn.add(Dense(clases, activation='softmax'))

#que se usa para la compilacion, optimizando el algoritmo
cnn.compile(loss='categorical_crossentropy', #Entropia cruzada categorica como funcion de perdida ----CHECAR
            optimizer=optimizer_v2.adam.Adam(learning_rate=lr), #Optimizador Adam con una tasa de aprendizaje definida anteriormente
            metrics=['accuracy']) #Metrica de como sabremos como va la red. En este caso, con la precision


#ENTRENAMIENTO
cnn.fit_generator( #Parametros para entrenar a la red
    entrenamiento_generador, #Las imagenes de entrenamiento
    steps_per_epoch=pasos, #Los pasos por epoca 1000
    epochs=epocas, #Las epocas 20
    validation_data=validacion_generador, #Imagenes de validacion
    validation_steps=pasos_validacion) #Pasos de la validacion 300

#Directorio donde se mete el modelo
target_dir = './modelo/'
#Creacion si no existe
if not os.path.exists(target_dir):
  os.mkdir(target_dir)
   #Guardado del modelo
cnn.save('./modelo/modelo.h5') #           HDF5 (.ha) "Hierarchical Data Format" o Formato Jerarquico de datos. 
#                                          Utilizado para guardar y organizar grandes cantidades de datos
cnn.save_weights('./modelo/pesos.h5') #    Grabamos los pesos de la red