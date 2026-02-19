from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def Binary_to_decimal(request):

    context = {}
    if request.method == 'POST':
        
        context['decimal'] = int(request.POST.get('binary'), 2)

    return render(request, 'Binary_to_decimal.html', context)

    

def Decimal_to_binary(request):

    context = {}
    if request.method == 'POST':
        
        context['binary'] = bin(int(request.POST.get('decimal')))[2:]

    return render(request, 'Decimal_to_binary.html', context)
