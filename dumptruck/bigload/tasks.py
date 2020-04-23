import json
import time
from celery import shared_task
from bigload.models import Trash


@shared_task
def create_trash(title, contents):

    time.sleep(2)
    trash = Trash(title=title, contents=contents)
    trash.save()

    return
