from rest_framework import serializers

from apps.references.models import Status, Type, Category, SubCategory
from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
        source='status',
        write_only=True
    )
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(),
        source='type',
        write_only=True
    )
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )
    subcategory_id = serializers.PrimaryKeyRelatedField(
        queryset=SubCategory.objects.all(),
        source='subcategory',
        write_only=True,
        many=True
    )
    status = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Record 
        fields = '__all__'
    
    def validate(self, attrs):
        category = attrs.get('category')
        type = attrs.get('type')
        subcategory = attrs.get('subcategory')

        if category and type and category.type != type:
            raise serializers.ValidationError(
                'Выбранная категория не относится к выбранному типу!'
            )
        
        if subcategory and category:
            for subcat in subcategory:
                if subcat.category != category:
                    raise serializers.ValidationError(
                        'Выбранная подкатегория не относится к выбранной категории!'
                    )

        return attrs