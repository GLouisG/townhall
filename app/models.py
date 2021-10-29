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