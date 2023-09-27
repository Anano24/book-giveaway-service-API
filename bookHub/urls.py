from django.urls import path
from .views import TakeBookView, ReturnBookView

urlpatterns = [
    path('books/<int:book_id>/take/', TakeBookView.as_view(), name='take-book'),
    path('books/<int:book_id>/return/', ReturnBookView.as_view(), name='return-book'),
]
