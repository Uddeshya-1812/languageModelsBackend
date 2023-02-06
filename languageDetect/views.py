# from django.shortcuts import render
from django.http import JsonResponse
from language import getLanguageId
import json

def detectLanguage(request):
    try:
        if request.headers['Auth'] != '!_randomString_!':
            raise Exception('Authentication Error!')
        elif not (request.body):
            raise Exception('No text provided')
        else:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            if body['text']:
                textLanguage = getLanguageId(body['text'])
            else:
                raise Exception('No text provided!')
        return JsonResponse({
            'status': 200,
            'msg': textLanguage
        })
    except Exception as e:
        return JsonResponse({
            'status': 400,
            'msg': str(e)
        })

# Create your views here.
