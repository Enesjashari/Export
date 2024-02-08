from django.db import models
from datetime import datetime,timedelta
from embed_video.fields import EmbedVideoField


# Create your models here.
import os
class Pytje(models.Model):
    EmriMbiemri = models.CharField(max_length = 1000)
    NumriTelefonit = models.CharField(max_length = 1000)
    Email = models.CharField(max_length = 1000)
    Pytja = models.TextField(max_length = 1000)
    Ju_kam_Pergjigjur = models.BooleanField(blank=True, default = False)

    def __str__(self):
        return f'{self.EmriMbiemri} : {self.Pytja[:40]}'
    


current_time = datetime.now()

# Add one hour to the current time
new_time = current_time + timedelta(hours=1)
new_2 = new_time - timedelta(hours=1)
class Njoftime(models.Model):
    Titulli = models.CharField(max_length = 1000)
    Teksti = models.TextField(max_length = 100000)
    Foto  = models.ImageField(blank=True,default='media/images/No_image/No_image_available.png',upload_to = "images/")
    Data = models.DateTimeField(default=new_2, blank=True)

    def save(self, *args, **kwargs):
        # Check if the instance is being updated
        if self.pk:
            # Get the current instance from the database
            old_instance = Njoftime.objects.get(pk=self.pk)
            # Check if the Foto field has been modified or cleared
            if old_instance.Foto and self.Foto != old_instance.Foto:
                # Delete the old file associated with the Foto field
                if os.path.isfile(old_instance.Foto.path):
                    os.remove(old_instance.Foto.path)

        super(Njoftime, self).save(*args, **kwargs)
    def __str__(self):
        return f'[{self.Data.hour}:{self.Data.minute}:{self.Data.second}]  {self.Titulli.upper()} | {self.Teksti.capitalize()[:70]} . . .'
    

class Video(models.Model):
        Emri = models.CharField(max_length=  10000)
        Data = models.DateTimeField(default=new_2, blank=True)
        Video_Youtube = EmbedVideoField( blank=True , default=" ")  # same like models.URLField()

        def __str__(self):
            return f'{self.Emri}'