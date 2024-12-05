
from djongo import models
from bson import ObjectId


class Cargo(models.Model):
    cargo_id = models.ObjectIdField()  # ID único para cada cargo
    concepto = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=[('%', 'Porcentaje'), ('fijo', 'Fijo')])
    mes = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Estudiante(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # El identificador único de MongoDB
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=20, unique=True)
    id_curso = models.ObjectIdField()
    edad = models.IntegerField()
    cargos = models.ArrayField(
        model_container=Cargo,
        default=list,  # Lista vacía por defecto
    )

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
