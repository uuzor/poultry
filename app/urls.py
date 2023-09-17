from django.urls import path
from .views import HomeClass, VaccinatingperiodClass, BreedsavailableClass, AnimalNutritionClass, AboutClass, HealthyfeedpracticeClass


urlpatterns = [
    path('', HomeClass, name='home'),
    path('vaccinatingperiod/', VaccinatingperiodClass, name='vaccinationperiod'),
    path('breedsavailable/', BreedsavailableClass, name='Breedsavailable'),
    path('animalNutrition/', AnimalNutritionClass, name= 'AnimalNutrition'),
    path('about/', AboutClass, name='about'),
    path('healthyfeedpractice/', HealthyfeedpracticeClass, name= 'Healthyfeedpractice')
]