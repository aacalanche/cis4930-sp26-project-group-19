from django import forms
from .models import Game, Genre, Publisher


class GameForm(forms.ModelForm):
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all().order_by('name'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Select a Genre"
    )
    publisher = forms.ModelChoiceField(
        queryset=Publisher.objects.all().order_by('name'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Select a Publisher"
    )
    
    class Meta:
        model = Game
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter game title'}),
            'platform': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Nintendo Switch 2'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': '1947-01-01', 'max': '2026-12-31'}),
            'developer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Nintendo'}),
            'na_sales': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'eu_sales': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'jp_sales': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'other_sales': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'global_sales': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'critic_score': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'max': '100'}),
            'critic_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'user_score': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'max': '10'}),
            'user_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
        }