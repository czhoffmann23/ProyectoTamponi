from bottle import route, run, template,static_file,error,post, request, redirect, url
import sys
sys.path.append('./controllers/')
from asigController import *
import sys
sys.path.append('./controllers/')
from profController import *
sys.path.append('./controllers/')
from alumController import *

@error(404)
def error404(error):
    return '<h1> TE EQUIVOCASTE OE ERROR 404 </h1>'

#===========  Visualizar  ===========
@route('/ProfesorAll')
def profesores():
    resultado=ProfesorAll()
    return template('ProfesorAll',rows=resultado)

@route('/AsignaturaAll')
def asignaturas():
    resultado=AsignaturasAll()
    return template('AsignaturaAll',rows=resultado)

@route('/AlumnoAll')
def asignaturas():
    resultado=AlumnoAll()
    return template('AlumnoAll',rows=resultado)
#===========  Detalle     ===========
@route('/Profesor/Detalle/<id>')
def profesorDetalle(id):
    resultado=ProfesorDetalle(id)
    return template('ProfesorDetalle',rows=resultado)

@route('/Asignatura/Detalle/<id>')
def asginaturaDetalle(id):
    resultado=AsignaturasDetalle(id)
 
    return template('AsignaturaDetalle',rows=resultado)

@route('/Alumno/Detalle/<id>')
def alumnoDetalle(id):
    resultado=AlumnoDetalle(id)
    return template('AlumnoDetalle',rows=resultado)

#===========  Modificar   ===========
@route('/Profesor/Modificar/<id>')
def profesorModificar(id):
    resultado=ProfesorDetalle(id)
    return template('ProfesorModificar',rows=resultado)
@route('/modificarprof', method="POST")
def process():
    obj=[]
    nombre = request.forms.get('nombre')
    apellido = request.forms.get('apellido')
    curso = request.forms.get('curso')
    rut = request.forms.get('rut')
    obj.append(nombre)
    obj.append(apellido)
    obj.append(curso)
    obj.append(rut)
  
    opcion=ProfesorUpdate(obj)
    if opcion==1: #exito
        redirect(url('/ProfesorAll') + '#exitoupdate')
    if opcion == 2:          #error en ingreso
        redirect(url('/ProfesorAll') + '#errorupdate')
@route('/Alumno/Modificar/<id>')
def profesorModificar(id):
    resultado=AlumnoDetalle(id)
    return template('AlumnoModificar',rows=resultado)
@route('/modificaralum', method="POST")
def process():
    obj=[]
    nombre = request.forms.get('nombre')
    apellido = request.forms.get('apellido')
    curso = request.forms.get('curso')
    rut = request.forms.get('rut')
    obj.append(nombre)
    obj.append(apellido)
    obj.append(curso)
    obj.append(rut)
  
    opcion=AlumnoUpdate(obj)
    if opcion==1: #exito
        redirect(url('/AlumnoAll') + '#exitoupdate')
    if opcion == 2:          #error en ingreso
        redirect(url('/AlumnoAll') + '#errorupdate')
@route('/Asignatura/Modificar/<id>')
def asignaturaModificar(id):
    resultado=AsignaturasDetalle(id)
    return template('AsignaturaModificar',rows=resultado)
@route('/modificar', method="POST")
def process():
    obj=[]
    nombre = request.forms.get('nombre')
    semestre = request.forms.get('semestre')
    carrera = request.forms.get('carrera')
    nrc = request.forms.get('nrc')
    obj.append(nombre)
    obj.append(semestre)
    obj.append(carrera)
    obj.append(nrc)
  
    opcion=AsignaturaUpdate(obj)
    if opcion==1: #exito
        redirect(url('/AsignaturaAll') + '#exitoupdate')
    if opcion == 2:          #error en ingreso
        redirect(url('/AsignaturaAll') + '#errorupdate')


#===========  Eliminar    ===========
@route('/Profesor/Eliminar/<id>')
def profesorEliminar(id):
    opcion=ProfesorDelete(id)
    if opcion==1: #exito
        redirect(url('/ProfesorAll') + '#exitoborrar')
    if opcion == 2:          #error en ingreso
        redirect(url('/ProfesorAll') + '#errorborrar')

@route('/Asignatura/Eliminar/<id>')
def asignaturaEliminar(id):
    opcion=AsignaturaDelete(id)
    if opcion==1: #exito
        redirect(url('/AsignaturaAll') + '#exitoborrar')
    if opcion == 2:          #error en ingreso
        redirect(url('/AsignaturaAll') + '#errorborrar')

@route('/Alumno/Eliminar/<id>')
def asignaturaEliminar(id):
    opcion=AlumnoDelete(id)
    if opcion==1: #exito
        redirect(url('/AlumnoAll') + '#exitoborrar')
    if opcion == 2:          #error en ingreso
        redirect(url('/AlumnoAll') + '#errorborrar')

#===========    Crear     ===========
@route('/Profesor/Nuevo')
def profesoresCrear():
    return template('ProfesorNueva')

@route('/profesornuevo', method="POST")
def process():
    obj=[]
    nombre = request.forms.get('nombre')
    apellido = request.forms.get('apellido')
    curso = request.forms.get('curso')
    rut = request.forms.get('rut')
    obj.append(nombre)
    obj.append(apellido)
    obj.append(curso)
    obj.append(rut)
  
    opcion=ProfesorCreate(obj)
    if opcion==1: #exito
        redirect(url('/Profesor/Nuevo') + '#exito')
    if opcion == 2:          #error en ingreso
        redirect(url('/Profesor/Nuevo') + '#error')
    if opcion ==3:  #error de nrc
        redirect(url('/Profesor/Nuevo') + '#errornrc')
        
    return template('ProfesorNueva')

@route('/Alumno/Nuevo')
def profesoresCrear():
    return template('AlumnoNueva')

@route('/alumnonuevo', method="POST")
def process():
    obj=[]
    nombre = request.forms.get('nombre')
    apellido = request.forms.get('apellido')
    curso = request.forms.get('curso')
    rut = request.forms.get('rut')
    obj.append(nombre)
    obj.append(apellido)
    obj.append(curso)
    obj.append(rut)
  
    opcion=AlumnoCreate(obj)
    if opcion==1: #exito
        redirect(url('/Alumno/Nuevo') + '#exito')
    if opcion == 2:          #error en ingreso
        redirect(url('/Alumno/Nuevo') + '#error')
    if opcion ==3:  #error de nrc
        redirect(url('/Alumno/Nuevo') + '#errornrc')
        
    return template('AlumnoNueva')

@route('/Asignatura/Nueva')
def asignaturaCrear():
    return template('AsignaturaNueva')

@route('/', method="POST")
def process():
    obj=[]
    nombre = request.forms.get('nombre')
    semestre = request.forms.get('semestre')
    carrera = request.forms.get('carrera')
    nrc = request.forms.get('nrc')
    obj.append(nombre)
    obj.append(semestre)
    obj.append(carrera)
    obj.append(nrc)
  
    opcion=AsignaturaCreate(obj)
    if opcion==1: #exito
        redirect(url('/Asignatura/Nueva') + '#exito')
    if opcion == 2:          #error en ingreso
        redirect(url('/Asignatura/Nueva') + '#error')
    if opcion ==3:  #error de nrc
        redirect(url('/Asignatura/Nueva') + '#errornrc')
        
    return template('AsignaturaNueva')



#===========   Rutas Estaticas   ===========
@route('/staticjs/<filename>')
def server_static(filename):
    return static_file(filename,root='./js')
@route('/staticss/<filename>')
def server_static(filename):
    return static_file(filename,root='./css')


if __name__== '__main__':
    run(debug=True, reloader=True)