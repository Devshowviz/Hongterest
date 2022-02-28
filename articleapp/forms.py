from django.forms import ModelForm, forms
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="게시판을 선택하세요", required=False)
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']