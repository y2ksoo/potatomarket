from django.db import models

class BasicModel(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class Category(BasicModel):
    
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["created"]
    
    def __str__(self):
        return self.name


# class Photo(BasicModel):

#     caption = models.CharField(max_length=80)
#     file = models.ImageField(upload_to="ware_photos")
#     wares = models.ForeignKey(
#         "Ware", related_name='photos', on_delete=models.CASCADE, blank=True
#         )

#     def __str__(self):
#         return self.caption


class Ware(BasicModel):
    
    name = models.CharField(max_length=140)
    photo = models.ImageField(upload_to="ware_photos")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    city = models.CharField(max_length=80)
    seller = models.ForeignKey("users.User", related_name="ware", on_delete=models.CASCADE)
    category = models.ManyToManyField("Category", related_name="ware", blank=True)

    def __str__(self):
        return self.name

    def count(self):
        return self.count
