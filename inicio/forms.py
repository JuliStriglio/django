from django import forms

class cursoFormularioBase(forms.Form) :
    titulo = forms.CharField(max_length=50) 
    numero = forms.IntegerField()
    
class crearCursoFormulario(cursoFormularioBase):
    ...
class editarCursoFormulario(cursoFormularioBase):
    ...
class cursoBusquedaFormulario(forms.Form) :
    titulo = forms.CharField(max_length=50, required=False) 

         
    