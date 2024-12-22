from django.urls import path
from Library_Users.views import (signup_view, login_view,
                                 verify_email_view, confirm_email)  # email_send_view


urlpatterns=[
    path('signup/', signup_view, name='signup'),
    path('login/',  login_view, name='login'),

    path('verify/', verify_email_view, name='verify'),
    path('confirm_email/<uidb64>/<token>/', confirm_email, name='confirm_email'),

    #path('send_email/', email_send_view, name='send_email'),
]