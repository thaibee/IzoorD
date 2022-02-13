from django.db import models
from IzoorD.mssql_uuid import MssqlUUID


class Testing(models.Model):
    id = MssqlUUID(primary_key=True, max_length=36, editable=False, default=None)
    name = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        db_table = 'testing'

    def __str__(self):
        return self.name
