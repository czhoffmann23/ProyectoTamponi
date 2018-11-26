from services import *

def AlumnoAll():
    data=CallServiceGet("Alumno")
    error=[]
    if data==error:
       print("no llego")

    else:
        return data

def AlumnoDetalle(rut):
    data=CallServiceGetRut("Alumno",rut)
    error=[]
    if data==error:
       print("no llego")

    else:
        return data

def AlumnoCreate(obj):
    rut = obj[3]
    error=[]
    data_nrc=CallServiceGetRut("Alumno",rut)
    if data_nrc==error: #no existe nrc
        data_obj=CallServiceSaveAlumno("Alumno",obj)
        if data_obj == None:
                return 2
        else:
                return 1
    else: #existe nrc
        return 3
def AlumnoUpdate(obj):
    error=[]
    data_obj=CallServiceUpdateAlumno("Alumno",obj)
    if data_obj == None:
        return 2
    else:
        return 1
    
def AlumnoDelete(id):
    data_nrc=CallServiceDeleteAlum("Alumno",id)
    if data_nrc == None:
        return 2
    else:
        return 1
   