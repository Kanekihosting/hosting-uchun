from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from app.models import Dokument, Hamkorlar, Visa


# Create your views here.

class DokumentView(ListView):
    model = Dokument
    template_name = 'index/index.html'
    context_object_name = 'dokument'

    def get_queryset(self, **kwargs):
        dokuments = Dokument.objects.all().order_by('-yaratilgan_vaqti')

        return dokuments

# def doc_detail(request, news):
#     news = get_object_or_404(Dokument, slug=news)
#     context = {
#         'news': news
#     }
#     return render(request, 'index/doc_detail.html', context)


class Kopaytir(ListView):
    model = Dokument
    template_name = 'index/index.html'
    context_object_name = 'kop'

    def Kopaytma_visa(self):
        dokuments = int(Dokument.turistlar_soni)
        narx = int(Visa.visa_narxi)

        kopaytma = narx * dokuments

        return kopaytma







class DokumentCreateView(CreateView):
    model = Dokument
    fields = ('xujjat_nomi','turistlar_soni', 'hamkor', 'visa', 'yaratilgan_vaqti')
    template_name = 'crud/dokementqoshish.html'
    success_url = reverse_lazy('dokumentlist')

class NewsUpdtaeView(UpdateView):
    model = Dokument
    fields = ('xujjat_nomi','turistlar_soni', 'hamkor', 'visa', 'yaratilgan_vaqti')
    template_name = 'crud/doc_edit.html'
    success_url = reverse_lazy('dokumentlist')


class NewsDeleteView(DeleteView):
    model = Dokument
    template_name = 'crud/doc_delete.html'
    success_url = reverse_lazy('dokumentlist')


class HamkorCreateView(CreateView):
    model = Hamkorlar
    fields = ('hamkor_nomi',)
    template_name = 'crud/hamkorqoshish.html'
    success_url = reverse_lazy('dokumentlist')

class VisaCreateView(CreateView):
    model = Visa
    fields = ('visa_turi', 'visa_narxi')
    template_name = 'crud/visa_turi.html'
    success_url = reverse_lazy('dokumentlist')