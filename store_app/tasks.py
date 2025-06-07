from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_notification_add_product(recepient_email, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email='lizet@mail.ru',
        recipient_list=[recepient_email],
    )
    return f'Send email to {recepient_email}'
