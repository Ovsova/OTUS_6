import pytest
from store_app.tasks import send_notification_add_product


@pytest.mark.django_db
def test_send_notification_task_enqueue():
    task_result = send_notification_add_product.delay(
        recepient_email='test@example.com',
        subject='Тест',
        message='Тестовое сообщение '
    )

    assert task_result is not None
    assert task_result.task_id is not None
    assert task_result.status in ('PENDING', 'SUCCESS')