import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

logger = logging.getLogger(__name__)


def run():
    User = get_user_model()
    try:
        User.objects.create(
            username="defaultadmin",
            first_name="default",
            last_name="admin",
            email="defaultadmin@sbs.com",
            is_superuser=True,
            password=settings.SUPER_USER_PASSWORD,
        )
        logger.info("Createcd default admin")
    except IntegrityError:
        logger.info("Default admin already exists, skipping creation")
