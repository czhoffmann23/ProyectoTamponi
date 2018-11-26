from services import *

def ProfesorAll():
    data=CallServiceGet("Profesor")
    error=[]
    if data==error:
       print("no llego")

    else:
        return data

def ProfesorDetalle(rut):
    data=CallServiceGetRut("Profesor",rut)
    error=[]
    if data==error:
       print("no llego")

    else:
        return data

def ProfesorCreate(obj):
    rut = obj[3]
    error=[]
    data_nrc=CallServiceGetRut("Profesor",rut)
    if data_nrc==error: #no existe nrc
        data_obj=CallServiceSaveProfesor("Profesor",obj)
        if data_obj == None:
                return 2
        else:
                return 1
    else: #existe nrc
        return 3
def ProfesorUpdate(obj):
    error=[]
    data_obj=CallServiceUpdateProfesor("Profesor",obj)
    if data_obj == None:
        return 2
    else:
        return 1
    
def ProfesorDelete(id):
    data_nrc=CallServiceDeleteProf("Profesor",id)
    if data_nrc == None:
        return 2
    else:
        return 1
   