from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
    path('addingTwo', views.addTwo),
    path('anyNum', views.anyNumber),
    # path('anyNum/<int:anyNumber>', views.anyNumber)
]