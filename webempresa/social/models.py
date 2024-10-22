from django.db import models

class Link(models.Model):
    key = models.SlugField(verbose_name=" Nombre clave", max_length=200, unique=True)
    name =models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=250, null=True, blank=True )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")
    

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name
