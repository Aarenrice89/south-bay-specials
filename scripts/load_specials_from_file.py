import json
import logging

from django.conf import settings

from apis.constants import LOCAL
from locations.models import Location
from specials.models import Special

logger = logging.getLogger(__name__)


def run():
    if not (settings.ENVIRONMENT == LOCAL or settings.BYPASS_LOAD_SPECIALS):
        logger.info(
            "Skipping loading specials from file as the environment is not LOCAL or BYPASS_LOAD_SPECIALS is set."
        )
        return
    if not settings.SPECIALS_LOAD_FILE:
        logger.info("No SPECIALS_LOAD_FILE specified, skipping loading specials.")
        return

    with open(settings.SPECIALS_LOAD_FILE) as file:
        specials = json.load(file)

    for special in specials:
        location, _ = Location.objects.get_or_create(**special.pop("location"))
        special, _ = Special.objects.get_or_create(location=location, **special)

    logger.info(f"Loaded {len(specials)} specials from {settings.SPECIALS_LOAD_FILE}.")
