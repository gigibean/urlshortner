from django.shortcuts import get_object_or_404, render
import random, string, json
from urlshortnerapp.models import Url
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'urlshortnerapp/home.html')

# original_url로 ㄱㄱ하는 함수
def redirect_original_url(request, shorten_id):
    print("redirect shorten_id", shorten_id)
    url= get_object_or_404(Url, pk= shorten_id)
    url.save()
    return HttpResponseRedirect(url.original_url)

# get_id 함수에서 얻은 short_id를 original_url과 연결해주고, http에 띄워주는 함수
def shorten_url(request):
    url= request.POST.get('url', '')
    if not (url == ''):
        if Url.objects.filter(original_url= url):
            shorten_id= Url.objects.get(original_url= url).shorten_id
        else:
            shorten_id= get_random_short_id()
            print("shroten shorten_id", shorten_id)
            b = Url(original_url= url, shorten_id= shorten_id)
            b.save()

        response_data= {}
        response_data['url']= 'http://127.0.0.1:8000' + '/' + shorten_id
        print("response_data",response_data)
        return HttpResponse(json.dumps(response_data), content_type= "application/json")
    return HttpResponse(json.dumps({'error': 'error occurs'}), content_type= "application/json")
# 임의의 값을 가지는 id 리턴하는 함수
def get_random_short_id():
    length= 8
    char= string.ascii_letters + string.digits
    while True:
        shorten_id= ''.join([random.choice(char) for x in range(length)])
        return shorten_id 



