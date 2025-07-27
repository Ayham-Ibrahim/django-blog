from rest_framework import serializers
from .models import Category,Post,Comment


class CategorySerializer(serializers,ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        


class PostSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # category_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all(), source='category', write_only=True
    # )
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    category = serializers.SlugRelatedField(slug_field = 'name',queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ['id', 'name', 'category']
        
        
class CommentSerializer(serializers.ModelSerializer):
      class Meta:
        model = Comment
        fields = ['id', 'text']
        
        
        # new edit by hala 

{
  "title": "عنوان المنشور",
  "content": "محتوى المنشور",
  "category": 1    # this 1 is the pk of model Category
}



# get by id:

{
  "title": "عنوان المنشور",
  "content": "محتوى المنشور",
  "category": 1    # this 1 is the pk of model Category
}


# get by name ""

{
  "title": "عنوان المنشور",
  "content": "محتوى المنشور",
  "category": "cat1"    # this 1 is the pk of model Category
}
