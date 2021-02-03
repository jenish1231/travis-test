from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndeView.as_view()),
    path("ws/", views.websocket_view),
    #asdf
]
