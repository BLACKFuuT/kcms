from content.models import Category, Content
from rest_framework import serializers
        

 
class CategorySerializer(serializers.ModelSerializer):
    content_count = serializers.SerializerMethodField()

    def get_content_count(self, obj):
        return obj.contents.count()
    
    class Meta:
        model = Category
        fields = ["id", "name", "description", "content_count"]
        
class CategoryMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
        
        
class ContentSerializer(serializers.ModelSerializer):
    # 🔹 READ
    #category = CategoryMiniSerializer(read_only=True)
    category_name = serializers.StringRelatedField(read_only=True)
    author = serializers.StringRelatedField(source="created_by", read_only=True)

    # 🔹 WRITE
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
    )

    class Meta:
        model = Content
        fields = [
            "id",
            "title",
            "body",
            "is_active",
            "category",
            "category_name",
            "author",
            "created_at",
        ]
        read_only_fields = ["created_by", "created_at",]



