from django import forms
from tag.models import Repository

class RepositoryForm(forms.Form):
    repo_name=forms.CharField(label='Repository Name', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control col-sm-8','Placeholder':"Repository Name"}))
    repo_url = forms.CharField(label='Repository Url', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control col-sm-8','Placeholder':"Repository URL"}))
    development = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control col-sm-4 small','Placeholder':"Development"}))
    release = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control col-sm-4 small','Placeholder':"Release"}))


