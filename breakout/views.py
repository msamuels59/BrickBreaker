import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import Score
from .forms import ScoreForm


def index(request):
    score_form = ScoreForm()
    return render(request, 'index.html', {'score_form' : score_form})

def ajax_create_score(request):
    if request.method == 'POST':
        score = request.POST.get('score')
        intials = request.POST.get('initials')
        new_score = Score.objects.get_or_create(points=score, player=intials)
        data = serializers.serialize('json', [new_score[0]])
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'method': 'error method not permitted'})

def ajax_get_top_scores(request):
    top_scores = Score.objects.all().order_by('-points')[:5]
    data = serializers.serialize('json', top_scores)
    return HttpResponse(data, content_type='appilcation/json')