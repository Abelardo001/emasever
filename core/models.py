from django.db import models
from stdimage import StdImageField

# Create your models here.

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

# models.py
class Servico(Base):
    ICONES_CHOICES = (
        ('icon-autorenew', 'Auto Renew'),
        ('icon-backspace', 'Backspace'),
        ('icon-av_timer', 'Timer'),
        ('icon-beenhere', 'Been Here'),
        ('icon-business_center', 'Business Center'),
        ('icon-cloud_done', 'Cloud Done'),
        ('icon-trending_up', 'Trending Up'),
        ('icon-people', 'People'),
        ('icon-security', 'Security'),
        ('icon-account_balance', 'Account Balance'),
        ('icon-pie_chart', 'Pie Chart'),
        ('icon-assessment', 'Assessment'),
        ('icon-shield', 'Shield'),
        # Adicione quantos quiser – tem milhares no Material Icons
    )

    titulo = models.CharField('Título', max_length=100)
    descricao_curta = models.TextField('Descrição Curta', max_length=200)
    descricao_longa = models.TextField('Descrição Longa')
    icone = models.CharField(
        'Ícone (Material Icons)',
        max_length=50,
        choices=ICONES_CHOICES,
        default='icon-business',
        help_text='Escolha o ícone que aparece no site. Veja todos em: <a href="https://fonts.google.com/icons" target="_blank">fonts.google.com/icons</a>'
    )

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.titulo
class Equipe(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    foto = StdImageField('Foto', upload_to='equipe', variations={'thumb': (300, 300)})
    bio = models.TextField('Biografia', blank=True)
    facebook = models.URLField('Facebook', blank=True)
    twitter = models.URLField('Twitter', blank=True)
    linkedin = models.URLField('LinkedIn', blank=True)
    instagram = models.URLField('Instagram', blank=True)
    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.nome
class Testemunho(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=100)
    foto = StdImageField('Foto', upload_to='testemunhos', variations={'thumb': (100, 100)})
    depoimento = models.TextField('Depoimento')
    class Meta:
        verbose_name = 'Testemunho'
        verbose_name_plural = 'Testemunhos'

    def __str__(self):
        return self.nome

class BlogPost(Base):
    titulo = models.CharField('Título', max_length=200)
    conteudo = models.TextField('Conteúdo')
    imagem_capa = StdImageField('Imagem de Capa', upload_to='blog', variations={'thumb': (600, 400)})
    autor = models.CharField('Autor', max_length=100)
    data_publicacao = models.DateField('Data de Publicação')

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.titulo
class Cargo(Base):
    nome = models.CharField('Nome do Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.nome
            