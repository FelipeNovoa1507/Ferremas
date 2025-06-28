from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class UserAuthManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
class UserAuth(AbstractUser):
    username = None
    rut = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=9, unique=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    nivel_educacional = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)

    objects = UserAuthManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'rut', 'direccion', 'fecha_de_nacimiento', 'telefono', 'region', 'nivel_educacional']

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    


class Pedido(models.Model):
    Cliente = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Pedido ' + str(self.id) + ' - ' + str(self.Cliente)


    

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class Marca(models.Model):
    nombre = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class FormaDePago(models.Model):
    nombre = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    

    
class Producto(models.Model):
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    nombre = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    precio_Costo = models.IntegerField(blank=True, null=True)
    precio_Oferta = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField()
    creado_en = models.DateField()
    codigo = models.IntegerField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)    
    def __str__(self):
        return self.nombre, self.marca, self.categoria
    
class Carrito(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return 'Item ' + str(self.id) + ' - ' + str(self.producto)
    
class listaDeseos(models.Model):
    Cliente = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Item ' + str(self.id) + ' - ' + str(self.producto)