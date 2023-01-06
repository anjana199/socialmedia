from django.shortcuts import render
from social.serializers import UserSerializer,PostSerializer,CommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth.models import User
from social.models import Posts,Comments
from rest_framework import authentication,permissions
from rest_framework.decorators import action


class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class PostView(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Posts.objects.all
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    @action(methods=["GET"],detail=False)
    def my_posts(self,request,*args,**kw):
        qs=request.user.posts_set.all()
        serializer=PostSerializer(qs,many=True)
        return Response(data=serializer.data)

    
    @action(methods=["POST"],detail=True)
    def add_comments(self,request,*args,**kw):
        id=kw.get("pk")
        post=Posts.objects.get(id=id)    
        user=request.user
        serializer=CommentSerializer(data=request.data,context={"Posts":post,"user":user})
        if serializer.is_valid():
            serializer.save()
            return Response (data=serializer.data)
        else:
            return Response(data=serializer.errors)

    @action(methods=["GET"],detail=True)
    def list_comments(slef,request,*args,**kw):
        id=kw.get("pk")
        post=Posts.objects.get(id=id) 
        com=post.comments_set.all()
        serializer=CommentSerializer(com,many=True)
        return Response(data=serializer.data)


class CommentView(ModelViewSet):
    serializer_class=CommentSerializer
    queryset=Comments.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=["GET"],detail=True)
    def likes(self,requet,*args,**kw):
        comm=self.get_object()
        user=self.request.user
        comm.likes.add(user)
        return Response (data="liked")






        
   