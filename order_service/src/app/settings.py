# order_service/app/settings.py
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    product_service_url: str
    discount_service_url: str
    database_url: str


def get_settings() -> Settings:
    def required(name: str) -> str:
        value = os.getenv(name)

        if not value:
            raise RuntimeError(
                f"Environment variable '{name}' is required for order-service",
            )

        return value

    return Settings(
        product_service_url=required("PRODUCT_SERVICE_URL"),
        discount_service_url=required("DISCOUNT_SERVICE_URL"),
        database_url=os.getenv(
            "DATABASE_URL",
            "postgresql://app:app@127.0.0.1:5432/orders",
        ),
    )