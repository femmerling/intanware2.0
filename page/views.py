# Create your views here.
from page.models import Page
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request, page_id="home"):
  p = get_object_or_404(Page, pk=page_id)
  return render_to_response('page/view.html', {'page': p})

def view(request, page_id):
  p = get_object_or_404(Page, pk=page_id)
  return render_to_response('page/view.html', {'page': p})
