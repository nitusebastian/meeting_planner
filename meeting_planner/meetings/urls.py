from meetings.views import detail, rooms_list
from django.urls import path

urlpatterns = [
    path('<int:id>', detail, name="detail"),
    path('', rooms_list, name="rooms"),
]