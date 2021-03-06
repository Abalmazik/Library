from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.db.models import Count, Avg, Max, Min, Q, F
from rest_auth.registration.views import SocialLoginView, SocialConnectView

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import BookSerializer, AuthorDetailSerializer
from mylib.models import Book, Author


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer

    def get_queryset(self):
        count_books_after_1910 = Count('book',
                                       distinct=True,
                                       filter=Q(book__year__gt=1910))

        avg_page = Avg('book__number_page', distinct=True)

        min_page_before_1910 = Min('book__number_page',
                                   distinct=True,
                                   filter=Q(book__year__lt=1910))

        avg_rating = Avg('book__ratings__average')
        max_rating = Max('book__ratings__average')

        annotates = {
            'count_books_after_1910': count_books_after_1910,
            'avg_page': avg_page,
            'min_page_before_1910': min_page_before_1910,
            'avg_rating': avg_rating,
            'max_rating': max_rating
        }

        return super().get_queryset().annotate(**annotates)


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title', 'authors', 'year', 'publishing')
    ordering_fields = ('title', 'year', 'authors')

    def get_queryset(self):
        return super().get_queryset().annotate(rating_avg=F('ratings__average'))


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class GoogleConnect(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter