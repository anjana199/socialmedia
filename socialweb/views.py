from django.shortcuts import render,redirect
from socialweb.forms import PostForm,UserRegistrationForm,LoginForm
from django.views.generic import View,CreateView,ListView,FormView,TemplateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from social.models import Posts,Comments
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kw) 
    return wrapper    
           
decs=[signin_required,never_cache]


class SignupView(CreateView):
    template_name="register.html"
    form_class=UserRegistrationForm
    model=User
    success_url=reverse_lazy("signin")
    
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"Registration Successfull")
        return super().form_valid(form)
  
    
class SigninView(FormView):
    template_name="login.html"
    form_class=LoginForm
   
    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                messages.error(request,"invalid credentials")
                print("invalid")
                return render(request,self.template_name,{"form":form})    

@method_decorator(decs,name="dispatch")
class PostAddView(CreateView):
    template_name="addpost.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("index")

    def form_valid(self, form): 
        form.instance.user=self.request.user
        messages.success(self.request,"Post created")
        return super().form_valid(form)  

@method_decorator(decs,name="dispatch")
class IndexView(CreateView,ListView,DeleteView):
    template_name="index.html"
    form_class=PostForm
    success_url=reverse_lazy("index")
    model=Posts
    context_object_name="posts"
  

              

    # def form_valid(self,form):
    #     form.instance.user=self.request.user
    #     messages.success(self.request,"your post is added")
    #     return super().form_valid(form)
                    
    def get_queryset(self):
        return Posts.objects.order_by("-created_date")       
decs
def post_delete_view(request,*args,**kw):
    id=kw.get("id")
    qs=Posts.objects.get(id=id).delete()
    messages.success(request,"Post has been deleted")
    return redirect("index")                     

decs                 
def add_comments(request,*args,**kw):
    id=kw.get("id")
    post=Posts.objects.get(id=id)
    comment=request.POST.get("comments")
    Comments.objects.create(post=post,comments=comment,user=request.user)
    return redirect("index")

def comment_like(request,*args,**kw):
    id=kw.get("id")
    comment=Comments.objects.get(id=id)
    comment.likes.add(request.user)
    return redirect("index")

decs
def comment_delete_view(request,*args,**kw):
    id=kw.get("id")
    qs=Comments.objects.get(id=id).delete()
    messages.success(request,"comment has been deleted")
    return redirect("index") 

decs
def signout_view(request,*args,**kw):
    logout(request)
    return redirect("signin")

