from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Curso
from inicio.forms import cursoFormulario, cursoBusquedaFormulario

# Create your views here.

def inicio (request) :
    
    datos = {
        "fecha" : datetime.now() 
        }
  
        

    
    #v1 
   # archivo = open(r'inicio\templates\inicio.html', 'r') 
   # template = Template(archivo.read()) 
   # archivo.close()
   # contexto = Context(datos)
   # template_renderizado = template.render(contexto)
   # return HttpResponse(template_renderizado)
    
    #v2 
    
   # template = loader.get_template(r'inicio\inicio.html')
   # template_renderizado = template.render(datos)
   # return HttpResponse(template_renderizado)

#v3 
    return render(request , r'inicio\inicio.html' , datos)
  
#def crear_curso(request, titulo, numero) :
    
 #   curso = Curso(titulo=titulo, numero=numero)
  #  curso.save()
    
  #  return render(request, r'inicio\curso_creado.html', {})
  
def crear_curso(request) :
  
    if request.method == 'POST' :
        formulario = cursoFormulario(request.POST)
        if formulario.is_valid(): 
            data= formulario.cleaned_data
            curso = Curso(titulo=data.get('titulo'), numero=data.get('numero'))
            curso.save()
        else : 
            return render(request, r'inicio\crear_curso.html', {'formulario' : formulario})
            
    formulario = cursoFormulario()
    return render(request, r'inicio\crear_curso.html', {'formulario' : formulario})



def listado_cursos(request) :
  

    formulario = cursoBusquedaFormulario(request.GET)
    if formulario.is_valid(): 
      titulo_a_buscar= formulario.cleaned_data.get('titulo')
      cursos_encontrados = Curso.objects.filter(titulo__icontains=titulo_a_buscar)

    else : 
         cursos_encontrados = Curso.objects.all()
            
    formulario = cursoBusquedaFormulario()
    return render(request, r'inicio\listado_cursos.html', {'formulario' : formulario, 'cursos_encontrados' : cursos_encontrados})