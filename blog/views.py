from rest_framework.views import APIView
from rest_framework import viewsets

from django.shortcuts import render
from .models import Post
from django.shortcuts import render
from django.db.models import Count
from .serializers import PostSerializer
from .models import User
# Create your views here.



# def active_users(rquest):
#     users = User.objects.annotate(post_count=Count('post')).filter(post_count__gt=5)
#     return render(request,'blog/users.html',{'users':users})



# APIView

# class ProductList(APIView):
    
#     def get(self,request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts,many =true)
#         return Response(serializer.data)



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    