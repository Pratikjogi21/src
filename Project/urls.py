
from django.contrib import admin
from django.urls import path
from App.views import home,add,delete,viewone,edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('add',add),
    path('delete/<int:id>',delete),
    path('viewone/<int:id>',viewone),
    path('edit/<int:id>',edit)
]
