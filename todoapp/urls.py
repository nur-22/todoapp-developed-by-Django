from django.urls import path
from .views import index, home, about, deleteTodo, footer

urlpatterns = [
    path('', index, name="index"),
    path('home/', home, name="home"),
    path('about/', about, name="about"),
    path('delete-todo/<int:id>/', deleteTodo, name='deleteTodo'),
    path('components/footer/',footer, name='footer')
]
