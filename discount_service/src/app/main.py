from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Discount Service")


class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    promocode: Optional[str] = None


class DiscountResponse(BaseModel):
    discount_percent: int
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "discount-service"}


@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest) -> DiscountResponse:
    if request.promocode == "STUDENT10":
        return DiscountResponse(
            discount_percent=10,
            reason="Promo code STUDENT10 applied",
        )

    if request.quantity >= 10:
        return DiscountResponse(
            discount_percent=15,
            reason="Bulk discount applied for 10 or more items",
        )

    if request.quantity >= 5:
        return DiscountResponse(
            discount_percent=10,
            reason="Bulk discount applied for 5 or more items",
        )

    if request.promocode:
        return DiscountResponse(
            discount_percent=0,
            reason=f"Promo code '{request.promocode}' is not valid",
        )

    return DiscountResponse(
        discount_percent=0,
        reason="No discount applies",
    )
