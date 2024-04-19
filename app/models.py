from django.db import models

class VoiceRecording(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



# model pour ecouter le voice
class VoiceListening(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio_files/')
    transcription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



# model pour le texte
class Writing(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
