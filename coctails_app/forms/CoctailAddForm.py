from django import forms

class CoctailAddForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nazwa koktajlu')
    category = forms.CharField(max_length=100, label='Kategoria')
    instructions = forms.CharField(widget=forms.Textarea, label='Instrukcje')
    is_alcoholic = forms.BooleanField(required=False, label='Czy alkoholowy?')