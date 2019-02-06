from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from APIRequests import *
from forms import *
from django.utils import simplejson
import datetime
from django.http import HttpResponse

def index(request):
    if request.method == 'POST': #check to see if a POST request is sent
        form = APIKeySubmit(request.POST) #make a copy of the data in the post body
        if form.is_valid(): #check to see if the post body matches up with the form we have defined for the API key
            apikey = form.cleaned_data['apikey'] #store the apikey in a variable to use later
            sitedata = getSiteData(apikey) #make a request to the Sentinel API with the API key

            return render(request, 'riskDashboard2/index.html', {'sitedata': sitedata,'apikey': apikey})
    else:
        form = APIKeySubmit() #if its not a POST request, make a new form instance

    return render(request, 'riskDashboard2/index.html', {'form':form}) #render the page with the new form instance

@csrf_exempt
def vulnData(request):
    data = getVulnData(request.POST.get('apikey'),'open',request.POST.get('site'))
    vulndict = []

    for item in data:
        temp = [item.attrib['id'],item.attrib['class'],item.attrib['severity'],item.attrib['threat'],'0']
        vulndict.append(temp)

    return render(request, 'riskDashboard2/vulndata.html', {'vulndict':vulndict})

def appmanagement(request):
    if request.method == 'POST': #check to see if a POST request is sent
        form = APIKeySubmit(request.POST) #make a copy of the data in the post body
        if form.is_valid(): #check to see if the post body matches up with the form we have defined for the API key
            apikey = form.cleaned_data['apikey'] #store the apikey in a variable to use later
            sitedata = getSiteData(apikey) #make a request to the Sentinel API with the API key

            return render(request, 'riskDashboard2/appmanagement.html', {'sitedata': sitedata,'apikey': apikey})
    else:
        form = APIKeySubmit() #if its not a POST request, make a new form instance

    return render(request, 'riskDashboard2/appmanagement.html', {'form':form}) #render the page with the new form instance
