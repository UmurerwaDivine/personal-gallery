from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.divine= Image(name= 'sunset', description ='the sun', location ='kigali',category='wallpaper')
        #Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.divine,Image))

    def test_save(self):
        self.blackish.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    def test_delete(self):
        self.new_image = Image(name= 'sunset', description ='the sun', location ='kigali',category='wallpaper')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.nature = Category(name = 'quote')

    def test_instance(self):
        self.assertTrue(isinstance(self.quote, Category))

    def test_save(self):
        self.quote.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)        

    def test_delete(self):
        self.new_category = Category(name = 'wallpaper')
        self.new_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0) 
class LocationTestClass(TestCase):    
    def setUp(self):
        self.Rwanda = Location(name = 'Rwanda')

    def test_instance(self):
        self.assertTrue(isinstance(self.Rwanda, Location))

    def test_save(self):
        self.Rwanda.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete(self):
        self.new_location = Location(name = 'Kigali')
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)


