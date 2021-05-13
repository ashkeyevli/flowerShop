from rest_framework import serializers

from _auth.serializers import CustomerSerializer, ManagerSerializer
from review.models import Review, Comment, Reply


class postContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('description', 'created_date')
    #
    # description = serializers.CharField(style={'base_template': 'textarea.html'})
    # created_date = serializers.DateField()
    #
    # def create(self, validated_data):
    #     postContent = Review.objects.create(**validated_data)
    #     return postContent
    #
    # def update(self, instance, validated_data):
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.created_date = validated_data.get('created_date', instance.created_date)
    #     instance.save()
    #     return instance

class ReviewSerializer(postContentSerializer):
    customer = CustomerSerializer(read_only=True)


    class Meta(postContentSerializer.Meta):
        model = Review
        fields = postContentSerializer.Meta.fields + ('title', 'rate', 'customer')

class ReplySerializer(postContentSerializer):
    review = ReviewSerializer(read_only=True)
    manager = ManagerSerializer(read_only=True)


    class Meta(postContentSerializer.Meta):
        model = Reply
        fields = postContentSerializer.Meta.fields + ('review', 'manager')

class ReplyForReviewSerializer(postContentSerializer):
    manager = ManagerSerializer(read_only=True)


    class Meta(postContentSerializer.Meta):
        model = Reply
        fields = postContentSerializer.Meta.fields + ('manager',)

class ReviewFullSerializer(ReviewSerializer):
    reply = ReplyForReviewSerializer(many= True, read_only=True)
    class Meta(ReviewSerializer.Meta):
        fields = ReviewSerializer.Meta.fields + ('reply',)