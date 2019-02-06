from django import forms
from validators import isValidApiKey

class APIKeySubmit(forms.Form):
    apikey = forms.CharField(label='API Key', max_length=36, validators=[isValidApiKey], required=True)#, initial='XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX')
