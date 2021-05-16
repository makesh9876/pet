from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django.core.validators import RegexValidator
COLOR_CHOICES = (
 ('Andhra Pradesh','Andhra Pradesh'),	
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chhattisgarh','Chhattisgarh'),	
('Goa','Goa'),
('Gujarat','Gujarat'),	
('Haryana	','Haryana	'),
('Himachal','Himachal'), 
('Jharkhand','Jharkhand'),	
('Karnataka','Karnataka'),	
('Kerala','Kerala'),
('Madhya Pradesh','Madhya Pradesh'),	
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram aizawl','Mizoram aizawl'),	
('Nagaland','Nagaland'),
('Odisha','Odisha'),	
('Punjab	','Punjab	'),
('Rajasthan','Rajasthan'),	
('Sikkim	','Sikkim	',),
('Tamil Nadu','Tamil Nadu'),	
('Telangana','Telangana'),
('Tripura','Tripura	'),	
('Uttar Pradesh','Uttar Pradesh'),
('Uttarakhand ','Uttarakhand '),
('West Bengal','West Bengal')
)



class Dogs(models.Model):
	image=models.ImageField(upload_to ='uploads/')
	breed=models.CharField(max_length=100)
	description=models.TextField(max_length=300)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	location=models.CharField(max_length=30, choices=COLOR_CHOICES, default='green')
	created_on=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['-created_on']
	def __str__(self):
		return self.breed

class Req(models.Model):
	name=models.CharField(max_length=30)
	need=models.TextField(max_length=300)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	created_on=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['-created_on']

	def __str__(self):
		return self.name


class Message(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=70)
	subject=models.CharField(max_length=100)
	message=models.CharField(max_length=300)


	def __str__(self):
		return self.name



STATUS=(
	(0,"Draft"),
	(1,"Publish")
	)

class Test(models.Model):
	tit=models.CharField(max_length=10)
	content=models.TextField(blank=True)

	def __str__(self):
		return self.tit



