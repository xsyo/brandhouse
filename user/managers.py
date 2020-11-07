from django.db.models import Manager


class UserManager(Manager):


    def __init__(self, role:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._role = role

    def get_queryset(self):
        
        return super().get_queryset().filter(role=self._role)