from rest_framework.serializers import ModelSerializer,SerializerMethodField
from blogs.models import Blog,Tag,Review
from users.models import Profile


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class BlogSerializer(ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    reviews = SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_reviews(self,obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews,many=True)
        return serializer.data



