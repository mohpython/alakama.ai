from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import VoiceRecording, VoiceListening
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, "index.html")


def voice_recorder(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio_file')
        if audio_file:
            fs = FileSystemStorage()
            filename = fs.save(audio_file.name, audio_file)
            return JsonResponse({'message': 'Enregistrement vocal sauvegardé avec succès.'})
        else:
            return JsonResponse({'message': 'Aucun fichier audio n\'a été reçu.'}, status=400)
    else:
        return render(request, "voice_recorder.html")


def voice_listening(request):
    phrase = VoiceListening.objects.first()  # Récupérer la première phrase pour l'exemple
    return render(request, "voice_listening.html", {'phrase': phrase})

def play_audio(request, pk):
    phrase = get_object_or_404(VoiceListening, pk=pk)
    audio_url = phrase.audio_file.url
    return JsonResponse({'audio_url': audio_url})


def writing(request):
    return render(request, "writing.html")

def send_text(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_text', '')
        return JsonResponse({'message': 'Texte envoyé avec succès.', 'user_text': user_text})
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)



