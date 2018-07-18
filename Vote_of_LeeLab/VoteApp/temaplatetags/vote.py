from django.utils import timezone
import datetime, time, locale

#@register.filter            # 1
#def add_str(left, right):
#    return left + right

@register.simple_tag            # 2
def is_vote():
    if COUNTDOWN_TARGET_DATE > timezone.localtime():
        return False
    else:
        return True

#@register.assignment_tag            # 3
#def max_int(a, b):
#    return max(int(a), int(b))

#@register.inclusion_tag(div.html, takes_context=True)            # 4
#def include_div(context): 
#    return {
#        'div_param': context['param']
#        }