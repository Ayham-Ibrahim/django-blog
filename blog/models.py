from django.db import models

# Create your models here.


# class User(models.Model):
#     username = models.CharField(max_length=255)
    
    
# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     bio = models.TextField()


# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     user = models.ForeignKey(User,related_name='post',on_delete=models.CASCADE)



class Category(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)