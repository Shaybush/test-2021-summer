from typing import Optional

def get_price(price: Optional[float] = None) -> str:
    if price is None:
        return "Price not available"
    return f"${price:.2f}"
