# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class InfoDownload:
    def __init__(self,idInfoDownload, video, peso):
        self.__idInfoDownload = idInfoDownload
        self.__video = video
        self.__peso = peso

    def orden(self,video,peso):
        self.__video = video
        self.__peso = peso

    @property
    def idInfoDownload(self):
        return self.__idInfoDownload
    
    @idInfoDownload.setter
    def idInfoDownload(self,idInfoDownload):
        self.__idInfoDownload = idInfoDownload
    
    @property
    def video(self):
        return self.__video
    
    @video.setter
    def video(self,video):
        self.__video = video
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,peso):
        self.__peso = peso

    def __str__(self):
        return "InfoDownload: [Video:" + str( self.__video) + "], [Peso:" + str( self.__peso) + "]"


# %%
class Video:
    def __init__(self, idVideo, url, titulo, descripcion, duracion):
        self.__idVideo = idVideo
        self.__url = url
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__duracion = duracion

    def orden(self,video):
        self.__video = video

    @property
    def idVideo(self):
        return self.__idVideo
    
    @idVideo.setter
    def idVideo(self,idVideo):
        self.__idVideo = idVideo

    @property
    def url(self):
        return self.__url
    
    @url.setter
    def idVideo(self,url):
        self.__url = url
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self,titulo):
        self.__titulo = titulo

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self,descripcion):
        self.__descripcion = descripcion
    
    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self,duracion):
        self.__duracion = duracion

    def __str__(self):
        return "Video: [idVideo:" + str( self.__idVideo) + "], [Url:" + str( self.__url) + "]" +  "], [Titulo:" + str(self.__titulo) + "]" + ", [Descripcion:" + str( self.__descripcion) + "]" + ", [Duracion:" + str( self.__duracion) + "]"


# %%
class Orden:
    def __init__(self,url,peso):
        self.__url = url 
        self.__peso = peso
    
    @property
    def video(self):
        return self.__video
    
    @video.setter
    def video(self,video):
        self.__video = video
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,peso):
        self.__peso = peso

    def __str__(self):
        return "InfoDownload: [Video:" + str( self.__video) + "], [Peso:" + str( self.__peso) + "]"


# %%



