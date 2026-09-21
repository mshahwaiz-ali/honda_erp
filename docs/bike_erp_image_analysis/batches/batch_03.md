# BIKE-BATCH-03 — Dealer Customer, Cash Payment Voucher, and Advance Booking Analysis

## Batch scope

| Image ID | Source | Actual visible screen |
|---|---|---|
| BIKE-007 | `dealer_customer.png` | `DEALER CUSTOMER` |
| BIKE-008 | `booking.png` | `CASH PAYMENT VOUCHER` |
| BIKE-009 | `advance_booking_customer.png` | `ADVANCE BOOKING CUSTOMER` |

> Important evidence-quality finding: **`booking.png` is not a booking form.** Its visible screen title is `CASH PAYMENT VOUCHER`. File names are therefore useful inventory labels but are not trusted as the business truth; the visible UI remains authoritative.

---

# BIKE-007 — `dealer_customer.png`

## Screen classification

- **Visible title:** `DEALER CUSTOMER`
- **Type:** bike/dealer customer transaction or invoice-style form
- **Confidence:** high for visible fields; medium for exact accounting/document semantics

## Visible actions

- SAVE
- ADD NEW
- Find
- VIEW
- Last
- DELETE
- BACK
- PRINT

## Visible fields

### Document/header

- Sr no
- Invoice no #
- Date

### Dealer / company / item / vehicle

- Dealers Code
- adjacent dealer-name/lookup-style field
- Company Name
- Item Code
- adjacent item-name/lookup-style field
- Engine no
- Chassis no
- Brand
- Color

### End-customer identity

- Customer Name
- Father Name
- Cnic
- Mobile #
- Address

### Financial/tax panel

- Cost Price
- Sales Tax 18%
- N.E.V Levy
- Net Price

## Direct evidence

The form explicitly ties a transaction to:

- a dealer code
- a specific item
- engine number
- chassis number
- brand and color
- end-customer identity
- tax/levy amounts
- net price

This is strong evidence that Bike sales are **vehicle-unit-specific**, not quantity-only stock transactions.

## Tax evidence

`Sales Tax 18%` and `N.E.V Levy` are visible as separate financial components.

This proves the legacy form contains dedicated tax/levy fields. It does **not** prove:

- the tax base
- automatic calculation formula
- posting accounts
- exemption logic
- FBR submission behavior

Those remain separate requirements to verify later.

## Open relationship question

Batch 01 showed both:

- `DEALER CUSTOMER INVOICE`
- `DEALER SALE`

This screen is likely related to the former, but the exact distinction between Dealer Customer and Dealer Sale remains unresolved until the Dealer Sale screenshot is analyzed.

---

# BIKE-008 — `booking.png`

## Screen classification

- **Visible title:** `CASH PAYMENT VOUCHER`
- **Type:** accounting/payment voucher
- **Confidence:** high

## Critical filename correction

The source filename is `booking.png`, but the screenshot visibly shows **CASH PAYMENT VOUCHER**.

For all later reconstruction:

- source filename is retained for traceability
- screen title/content is treated as authoritative
- no booking-form behavior will be inferred from this filename

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- LAST RECORD
- DELETE
- BACK

## Visible header fields

- Sr No.
- Ref Inv
- Booking #
- Date
- Payment Type

The visible Payment Type value is:

- `CLEAR`

The option set and meaning of `CLEAR` are unknown.

## Visible line-item grid

Columns:

- Pay To
- Ac Name
- Description
- Amount

Row controls include:

- `+` for adding/selecting a row
- `x` for removing a row

A `Total` field is visible at the bottom.

## Accounting evidence

This is a multi-line outgoing payment voucher. It supports:

- one voucher header
- multiple pay-to/account/description/amount lines
- total aggregation

The presence of both `Ref Inv` and `Booking #` directly shows that a cash payment voucher can carry references to invoice/booking identifiers.

What those references do operationally is not yet proven.

## ERPNext relevance — non-final

This should later be compared with standard ERPNext:

- Payment Entry
- Journal Entry
- party/account allocation
- reference-document allocation

Do not recreate the legacy grid until the actual accounting semantics are known.

---

# BIKE-009 — `advance_booking_customer.png`

## Screen classification

- **Visible title:** `ADVANCE BOOKING CUSTOMER`
- **Type:** bike advance-booking/customer reservation form
- **Confidence:** high

## Visible actions

- SAVE
- ADD
- VIEW
- FIND
- DELETE
- LAST
- PRINT
- BACK

## Visible context

- USER: `ADMIN`
- BRANCH: `REHMAN HONDA PALACE`

These are visible contextual values; they do not establish the full role/branch model.

## Visible dates and identifiers

- Delivery Date
- Invoice Date
- Sr No.
- Bill no

## Visible customer fields

- Customer Name
- Father Name
- C.N.I.C
- Address
- Mobile No
- City
- District
- Remarks

## Visible booking/vehicle fields

- Item Code
- adjacent item-description/lookup-style field
- Color
- Status

Visible status value:

- `WAITING`

This proves the booking record has a status field. Other status values and transitions are not visible.

## Visible financial fields

- Amount
- Advance
- Balance

The captured `Balance` shows `0`, but because the form is otherwise blank this does not prove a formula by itself.

## Strong workflow evidence

Unlike the menu-only evidence in Batch 01, this screenshot directly proves that advance booking stores:

- customer identity
- desired bike/item
- color
- intended delivery date
- booking status
- total amount
- advance amount
- balance amount

This gives us the first concrete model of a Bike booking/reservation record.

## Likely workflow hypothesis

A probable business sequence is:

`Advance Booking Customer → waiting/reservation → vehicle allocation/sale → remaining balance settlement`

The first node is proven. The downstream relationship is still a hypothesis and must be tested against:

- Cash Balance Receive
- Cash Sale
- Dealer Sale
- booking reports
- engine/chassis allocation evidence

---

# Cross-image findings

## 1. Booking references appear in accounting

The Cash Payment Voucher has a `Booking #` reference, while Advance Booking Customer creates a booking-oriented record with Bill/Sr identifiers and financial values.

This is evidence of a **relationship surface** between booking and accounting, but it does not yet prove automatic posting or allocation.

## 2. Vehicle identity and booking start at different levels

Dealer Customer includes:

- Engine no
- Chassis no

Advance Booking Customer includes:

- Item Code
- Color

but no visible engine/chassis fields in this captured viewport.

This suggests — but does not yet prove — that advance booking may reserve a model/color before a specific chassis/engine is allocated.

## 3. Customer identity is duplicated directly on business documents

Both Dealer Customer and Advance Booking Customer visibly contain customer identity/contact fields instead of only a customer-code field.

This is a legacy design observation. In ERPNext, we should later determine whether these values belong in standard Customer/Contact/Address masters plus transaction snapshots rather than duplicating a custom customer structure.

---

# Unknowns carried forward

- distinction between Dealer Customer Invoice and Dealer Sale
- dealer-code master and dealer-name source
- calculation of Cost Price / Sales Tax 18% / N.E.V Levy / Net Price
- whether tax fields are editable or calculated
- meaning/options of Cash Payment Voucher `Payment Type`
- exact role of `Ref Inv`
- exact role of `Booking #` on payment vouchers
- all Advance Booking status values and transition rules
- how/when an engine/chassis is assigned to a booking
- whether booking advance creates an accounting entry automatically
- how remaining booking balance is collected
- cancellation/refund behavior
- whether Delivery Date is promised, scheduled, or actual delivery date

---

# Batch completion status

**BIKE-BATCH-03: ANALYZED**

All three screenshots were manually reviewed at full resolution. The visible UI, not the filename, is treated as the evidence source.
