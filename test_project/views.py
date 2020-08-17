from django.shortcuts import render
from test_project.forms import PostForm, SizeForm
from bs4 import BeautifulSoup
import requests
from django.db import connection
import sqlite3
from test_project.models import Post


def init(request):
    images = Post.objects.all()
    return render(request, 'list_of_images.html', {'images': images})


def add_new_images(request):
    return render(request, 'add_new_image.html')


def image_page(request, id):
    images = Post.objects.get(id=id)
    url = images.url
    files = images.files
    width = images.width
    height = images.height
    if request.method == 'POST':
        # size_form = SizeForm(request.POST)
        # if size_form.is_valid():
        #     width = size_form['width']
        #     height = request.FILES['height']
        #     size_form.save()
        # else:
        #     print('Error!')
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if len(form['url'].value()) > 0:
                url = form['url'].value()
                new_image = Post(url=url, files=url.split('/')[-1])
                new_image.save()
            else:
                files = request.FILES['files'].name
                form.save()
        else:
            print('Error here!')
    return render(request, 'image_page.html', {'url': url, 'files': files, 'width': width, 'height': height})
