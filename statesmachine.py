# Máquina de estados

# Libs
import time
import requests
import os
import shutil
import getpass
import _thread as thread
import youtube_dl
from tkinter import *
from tkinter import messagebox
from tkinter import Tk
from tkinter.filedialog import askopenfile
username = getpass.getuser()
listDownloads = []
listaLiinks = list()  # o tambien "listaLiinks=[]"
ordenDescargas = list()
listPeso = []
directorio = "C:/Users/"+username+"/Desktop/Videos"

# %% -- Crea una nueva celda
# CREACIÓN DE UN DIRECTORIO:
def createFolder():
    try:
        os.mkdir(directorio)
    except OSError:
        messagebox.showerror("Error", "La creación del directorio " +
                             directorio+" falló\n verifíque si estaba creada")
    else:
        messagebox.showinfo(
            "Creada", "Se ha creado el directorio: " + directorio)


# %%
# Descarga la descripción del video
def downloadDescription(link, contador):
    ydl_opts = {}
    listaInfo=list()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(link, download=False) 
        listaInfo.append('Subido por: ' + meta['uploader'])
        listaInfo.append('Visitas: ' + str(meta['view_count']))
        listaInfo.append('Duracion: ' + str(meta['duration']))
        listaInfo.append('Titulo: ' +meta['title'])
        listaInfo.append('Descripcion: '+meta['description'])
        listDownloads.append(listaInfo)

    return listDownloads.pop()


# %%
# Realiza la descarga del video y la guarda en el directorio asignado previamente
def descarga(item, contador):
    ydl_opts = {
        'outtmpl': 'c:/Users/{username}/Desktop/Videos/%(title)s-%(id)s.%(ext)s'.format(username=username),
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([item])
    
    time.sleep(2)
    return True


# %%
# Lee el archivo cargado desde la interfaz
def readAndListLinks():
    Tk().withdraw()
    archivo = askopenfile() # Pide al usuario un archivo
    for linea in archivo:
        listaLiinks.append(linea)

    archivo.close()


# %%
# Procesamiento de peticiones para descargar los videos junto con la descripción de cada uno
def runDowload():

    contador = 0

    # DESCARGA MÚLTIPLE:
    if not listaLiinks:
        messagebox.showinfo(message="No ha cargado los links", title="ERROR")
    else:
        menssageOrButtonCreate()
        for downloadLink in listaLiinks:
            if(thread.start_new_thread(descarga, (downloadLink, contador, ))):  # ESTADO DE LA DESCARGA
                print("\n\n******************** DETALLES VIDEO " +
                      str(contador + 1)+" ****************************")
                print(downloadDescription(downloadLink, contador))

            contador = contador + 1


def showLinksDownloads():

    # DESCARGA MÚLTIPLE:
    if not listaLiinks:
        messagebox.showinfo(message="No ha cargado los links", title="ERROR")
    else:
        getLinks()


# %%
# Evento de cierre de interfaz
def close_window():
    if messagebox.askokcancel("Salir", "Va a salir de la aplicación"):
        ventana.destroy()


# %%
# Evento de instrucciones sobre el uso de la interfaz
def instructions():
    texto1 = "1- Si aun no creó la carpeta, Pulse el boton \"Crear carpeta de descarga\" \n        (al hacer esto se creará una carpeta llamada videos en su escritorio)        \n\n"
    texto2 = "2- Pulse el boton \"Cargar links\"  (con esto se copiarán los links del txt)  \n\n"
    texto3 = "3- Pulse el boton \"Comenzar descarga\" (con esto se iniciará la descarga)\n\n\n\n"
    texto4 = "NOTA: Si está creada la carpeta (la del punto 1), el botón no aparecerá, en    \n su lugar se mostrará un mensaje informando la existencia de la carpeta \n"
    texto5 = "ACTUALIZACION: la creacion de la carpeta de descargas se \n valida al momento de iniciar la descarga"
    return texto1+texto2+texto3+texto4+texto5

#Muestra información con respecto a los links cargados
def links():
    text = ""

    for downloadLink in listaLiinks:

        text += downloadLink

    return text

# %%
# Configuración de la interfaz
def getHelp():
    ventana = Tk()
    ventana.geometry("700x400")
    ventana.title("AYUDA")
    # ventana.iconbitmap(r"/Icono.ico")#ícono
    ventana.configure(background="black")
    # anula la opción de máximizar y de cambiar el tamaño arrastrando con el puntero del mouse
    ventana.resizable(width=0, height=0)
    titulo = Label(ventana, text="Estimado "+username +
                   " acá se muestran las instrucciones \n", bg="yellow", fg="red")
    titulo.pack()
    titulo.config(fg="yellow", bg="black", font=("Verdana", 16))

    texto = Label(ventana, text=instructions(), bg="black", fg="red")
    texto.pack()
    texto.config(fg="yellow", bg="black", font=("Verdana", 12))

    boton = Button(ventana, text="Cerrar Ventana", command=ventana.destroy, font="Verdana",
                   background="red", activebackground="#EF9F72", relief="raised", borderwidth=7, width=12)
    boton.place(x=290, y=460)

    ventana.mainloop()


def getLinks():
    ventana = Tk()
    ventana.geometry("700x400")
    ventana.title("Links")

    # ventana.iconbitmap(r"/Icono.ico")#ícono
    ventana.configure(background="black")
    # anula la opción de máximizar y de cambiar el tamaño arrastrando con el puntero del mouse
    ventana.resizable(width=0, height=0)
    titulo = Label(ventana, text="Estimado "+username +
                   " acá se muestran los links de los videos\n a descargar \n\n", bg="yellow", fg="red")
    titulo.pack()
    titulo.config(fg="yellow", bg="black", font=("Verdana", 16))

    texto = Label(ventana, text=links(), bg="black", fg="red")
    texto.pack()
    texto.config(fg="yellow", bg="black", font=("Verdana", 12))

    boton = Button(ventana, text="Cerrar Ventana", command=ventana.destroy, font="Verdana",
                   background="red", activebackground="#EF9F72", relief="raised", borderwidth=7, width=12)
    boton.place(x=290, y=460)

    ventana.mainloop()

# %%
# Comprueba el estado de creación del directorio de destino de las descargas

def menssageOrButtonCreate():
    if os.path.isdir(directorio) == False:  # si NO se creo la carpeta
        createFolder()
    else:  # si ya se creo la carpeta y se corre nuevamente el programa
        mensaje = Label(
            ventana, text="Se ha creado la carpeta, la descarga se hará en: " + directorio)
        mensaje.pack()  # en lugar del boton, se avisa que ya está creada
        mensaje.config(fg="white", bg="dark green", font=("Arial", 10))
        mensaje.place(relx=0.05, rely=0.26)


# %%
# Botones / opciones del programa
def buttons():
    ventana.update()
    centro_x = (ventana.winfo_width()/2)
    boton3 = Button(ventana, text="Cargar links", command=readAndListLinks, font="Verdana",
                    background="#FFFFFF", activebackground="#A0D1FC", bd=10, width=14)
    # centro_x-70 es por que el ancho del botón es 14 (14x5=70)
    boton3.place(x=(centro_x-280), y=80)
    boton4 = Button(ventana, text="Comenzar descarga", command=runDowload, font="Verdana",
                    background="#FFFFFF", activebackground="#A0D1FC", bd=10, width=18)
    # centro_x-90 es por que el ancho del botón es 18 (18x5=90)
    boton4.place(x=(centro_x-280), y=140)
    boton5 = Button(ventana, text="Info. Links cargados", command=showLinksDownloads, font="Verdana",
                    background="#FFFFFF", activebackground="#A0D1FC", bd=10, width=18)
    # centro_x-90 es por que el ancho del botón es 18 (18x5=90)
    boton5.place(x=(centro_x-280), y=200)
    boton1 = Button(ventana, text="Ayuda", command=getHelp, font="Verdana",
                    background="#FFFFFF", activebackground="#A0D1FC", bd=10, width=12)
    # centro_x-60 es por que el ancho del botón es 12 (12x5=60)
    boton1.place(x=(centro_x-280), y=260)
    boton = Button(ventana, text="Salir", command=close_window, font="Verdana",
                   background="#FFFFFF", activebackground="#EF9F72", relief="raised", borderwidth=7, width=6)
    # centro_x-30 es por que el ancho del botón es 6 (6x5=30)
    boton.place(x=(centro_x-280), y=320)


# %%
# Corre la el programa y su interfaz
scriptDir = os.getcwd()
os.chdir(scriptDir)
ventana = Tk()  # crea el objeto
ventana.geometry("600x500")  # tamaño de la ventana
photo = PhotoImage(file="fondo.png")
label = Label(ventana, image=photo)
label.pack()
# ventana.wm_state('zoomed')#maximiza la ventana al iniciar la app
# anula la opción de máximizar y de cambiar el tamaño arrastrando con el puntero del mouse
ventana.resizable(width=0, height=0)
ventana.configure(background="lawn green")  # fondo de color sólido
ventana.title("Gestor de descargas de videos")  # título
# ventana.iconbitmap("/Icono.ico")  # ícono
# si se preciona la "X" para cerrar la app, llamo a close_window que pide confirmar
ventana.protocol("WM_DELETE_WINDOW", close_window)

buttons()  # botones/acciones

ventana.mainloop()


# %%
