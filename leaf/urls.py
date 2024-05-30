from django.urls import re_path

from .views import LeafTemplateView

urlpatterns = [
    re_path(r'(?P<leaf_url>.*)(/)?$', LeafTemplateView.as_view(), name='page'),
]
