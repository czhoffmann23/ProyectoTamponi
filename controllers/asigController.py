from services import *

def AsignaturasAll():
    data=CallServiceGet("Asignatura")
    error=[]
    if data==error:
       print("no llego")

    else:
        return data

def AsignaturasDetalle(nrc):
    data=CallServiceGetNRC("Asignatura",nrc)
    error=[]
    if data==error:
       print("no llego")

    else:
        return data

def AsignaturaCreate(obj):
    nrc = obj[3]
    error=[]
    data_nrc=CallServiceGetNRC("Asignatura",nrc)
    if data_nrc==error: #no existe nrc
        data_obj=CallServiceSaveAsignatura("Asignatura",obj)
        if data_obj == None:
                return 2
        else:
                return 1
    else: #existe nrc
        return 3
def AsignaturaUpdate(obj):
    error=[]
    data_obj=CallServiceUpdateAsignatura("Asignatura",obj)
    if data_obj == None:
        return 2
    else:
        return 1
    
def AsignaturaDelete(id):
    data_nrc=CallServiceDelete("Asignatura",id)
    if data_nrc == None:
        return 2
    else:
        return 1
   