from django.core.validators import RegexValidator

isValidApiKey = RegexValidator(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$', message='The API key entered contains invalid characters', code='Invalid API Key')