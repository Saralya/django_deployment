from django.conf.urls import url
from django.urls import path
from first_app import views


app_name = "first_app"

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.index, name='index'),
    #path('contact/', views.contact, name='contact'),
    #path('about/', views.about, name='about'),
    #path('form/', views.form, name='form'),
    
    
    # for class based view
    path('home/', views.HomeView.as_view(), name='home'),
    path('content/', views.ContentView.as_view(), name='content'),
    path('musician_details/<pk>/', views.MusicianDetail.as_view(), name='musician_details'),
    path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
    path('musician_update/<pk>/', views.UpdateMusician.as_view(), name='musician_update'),
    path('musician_delete/<pk>/', views.DeleteMusician.as_view(), name='musician_delete'),
    
]
