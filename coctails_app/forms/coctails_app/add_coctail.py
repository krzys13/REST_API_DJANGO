from django import forms

class AddCocktailForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nazwa')
    instructions = forms.CharField(widget=forms.Textarea, label='Instructios')
    is_alcoholic = forms.BooleanField(required=False, label='Is with an alcohol?')