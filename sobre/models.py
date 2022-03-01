from django.db import models
from django.conf import settings
from django.utils.text import slugify

from PIL import Image
import os


class Projeto(models.Model):
    descricao_longa = models.TextField()

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projeto'


class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='sobre_imagens/%Y/%m', blank=True, null=True)

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Desenvolvedor'
        verbose_name_plural = 'Desenvolvedor'