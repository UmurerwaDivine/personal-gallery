from django.db import models

# Create your models here.



class Location(models.Model):
    name = models.CharField(max_length =30)

    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()
    
    def update_location(self, update):
        self.location = update
        self.save()

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length =30)

    def save_category(self):
        self.save()
       

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.category = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/s',blank=False)
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
    def get_image_by_id(cls,image_id):
        images= Image.objects.get(id=image_id)
        return images
    
    @classmethod
    def search_image(cls,search_category):
        category = Image.objects.filter(category__category_icontains=search_category)
        return category
    

    @classmethod
    def filter_by_location(cls, filter_location):
        location = Image.objects.filter(location__id=filter_location)
        return location   
    
    # @classmethod
    # def get_image_by_id(cls,id):
    #     images = cls.objects.filter(Location = location)


   
