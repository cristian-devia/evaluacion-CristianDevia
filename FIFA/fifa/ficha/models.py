from django.db import models
from datetime import datetime
from django.utils.html import format_html


# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Equipo")
    flag_image = models.ImageField(upload_to='flags/', verbose_name="Imagen de Bandera")
    shield_image = models.ImageField(upload_to='shields/', verbose_name="Escudo del Equipo")

    def __str__(self):
        return self.name
    
    def show_photo(self):
        return format_html('<img src={} width="70" /> ', self.photo.url)

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        db_table = "equipo"



class Player(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido")
    birth_date = models.DateField(verbose_name="Fecha de nacimiento")
    position = models.CharField(max_length=50, verbose_name="Posición en la que juega")
    number = models.IntegerField(verbose_name="Número de camiseta")
    is_starting = models.BooleanField(verbose_name="¿Es titular?")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Equipo")
    photo = models.ImageField(upload_to='player/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def show_photo(self):
        if self.photo:
            return format_html('<img src="{}" width="70" />', self.photo.url)
        return "No photo"

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        db_table = "jugador"

class PlayingPosition(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Posición de juego"
        verbose_name_plural = "Posiciones de juego"
        db_table = "posicion_juego"


class Coach(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido")
    birth_date = models.DateField(verbose_name="Fecha de nacimiento")
    
    NATIONALITIES = [
        ('ARG', 'Argentina'),
        ('ESP', 'España'),
        ('BRA', 'Brasil'),
    
    ]
    nationality = models.CharField(max_length=3, choices=NATIONALITIES, verbose_name="Nacionalidad")
    
    ROLE_CHOICES = [
        ('técnico', 'Técnico'),
        ('asistente', 'Asistente'),
        ('médico', 'Médico'),
        ('preparador', 'Preparador'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name="Rol")

    def __str__(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"
        db_table = "tecnico"



