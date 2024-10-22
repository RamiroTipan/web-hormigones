from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título", blank=True, null=True)
    subtitle = models.CharField(max_length=200, verbose_name="Sub Título", blank=True, null=True)
    content = models.TextField(verbose_name="Contenido", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Editado")

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        