from database.base import BaseAccessor
from database.dataclasses import AdminDC
from database.models import Admin


class AdminAccessor(BaseAccessor):
    model = Admin
    model_dc = AdminDC
