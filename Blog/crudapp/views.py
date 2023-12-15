from django.shortcuts import render, redirect
from blogapp.models import Post

# Create your views here.
def D_delete(request, pk):
    usr = Post.objects.get(pk=pk)
    usr.delete()
    return redirect('index.html')


