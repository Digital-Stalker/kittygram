from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


"""
class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class APICat(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICatDetail(APIView):
    def get(self, request, pk):
        cat = get_object_or_404(Cat, id=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data)

    def put(self, request, pk):
        cat = get_object_or_404(Cat, id=pk)
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        cat = get_object_or_404(Cat, id=pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cat = get_object_or_404(Cat, id=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'POST':
        serializer = CatSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
# Применили декоратор и указали разрешённые методы
def hello(request):
    # По задумке, в ответ на POST-запрос нужно вернуть JSON с теми данными,
    # которые получены в запросе.
    # Для этого в объект Response() передаём словарь request.data.
    if request.method == 'POST':
        return Response({'message': 'Получены данные', 'data': request.data})

    # В ответ на GET-запрос нужно вернуть JSON
    # Он тоже будет создан из словаря, переданного в Response()
    return Response({'message': 'Это был GET-запрос!'})
"""
