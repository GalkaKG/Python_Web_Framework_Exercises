from rest_framework.serializers import ModelSerializer

from todos_rest_workshop.todos_api.models import Todo, Category





class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
