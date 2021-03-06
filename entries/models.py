from django.db import models

# Create your models here.
class Entries(models.Model):
    title = models.CharField(max_length=50,null=True)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 'My Diary Entry #{}'.format(self.id)
    
    class Meta:
        verbose_name_plural = 'Entries'