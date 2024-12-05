from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Estudiante
import json


@csrf_exempt
def create_estudiante(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        estudiante = Estudiante.objects.create(
            nombre=data['nombre'],
            codigo=data['codigo'],
            id_curso=data['id_curso'],
            edad=data['edad'],
        )
        return JsonResponse({'message': 'Estudiante creado', 'id': str(estudiante._id)})


def list_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    data = [{'id': str(est._id), 'nombre': est.nombre, 'codigo': est.codigo, 'edad': est.edad} for est in estudiantes]
    return JsonResponse(data, safe=False)


def get_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, _id=id)
    data = {
        'id': str(estudiante._id),
        'nombre': estudiante.nombre,
        'codigo': estudiante.codigo,
        'edad': estudiante.edad,
        'cargos': list(estudiante.cargos)
    }
    return JsonResponse(data)


@csrf_exempt
def update_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, _id=id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        estudiante.nombre = data.get('nombre', estudiante.nombre)
        estudiante.codigo = data.get('codigo', estudiante.codigo)
        estudiante.id_curso = data.get('id_curso', estudiante.id_curso)
        estudiante.edad = data.get('edad', estudiante.edad)
        estudiante.save()
        return JsonResponse({'message': 'Estudiante actualizado'})


@csrf_exempt
def delete_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, _id=id)
    if request.method == 'DELETE':
        estudiante.delete()
        return JsonResponse({'message': 'Estudiante eliminado'})
