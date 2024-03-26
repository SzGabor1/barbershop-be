from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import News

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    model_data = News.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])
    return Response(data)