# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%


# %% [markdown]
# # Máquina de estados

# %%
import time
import requests
import pytube
import os
import getpass
import _thread as thread
from infoDownload import InfoDownload
from infoDownload import Video
from infoDownload import Orden
from tkinter import * 
from tkinter import messagebox
from tkinter import Tk
from tkinter.filedialog import askopenfile
username = getpass.getuser()
listDownloads = []
listaLiinks=list() # o tambien "listaLiinks=[]"
ordenDescargas=list() 
listPeso = []
directorio = "C:/Users/"+username+"/Desktop/Videos"


# %%
#CREACIÓN DE CARPETA:
def createFolder():
    try:
        os.mkdir(directorio)
    except OSError:
        messagebox.showerror("Error", "La creación del directorio "+directorio+" falló\n verifíque si estaba creada")  
    else:
        messagebox.showinfo("Creada","Se ha creado el directorio: "+ directorio)


# %%
def downloadDescription(link, contador):
    youtube = pytube.YouTube(link)
    listDownloads.append(InfoDownload(contador,Video(youtube.video_id,link,youtube.title,            youtube.description,    youtube.length), youtube.streams.first().filesize))
    return listDownloads.pop()


# %%
def descarga(item, contador):
    youtube = pytube.YouTube(item)
    video = youtube.streams.first()
    video.download("C:/Users/"+username+"/Desktop/Videos")
    listDownloads.append(InfoDownload(contador,Video(youtube.video_id,item,youtube.title,            youtube.description,    youtube.length),video.filesize))
    time.sleep(2)
    
    return True


# %%
def readAndListLinks():
    #archivo = open("/links.txt","r")
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    archivo = askopenfile() # show an "Open" dialog box and return the path to the selected file
    for linea in archivo:
        listaLiinks.append(linea)

    archivo.close()


# %%
def runDowload():

    contador = 0

    #DESCARGA MÚLTIPLE:
    for downloadLink in listaLiinks:
        if(thread.start_new_thread(descarga,(downloadLink, contador, ))): #ESTADO DE LA DESCARGA
            print("\n\n******************** DETALLES VIDEO "+str(contador+ 1)+" ****************************")
            print(downloadDescription(downloadLink, contador))
        
        contador = contador + 1


# %%
def close_window(): 
    if messagebox.askokcancel("Salir","Va a salir de la aplicación"):
        ventana.destroy()


# %%
def instructions():
    texto1="1- Si aun no creó la carpeta, Pulse el boton \"Crear carpeta de descarga\" \n        (al hacer esto se creará una carpeta llamada videos en su escritorio)        \n\n"
    texto2="2- Pulse el boton \"Cargar links\"  (con esto se copiarán los links del txt)  \n\n"
    texto3="3- Pulse el boton \"Comenzar descarga\" (con esto se iniciará la descarga)\n\n\n\n"
    texto4="NOTA: Si está creada la carpeta (la del punto 1), el botón no aparecerá, en    \n su lugar se mostrará un mensaje informando la existencia de la carpeta"  
    return texto1+texto2+texto3+texto4


# %%
def getHelp():
    ventana = Tk()
    ventana.geometry("700x600")
    ventana.title("AYUDA")
    #ventana.iconbitmap(r"/Icono.ico")#ícono
    ventana.configure(background = "yellow")
    ventana.resizable(width=0, height=0)#anula la opción de máximizar y de cambiar el tamaño arrastrando con el puntero del mouse
    titulo=Label(ventana, text = "Estimado "+username+" acá se muestran las instrucciones \n\n\n" , bg = "yellow",fg = "red")
    titulo.pack()
    titulo.config(fg="black",bg="yellow",font=("Verdana",16)) 
    
    texto = Label(ventana, text = instructions() , bg = "yellow",fg = "red")
    texto.pack()
    texto.config(fg="red",bg="yellow",font=("Verdana",12)) 
    
    boton = Button(ventana, text = "Cerrar Ventana",command= ventana.destroy,font ="Verdana",background = "red", activebackground="#EF9F72",relief="raised", borderwidth=7, width = 12)
    boton.place(x=290, y=460)
    
    ventana.mainloop()


# %%
def menssageOrButtonCreate():
    if os.path.isdir(directorio)==False:#si NO se creo la carpeta
        boton2 = Button(ventana, text = "Crear carpeta de descarga", command = createFolder,font ="Verdana",background = "deep pink",activebackground="#A0D1FC",bd=10, width = 22)
        boton2.place(x=190, y=120)#centro_x-100 es por que el ancho del botón es 20 (20x5=90)
    else:#si ya se creo la carpeta y se corre nuevamente el programa
        mensaje=Label(ventana, text = "Se ha creado la carpeta, la descarga se hará en: "+ directorio)
        mensaje.pack()#en lugar del boton, se avisa que ya está creada
        mensaje.config(fg="white",bg="dark green",font=("Arial",10))
        mensaje.place(relx = 0.05,rely = 0.26) 


# %%
def buttons():
    ventana.update()
    centro_x = (ventana.winfo_width()/2)
    boton1 = Button(ventana, text = "Ayuda", command = getHelp,font ="Verdana",background = "coral",activebackground="#A0D1FC",bd=10, width = 12)
    boton1.place(x=(centro_x-60), y=60)#centro_x-60 es por que el ancho del botón es 12 (12x5=60)
    menssageOrButtonCreate()
    boton3 = Button(ventana, text = "Cargar links", command = readAndListLinks,font ="Verdana",background = "dodger blue",activebackground="#A0D1FC",bd=10, width = 14)
    boton3.place(x=(centro_x-70), y=180)#centro_x-70 es por que el ancho del botón es 14 (14x5=70)
    boton4 = Button(ventana, text = "Comenzar descarga", command = runDowload,font ="Verdana",background = "forest green",activebackground="#A0D1FC",bd=10, width = 18)
    boton4.place(x=(centro_x-90), y=240)#centro_x-90 es por que el ancho del botón es 18 (18x5=90)
    boton = Button(ventana, text = "Salir",command=close_window,font ="Verdana",background = "red", activebackground="#EF9F72", relief="raised", borderwidth=7, width = 6)
    boton.place(x=(centro_x-30), y=360)#centro_x-30 es por que el ancho del botón es 6 (6x5=30)



# %%
ventana = Tk()#crea el objeto
ventana.geometry("600x500")#tamaño de la ventana
#ventana.wm_state('zoomed')#maximiza la ventana al iniciar la app
ventana.resizable(width=0, height=0)#anula la opción de máximizar y de cambiar el tamaño arrastrando con el puntero del mouse  
ventana.configure(background = "lawn green")#fondo de color sólido
ventana.title("Descarga de videos")#título
#ventana.iconbitmap(r"/Icono.ico")#ícono
ventana.protocol("WM_DELETE_WINDOW",close_window)#si se preciona la "X" para cerrar la app, llamo a close_window que pide confirmar

buttons() #botones/acciones

ventana.mainloop()


# %%



