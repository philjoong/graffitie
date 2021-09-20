from django import forms
from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all())

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']



class ArticleUpdateForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left'}))
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']