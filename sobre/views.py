from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from . import models


class Projeto(View):
    template_name = 'sobre/projeto.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.rederizar = render(self.request, self.template_name)

    def get(self, *args, **kwargs):
        return self.rederizar


class Desenvolvedor(View):
    template_name = 'sobre/desenvolvedor.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        contexto = {
            'imagem': self.request.session.get('imagem', {})
        }
        self.rederizar = render(self.request, self.template_name, contexto)

    def get(self, *args, **kwargs):
        return self.rederizar

