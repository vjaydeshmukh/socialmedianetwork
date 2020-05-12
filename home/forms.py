from django import forms
from .models import Comments  , Post
from django.contrib.auth.models import User


post_type = (
    ('F','FEED'),
    ('S','STORY')
)

class CommentsForm(forms.Form):
        post_comment = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={
            'class':'comment',
            'border':'none',
            'background':'transparent',
            'outline':'none',
            'placeholder':'add comment',

        }))



class NewPostForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'id':'image',
        'class':'image_field',
        }))
    discription = forms.CharField(max_length=100, required = False,widget=forms.TextInput(attrs={
        'class':'new_post_input',
        'placeholder':'What\'s in your mind'
    }) )

    post_type = forms.ChoiceField(choices=post_type)
    

class PostEditForm(forms.ModelForm):
    discription = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={
            'class':'discription',
        }))
    class Meta:
        model = Post
        fields = 'discription',
