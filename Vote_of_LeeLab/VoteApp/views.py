from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone
import datetime, time, locale

# Like and Dislike
# https://wayhome25.github.io/django/2017/03/01/django-99-my-first-project-4/
#try:
#    from django.utils import simplejson as json
#except ImportError:
#    import json
#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
#from django.views.decorators.http import require_POST

# Registrator of user
from .forms import BootstrapAuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

# CountDown
locale.setlocale(locale.LC_CTYPE, 'korean')
COUNTDOWN_TARGET_DATE = timezone.make_aware(datetime.datetime(2018, 7, 16, 14, 00, 00, 000000))
DURIONG_DATE = datetime.timedelta(days=6, seconds=86399)

def index(request):
    if COUNTDOWN_TARGET_DATE > timezone.localtime():
        td = COUNTDOWN_TARGET_DATE - timezone.localtime()
        send_data = (td.days * 86400) + td.seconds
        return render(
            request,
            "VoteApp/index.html",
           {
               'active_home' : "active",
               'title' : "투표까지 남은시간",
               'url' : "http://210.119.85.76/",
               'description' : "LEE LAB 투표 예정일",
               'sitename' : "Lee Lab Server",
               'locale' : "ko_KR",
               'type' : "article",
               'date_of_begin_time' : "투표 예정일 : " + COUNTDOWN_TARGET_DATE.strftime('%Y년 %m월 %d일 - %H시 %M분 %S초'),
               'server_time' : send_data
           }
        )
    elif (COUNTDOWN_TARGET_DATE + DURIONG_DATE) > timezone.localtime():
        td = (COUNTDOWN_TARGET_DATE + DURIONG_DATE) - timezone.localtime()
        send_data = (td.days * 86400) + td.seconds
        return render(
            request,
            "VoteApp/index.html",
           {
               'active_home' : "active",
               'title' : "투표 종료까지 남은시간!",
               'url' : "http://210.119.85.76/",
               'description' : "LEE LAB 투표 진행중!",
               'sitename' : "Lee Lab Server",
               'locale' : "ko_KR",
               'type' : "article",
               'date_of_begin_time' : "투표 종료일 : " + (COUNTDOWN_TARGET_DATE + DURIONG_DATE).strftime('%Y년 %m월 %d일 - %H시 %M분 %S초'),
                'server_time': send_data
            }
        )
    else:
        return render(
            request,
            "VoteApp/index.html",
           {
               'active_home' : "active",
               'title' : "투표 종료",
               'url' : "http://210.119.85.76/",
               'description' : "LEE LAB 투표 결과",
               'sitename' : "Lee Lab Server",
               'locale' : "ko_KR",
               'type' : "article",
               'date_of_begin_time' : "투표 종료일 : " + (COUNTDOWN_TARGET_DATE + DURIONG_DATE).strftime('%Y년 %m월 %d일 - %H시 %M분 %S초'),
                'server_time': 0
            }
        )


def about(request):
    return render(
        request,
        "VoteApp/about.html",
        {
            'active_about' : "active",
            'title' : "도움말",
            'content' : "테스트 페이지"
        }
    )

def signup(request):
    if request.method == "POST":
        form = BootstrapAuthenticationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = BootstrapAuthenticationForm()
        return render(request, 'VoteApp/signup.html', {'form': form})


def handler400(request, exception, template_name='VoteApp/400.html'):
    return render(request, template_name, status=400)


def handler403(request, exception, template_name='VoteApp/403.html'):
    return render(request, template_name, status=403)


def handler404(request, exception, template_name='VoteApp/404.html'):
    return render(request, template_name, status=404)


def handler500(request, exception, template_name='VoteApp/500.html'):
    return render(request, template_name, status=500)