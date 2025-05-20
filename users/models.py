from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.exceptions import ValidationError
from django.utils import timezone
import mimetypes
# Create your models here.


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='default.jpg', upload_to='perfil_pics')
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    sobre = models.TextField()
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
        
        #return f' perfil de {self.user.username}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open the image
        img_path = self.imagem.path
        img = Image.open(img_path)

        # Resize and crop to 40x40
        img = img.resize((800, 800), Image.Resampling.LANCZOS)
        img.save(img_path)


def validate_pdf(file):
    if not file.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')

    if hasattr(file, 'content_type'):
        if file.content_type != 'application/pdf':
            raise ValidationError('File type must be PDF.')
    else:
        # Fallback check using mimetypes (for stored files)
        mime_type, _ = mimetypes.guess_type(file.name)
        if mime_type != 'application/pdf':
            raise ValidationError('Invalid file type.')
    
class Monografia(models.Model):
    
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='monografias')
    titulo = models.CharField(max_length=255)
    resumo = models.TextField()
    ficheiro = models.FileField(upload_to='monografias/', validators=[validate_pdf])
    capa = models.ImageField(upload_to='monografias/capas/', null=True, blank=True)  # The preview image
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titulo