# BIKE-BATCH-04 — Quotation, Purchase Order, and Bike Inventory Receipt

## Batch scope

This batch gives the first direct evidence of the new-bike quote-to-procurement-to-receipt area. It proves document structures and a visible P.O. reference on inventory receipt, but does not prove automatic document creation or posting.

---

# BIKE-010 — `quotation.png`

- **Visible title:** QUOTATION
- **Type:** quotation / customer offer transaction
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- VIEW
- FIND
- LAST RECORD
- DELETE
- PRINT
- BACK

## Visible fields / filters

- Sr no
- M / S
- A / C
- Date

## Visible grid/report columns

- CODE
- ITEM
- CATAGORY
- Colours
- QTY
- RATE
- Registration Fee
- AMOUNT

## Direct evidence

- Quotation supports multiple line items with quantity, rate, registration fee and amount.
- The quotation header contains both M/S and A/C fields; exact business meaning/options are not visible.
- A document total is shown at the bottom.

## Inferences — not yet proven

- Registration fee can be quoted together with the bike/item line, but later invoicing/accounting treatment is not proven.

## Unknowns carried forward

- Meaning of M/S
- Meaning/source of A/C
- Whether quotation converts directly to a sale/booking
- Tax treatment on quotation

---

# BIKE-011 — `purchase_order.png`

- **Visible title:** PURCHASE ORDER
- **Type:** bike purchase order
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- LAST RECORD
- DELETE
- PRINT
- BACK
- LEDGER

## Visible fields / filters

- Sr No.
- P.O No
- DATE
- A/C CODE
- From
- To

## Visible grid/report columns

- CODE
- PRODUCT NAME
- PART NO
- BRAND
- COLOUR
- QTY
- RATE
- AMOUNT

## Direct evidence

- Purchase order is account-linked through A/C CODE plus an adjacent name/description field.
- The grid captures product identity, part number, brand, colour, quantity, rate and amount.
- A date-range plus LEDGER action is visible inside the purchase-order screen.
- A total amount field is present.

## Inferences — not yet proven

- A/C CODE likely identifies supplier/account, but the exact master type is not proven.

## Unknowns carried forward

- Supplier/account semantics of A/C CODE
- Purpose of embedded LEDGER date filter
- Approval/submission states
- Whether P.O. is mandatory for receiving

---

# BIKE-012 — `receive_inventory_bike.png`

- **Visible title:** RECEIVE INVENTORY BIKE
- **Type:** bike inventory receipt
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- LAST RECORD
- DELETE
- PRINT
- BACK

## Visible fields / filters

- Sr No.
- DATE
- DELIVERY ORDER NO
- TRUCK NO

## Visible grid/report columns

- QTY
- P . O NO
- CODE
- PRODUCT NAME
- CHASSIS NO
- ENGINE NO
- COLOUR
- REG NO
- RATE
- AMOUNT
- L
- X

## Direct evidence

- Inventory receipt records P.O. number per line.
- Receipt records vehicle-unit identifiers Chassis No and Engine No.
- Delivery Order No and Truck No are captured at document header level.
- Registration No can also be recorded on receipt lines.
- Rate, amount and overall total are visible.

## Inferences — not yet proven

- Purchase Order to Receive Inventory is strongly suggested by the line-level P.O. No field, but automatic linkage/validation is not shown.

## Unknowns carried forward

- Meaning of L button/control
- Whether serial/chassis uniqueness is enforced
- Warehouse/godown handling
- Accounting/stock posting timing

---

## Cross-image findings

- Batch 04 materially strengthens the procurement chain: Purchase Order and Receive Inventory are separate documents, and receipt lines carry a P.O. reference.
- Vehicle identity enters the stock process at receipt through chassis and engine numbers.
- Quotation and purchasing both carry item/model, colour, quantity, rate and amount concepts, but no direct quote-to-purchase relationship is implied.

## Preliminary ERPNext relevance — non-final

- Later compare Quotation with standard ERPNext Quotation.
- Later compare Purchase Order with standard ERPNext Purchase Order.
- Receive Inventory Bike should be compared with Purchase Receipt plus serial/batch/custom vehicle-identity handling before any custom receipt DocType is created.

## Batch completion status

**BIKE-BATCH-04: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
