
from django.contrib import admin
from django.urls import path, include
from app import views as hv


from app.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", hv.home, name="home"),
    path("voice_recorder/", hv.voice_recorder, name="voice_recorder"),
    path("voice_listening/", hv.voice_listening, name="voice_listening"),
    path('play_audio/<int:pk>/', hv.play_audio, name='play_audio'),
    path("writing/", hv.writing, name="writing"),
    path('send_text/', hv.send_text, name='send_text')

]
