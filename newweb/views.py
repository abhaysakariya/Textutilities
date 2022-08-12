from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

# def answer(request):
#     formtext = request.GET.get('text')
#     upper = request.GET.get('upper','off')
#     lower = request.GET.get('lower','off')
#     if upper == request.GET.get('upper'):
#         analyzed = formtext.upper()
#         return HttpResponse(analyzed)
#     elif lower == request.GET.get('lower'):
#         analyzed = formtext.lower()
#         return HttpResponse(analyzed)
#     else:
#         return HttpResponse(formtext)

def answer(request):
    formtext = request.GET.get('text')
    upper = request.GET.get('upper','off')
    lower = request.GET.get('lower','off')
    if upper == request.GET.get('upper'):
        analyzed = formtext.upper()
     #   return HttpResponse(analyzed)
    elif lower == request.GET.get('lower'):
        analyzed = formtext.lower()
    #    return HttpResponse(analyzed)
    else:
        return HttpResponse(formtext)
    params = {'name': analyzed}
    return render(request,'answer.html',params)
    