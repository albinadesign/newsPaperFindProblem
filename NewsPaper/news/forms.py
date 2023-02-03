from django import forms
from .models import Post


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['author', 'postCategory', 'title', 'text']

   def clean(self):
       cleaned_data = super().clean()
       return cleaned_data
