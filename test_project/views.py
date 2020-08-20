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


def image_page(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if (form['url'].value() or form['files'].value()) is not None:
            if form.is_valid():
                if len(form['url'].value()) > 0:
                    urls = form['url'].value()
                    res = re.findall(r'(?<=\/)[^\/\?#]+(?=[^\/]*$)', urls)
                    files = res[0]
                    img_data = requests.get(urls).content
                    im = Image.open(BytesIO(img_data))
                    width = im.size[0]
                    height = im.size[1]
                    new_image = Post(url=urls, files=res[0], width=width, height=height)
                    new_image.save()
                    return render(request, 'image_page.html', {'urls': urls, 'files': files, 'width': width, 'height': height})
                else:
                    urls = ''
                    files = request.FILES['files'].name
                    image = Image.open(request.FILES['files'])
                    (width, height) = image.size
                    # new_image = Post(url=urls, files=files, width=width, height=height)
                    form.save()
                    return render(request, 'image_page.html', {'urls': urls, 'files': files, 'width': width, 'height': height})
        else:
            item = Post.objects.latest('id').id
            size_form = SizeForm(request.POST)
            if size_form.is_valid():
                width = size_form['width'].value()
                height = size_form['height'].value()
                pre_image = Post.objects.get(id=item)
                files = pre_image.files
                urls = pre_image.url
                # new_files = width + 'x' + height + '___' + str(files)
                new_image = Post(url=urls, files=files, width=width, height=height)
                new_image.save()
                return render(request, 'image_page.html', {'urls': urls, 'files': files, 'width': width, 'height': height})


def image_page_from_list(request, id):
    images = Post.objects.get(id=id)
    urls = images.url
    files = images.files
    width = images.width
    height = images.height
    if request.method == 'POST':
        size_form = SizeForm(request.POST)
        if size_form.is_valid():
            width = size_form['width'].value()
            height = size_form['height'].value()
            # new_files = width + 'x' + height + '___' + str(files)
            new_image = Post(url=urls, files=files, width=width, height=height)
            new_image.save()
            return render(request, 'image_page.html', {'urls': urls, 'files': files, 'width': width, 'height': height})
    return render(request, 'image_page.html', {'urls': urls, 'files': files, 'width': width, 'height': height})
