from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status

from root001 import verification



def verification_code(request):
    text, img = verification.VerificationCode().gene_code()
    # request.session['verifycode'] = text
    # key = request.session.session_key
    # print('key',key)
    # request.session['verification_code'] = text
    # img.show()  # 显示一下效果
    # stream = io.BytesIO()    # 创建一个io对象
    # img.save(stream, "png")    # 将图片对象im保存到stream对象里
    # stream.getvalue() 图片二级制内容，再通过HttpResponse封装，返回给前端页面
    with open('test.png', 'wb') as f:
        img.save(f,'png')
    with open('test.png', 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type="image/png")