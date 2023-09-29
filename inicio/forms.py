from django import forms

class cursoFormulario(forms.Form) :
    titulo = forms.CharField(max_length=50) 
    numero = forms.IntegerField()
    
class cursoBusquedaFormulario(forms.Form) :
    titulo = forms.CharField(max_length=50, required=False) 

         
    