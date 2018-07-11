from django.shortcuts import render
import datetime, time

# Create your views here.

# CountDown
COUNTDOWN_TARGET_DATE = datetime.datetime(2018, 9, 1, 00, 00, 00, 000000)

def index(request):
    if COUNTDOWN_TARGET_DATE > datetime.datetime.now():
        td = COUNTDOWN_TARGET_DATE - datetime.datetime.now()
        send_data = (td.days * 86400) + td.seconds
        return render(
            request,
            "VoteApp/index.html",
           {
               'title' : "투표까지 남은시간",
               'day' : "일",
               'hour' : "시간",
               'min' : "분",
               'sec' : "초",
               'server_time' : send_data
           }
        )
    else:
        return render(
            request,
            "VoteApp/index.html",
           {
                'server_time': 0
            }
        )


def about(request):
    return render(
        request,
        "VoteApp/about.html",
        {
            'title' : "도움말",
            'content' : "테스트 페이지"
        }
    )
