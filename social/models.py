from django.db import models
from django.db.models import Count

# Create your models here.
from django.contrib.auth.models import User

class Posts(models.Model):
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=400)
    image=models.ImageField(upload_to="images",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)

    def post_comment(self):
        qs=self.comments_set.all().annotate(u_count=Count('likes')).order_by('-u_count')
        return qs


    def __str__(self):
        return self.title



class Comments(models.Model):
    
    comments=models.CharField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name="likes")

    def __str__(self):
        return self.comments

    @property
    def likedby(self):
        return self.likes.all().count()    