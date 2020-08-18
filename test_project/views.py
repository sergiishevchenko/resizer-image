from django.shortcuts import render
from test_project.forms import PostForm, SizeForm
import requests
from django.db import connection
import sqlite3
from django.shortcuts import redirect
from test_project.models import Post
import re
from PIL import Image
from io import BytesIO


def init(request):
    images = Post.objects.all()
    return render(request, 'list_of_images.html', {'images': images})


def add_new_images(request):
    return render(request, 'add_new_image.html')


def image_page(request, id):
    images = Post.objects.get(id=id)
    urls = images.url
    files = images.files
    width = images.width
    height = images.height

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form in request.POST:
            if form.is_valid():
                if len(form['url'].value()) > 0:
                    urls = form['url'].value()
                    res = re.findall(r'(?<=\/)[^\/\?#]+(?=[^\/]*$)', urls)
                    img_data = requests.get(urls).content
                    im = Image.open(BytesIO(img_data))
                    width = im.size[0]
                    height = im.size[1]
                    new_image = Post(url=urls, files=res[0], width=width, height=height)
                    new_image.save()
                else:
                    files = request.FILES['files'].name
                    form.save()
            else:
                print('Error here!')
        else:
            size_form = SizeForm(request.POST)
            if size_form.is_valid():
                width = size_form['width'].value()
                height = size_form['height'].value()
                files = width + 'x' + height + '___' + str(files)
                new_image = Post(url=urls, files=files, width=width, height=height)
                new_image.save()
            else:
                print('Error size!')
    return render(request, 'image_page.html', {'urls': urls, 'files': files, 'width': width, 'height': height, 'id': id})
