from django.shortcuts import render
from django.http import JsonResponse
from .models import VoiceRecording
from . import views as hv


def home(request):
    return render(request, "index.html")


def voice_recorder(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio_file')
        if audio_file:
            title = 'Voice Recording'
            voice_recording = VoiceRecording.objects.create(title=title, audio_file=audio_file)
            return JsonResponse({'message': 'Enregistrement vocal sauvegardé avec succès.'})
        else:
            return JsonResponse({'message': 'Aucun fichier audio n\'a été reçu.'}, status=400)
    else:
        return render(request, "voice_recorder.html")


def voice_listening(request):
    return render(request, "voice_listening.html")


def writing(request):
    return render(request, "writing.html")
