from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from . import views

urlpatterns = [
    path('content_hub/', views.news_view, name='news'),
    path('content_hub/<int:id>/', views.article_view, name='article_view'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('accounts/registration', views.register_view, name='registration'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('policy/', views.policy_view, name='policy'),
    path('promo_codes/', views.promo_codes_view, name='promo_codes'),
    path('concepts/', views.concept_view, name='concepts'),
    path('vacancies/', views.vacancies_view, name='vacancies'),
    path('account/', views.account_view, name='account'),
]
