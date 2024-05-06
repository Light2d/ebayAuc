from django.utils.translation import activate
from django.conf import settings

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        if language:
            lang = language.split(',')[0].lower()  # Приведем язык к нижнему регистру
            if lang in dict(settings.LANGUAGES).keys():
                activate(lang)
                request.LANGUAGE_CODE = lang
        else:
            activate(settings.LANGUAGE_CODE)
        response = self.get_response(request)
        return response
