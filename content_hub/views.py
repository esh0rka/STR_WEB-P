from django.shortcuts import render, redirect
from .models import Article, Review, Concept
from django.shortcuts import get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import login
from django.contrib.auth.models import Group, User


def news_view(request):
    articles = Article.objects.all()

    return render(request,
                  'content_hub/news.html',
                  {'articles': articles}
                  )


def article_view(request, id):
    article = get_object_or_404(Article, id=id)

    return render(request,
                  'content_hub/article.html',
                  {'title': article.title,
                   'image': article.image,
                   'content': article.content,
                   'short_description': article.short_description,
                   'pub_date': article.pub_date, }
                  )


def feedback_view(request):
    reviews = Review.objects.all()

    return render(request,
                  'content_hub/feedback.html',
                  {'reviews': reviews, }
                  )


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            group, created = Group.objects.get_or_create(name='Клиент')
            user.groups.add(group)

            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'form': form}
                  )


def about_view(request):
    return render(request,
                  'content_hub/about.html',
                  )


def contacts_view(request):
    return render(request,
                  'content_hub/contacts.html',
                  )


def policy_view(request):
    return render(request,
                  'content_hub/policy.html',
                  )


def promo_codes_view(request):
    return render(request,
                  'content_hub/promo_codes.html',
                  )


def concept_view(request):
    concepts = Concept.objects.all()

    return render(request,
                  'content_hub/concepts.html',
                  context={
                      'concepts': concepts,
                  })


def vacancies_view(request):
    return render(request,
                  'content_hub/vacancies.html',
                  )


def account_view(request):
    if request.method == 'POST':
        rate = request.POST.get('range')
        text = request.POST.get('comment')
        username = request.POST.get('user')
        account = request.POST.get('account')
        if username != '-1NONE':
            if account == '2':
                username = 'Анонимно'
            new_feedback = Review(
                rating=rate,
                text=text,
                user=User.objects.get(username=username)
            )
            new_feedback.save()

    return render(request,
                  'content_hub/account.html',
                  )
