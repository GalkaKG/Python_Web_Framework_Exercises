from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer

from todos_rest_workshop.todos_api.models import Todo, Category
from todos_rest_workshop.todos_api.serializers import CategorySerializer, TodoSerializer


class TodoCreateSerializer(ModelSerializer):
    pass


class CategoriesApiListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TodosApiView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
