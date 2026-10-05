from django.conf import settings

def checkAvailableLanguages(requestCode):
    for code , name in settings.LANGUAGES:
            if(code == requestCode):
               return True
            else : 
                return False