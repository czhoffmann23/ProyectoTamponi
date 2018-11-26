
# -*- coding: utf-8 -*-
#!/usr/bin/env python
from pymongo import Connection
 
connection = Connection('localhost', 27017)
db = connection.Proyecto

#==============  Get ================
def CallServiceGet(Tabla):
    data=[]
    error=[]
    query= db[Tabla].find({})
    if query is None:
       return error

    else:
        for x in query:
            data.append(x.values())
        return data

#==============  Delete ================
def CallServiceDelete(Tabla,nrc):
    data=[]
    error=[]
    query= db[Tabla].remove({'nrc':nrc})
    if query is None:
        return error
    else:
        return data
def CallServiceDeleteProf(Tabla,rut):
    data=[]
    error=[]
    query= db[Tabla].remove({'rut':rut})
    if query is None:
        return error
    else:
        return data
def CallServiceDeleteAlum(Tabla,rut):
    data=[]
    error=[]
    query= db[Tabla].remove({'rut':rut})
    if query is None:
        return error
    else:
        return data
def CallServiceDeleteSal(Tabla,cod):
    data=[]
    error=[]
    query= db[Tabla].remove({'codigo':cod})
    if query is None:
        return error
    else:
        return data
#==============  GetNRC ================
def CallServiceGetNRC(Tabla,nrc):
    data=[]
    error=[]
    query= db[Tabla].find_one({'nrc':nrc})

    if query is None:
        return error
    else:
        data.append(query.values())
        return data
#==============  GetCod ================
def CallServiceGetCod(Tabla,cod):
    data=[]
    error=[]
    query= db[Tabla].find_one({'codigo':cod})

    if query is None:
        return error
    else:
        data.append(query.values())
        return data
#==============  GetRUT ================
def CallServiceGetRut(Tabla,rut):
    data=[]
    error=[]
    query= db[Tabla].find_one({'rut':rut})

    if query is None:
        return error
    else:
        data.append(query.values())
        return data        
#==============  Save ================
def CallServiceSaveProfesor(Tabla,obj):
    data=[]
    error=[]
    query= db[Tabla].insert({'nombre':obj[0],'apellido':obj[1],'curso':obj[2],'rut':obj[3]})
    if query is None:
        return error 

    else:
        return data
def CallServiceSaveAlumno(Tabla,obj):
    data=[]
    error=[]
    query= db[Tabla].insert({'nombre':obj[0],'apellido':obj[1],'curso':obj[2],'rut':obj[3]})
    if query is None:
        return error 

    else:
        return data
def CallServiceSaveSala(Tabla,obj):
    data=[]
    error=[]
    query= db[Tabla].insert({'codigo':obj[0],'edificio':obj[1],'curso':obj[2]})
    if query is None:
        return error 

    else:
        return data
def CallServiceSaveAsignatura(Tabla,obj):
    data=[]
    error=[]
    query= db[Tabla].insert({'nombre':obj[0],'semestre':obj[1],'carrera':obj[2],'nrc':obj[3]})
    if query is None:
        return error 

    else:
        return data

#==============  UpdateASignatura ================
def CallServiceUpdateAsignatura(Tabla,obj):
    query= db[Tabla].update({"nrc": obj[3]},{"$set": {'nombre':obj[0],'semestre':obj[1],'carrera':obj[2],'nrc':obj[3]}})
    error=[]
    if query is None:
        return error 

    else:
        return data
def CallServiceUpdateProfesor(Tabla,obj):
    query= db[Tabla].update({"rut": obj[3]},{"$set": {'nombre':obj[0],'apellido':obj[1],'curso':obj[2],'rut':obj[3]}})
    error=[]
    if query is None:
        return error 

    else:
        return data
def CallServiceUpdateAlumno(Tabla,obj):
    query= db[Tabla].update({"rut": obj[3]},{"$set": {'nombre':obj[0],'apellido':obj[1],'curso':obj[2],'rut':obj[3]}})
    error=[]
    if query is None:
        return error 

    else:
        return data
def CallServiceUpdateSala(Tabla,obj):
    query= db[Tabla].update({"codigo": obj[0]},{"$set": {'codigo':obj[0],'edificio':obj[1],'curso':obj[2]}})
    error=[]
    if query is None:
        return error 

    else:
        return data