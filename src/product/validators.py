from core.validators import BaseValidation
from .crud import product_crud
from .models import Product


class ProductValidator(BaseValidation):
    pass


product_validator = ProductValidator(Product, product_crud)
