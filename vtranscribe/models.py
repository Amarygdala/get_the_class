from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True,
                                 verbose_name="")

    def str(self):
        return str(self.videofile)