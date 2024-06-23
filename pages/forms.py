from django import forms
from .models import Comment


# Definir formulario para añadir comentarios, se usa modelo Comment para crear el formulario
# y se especifica que solo se mostrará el campo text
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


# Definir formulario para tener configuracion del usuario en la aplicacion
class ConfigForm(forms.Form):
    commenter_name = forms.CharField(max_length=255, label='Nombre del comentarista')
    font_size = forms.ChoiceField(choices=[('small', 'Pequeña'), ('medium', 'Mediana'), ('large', 'Grande')],
                                  label='Tamaño de la letra')
    font_type = forms.ChoiceField(choices=[('arial', 'Arial'), ('verdana', 'Verdana'), ('times', 'Times New Roman')],
                                  label='Tipo de letra')
