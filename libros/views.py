from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Libro
from .serializers import LibroSerializer
from rest_framework import viewsets
from django.http import HttpResponse

"""
class LibroListView(APIView):
    def get(self, request):
        libros = Libro.objects.all()
        libros_data = []
        for libro in libros:
            libros_data.append({
                'id': libro.id,
                'titulo': libro.titulo,
                'autor': libro.autor,
                'anio_publicacion': libro.anio_publicacion
            })
        return Response(libros_data,status=status.HTTP_200_OK)

    def post(self, request):
        # Extraer datos de la petición
        titulo = request.data.get('titulo')
        autor = request.data.get('autor')
        anio_publicacion = request.data.get('anio_publicacion')
    
        # Validación básica
        if not all([titulo, autor, anio_publicacion]):
            return Response(
            {'error': 'Todos los campos son requeridos'}, 
            status=status.HTTP_400_BAD_REQUEST
             )

        if autor == "Paulo Coelho":
            return Response(
                {"error": "Le pedimos respetar la librería, no admitimos esas cosas"},
                status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
            )
    
    # Crear libro
        libro = Libro.objects.create(
            titulo=titulo,
            autor=autor,
            anio_publicacion=anio_publicacion
        )
    
        return Response({
            'id': libro.id,
            'titulo': libro.titulo,
            'autor': libro.autor
        }, status=status.HTTP_201_CREATED)
"""
def inicio(request):
    return HttpResponse('<h1>Hola mundoz</h1>')


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_queryset(self):
        """Filtrar libros por año si se especifica"""

        queryset = Libro.objects.all()

        anio = self.request.query_params.get('anio')
        autor = self.request.query_params.get('autor')
        if anio is not None:
            queryset = queryset.filter(anio_publicacion=anio)
        if autor is not None:
            queryset = queryset.filter(autor=autor)
        return queryset