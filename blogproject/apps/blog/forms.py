from django import forms
from apps.blog.models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','content','image']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write content'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }