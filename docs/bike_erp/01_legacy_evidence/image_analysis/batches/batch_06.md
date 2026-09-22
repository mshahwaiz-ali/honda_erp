# BIKE-BATCH-06 — Used-Bike Purchase and Cash Collection Vouchers

## Batch scope

This batch closes the visible used-bike buy/sell pair and distinguishes generic cash receipts from the bike-specific cash-balance collection screen.

---

# BIKE-016 — `used_bike_purchase_invoice.png`

- **Visible title:** USED BIKE PURCHASE INVOICE
- **Type:** used-bike purchase / stock-in transaction
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- DELETE
- LAST RECORD
- PRINT
- BACK

## Visible fields / filters

- Sr No
- Ref No
- DATE
- Account Code
- Customer Name

## Visible grid/report columns

- CODE
- PRODUCT NAME
- BRAND
- ENG NO.
- CH NO.
- IN QTY
- RATE
- AMOUNT
- L
- X

## Direct evidence

- Used-bike purchasing is a dedicated transaction.
- The transaction captures account/customer identity plus engine/chassis.
- An explicit IN QTY is recorded.
- Rate, amount, total quantity and total amount are present.

## Inferences — not yet proven

- Together with Used Bike Sale OUT QTY, this provides strong evidence of a stock-in/stock-out lifecycle for used bikes.

## Unknowns carried forward

- Whether seller should be a supplier or customer in business semantics
- Inspection/condition fields
- Ownership/document checks
- Accounting/tax posting

---

# BIKE-017 — `cash_receive_voucher.png`

- **Visible title:** CASH RECEIVE VOUCHER
- **Type:** multi-line incoming cash/accounting voucher
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- LAST RECORD
- DELETE
- BACK

## Visible fields / filters

- Sr No
- Ref Inv
- Date
- Total

## Visible grid/report columns

- Rec From
- Ac Name
- Description
- Amount

## Direct evidence

- Incoming cash voucher supports multiple receipt lines.
- A Ref Inv field is available at header level.
- Each line records receipt source, account name, description and amount.
- A total is visible.

## Inferences — not yet proven

- Ref Inv may link receipts to sales invoices, but allocation behavior is not shown.

## Unknowns carried forward

- Whether Rec From is party code or text
- How accounts are selected
- Whether one receipt can allocate across multiple invoices
- Posting/approval rules

---

# BIKE-018 — `cash_balance_receive.png`

- **Visible title:** CASH BALANCE RECEIVE (BIKE)
- **Type:** bike-specific outstanding/balance collection
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- LAST RECORD
- DELETE
- BACK

## Visible fields / filters

- Sr No.
- Date
- head of A/c
- Sub A/c

## Visible grid/report columns

- Bill No.
- Coustomer Name
- Discriptoin
- Amount

## Direct evidence

- This is a distinct Bike-specific balance-receipt form, separate from generic Cash Receive Voucher.
- The header uses Head of A/c and Sub A/c account selectors.
- Receipt lines are explicitly bill-number/customer/description/amount oriented.

## Inferences — not yet proven

- This screen likely collects outstanding balances against prior bike bills, consistent with cash-sale and dealer-sale balance concepts.

## Unknowns carried forward

- Source documents eligible for Bill No
- Whether booking balances use this form
- Head/Sub Account hierarchy semantics
- Partial allocation behavior

---

## Cross-image findings

- Used Bike Purchase and Used Bike Sale form an explicit IN QTY / OUT QTY pair around engine/chassis-identified units.
- The system distinguishes generic incoming cash voucher entry from Bike-specific bill-balance collection.
- Invoice/bill references are recurring accounting link surfaces across payment and receipt screens.

## Preliminary ERPNext relevance — non-final

- Used-bike buying may map to standard purchase/stock concepts plus vehicle master/serial identity, but seller-party semantics need clarification.
- Cash Receive and Cash Balance Receive should later be compared with ERPNext Payment Entry/reference allocation rather than copied literally.

## Batch completion status

**BIKE-BATCH-06: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
