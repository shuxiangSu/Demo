from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def MainPage(request):
    returnList = {}
    return render(request, "MainPage.html", returnList)


def FreshStatus(request):
    returnList = {}
    sub1 = {"ID":"BJ PSD BTT1", "Hostname":'Machine 1', "Status": 'Enable'}
    sub2 = {"ID":"BJ PSD BTT2", "Hostname":'Machine 2', "Status": 'Offline'}
    sub3 = {"ID":"BJ PSD 1", "Hostname":'Machine 3', "Status": 'Offline'}
    sub4 = {"ID": "BJ PSD 2", "Hostname": 'Machine 4', "Status": 'Offline'}
    returnList["machine"] = []
    returnList["machine"].append(sub1)
    returnList["machine"].append(sub2)
    returnList["machine"].append(sub3)
    returnList["machine"].append(sub4)
    # print(returnList)
    return JsonResponse(returnList, safe=False)