from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
import logging
# from urllib.parse import quote
# import os, requests
# from io import BytesIO
# from PIL import Image, ImageDraw, ImageFont

logger = logging.getLogger(__name__)    # __name__ => "shop.views"

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)

    logger.debug('query: {}'.format(q))

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q,
    })

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item
    })


def item_new(request, item=None):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(item)
    else:
        form = ItemForm(instance=item)

    return render(request, 'shop/item_form.html', {
        'form': form,
    })


def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)

# def response_excel(request):
#     filepath = r'C:\Users\jc\Downloads\test_file.xlsx'
#     filename = os.path.basename(filepath)

#     with open(filepath, 'rb') as f:
#         response = HttpResponse(f, content_type='application/vnd.ms-excel')
#         encoded_filename = quote(filename)
#         response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)
#     return response

# def response_image(request):
#     ttf_path = r'C:\Windows\Fonts\Gadugi.ttf'

#     image_url = r'C:\Users\jc\Downloads\jcjang.png'
    
#     canvas = Image.open(image_url)
#     font = ImageFont.truetype(ttf_path, 40)
#     draw = ImageDraw.Draw(canvas)

#     text = 'jc Jang'
#     left, top = 10, 10
#     margin = 10
#     width, height = font.getsize(text)
#     right = left + width + margin
#     bottom = top + height + margin
#     draw.rectangle((left, top, right, bottom), (255, 255,224))
#     draw.text((15, 15), text, font=font, fill=(20, 20, 20))

#     response = HttpResponse(content_type='image/png')
#     canvas.save(response, format='PNG')
#     return response
