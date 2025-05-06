from rest_framework import serializers

from .models import Status, Type, Category, SubCategory


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status 
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type 
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(),
        source='type',
        write_only=True
    )
    type = serializers.StringRelatedField()
    
    class Meta:
        model = Category 
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        source='category'
    )
    category = serializers.StringRelatedField()

    class Meta:
        model = SubCategory
        fields = '__all__'
       
