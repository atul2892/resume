from django.db import models
from ckeditor.fields import RichTextField


class Users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    username=models.CharField(max_length=100,default='',null=True,blank=True)
    email=models.EmailField(default='',null=True,blank=True)
    phone=models.CharField(max_length=10,default='',null=True,blank=True)
    address=models.CharField(max_length=100,default='',null=True,blank=True)
    city=models.CharField(max_length=100,default='',null=True,blank=True)
    state=models.CharField(max_length=100,default='',null=True,blank=True)
    pin=models.CharField(max_length=100,default='',null=True,blank=True)
    password=models.CharField(max_length=100,default='',null=True,blank=True)
    otp=models.IntegerField(default=9241,null=True,blank=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    
    def __str__(self):
        return str(self.username)+" "+self.email
    
class Resume(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,default='',null=True,blank=True)
    
    name=models.CharField(max_length=200,default='',null=True,blank=True)
    email=models.EmailField(default='',null=True,blank=True)
    phone=models.CharField(max_length=10,default='',null=True,blank=True)
    address=models.CharField(max_length=100,default='',null=True,blank=True)
    image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    education=RichTextField(default='',null=True,blank=True)
    skills=RichTextField(default='',null=True,blank=True)
    internship=RichTextField(default='',null=True,blank=True)
    experience=RichTextField(default='',null=True,blank=True)
    project=RichTextField(default='',null=True,blank=True)
    video=models.FileField(upload_to="uploads",default='',null=True,blank=True)
            
    def __str__(self):
        return str(self.id)+"-- "+str(self.name)
