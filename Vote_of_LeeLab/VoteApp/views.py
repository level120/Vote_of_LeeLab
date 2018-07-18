from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.utils import timezone
import datetime, time, locale

# Like and Dislike
# https://wayhome25.github.io/django/2017/03/01/django-99-my-first-project-4/
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.http import HttpResponse
from django.core import serializers
from .models import Like

# Registrator of user
from .forms import BootstrapAuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

# CountDown
# 개발용 locale 설정, 배포시 반드시 주석처리 할 것.
#locale.setlocale(locale.LC_CTYPE, 'korean')

COUNTDOWN_TARGET_DATE = timezone.make_aware(datetime.datetime(2018, 7, 16, 00, 00, 00, 000000))
DURIONG_DATE = datetime.timedelta(days=6, seconds=86399)

def index(request):
    '''
    [index page]
    "if" is before start time,
    "elif" is after start time and before end time
    "else" is after end time
    '''
    # 좋아요 순서
    #likes = Like.objects.annotate(like_count=Count('likes')).order_by('-like_count', '-update_date')
    likes = get_object_or_404(Like, pk=1)

    if COUNTDOWN_TARGET_DATE > timezone.localtime():
        td = COUNTDOWN_TARGET_DATE - timezone.localtime()
        send_data = (td.days * 86400) + td.seconds
        return render(
            request,
            "VoteApp/index.html",
           {
               'active_home' : "active", # begin common
               'title' : "투표까지 남은시간",
               'url' : "https://chenny.ml/",
               'description' : "LEE LAB 투표 예정일",
               'sitename' : "Lee Lab Server",
               'locale' : "ko_KR",
               'type' : "article", # end common
               'noti_title' : "[시작 알림!!]", # begin noti
               'noti_context' : "투표가 시작되었습니다! 투표를 시작하세요!",
               'noti_img' : "https://chenny.ml/static/img/logo2.png", # end noti
               'date_of_begin_time' : "투표 예정일 : " + COUNTDOWN_TARGET_DATE.strftime('%Y년 %m월 %d일 - %H시 %M분 %S초'),
               'server_time' : send_data,
               'likes' : likes.id
           }
        )
    elif (COUNTDOWN_TARGET_DATE + DURIONG_DATE) > timezone.localtime():
        td = (COUNTDOWN_TARGET_DATE + DURIONG_DATE) - timezone.localtime()
        send_data = (td.days * 86400) + td.seconds
        return render(
            request,
            "VoteApp/index.html",
           {
               'active_home' : "active", # begin common
               'title' : "투표 진행 중!",
               'url' : "https://chenny.ml/",
               'description' : "LEE LAB 투표 진행중!",
               'sitename' : "Lee Lab Server",
               'locale' : "ko_KR",
               'type' : "article", # end common
               'noti_title' : "[종료 알림!!]", # begin noti
               'noti_context' : "투표가 종료되었습니다! 결과를 확인하세요!",
               'noti_img' : "https://chenny.ml/static/img/logo2.png", # end noti
               'date_of_begin_time' : "투표 종료일 : " + (COUNTDOWN_TARGET_DATE + DURIONG_DATE).strftime('%Y년 %m월 %d일 - %H시 %M분 %S초'),
               'server_time': send_data,
               'likes' : likes.id
            }
        )
    else:
        return render(
            request,
            "VoteApp/index.html",
           {
               'active_home' : "active", # begin common
               'title' : "투표 종료",
               'url' : "https://chenny.ml/",
               'description' : "LEE LAB 투표 결과",
               'sitename' : "Lee Lab Server",
               'locale' : "ko_KR",
               'type' : "article", # end common
               'date_of_begin_time' : "투표 종료일 : " + (COUNTDOWN_TARGET_DATE + DURIONG_DATE).strftime('%Y년 %m월 %d일 - %H시 %M분 %S초'),
               'server_time': 0,
               'likes' : likes.id
            }
        )


def about(request):
    '''
    [about page]
    now, it's a page of privacy policy
    '''
    return render(
        request,
        "VoteApp/about.html",
        {
            'active_about' : "active",
            'url' : "https://chenny.ml/about/",
            'description' : "LEE LAB 투표 결과",
            'sitename' : "Lee Lab Server",
            'locale' : "ko_KR",
            'type' : "article",
            'title' : "도움말",
            'content' : "테스트 페이지"
        }
    )


def vote(request):
    '''
    [vote page]
    almost request & reply uesd ajax
    '''
    if (COUNTDOWN_TARGET_DATE + DURIONG_DATE) > timezone.localtime():
        td = (COUNTDOWN_TARGET_DATE + DURIONG_DATE) - timezone.localtime()
        send_data = (td.days * 86400) + td.seconds
        return render(
            request,
            "VoteApp/vote.html",
           {
               'active_home' : "active", # begin common
               'title' : "투표 진행 중!",
               'url' : "https://chenny.ml/",
               'description' : "LEE LAB 투표 진행중!",
               'sitename' : "Lee Lab Server",
               'locale' : "ko_KR",
               'type' : "article", # end common
               'noti_title' : "[종료 알림!!]", # begin noti
               'noti_context' : "투표가 종료되었습니다! 결과를 확인하세요!",
               'noti_img' : "https://chenny.ml/static/img/logo2.png", # end noti
               'date_of_begin_time' : "투표 종료일 : " + (COUNTDOWN_TARGET_DATE + DURIONG_DATE).strftime('%Y년 %m월 %d일 - %H시 %M분 %S초'),
               'server_time': send_data,
            }
        )
    else:
        return render(
            request,
            "VoteApp/vote.html",
           {
               'active_home' : "active", # begin common
               'title' : "투표 종료",
               'url' : "https://chenny.ml/",
               'description' : "LEE LAB 투표 결과",
               'sitename' : "Lee Lab Server",
               'locale' : "ko_KR",
               'type' : "article", # end common
               'date_of_begin_time' : "투표 종료일 : " + (COUNTDOWN_TARGET_DATE + DURIONG_DATE).strftime('%Y년 %m월 %d일 - %H시 %M분 %S초'),
               'server_time': 0,
            }
        )


def capstone(request):
    '''
    [privacy policy page]
    page of privacy policy, just linked dev-favebook
    '''
    return render(
        request,
        "VoteApp/capstone_design.html",
        {
            'title' : "개인정보처리방침",
        }
     )

def signup(request):
    '''
    [signup page]
    this page is unsafe
    '''
    if request.method == "POST":
        form = BootstrapAuthenticationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = BootstrapAuthenticationForm()
        return render(request, 'VoteApp/signup.html', {'form': form})


@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        name_id = request.POST.get('pk', None)
        obj = Like.objects.get(pk = name_id)

        if obj.likes.filter(pk = name_id).exists():
            obj.likes.remove(user)
            message = '좋아요! '
        else:
            obj.likes.add(user)
            message = '좋아요 취소 '

    context = {'likes_count': obj.total_likes, 'message': message}
    return HttpResponse(json.dumps(context), content_type='application/json')


@login_required
@require_POST
def like_ready(request):
    if request.method == 'POST':
        user = request.user
        name_id = request.POST.get('pk', None)
        obj = Like.objects.get(pk = name_id)

        if obj.likes.filter(pk = name_id).exists():
            message = '좋아요 취소 '
        else:
            message = '좋아요! '

    context = {'likes_count': obj.total_likes, 'message': message}
    return HttpResponse(json.dumps(context), content_type='application/json')


@require_POST
def like_anonymous(request):
    if request.method == 'POST':
        name_id = request.POST.get('pk', None)
        obj = Like.objects.get(pk = name_id)
        message = '좋아요! '

    context = {'likes_count': obj.total_likes, 'message': message}
    return HttpResponse(json.dumps(context), content_type='application/json')


# below pages are handler of exception for 400, 403, 404 and 500
def handler400(request, exception, template_name='VoteApp/400.html'):
    return render(request, template_name, status=400)


def handler403(request, exception, template_name='VoteApp/403.html'):
    return render(request, template_name, status=403)


def handler404(request, exception, template_name='VoteApp/404.html'):
    return render(request, template_name, status=404)


def handler500(request, exception, template_name='VoteApp/500.html'):
    return render(request, template_name, status=500)