from django import forms

from auth_exercise.web.models import Article


class ArticleBaseForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
