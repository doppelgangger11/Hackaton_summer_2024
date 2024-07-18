from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', playbill_list, name='playbill_list'),
    path('accounts/password/reset/', auth_views.PasswordResetView.as_view(template_name="account/password_reset_form.html"), name='password_reset'),
    path('accounts/password/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"), name='password_reset_complete'),
    path('buy-ticket/<int:playbill_id>/', buy_ticket, name='buy_ticket'),
    path('confirm-purchase/<int:ticket_id>/', confirm_purchase, name='confirm_purchase'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
