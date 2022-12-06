from django.shortcuts import render, HttpResponse
import urllib, json

# Create your views here.
def index(request):
    url="https://api.opencovid.ca/summary?geo=pt&fill=true&version=true&pt_names=canonical&hr_names=canonical&fmt=json"
    res=urllib.request.urlopen(url)
    data=json.loads(res.read())
    return render(request, 'index.html', {'data':data})
