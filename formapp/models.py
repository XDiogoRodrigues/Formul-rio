from django.db import models

from stdimage import StdImageField


class Base(models.Model):
    create = models.DateField('Data de criação', auto_now_add=True)
    modified = models.DateField('Data de atualização', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)


class UserSystem(Base):
    name = models.CharField('Nome', max_length=255)
    surname = models.CharField('Sobrenome', max_length=255)
    email = models.EmailField('E-mail', max_length=100)
    password = models.CharField('Senha', max_length=255, editable=False)
    photo = StdImageField('Foto', upload_to='images_users', variations={'thumb': (125,125)})

    class Meta:
        db_table = 'Usuários'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

