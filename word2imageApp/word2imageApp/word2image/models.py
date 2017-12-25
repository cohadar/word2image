from django.db import models


class Word2image(models.Model):
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

    @staticmethod
    def get_next_for_updating():
        sql_query = 'SELECT * FROM word2image_word2image WHERE '
        sql_query += '("approvedPic1" = FALSE OR "approvedPic2" = FALSE OR "approvedPic3" = FALSE OR "approvedPic4" = FALSE)'
        sql_query += 'ORDER BY "lastUpdate"'
        return Word2image.objects.raw(sql_query)

