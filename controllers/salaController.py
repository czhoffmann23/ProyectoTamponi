from services import *

def SalaAll():
    data=CallServiceGet("Sala")
    error=[]
    if data==error:
       print("no llego")

    else:
        return data

def SalaDetalle(cod):
    data=CallServiceGetCod("Sala",cod)
    error=[]
    if data==error:
       print("no llego")

    else:
        return data

def SalaCreate(obj):
    cod = obj[0]
    error=[]
    data_nrc=CallServiceGetCod("Sala",cod)
    if data_nrc==error: #no existe nrc
        data_obj=CallServiceSaveSala("Sala",obj)
        if data_obj == None:
                return 2
        else:
                return 1
    else: #existe nrc
        return 3
def SalaUpdate(obj):
    error=[]
    data_obj=CallServiceUpdateSala("Sala",obj)
    if data_obj == None:
        return 2
    else:
        return 1
    
def SalaDelete(id):
    data_nrc=CallServiceDeleteSal("Sala",id)
    if data_nrc == None:
        return 2
    else:
        return 1
   