from django import forms
from .models import Comment


# https://docs.djangoproject.com/en/4.2/ref/forms/fields/#module-django.forms.fields
class EmailPostForm(forms.Form):

    name = forms.CharField(max_length=25)  # имя отправившего пост
    email = forms.EmailField()  # электронная почта отправителя
    to = forms.EmailField()  # электронная почта получателя
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)  # поле комментариев


class CommentForm(forms.ModelForm):
    """
    #https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
    """
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
