from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
ADULTHELP = (
    ('Y', 'Yes'),
    ('N', 'No')
)
class Word(models.Model):
    GRADE_CHOICES = [(i, str(i)) for i in range(0, 13)]
    
    word = models.CharField(max_length=50)
    color = models.CharField(max_length=20, default='green')
            
    grade = models.IntegerField(
        choices=GRADE_CHOICES,
        default=1
    )
    
    def __str__(self):
        return self.word
    def get_absolute_url(self):
        return reverse('word-detail', kwargs={'pk': self.id})
    
class Speller(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    grade = models.IntegerField()
    words = models.ManyToManyField(Word)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('speller-detail', kwargs={'speller_id': self.id})
    
class Study(models.Model):
    WORD_CHOICES = [(i, str(i)) for i in range(0, 101)]
    
    date = models.DateField('Study Date')
    minutes = models.IntegerField()
    numberofwords = models.IntegerField(
        choices=WORD_CHOICES,  
        default=0  
    )
    speller = models.ForeignKey(Speller, on_delete=models.CASCADE)
    adulthelp = models.CharField(
        max_length=1,
        choices=ADULTHELP,
        default=ADULTHELP[0][0]
    )
   
    def __str__(self):
        return f"{self.minutes} minutes on {self.date}"
    
    class Meta:
        ordering = ['-date']

        
   