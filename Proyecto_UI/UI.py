from tkinter import *
import cv2
from tkinter import ttk
import time
from PIL import ImageTk, Image
import imutils

import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model


class window(ttk.Frame):
    def __init__(self, win):
        super().__init__(win)
        win.title('Sistema de Cobro')
        win.columnconfigure(0, weight=1)
        win.rowconfigure(0, weight=1)

        self.columnconfigure(0, uniform=10)  # Separador
        self.columnconfigure(1, weight=40)  # Contenido
        self.columnconfigure(2, uniform=10)  # Separador
        self.columnconfigure(3, weight=80)  # Contenido
        self.columnconfigure(4, uniform=10)  # Separador

        self.rowconfigure(0, weight=2)  # Separador
        self.rowconfigure(1, weight=8)  # Video Capufe
        self.rowconfigure(2, weight=20)  # Separador
        self.rowconfigure(3, weight=10)  # coso welcome
        self.rowconfigure(4, weight=10)  # vehiculo y precio
        self.rowconfigure(5, weight=10)  # Separadorsote
        self.rowconfigure(6, weight=10)  # Total
        self.rowconfigure(7, weight=10)  # Status autorizacion / barra
        self.rowconfigure(8, weight=1)  # los copyrights

        #Video a ver si se hace o nel
        self.cap = cv2.VideoCapture('vidKpufaSS.mp4')  # Aqui va el videisho
        #Imagen banner
        self.image = Image.open("banner.PNG")
        self.img2 = self.image.resize((1186, 191), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img2)

        #Banner
        self.lblCapufe = ttk.Label(self, image=self.img, background="cyan4")
        self.lblCapufe.grid(row=1, column=1, columnspan=3, sticky="new")
        # # # Separador 1
        # self.separador1 = ttk.Label(self, text="-", background="cyan3")
        # self.separador1.grid(row=2, column=1, columnspan=3, sticky="new")
        #Publicidad
        self.lblVideo = ttk.Label(self, text="Publicidadcini", background="cyan4")
        self.lblVideo.grid(row=2, column=1, columnspan=1, rowspan=6, sticky="nswe")

        self.lblCosoBienvenida = ttk.Label(self, text="Bienvenido!", background="cyan4",
                                           font=("Courier", 28, "bold"))
        self.lblCosoBienvenida.grid(row=2, column=3, rowspan=1, sticky="nswe")

        self.lblVehiculo = ttk.Label(self, text="Vehiculo:\t$-", background="cyan4", font=("Courier", 18))
        self.lblVehiculo.grid(row=3, column=3, rowspan=1, sticky="wnse")

        self.lblSeparadorsote = ttk.Label(self, text="", background="cyan4", font=("Courier", 18))
        self.lblSeparadorsote.grid(row=4, column=3, rowspan=2, sticky="nswe")

        self.lblPrecioTotal = ttk.Label(self, text="Total:\t\t$-", background="cyan4", font=("Courier", 18, "bold"))
        self.lblPrecioTotal.grid(row=6, column=3, rowspan=1, sticky="nsew")

        self.lblStatusAutorizacion = ttk.Label(self, text="--", background="cyan4", font=("Courier", 18))
        self.lblStatusAutorizacion.grid(row=7, column=3, rowspan=1, sticky="nsew")

        self.lblCopyrights = ttk.Label(self,
                                       text="Copyright © 2020 CDMX Mexico, Inc. All rights reserved",
                                       background="cyan4", font=("Arial", 12, "bold", "italic"))
        self.lblCopyrights.grid(row=8, column=0, columnspan=5, sticky="ewns")
        self.grid(sticky="nsew")

        self.flag = ''
        self.pFlag = ''
        self.sFlag = ''
        self.respuesta = 5
        self.i=0

    def prueba(self):
        #Visualizando video
        ret, frame = self.cap.read()
        if ret:
            frame = imutils.resize(frame, width=900)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im1 = Image.fromarray(frame)
            im2 = ImageTk.PhotoImage(image=im1)

            self.lblVideo.configure(image=im2)
            self.lblVideo.image = im2

        #Bandera del boton
        fButton = open('_buttonFlag.txt', 'r')
        for i in fButton:
            self.flag = i
        fButton.flush()
        fButton.close()

        #Bandera del sensor
        sButton = open('_sensorFlag.txt', 'r')
        for k in sButton:
            self.sFlag = k
        sButton.flush()
        sButton.close()

        if self.flag == "0" and self.sFlag == "0\n":
        #if self.sFlag == "0\n":
            self.lblCosoBienvenida.configure(text="BIENVENIDO!\n")
            self.lblVehiculo.configure(text="Vehiculo:\t$-")
            self.lblPrecioTotal.configure(text="Total:\t$-")
            self.lblStatusAutorizacion.configure(text="--")
        if self.sFlag == "1\n" and self.flag == "0":
            self.lblCosoBienvenida.configure(text="PROCESANDO\n")
            f = open('_buttonFlag.txt', 'w')
            f.write('2')
            f.flush()
            f.close()
        if self.flag == "2":
            cap = cv2.VideoCapture(0)
            leido, frame = cap.read()
            if leido:
                time.sleep(2)
                cv2.imwrite("foto1.png", frame)
                self.lblCosoBienvenida.configure(text="PAGAR:\n")
            else:
                self.lblCosoBienvenida.configure(text="Error al acceder a la camara")
            cap.release()
            f = open('_buttonFlag.txt', 'w')
            f.write('3')
            f.flush()
            f.close()
        if self.flag == "3":
            #Hace la prediccion
            #self.respuesta = self.predict('auto18.jpg')
            self.respuesta = self.predict('foto.png')
            f = open('_buttonFlag.txt', 'w')
            f.write('4')
            f.flush()
            f.close()
        if self.flag == "4":
            #Escribe lo pertinente al precio
            if self.respuesta == 0:
                self.lblVehiculo.configure(text="Auto:\t$22")
                self.lblPrecioTotal.configure(text="Total:\t$22")
                f = open('_buttonFlag.txt', 'w')
                f.write('5')
                f.flush()
                f.close()
            if self.respuesta == 1:
                self.lblVehiculo.configure(text="Camion:\t$44")
                self.lblPrecioTotal.configure(text="Total:\t$44")
                f = open('_buttonFlag.txt', 'w')
                f.write('5')
                f.flush()
                f.close()
            if self.respuesta == 2:
                self.lblVehiculo.configure(text="Moto:\t$12")
                self.lblPrecioTotal.configure(text="Total:\t$12")
                f = open('_buttonFlag.txt', 'w')
                f.write('5')
                f.flush()
                f.close()
            if self.respuesta == 5:
                self.lblCosoBienvenida.configure(text="Ugghhh no jalo")
                f = open('_buttonFlag.txt', 'w')
                f.write('5')
                f.flush()
                f.close()
        if self.flag == "5":
            fPay = open('_paymentFlag.txt', 'r')
            for j in fPay:
                self.pFlag = j
            fPay.flush()
            fPay.close()
            if self.pFlag == "1":
                self.lblCosoBienvenida.configure(text="LISTO!\n")
                self.lblStatusAutorizacion.configure(text="Buen viaje!")
                f = open('_buttonFlag.txt', 'w')
                f.write('6')
                f.flush()
                f.close()

                f2 = open('_paymentFlag.txt', 'w')
                f2.write('0')
                f2.flush()
                f2.close()
        if self.flag == "6":
            if self.i < 200:
                self.i = self.i+1
            else:
                f = open('_buttonFlag.txt', 'w')
                f.write('0')
                f.flush()
                f.close()
                self.i = 0

        self.after(10, self.prueba)

    def predict(self, file):
        # cargamos la imagen
        img = load_img(file,  # Archivo de la imagen a predecir
                       target_size=(longitud, altura))  # Dimensiones de la imagen a leer
        img = img_to_array(img)  # Convierte la imagen en un arreglo de valores en un vector unidimensional
        img = np.expand_dims(img, axis=0)  # Se agrega una dimension para que coincida con los datos entrenados
        array = cnn.predict(img)  # Funcion de prediccion
        # La funcion arroja un arreglo con 3 valores, donde el valor marcado como 1 es el que es mas probable que sea --> [[0,1,0]]
        result = array[0]  # ----> Tomamos la dimension donde esta la prediccion
        answer = np.argmax(result)  # Devuelve el indice donde se encuentra el mayor valor

        # 0: Auto
        # 1: Camion
        # 2 Motocicleta

        return answer

#Directorios
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'

#Parametros para procesar las imagenes
longitud, altura = 150, 150 #Tamanio en pixeles de las imageness

cnn = load_model(modelo) #Se manda a llamar el modelo
cnn.load_weights(pesos_modelo) #Se llama a los pesos

rootMyWindow = Tk()
MyWindow = window(rootMyWindow)
rootMyWindow.geometry("1200x660+10+10")

MyWindow.prueba()
MyWindow.mainloop()