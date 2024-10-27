from django.shortcuts import render,HttpResponse

def produtos(request):
    return render(request, 'html/produtos.html')