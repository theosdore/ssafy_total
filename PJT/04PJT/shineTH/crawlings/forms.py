from django import forms
from .models import Comment, Analyst

class GetComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nickname','content', 'post_time', 'ttabong','ZZal','company_name','company_code']