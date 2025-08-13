# GroceryMate - State Transition Testing & Coverage

## Requirement Questions (GroceryMate)

### Product Rating
1. How will ratings be averaged if a product has multiple reviews? Will all reviews have equal weight?
2. Should only verified buyers be allowed to rate products?
3. Is there a minimum/maximum rating value (e.g., 1–5 stars), and how will invalid ratings be handled?

### Age Verification
1. What is the minimum age for restricted products, and how will it vary by country?
2. Should the system block purchase at checkout or before adding to the cart?
3. How will the system verify the customer's age (e.g., ID upload, third-party verification)?

### Shipping Cost
1. What is the base shipping cost, and does it vary by region or delivery speed?
2. How should the system handle free shipping thresholds? Are they based on total price or number of items?
3. Will Prime members always get free shipping regardless of price or item count?

---

## State Transition Testing Example (Webshop Shipping)

| State | Event | Next State |
|-------|-------|------------|
| Start | User adds items | Cart Updated |
| Cart Updated | User checks out | Shipping Calculated |
| Shipping Calculated | Free shipping condition met | Order Placed |
| Shipping Calculated | Free shipping condition NOT met | Shipping Fee Added |
| Order Placed | Payment processed | Completed |

---

## Coverage Report

- Statement Coverage: Improved after adding boundary tests
- Branch Coverage: All branches tested including `C == False`
