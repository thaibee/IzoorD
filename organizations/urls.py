from django.urls import path
from .views import *

urlpatterns = [
    path('', OrgList.as_view(), name='org_list'),
    path('detail/<slug:slug>/', OrgDetail.as_view(), name='org_detail'),
    path('test_func', test_func, name='test_func'),
]
