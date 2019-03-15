from django.db import models

# Create your models here.



class Location(models.Model):
    name = models.CharField(max_length =30)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/',blank=False)
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =60)
    location = models.ForeignKey(Location,blank=True)
    category= models.ForeignKey(Category)

    def save_image(self):
        self.save()

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
    @classmethod
    def one_image(cls,id):
        images = Image.objects.all()
        # location = cls.objects.filter(Image = images)
        return images
    @classmethod
    def filter_location(cls,location):
        location = cls.objects.filter(Location = location)
        return location
    @classmethod
    def search_by_category(cls,search_term):
        category = cls.objects.filter(category__icontains=search_term)
        return category  

