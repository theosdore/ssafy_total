from django.db import models

# Create your models here.
class FavoriteCompany(models.Model):
	nickname = models.ForeignKey('accounts.User',  on_delete=models.CASCADE)
	company_name = models.CharField(max_length=100)
	create_at= models.DateTimeField(auto_now_add=True)
	super_fav = models.BooleanField(default=False)
	