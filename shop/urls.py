from django.urls import path, register_converter
from . import views
from .converters import FourDigitYearConverter

app_name = 'shop'

register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year, name="archives_year"),
    path('', views.item_list, name="item_list"),
    path('<int:pk>/', views.item_detail, name="item_detail"),
    path('new/', views.item_new, name="item_new"),
    path('<int:pk>/edit/', views.item_edit, name="item_edit"),
    # path('response_excel/', response_excel),
    # path('response_image/', response_image)
]
