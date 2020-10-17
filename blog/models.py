from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=50)
    chead0= models.CharField(max_length=5000)
    head1 = models.CharField(max_length=50)
    chead1= models.CharField(max_length=5000)
    head2 = models.CharField(max_length=50)
    chead2= models.CharField(max_length=5000)
    pub_date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title
    
