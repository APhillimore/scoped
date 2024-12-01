from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserCreatedModel(BaseModel):
    # created_by = models.ForeignKey(
    #     "tenant.TenantUser", on_delete=models.PROTECT, null=True
    # )
    # tenant = models.ForeignKey(
    #     "tenant.Tenant", on_delete=models.PROTECT, null=True
    # )  # schedule for removal

    class Meta:
        abstract = True
