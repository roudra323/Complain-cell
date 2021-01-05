

from django.contrib import admin
from django.urls import path
from cell import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='todo'),
    path('com', views.index, name='conformation'),

]
