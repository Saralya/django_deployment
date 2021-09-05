from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
    #main project folder er urls.py e amra sob app er urls likhte gele onek complicated hoye jabe
    #tai proti ta app er jonno alada urls.py banabo and segula k ekhane include kore dibo
    path('login_app/', include('login_app.urls')),
]
