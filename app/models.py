from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Neighbourhood(models.Model):
      name = models.CharField(max_length=80)
      location = models.CharField(max_length=250)
      # resident = models.ForeignKey('User', on_delete=models.CASCADE)
      census = models.PositiveIntegerField(default=0)
      contacts = models.CharField(max_length=250)
      image = models.ImageField(upload_to = 'hood/', default='scene.jpg')
      def __str__(self):
            return f'Neighbourhood {self.name}'  
      def create_neigbourhood(self):
            self.save()

      def delete_neigbourhood(self):
            self.delete()         
      def update_neighbourhood(self, new_img, cont):
            try:
                  self.image = new_img
                  self.contacts = cont
                  self.save()
                  return self
            except self.DoesNotExist:
                  print('Neighbourhood not found')                

class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      residence =   models.ForeignKey('User', on_delete=models.CASCADE)
      about = models.CharField(max_length=250)
      def __str__(self):
            return f'Profile {self.about}' 
      def create_profile(self):
            self.save()
      def delete_profile(self):
            self.delete()   

class Business(models.Model):
      name = models.CharField(max_length=80) 
      description = models.CharField(max_length=250)
      residence = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
      owner = models.ForeignKey(Profile, on_delete=models.CASCADE)       
      email = models.EmailField()
      def __str__(self):
            return f'Business {self.name}'  
      def create_business(self):
            self.save()

      def delete_business(self):
            self.delete()  
      def update_business(self, new_name, new_description):
            try:
                  self.name = new_name
                  self.description = new_description
                  self.save()
                  return self
            except self.DoesNotExist:
                  print('Business not found')
      @classmethod              
      def find_business(cls, name):
          businesses = cls.objects.filter(name__contains = name)  
          return businesses
      @classmethod              
      def find_businesses(cls, id):
          businesses = cls.objects.filter(id = id)  
          return businesses 

class Posts(models.Model):
      owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
      content = models.CharField(max_length=200)
      residence = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
      def __str__(self):
            return f'Posts {self.content}'
                      