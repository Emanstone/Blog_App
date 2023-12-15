from django.urls import path
from .views import Blog_post, Blog_Details, Category_list 
# from crudapp.views import D_delete

urlpatterns = [
    path("", Blog_post.as_view(), name='home'),
    path('details_blog/<int:pk>', Blog_Details.as_view(), name='details'),
    path('cat/<slug:category_slug>', Category_list.as_view(), name='category'),
    # path('D_delete/<int:pk>', D_delete, name='delete')
    
]

