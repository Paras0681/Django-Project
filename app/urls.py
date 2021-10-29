from django import views
from django.urls import path
from app.views import login, register, logout, report , HomeView, Saved_View, Sent_View

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('report/', report, name='report'),
    path('saved_incidents/', Saved_View.as_view(), name='saved_incidents')
]
