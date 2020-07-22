from django.contrib.auth.models import User

from rest_framework import serializers
from review.models import productReview

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = productReview
        fields = [ 'id','rating','comment','item','user']

        def save(self):
            ID = self.validated_data['item'],
            review = productReview(
                    user = self.user,
                    rating = self.validated_data['rating'],
                    comment = self.validated_data['comment'],
                    item =  product.objects.get(id=ID)
                )
            review.save()
            return review

class UserSerializer(serializers.ModelSerializer):
    reviews  = serializers.PrimaryKeyRelatedField(many=True, queryset=productReview.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'reviews']
        depth = 1   