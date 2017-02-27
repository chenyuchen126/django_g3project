# coding:utf-8
import uniout
import cosineSimilarity
from django.shortcuts import render
from django.utils import timezone
from .models import Address
from .models import Janet
from .models import Travel
from django.contrib.sessions.models import Session
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from textflow.models import FlowObject
from django.template.loader import render_to_string
import os

def about(request,fbid):
    #about  = Address.objects.get(fbid=fbid)
    about = Travel.objects.get(gid=fbid)
    #list1= Travel.objects.filter(recommends.1)
    print type(about)
    restaurant = Address.objects.filter(category="Restaurant").order_by('-overall_star_rating')[:10]
    print about
    return render(request,'g3site/about.html/',locals())

def index(request):
	addresss = Address.objects.all()	
	restaurant = Address.objects.filter(category="Restaurant").order_by('-overall_star_rating')[:2]
	restaurant1 = Address.objects.filter(category="Restaurant")[:2]
	hotel = Address.objects.filter(category="Hotel").order_by('-overall_star_rating')[:2]
	hotel1 = Address.objects.filter(category="Hotel")[:2] 
        travel_1 = Travel.objects.filter(category_ming="餐廳")        
        travel_2 = Travel.objects.filter(category_ming="農場")        
        travel_3 = Travel.objects.filter(category_ming="民宿")        
        travel_4 = Travel.objects.filter(category_ming="觀光工廠")        
        travel_5 = Travel.objects.filter(category_ming="公園")        
        travel_6 = Travel.objects.filter(category_ming="飯店")        
        travel_7 = Travel.objects.filter(category_ming="博物館")        
        travel_8 = Travel.objects.filter(category_ming="親子館")        
        travel_9 = Travel.objects.filter(category_ming="文化園區")        
        travel_10 = Travel.objects.filter(category_ming="觀光景點")        
        travel_11 = Travel.objects.filter(category_ming="風景區")
        travel_12 = Travel.objects.filter(category_ming="露營區")
        travel_hotel = Travel.objects.filter(category_ming="飯店").order_by('-rating')[:6]
        travel_hotel1 = Travel.objects.filter(category_ming="飯店").order_by('-rating')[4:6]
        travel_rest = Travel.objects.filter(category_ming="餐廳").order_by('-rating')[:6]
        travel_rest1 = Travel.objects.filter(category_ming="餐廳").order_by('-rating')[4:6]
        traver_park = Travel.objects.filter(category_ming="公園").order_by('-rating')[:6]
        traver_park1 = Travel.objects.filter(category_ming="公園").order_by('-rating')[4:6]
 
	return render(request, 'g3site/index.html',locals())

def classification(request):
        travelall = Travel.objects.all().order_by('rating')[:400]
        address = Address.objects.all()
        return render(request, 'g3site/classification.html',locals())

def guasb(request):
        travelall = Travel.objects.all()
        address = Address.objects.all()
        return render(request, 'g3site/guasb.html',locals())

def gul(request):
        travelall = Travel.objects.all()
        address = Address.objects.all()
 
        return render(request, 'g3site/gul.html',locals())

def result(request):
	glist = []
        glist = request.GET.getlist('fname')
        print glist
        res_list = cosineSimilarity.cos_method(glist)
        print res_list
        list1 = Travel.objects.get(gid=res_list[0])
        list2 = Travel.objects.get(gid=res_list[1])
        list3 = Travel.objects.get(gid=res_list[2])
        list4 = Travel.objects.get(gid=res_list[3])
        list5 = Travel.objects.get(gid=res_list[4])
        list6 = Travel.objects.get(gid=res_list[5])
        list7 = Travel.objects.get(gid=res_list[6])
        list8 = Travel.objects.get(gid=res_list[7])
        list9 = Travel.objects.get(gid=res_list[8])
        list10 = Travel.objects.get(gid=res_list[9])
        #for x in rss_list:
        #    list[x] = Travel.objects.filter(gid=res_list[x])
            
        travel_1 = Travel.objects.all().order_by('-rating')[:8]        
    	travel_2 = Travel.objects.filter(category_ming="餐廳").order_by('-rating')[:8]        
    	travel_3 = Travel.objects.filter(category_ming="飯店").order_by('-rating')[:8]        
    	travel_1A = Address.objects.all().order_by('-overall_star_rating')[:8]        
    	travel_2A = Address.objects.filter(category="Restaurant").order_by('-overall_star_rating')[:8]        
    	travel_3A = Address.objects.filter(category="Hotel").order_by('-overall_star_rating')[:8]        

    	return render(request, 'g3site/result.html',locals())


def home(request):
    s = "Hello!"
    return HttpResponse(s)

def meta(request):
    values = request.META.items()  # 將字典的鍵值對抽出成為一個清單
    
    values.sort()                  # 對清單進行排序
    html = []
    for k, v in values:
        html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
    return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))
    
    #return render_to_response(request, 'g3site/meta.html',locals() )
