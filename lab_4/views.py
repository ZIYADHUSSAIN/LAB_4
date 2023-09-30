from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


tax_rate = 0.15

def firstpage(request):
    return HttpResponse("This is a page to calculate tax")

def calculate_tax(request, number):

        number = int(number)
        total_price = number * (1 + tax_rate)
        return HttpResponse(f"Total price after {tax_rate*100}% tax: ${total_price:.2f}")

def taxrate(request):
    return render(request, 'lab_4/index.html', {'tax_rate': tax_rate})
