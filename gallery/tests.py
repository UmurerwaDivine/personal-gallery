from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Image(name= 'sunset', description ='the sun', location ='kigali',category='wallpaper')
        #Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Image))