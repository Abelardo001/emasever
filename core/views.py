from django.views.generic import TemplateView
from .models import Equipe, Servico, Cargo, BlogPost, Testemunho
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

# Página inicial
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servico'] = Servico.objects.order_by('?').all()
        context['equipe'] = Equipe.objects.order_by('?').all()
        context['Testemunho'] = Testemunho.objects.order_by('?').all()
        context['blogpost'] = BlogPost.objects.order_by('-data_publicacao').all()[:3]
        return context

# View separada para envio de email
@csrf_exempt  # apenas para testes, depois use {% csrf_token %} no formulário
def enviar_email(request):
    if request.method == "POST":
        primeiro_nome = request.POST.get("fname")
        ultimo_nome = request.POST.get("lname")
        email_usuario = request.POST.get("email")
        assunto = request.POST.get("subject")
        mensagem = request.POST.get("message")

        corpo_email = f"""
        Nova mensagem de contato:

        Nome: {primeiro_nome} {ultimo_nome}
        Email: {email_usuario}
        Assunto: {assunto}

        Mensagem:
        {mensagem}
        """

        try:
            send_mail(
                assunto,
                corpo_email,
                'abelardogs2000@gmail.com',       # remetente técnico
                ['abelardogs2000@gmail.com'],      # destinatário real
                fail_silently=False,
            )
            messages.success(request, "Mensagem enviada com sucesso!")
        except BadHeaderError:
            messages.error(request, "Erro: cabeçalho inválido.")
        except Exception as e:
            messages.error(request, f"Ocorreu um erro ao enviar: {e}")

        return redirect('index')  # redireciona para a página principal

    return redirect('index')
