import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    MANAGER = "MANAGER", "Manager"
    SALES_REP = "SALES_REP", "Sales Representative"

    
class User(AbstractUser):
    """
    Custom User pour ClientFlow :
    - UUID comme clé primaire
    - email utilisé comme identifiant
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    username = None  # suppression du champ username
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.SALES_REP,
    )

    @property
    def is_admin(self) -> bool:
        return self.role == UserRole.ADMIN

    @property
    def is_manager(self) -> bool:
        return self.role == UserRole.MANAGER

    @property
    def is_sales_rep(self) -> bool:
        return self.role == UserRole.SALES_REP