from django import forms

def validate_a(data):
    if data.lower().startswith('a') or len(data)<5:
        raise forms.ValidationError('not valide')

class SchoolForm(forms.Form):
    sname=forms.CharField(validators=[validate_a])
    sprincipal=forms.CharField()
    sloc=forms.CharField()
    Semail=forms.EmailField()
    SreenterEmail=forms.EmailField()
    def clean(self):
        
        Se=self.cleaned_data['Semail']
        Sr=self.cleaned_data['SreenterEmail']
        if Sr != Se:
            raise forms.ValidationError('not valid')
