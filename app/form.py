from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import List,Card,Comment

class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ("username","last_name","first_name","email")


class ListForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = List
        fields = ("title",)


class CardForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Card
        fields = ("title", "description", "list")


class CardCreateForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ("title", "description")


class CardCreateFromHomeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CardCreateFromHomeForm, self).__init__(*args,**kwargs)
        for field_name, field in  self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Card
        fields = ("title","description")


class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)
        for field_name, field in  self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    

    class Meta:
        model = Comment
        fields = ("description",)
