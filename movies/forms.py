from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    COMIC = "코미디"
    HOROR = '공포'
    ROMANCE = '로맨스'
    GENRE_CHOICES = [
        (COMIC, 'comedy'),
        (HOROR, 'horor'),
        (ROMANCE, 'romance'),
    ]
        
    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
    )
    
    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
            'min':0,
            'max':5,
            'step':0.5
            }
        )
    )
    
    realease_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type' : 'date'
            }
        )
    )

    
    
    class Meta:
        model = Movie
        fields = '__all__'