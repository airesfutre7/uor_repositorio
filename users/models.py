from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='default.jpg', upload_to='perfil_pics')
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    sobre = models.TextField()
    
    def __str__(self):
        return f"{self.nome} ({self.user.username})"
        
        #return f' perfil de {self.user.username}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open the image
        img_path = self.imagem.path
        img = Image.open(img_path)

        # Resize and crop to 40x40
        img = img.resize((800, 800), Image.Resampling.LANCZOS)
        img.save(img_path)