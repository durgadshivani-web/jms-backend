from rest_framework.viewsets import ModelViewSet
from .models import Paper, Review
from .serializers import PaperSerializer, ReviewSerializer


class PaperViewSet(ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
