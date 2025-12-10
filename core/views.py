from django.views.generic import TemplateView
from .models import Equipe, Servico, Cargo,  BlogPost, Testemunho

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
       context['servico'] = Servico.objects.order_by('?').all()
       context['equipe'] = Equipe.objects.order_by('?').all()
       context['Testemunho'] = Testemunho.objects.order_by('?').all()
       context['blogpost'] = BlogPost.objects.order_by('-data_publicacao').all()[:3]
       return context