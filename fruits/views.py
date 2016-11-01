from django.shortcuts import render
from .models import Fruits
import json

# Create your views here.
def index(request):
    data = Fruits.objects.order_by('-value')[:5].values('value', 'name')
    chart = {
        "chart": {
            "type": "pie",
            "title": "Top 5 fruits",
            "data": list(data),
            "container": "container"
        }
    }
    context = {"chartData": json.dumps(chart), "title": "Anychart Django template"}
    return render(request, 'fruits/index.html', context)