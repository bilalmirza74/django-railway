from django.shortcuts import render,HttpResponse
from cloud.models import CspRegisterModel
from django.contrib import messages
from users.models import CustomerCloudData,KNNSuggestionModel
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def CSPLoginCheck(request):
    if request.method=='POST':
        loginname = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        try:
            check = CspRegisterModel.objects.get(loginid=loginname, password=pswd)
            request.session['cspname']=check.name
            request.session['csploginname']=check.loginid
            request.session['service']=check.service
            return render(request,'csps/CspHome.html',{})

        except Exception as ex:
            messages.success(request, 'Please Check Your Login Details')
            print('Invalid Login Details')
            print(str(ex))

    return HttpResponse('Works CSP great')

@csrf_exempt
def getCSPLoginDetails(request):
    return render(request,'GetCSPLoginDetails.html',{})

@csrf_exempt
def GetCSPLoginData(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        try:
            check = CspRegisterModel.objects.get(mobile=mobile,email=email)
            logindata = check.loginid
            pswd = check.password
            print('Login ID ',logindata,' Password ',pswd)
            return render(request,'CspLogin.html',{'loginid':logindata,'pswd':pswd})
        except Exception as ex:
            messages.success(request, 'Login Details Not Found please approach Administrations')
            return render(request, 'CspLogin.html', {})

    messages.success(request, 'Login Details Not Found please approach Administrations')
    return render(request,'CspLogin.html',{})

@csrf_exempt
def CspDataView(request):
    csploginid = request.session['csploginname']
    cspservicename = request.session['service']
    data = CustomerCloudData.objects.filter(servicename=cspservicename)
    return render(request, 'csps/CspDataView.html', {'data': data})

@csrf_exempt
def CspViewSuggested(request):
    cspservicename = request.session['service']
    data = KNNSuggestionModel.objects.filter(servicename=cspservicename)
    return render(request, 'csps/CspSuggestions.html', {'data': data})




