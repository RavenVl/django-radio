from django.urls import path
from .views import AudioStreamingView

urlpatterns = [
    # ...
    path('stream/', AudioStreamingView.as_view(), name='audio_stream'),
    # ...
]

