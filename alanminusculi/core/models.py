from django.db import models


class Identity(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.CharField('Descrição', max_length=150)
    email = models.CharField('E-mail', max_length=150)
    github = models.CharField('GitHub', max_length=150, blank=True, null=True)    
    linkedin = models.CharField('LinkedINn', max_length=150, blank=True, null=True)
    instagram = models.CharField('Instagram', max_length=150, blank=True, null=True)
    facebook = models.CharField('Facebook', max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Identidade"
        verbose_name_plural = "Identidades"
        ordering = ['name']


class Skill(models.Model):
    name = models.CharField('Nome', max_length=100)
    icon = models.CharField('Ícon (Font Awesome)', max_length=100)
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"
        ordering = ['name']