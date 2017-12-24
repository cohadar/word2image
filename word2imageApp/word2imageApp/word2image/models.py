from django.db import models


class word2image(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=512)
    translation = models.CharField(max_length=512)
    pic1 = models.CharField(max_length=1024, blank=True)
    pic2 = models.CharField(max_length=1024, blank=True)
    pic3 = models.CharField(max_length=1024, blank=True)
    pic4 = models.CharField(max_length=1024, blank=True)
    approvedPic1 = models.BooleanField(default=False)
    approvedPic2 = models.BooleanField(default=False)
    approvedPic3 = models.BooleanField(default=False)
    approvedPic4 = models.BooleanField(default=False)
    lastUpdate = models.DateField()

    def __str__(self):
        return self.word

