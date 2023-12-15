from django.urls import path
from .views import Signup, Login, Logout, ProfilePage, EditProfilePage, BecomeAuthor, AuthorProfile


urlpatterns = [
    path("", Signup.as_view(), name='signup'),
    path("login/", Login.as_view(), name='login'),
    path("logout/", Logout, name='logout'),
    path("propage/", ProfilePage.as_view(), name='profiler'),
    path("proedit/", EditProfilePage.as_view(), name='editpro'),
    path("become/", BecomeAuthor.as_view(), name='beauthor'),
    path("authorpro/<int:pk>/", AuthorProfile.as_view(), name='aprofile'),
]

