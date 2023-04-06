from django.urls import path
from app import views
urlpatterns = [
    path('',views.index),
    path('create/',views.create),
    path('update/<int:id>/',views.update , name='update'),
    path('delete/<int:id>/',views.delete ,name='delete')
]
