from django.urls import path
from .views import DokumentView, DokumentCreateView, VisaCreateView, \
    HamkorCreateView

urlpatterns =[
    path('', DokumentView.as_view(), name='dokumentlist'),
    # path('dokument/<slug:news>', doc_detail, name='doc_detail_page'),
    path('dokument/create/', DokumentCreateView.as_view(), name='doc_create'),
    path('visa/create', VisaCreateView.as_view(), name='visa_create'),
    path('hamkor/create', HamkorCreateView.as_view(), name='hamkor_create'),

]