
from django.contrib import admin
from django.urls import path, include
from app import views as hv


from app.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hv.home, name="home"),
    path("voice_recorder/", hv.voice_recorder, name="voice_recorder"),
    path("voice_listening/", hv.voice_listening, name="voice_listening"),
    path("writing/", hv.writing, name="writing")

]
