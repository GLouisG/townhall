from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User

from django.test import TestCase

from app.models import Neighbourhood, Posts, Profile, Business

# Create your tests here.
class UserProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="Johnny")
        self.profile = Profile(user=self.user, pic="test.jpg", about = "A description" )    

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
    def test_save(self):
        self.profile.save_profile()
        the_profile = Profile.objects.all()
        self.assertTrue(len(the_profile)>0)
    def test_delete(self):
        self.profile.save_profile()      
        self.profile.delete_profile()
        self.assertTrue(len(Profile.objects.all())==0)

class PostTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="Johnny")
        self.user.save()
        self.hood = Neighbourhood(name="abc", location="abcd", census = 1, contacts="abcde")
        self.hood.save()
        self.profile = Profile(user=self.user, pic="test.jpg", about = "A description", residence =self.hood )
        self.profile.save_profile()
        self.test_pos = Posts(content="test", owner=self.profile, neighbourhood=self.hood)  
        self.test_pos.save_post()  

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Posts.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_delete(self):     
        self.test_pos.delete_post()
        self.assertTrue(len(Posts.objects.all())==0) 

class BusinessTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Johnny")
        self.user.save()
        self.hood = Neighbourhood(name="abc", location="abcd", census = 1, contacts="abcde")
        self.hood.save()
        self.profile = Profile(user=self.user, pic="test.jpg", about = "A description", residence =self.hood )
        self.profile.save_profile()
        self.test_pos = Posts(content="test", owner=self.profile, neighbourhood=self.hood)  
        self.test_pos.save_business()  

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Business.objects.all().delete()
        Neighbourhood.objects.all().delete()

    def test_delete(self):     
        self.test_pos.delete_business()
        self.assertTrue(len(Posts.objects.all())==0)     
    def test_find(self):
        img = Business.find_business(1)
        self.assertTrue(len(img)>0)         


class HoodTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="Johnny")
        self.user.save()
        self.hood = Neighbourhood(name="abc", location="abcd", census = 1, contacts="abcde")
        self.hood.save()
        self.profile = Profile(user=self.user, pic="test.jpg", about = "A description", residence =self.hood )
        self.profile.save_profile() 

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Neighbourhood.objects.all().delete()
    def test_delete(self):     
        self.hood.delete_neighbourhood()
        self.assertTrue(len(Neighbourhood.objects.all())==0)         