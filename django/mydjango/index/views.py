from django.http import JsonResponse
from .face_test_sdk1 import *
from django.shortcuts import render
import requests
import time


# 另外写一个处理上传过来的文件的方法，并在这里导入
# from somewhere import handle_uploaded_file

# def index(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES) # 注意获取数据的方式
#         if form.is_valid():
#             a = request.POST.get('url')
#             data_json = requests.get(a)
#             b = str(time.time())+'.png'
#             with open(b, mode='wb') as f:
#                 f.write(data_json.content)
#             c = Image.open(b)
#             c.show()
#             im = Image.open(request.FILES['file'])
#             print(request.FILES['file'])
#             print(type(request.FILES['file']))
#             img = request.FILES.get('files')
#             im_name = str(time.time()) + '.png'
#             im.show()
#             im.save(os.path.join('/home/candy/Py/django/mydjango/index/static/image/' + im_name))
#             return HttpResponse('图片保存成功')
#     else:
#         form = ProductForm()
#     return render(request, 'index.html', locals())

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.POST.get('im_src'):
        im_src = request.POST.get('im_src')
        print(im_src)
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        data_json = requests.get(im_src, headers=headers)
        print(data_json)
        print(data_json.status_code)
        name = str(time.time())+'.jpg'
        with open(name, 'wb') as f:
            f.write(data_json.content)
        js = check(name)
        data = {
            'img_json': js
        }
        return JsonResponse(data)
        # return render(request,  'index.html', context={'img': im_src, 'img_json': js})
    else:
        im = request.FILES.get('im_submit')
        name1 = str(time.time())+'.jpg'
        im_src = '/static/' + name1
        print(im_src)
        with open(file='index/static/' + name1, mode='wb') as f:
            f.write(im.read())
        js = check('index/static/' + name1)
        ch = {
            'img': im_src,
            'img_json': js
        }
        return JsonResponse(ch)
