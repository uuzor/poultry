# from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

# Create your views here.


# def MainPage(request):
#     customer = {
#         'name': 'Javis',
#         'item': 'Phone x'
#     }
    
#     if request.method == 'POST':
#         email = request.POST['email']
#         query = request.POST['query']
         
#         return render(request, 'main/index.html', {'obj': email})
        
        
#     return render(request, 'main/index.html', {'object': customer})

from django.shortcuts import render

# Create your views here.


def HomeClass(request):
    person = {
    'name': 'Prince',
    'gender': 'male',
    'goods': 'Poult'
    }
    print(request)
    return render(request, 'home/index.html')


def VaccinatingperiodClass(request):
    person = {
    'name': 'Prince',
    'gender': 'male',
    'goods': 'Poult'
    }
    print(request)
    return render(request, 'Vaccinatingperiod/index.html')

def BreedsavailableClass(request):
    person = {
    'name': 'Prince',
    'gender': 'male',
    'goods': 'Poult'
    }
    print(request)
    return render(request, 'Breedsavailable/index.html')

def AnimalNutritionClass(request):
    person = {
    'name': 'Prince',
    'gender': 'male',
    'goods': 'Poult'
    }
    print(request)
    return render(request, 'AnimalNutrition/index.html')


def AboutClass(request):
    person = {
    'name': 'Prince',
    'gender': 'male',
    'goods': 'Poult'
    }
    print(request)
    return render(request, 'about/index.html')


def HealthyfeedpracticeClass(request):
    person = {
    'name': 'Prince',
    'gender': 'male',
    'goods': 'Poult'
    }
    print(request)
    return render(request, 'Healthyfeedpractice/index.html')
