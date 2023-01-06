from rest_framework import serializers
from django.contrib.auth.models import User
from social.models import Posts,Comments

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["email","username","password"]
        
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)    




class CommentSerializer(serializers.ModelSerializer):

    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    post=serializers.CharField(read_only=True)
    likedby=serializers.CharField(read_only=True)
    class Meta:
        model=Comments
        fields=["user","created_date","post","likes","likedby","comments"]            


    def create(self, validated_data):
        post=self.context.get("Posts") 
        usr=self.context.get("user")
        return Comments.objects.create(**validated_data,post=post,user=usr)
        # return post.comments_set.create(user=usr,**validated_data)


class PostSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    class Meta:
        model=Posts
        fields=["title",
                "description",
                "image",
                "user","created_date"]