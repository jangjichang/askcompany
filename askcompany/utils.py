import os
from uuid import uuid4
from django.utils import timezone

def uuid_upload_to(instance, filename):
    uuid_name = uuid4().hex
    ext = os.path.splitext(filename)[-1].lower()

    return '/'.join([
        uuid_name[:2], # 256가지 조합
        uuid_name[2:4],
        uuid_name[4:] + ext
    ])


def uuid_name_upload_to(instance, filename):
    app_label = instance.__class__._meta.app_label
    cls_name = instance.__class__.__name__.lower()
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return '/'.join([
        app_label,
        cls_name,
        ymd_path,
        uuid_name[:2],
        uuid_name + extension,
    ])