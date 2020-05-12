from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('post/<str:pk>/comment/', views.AddCommentView , name='comment'),
    path('post/<str:pk>/like/', views.LikeAndDislikeView , name='like'),
    path('explore/', views.exploreView, name='explore'),
    path('search/', views.SearchView, name='search'),
    path('story/<str:pk>/', views.StoriesDetiels, name='story'),
    path('addpost/', views.AddPostView, name='addpost'),
    path('deletepost/<str:pk>/', views.DeletPostView, name='deletepost'),
    path('editepost/<str:pk>/', views.EditPostView, name='editepost'),
    path('resetpassword/',auth_views.PasswordResetView.as_view(template_name='home/reset.html'), name='reset_password'),
    path('resetpasswordsent/',auth_views.PasswordResetDoneView.as_view(template_name='home/resetsent.html'), name='password_reset_done'),
    path('resetpassword/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='home/resetconf.html'), name='password_reset_confirm'),
    path('resetpasswordcompete/',auth_views.PasswordResetCompleteView.as_view(template_name='home/resetcomplete.html'), name='password_reset_complete'),


]