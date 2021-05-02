from django import forms

from vtranscribe.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["name", "videofile"]
