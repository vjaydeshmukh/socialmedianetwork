from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.LoginView, name='login'),
    path('logout/',views.LogoutView, name='logout'),
    path('signup/',views.SignupView, name='signup'),
    path('<str:pk>/Edit/',views.EditProfileView, name='edit'),
    path('<str:pk>/Editimg/',views.EditProImgView, name='editimg'),
    path('<str:pk>/',views.ProfileView, name='profile'),
    path('<str:pk>/follow/', views.FollowView , name='follow'),
    path('<str:pk>/cancel/', views.CancelView , name='cancel'),
]