from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('register',views.register,name='register'),
    path('postj',views.post,name='postj'),
    path('job_single/<int:pk>/',views.job_single,name='job_single'),
    path('profile',views.profile,name='profile'),
    path('<int:pk>/apply_for_job',views.apply_for_job,name='apply_for_job'),
    path('application/<int:app_id>',views.view_application,name='view_application'),
    path('job/<int:id>',views.view_postedjob,name='view_postedjob')

]