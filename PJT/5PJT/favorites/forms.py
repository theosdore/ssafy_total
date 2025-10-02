from django import forms
from .models import FavoriteCompany
class FavoriteCompanyForm(forms.ModelForm):
    class Meta:
        model = FavoriteCompany
        # fields = '__all__'
        fields = [
          'company_name', 'super_fav'
        ]