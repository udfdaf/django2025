from django.shortcuts import render
from .models import MainContent

def index(request):
    content_list =MainContent.objects.order_by('-pub_date')#날짜 역순,최신순
    context={'content_list': content_list}
    return render(request,'product/content_list.html',context) #