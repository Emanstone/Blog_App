from django.urls import path
from .views import Create_userpost, Edit_userpost, Delete_userpost, Pendingpage, ApprovePost, UnapprovePost, Comments


urlpatterns = [
    path("", Create_userpost.as_view(), name='createpost'),
    path("editpost/<int:pk>/", Edit_userpost.as_view(), name='editor'),
    path("penpager/<int:pk>/", Pendingpage.as_view(), name='penpage'),
    path("deletapost/<int:pk>/", Delete_userpost.as_view(), name='deleta'),
    path("approvepost/<int:pk>/", ApprovePost.as_view(), name='approver'),
    path("unapprovepost/<int:pk>/", UnapprovePost.as_view(), name='unapprover'),
    path("commen/<int:pk>/", Comments.as_view(), name='commentas'),
    # path("engage/<int:pk>", engage, name='engagers'),
    # path("delpager/", delete_page, name='delpage'),  
]