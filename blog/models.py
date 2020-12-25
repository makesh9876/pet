from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse






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
class Blog(models.Model):
	title=models.CharField(max_length=100,unique=True)
	slug=models.SlugField(max_length=300,unique=True)
	author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog')
	updated_on=models.DateTimeField(auto_now=True)
	image=models.ImageField(null=True, blank=True,upload_to='uploads/',default='static/img/a.jpg')

	description=models.CharField(max_length=300,blank=True)
	stitle=models.CharField(max_length=100,blank=True)
	content=models.TextField(blank=True)
	stitle=models.CharField(max_length=100,blank=True)
	content=models.TextField(blank=True)
	stitle1=models.CharField(max_length=100,blank=True)
	content1=models.TextField(blank=True)
	stitle2=models.CharField(max_length=100,blank=True)
	content2=models.TextField(blank=True)
	stitle3=models.CharField(max_length=100,blank=True)
	content3=models.TextField(blank=True)
	stitle4=models.CharField(max_length=100,blank=True)
	content4=models.TextField(blank=True)
	stitle5=models.CharField(max_length=100,blank=True)
	content5=models.TextField(blank=True)
	stitle6=models.CharField(max_length=100,blank=True)
	content6=models.TextField(blank=True)
	created_on=models.DateTimeField(auto_now_add=True)
	status=models.IntegerField(choices=STATUS, default=0)



	class Meta:
		ordering=['-created_on']

	
	def __str__(self):
		return self.title



class UserBlog(models.Model):
	title=models.CharField(max_length=100,unique=True)
	author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userblog')
	updated_on=models.DateTimeField(auto_now=True)

	description=models.CharField(max_length=300,blank=True)
	stitle=models.CharField(max_length=100,blank=True)
	content=models.TextField(blank=True)
	stitle=models.CharField(max_length=100,blank=True)
	content=models.TextField(blank=True)
	stitle1=models.CharField(max_length=100,blank=True)
	content1=models.TextField(blank=True)
	stitle2=models.CharField(max_length=100,blank=True)
	content2=models.TextField(blank=True)
	stitle3=models.CharField(max_length=100,blank=True)
	content3=models.TextField(blank=True)
	stitle4=models.CharField(max_length=100,blank=True)
	content4=models.TextField(blank=True)
	stitle5=models.CharField(max_length=100,blank=True)
	content5=models.TextField(blank=True)
	stitle6=models.CharField(max_length=100,blank=True)
	content6=models.TextField(blank=True)
	created_on=models.DateTimeField(auto_now_add=True)
	status=models.IntegerField(choices=STATUS, default=0)

	class Meta:
		ordering=['-created_on']

	
	def __str__(self):
		return self.title



