# Bike Legacy System — Working Model Before ERPNext Planning

## Document status

**Phase:** system understanding  
**Implementation decisions:** intentionally not locked  
**Evidence basis:** 45 Bike-system screenshots analyzed across 15 logical batches  
**Purpose:** explain how the client's Bike software appears to operate as a business system before any ERPNext implementation plan is written.

This document is not a screen-copy specification and not an ERPNext customization plan.

It answers a more important question first:

> **What business process is this software actually supporting, how do its records appear to connect, and what must we understand before we rebuild it?**

Where a relationship is directly visible, it is marked **Observed**.  
Where the screenshots strongly suggest a relationship but do not prove it, it is marked **Likely**.  
Where the screenshots do not answer the question, it is marked **Unknown**.

---

# 1. Overall mental model

The Bike system appears to be a complete dealership operating system covering five connected areas:

1. **bike procurement and stock**
2. **customer/dealer sales and booking**
3. **registration processing**
4. **cash/accounting**
5. **operational and profitability reporting**

The main business object is not just an Item.

A motorcycle becomes operationally important as a **specific physical unit** identified by:

- model/item
- colour
- chassis number
- engine number
- sometimes registration number

That unit identity appears repeatedly across stock, sales, registration, ledger and profit reports.

---

# 2. Main records visible in the legacy system

The screenshots support the existence of the following conceptual records.

## Master / reference records

- Head
- Item
- Brand
- Category
- Dealer/account reference
- customer identity/details
- account names/codes

## Procurement / inventory records

- Purchase Order
- Receive Inventory Bike
- Stock Adjustment
- used-bike purchase
- physical bike unit identified by chassis + engine

## Sales / customer records

- Quotation
- Advance Booking Customer
- Cash Sale Invoice
- Dealer Sale Invoice
- Dealer Customer transaction/invoice
- Used Bike Sale Invoice
- cash-balance receipt

## Registration records

- Registration Form
- registration letter/document status
- registration agent details
- Registration Received Voucher

## Accounting records

- Cash Receive Voucher
- Cash Payment Voucher
- JV Voucher
- ledger entries
- cash book entries

## Reports

- booking/pending-order reports
- purchase reports
- sales reports
- engine-wise stock
- general ledger
- account ledger
- cash book
- balance summary
- expense summary
- bike profit
- registration profit
- FIFO profit/value
- daily consolidated transaction report

---

# 3. How new-bike procurement appears to work

## Step 1 — Purchase Order

**Observed**

The Purchase Order contains:

- P.O. number
- date
- account code/name
- item/product
- part number
- brand
- colour
- quantity
- rate
- amount

This is model/quantity-oriented procurement.

At this point the screenshot does not show a specific engine/chassis per ordered bike.

## Step 2 — Receive Inventory Bike

**Observed**

The receipt contains:

- delivery order number
- truck number
- P.O. number on the line
- product
- chassis number
- engine number
- colour
- registration number
- rate
- amount

This is the point where the evidence first clearly turns generic ordered quantity into individual physical motorcycle units.

## Working interpretation

**Likely**

```text
Purchase Order
    ↓
Receive Inventory Bike
    ↓
specific bike unit created/recognized
(model + colour + chassis + engine)
    ↓
available stock
```

The P.O. reference on receipt lines is strong evidence of this relationship.

## Still unknown

- whether every receipt requires a PO
- whether partial receiving is permitted
- whether over-receipt is permitted
- how warehouses/godowns are represented
- whether engine/chassis uniqueness is validated
- whether stock/accounting posting occurs on SAVE or another event

---

# 4. How bike stock appears to work

The system is strongly **unit-aware**.

Evidence repeatedly uses:

- Chassis No
- Engine No
- Colour
- Model/Item
- In Qty
- Out Qty
- Rate
- Amount

The Engine Wise Stock Report shows available stock by:

- category
- brand
- chassis
- engine
- amount

There is also a dedicated:

- Stock Adjust
- Stock Value/FIFO report
- special `ONLY 30-JUN STOCK` action

## Working interpretation

The old software likely keeps both:

1. item/model-level quantities
2. unit-level motorcycle identity

The replacement will need to preserve that distinction.

The exact future ERPNext mechanism is deliberately not decided here.

---

# 5. How advance booking appears to work

## Advance Booking Customer

**Observed**

The form records:

- customer name
- father name
- CNIC
- address
- mobile
- city/district
- item/model
- colour
- delivery date
- invoice date
- status
- amount
- advance
- balance

Observed booking status:

- `WAITING`

The booking screenshot does **not** visibly show engine/chassis fields.

## Booking reports

**Observed**

The report contains:

- received/date
- issue date
- customer identity/contact
- model
- account number
- amount
- status filtering

A rendered report specifically shows:

- Status: WAITING

Visible WAITING rows can have blank Issue Date.

## Working interpretation

**Likely**

A customer can reserve a model/colour before a specific physical motorcycle has been assigned.

A probable lifecycle is:

```text
customer requests bike
    ↓
Advance Booking Customer
    ↓
advance amount received / balance remains
    ↓
status = WAITING
    ↓
bike becomes available
    ↓
specific chassis/engine allocated
    ↓
final sale
    ↓
remaining balance settled
```

## Evidence linking booking to other screens

**Observed**

- Cash Sale Invoice contains `Booking #`
- Cash Payment Voucher contains `Booking #`
- Cash Payment Voucher also contains `Ref Inv`

This proves booking identifiers are used elsewhere in the system.

It does **not** prove automatic posting or conversion.

## Still unknown

- full booking status list
- booking cancellation
- refund behavior
- exact accounting entry for advance
- exact point when chassis/engine is assigned
- exact use of Issue Date
- whether booking converts automatically to Cash Sale
- whether balance is always settled through Cash Balance Receive

---

# 6. How Cash Sale appears to work

The Cash Sale Invoice is one of the most complete business screens.

## Customer / header information

**Observed**

- Ref No
- Date
- Sale Type
- Institutional Sales
- Customer Name
- Father Name
- CNIC
- Address
- Booking #
- City
- Company
- Mobile No

Observed examples:

- Sale Type = CASH
- Institutional Sales = NO

## Bike line

**Observed**

- Chassis No
- Engine No
- Model
- Colour
- Qty
- Sale Rate
- Sales Tax 18%
- N.E.V Levy 1%
- Total

## Settlement area

**Observed**

- Discount
- Registration Charges
- Net
- Cash Receive
- Balance
- FBR Amount

## Print outputs

- Invoice Print
- Receipt Print

## Working interpretation

A cash sale likely performs several business functions together:

```text
customer / optional booking
    ↓
select specific bike unit
(chassis + engine)
    ↓
calculate selling value
    ↓
tax / levy / discount / registration charges
    ↓
receive cash
    ↓
record any remaining balance
    ↓
print invoice / receipt
```

The exact financial formulas are not yet proven.

The visible `FBR Amount` confirms FBR-related data existed in the old form, but the future proper FBR integration is a separate later project phase.

---

# 7. How Dealer Sale appears to work

Dealer Sale is visibly different from Cash Sale.

## Observed dealer-sale concepts

- A/c Code
- Dealer Name
- Previous Balance
- Current Balance
- chassis
- engine
- model
- colour
- quantity
- retail
- amount
- Institutional Sale
- Cash Receive action

## Working interpretation

Dealer Sale is probably **account/credit oriented**.

A likely model is:

```text
dealer account
    ↓
existing balance
    ↓
bike(s) sold to dealer
    ↓
dealer receivable increases / balance changes
    ↓
cash receipt can later reduce balance
```

This is much closer to an account-based B2B sale than the consumer Cash Sale screen.

## Still unknown

- credit limits
- due dates / terms
- whether dealer sale can be cash-only
- exact previous/current balance formula
- how Cash Receive is linked
- Institutional Sale behavior

---

# 8. Dealer Customer versus Dealer Sale

This distinction is important and not yet fully resolved.

## Dealer Customer screen

**Observed**

It includes:

- dealer code
- company
- item code
- engine
- chassis
- brand
- colour
- end-customer name
- father name
- CNIC
- mobile
- address
- Cost Price
- Sales Tax 18%
- N.E.V Levy
- Net Price

## Working interpretation

The screen appears to connect:

```text
dealer
    +
specific motorcycle
    +
final/end customer
```

This may represent a dealer-mediated retail/customer-registration transaction.

However, that interpretation is not yet proven.

## Must be clarified

Before planning, we need the client's exact answer to:

> What business event is "Dealer Customer Invoice", and how is it different from "Dealer Sale Invoice"?

This is one of the highest-priority business questions.

---

# 9. How used-bike transactions appear to work

The used-bike flow is unusually clear from the screenshots.

## Used Bike Purchase

**Observed**

- Account Code
- Customer Name
- Engine No
- Chassis No
- Product/Brand
- **IN QTY**
- Rate
- Amount

## Used Bike Sale

**Observed**

- Account Code
- Customer Name
- Chassis No
- Engine No
- Product/Brand
- **OUT QTY**
- Rate
- Amount

## Working interpretation

```text
Used Bike Purchase
(IN QTY)
    ↓
used-bike stock
    ↓
Used Bike Sale
(OUT QTY)
```

The same physical identity concepts are retained through engine and chassis.

## Still unknown

- how seller ownership documents are handled
- bike condition/inspection
- repairs/refurbishment costs
- tax treatment
- seller should be considered Customer, Supplier, or generic party
- used-bike profit valuation method

---

# 10. How cash receipts and payments appear to work

The software has more than one money-entry screen.

## Cash Receive Voucher

**Observed**

- Ref Inv
- Date
- Rec From
- A/c Name
- Description
- Amount
- Total

Likely purpose:

incoming cash against accounts/invoices or other receipts.

## Cash Payment Voucher

The evidence capture is correctly named:

`cash_payment_voucher.png`

The visible screen title is:

`CASH PAYMENT VOUCHER`

**Observed**

- Ref Inv
- Booking #
- Date
- Payment Type
- Pay To
- A/c Name
- Description
- Amount
- Total

Observed Payment Type:

- CLEAR

Likely purpose:

outgoing payment against one or more accounts, optionally traceable to an invoice/booking.

## Cash Balance Receive (Bike)

**Observed**

- Head of A/c
- Sub A/c
- Bill No
- Customer Name
- Description
- Amount

## Working interpretation

The legacy system separates:

```text
generic cash receipt
generic cash payment
bike bill/balance collection
```

This distinction may reflect UI convenience rather than three fundamentally different accounting models.

That will be decided later when mapping to ERPNext.

---

# 11. Journal Voucher and manual accounting

JV Voucher provides a generic manual accounting mechanism.

**Observed**

- Voucher No
- Voucher Type
- account code/name
- narration
- cheque number
- pay order
- DR/CR
- debit
- credit
- debit/credit totals

This strongly supports a conventional double-entry accounting backbone.

---

# 12. What the ledgers tell us about posting

The strongest evidence that operational transactions and accounting are connected comes from the ledgers.

## Cash Book

Visible dedicated account:

- `CASH IN HAND (BIKE)`

Visible transaction/status examples:

- ADV/BOOK
- C/P
- C/S

It reports:

- opening balance
- debit
- credit
- running balance

## Account Ledger

It reports:

- date
- reference
- status
- description
- engine
- chassis
- In Qty
- Out Qty
- rate
- debit
- credit
- balance

## General Ledger

Visible examples include:

- SALE
- C/R
- CASH
- CHEQUE CLEAR
- DISCOUNT

## Working interpretation

Operational source transactions appear to feed a common accounting ledger.

The old software's ledger retains both:

- accounting values
- operational vehicle references

So users likely rely heavily on traceability:

```text
ledger line
    ↓
source transaction
    ↓
bike/customer/reference
```

This traceability is a business requirement even if the replacement data model is different.

---

# 13. How registration appears to work

Registration is clearly a standalone operational workflow, not just an invoice amount.

## Registration Form

**Observed**

per bike:

- Chassis No
- Engine No
- Date
- Customer Name
- Reg No
- Letter
- Letter Receive Date
- Letter Delivery Date
- Documents
- Documents Receive Date
- Documents Delivery Date
- Documents Receive Name
- Agent Name
- Agent Date
- Amount

Observed status values include:

- PENDING
- RECEIVED
- DELIVERED
- DELIVERED TO EXC
- DELIVERED TO CUSTOMER/DEALER

## Registration Received Voucher

**Observed**

- Ref Inv
- Rec From
- A/c Name
- Description
- Reg. Rec
- Reg. Pay

## Registration profit reports

**Observed**

normal registration:

- Received
- Pay Amt
- Profit

outdoor registration:

- Reg Receive
- Reg Pay
- Net Profit

## Working interpretation

Registration likely follows a lifecycle similar to:

```text
bike sold / customer identified
    ↓
registration record opened
    ↓
letter/documents processed
    ↓
external agent / authority interaction
    ↓
documents received
    ↓
documents delivered to customer/dealer
    ↓
registration money received / paid
    ↓
registration profit reported
```

## Still unknown

- exact meaning of EXC
- exact meaning of Outdoor registration
- exact status sequence
- agent settlement
- whether registration profit is recognized automatically

---

# 14. How purchase fulfillment is monitored

Pending Order Report explicitly contains:

- Order Qty
- Receive Qty
- Balance

This supports the working relationship:

```text
PO Qty
  ↓
one or more receipts
  ↓
received quantity
  ↓
pending/balance quantity
```

This is stronger evidence than simply seeing a PO number on a receipt.

---

# 15. How sales and stock are monitored

## Daily Cash Sale Report

tracks:

- invoice/reference
- customer
- mobile
- item/model
- colour
- chassis
- amount

## Dealer Sale Report

tracks:

- dealer/account
- model
- colour
- chassis
- engine
- amount

## Engine Wise Stock Report

tracks:

- category
- brand
- chassis
- engine
- amount

## Working interpretation

The dealership's day-to-day control depends on answering:

- which exact bikes are in stock?
- which exact bikes were sold?
- to whom?
- through cash or dealer channel?
- for what amount?

---

# 16. How profit appears to be monitored

The legacy system has several profitability views.

## Bike/unit profit

Visible dimensions include:

- engine
- chassis
- sale rate
- purchase rate
- discount
- net profit

## Item/part profit

Visible dimensions include:

- item
- part no
- qty
- total sale
- total purchase
- net profit

## FIFO profit/value

Visible dimensions include:

- Sale Qty
- Sale Rate
- Purchase Rate
- Total Sale
- Total Purchase
- Profit Amount

and another view:

- In Qty
- Out Qty
- Stock
- Rate
- Value

## Working interpretation

Management wants profitability visible at multiple levels:

- physical bike
- item/model
- date period
- registration activity
- inventory/FIFO value

The exact cost formula is not visible and must not be guessed.

---

# 17. Daily Transaction report — likely management control screen

The Daily Transaction rendered report includes sections such as:

- Purchase
- Market Purchase
- Parts Sale Invoice
- Cash Sale Invoice Bike
- Dealers Sale Invoice Bike
- payment activity

This suggests management wanted one report that answers:

> What happened today across the business?

It is likely operationally important even if the future implementation uses a completely different report engine.

---

# 18. Bike and Parts boundary

Project baseline:

- Bike system and Parts system were used as separate parallel systems
- separate records/accounting were desired by the client

However, Bike-side screenshots contain some part-oriented columns/reports.

Examples:

- Part No
- part-like Date Wise Profit rows
- Parts Sale Invoice section inside Daily Transaction

## Correct interpretation

This evidence means:

> the boundary needs clarification.

It does **not** mean:

> merge Bike and Parts accounting.

Possible explanations include:

- old report reuse
- partial shared reporting
- part sales available in both systems
- shared item code structures
- screenshots captured from overlapping menus
- common backend with separate operational/accounting groupings

This must be resolved during requirements clarification.

---

# 19. Likely data relationships

The following relationship model best fits the screenshots today.

```text
HEAD / PARTY / ACCOUNT
        │
        ├── Customer
        ├── Dealer
        ├── Supplier-like account
        └── expense/cash/other account roles
             (exact legacy TYPE mapping unknown)

ITEM / MODEL
        │
        ├── Brand
        ├── Category
        ├── Colour
        └── rates/pricing

PURCHASE ORDER
        │
        ▼
RECEIVE INVENTORY
        │
        ▼
BIKE UNIT
(engine + chassis)
        │
        ├─────────────► CASH SALE
        │
        ├─────────────► DEALER SALE
        │
        ├─────────────► DEALER CUSTOMER
        │
        └─────────────► REGISTRATION

ADVANCE BOOKING
(model + colour)
        │
        └──── likely later allocation ───► BIKE UNIT / SALE

USED BIKE PURCHASE
        │
        ▼
USED BIKE UNIT
        │
        ▼
USED BIKE SALE

SALES / BOOKING / OTHER TRANSACTIONS
        │
        ├── CASH RECEIVE
        ├── CASH PAYMENT
        ├── CASH BALANCE RECEIVE
        └── JV
                │
                ▼
        ACCOUNT / CASH / GENERAL LEDGERS
```

This is a working model, not a final schema.

---

# 20. What is directly known versus still hypothetical

## High-confidence business behavior

- new bikes are ordered and received
- bike units are identified by chassis and engine
- advance booking exists
- WAITING is a booking status
- cash sale exists
- dealer sale exists
- used-bike purchase and sale exist
- registration has a separate operational workflow
- registration has received/paid/profit accounting
- cash receipt/payment/JV screens exist
- debit/credit/running-balance ledgers exist
- stock/profit/FIFO reports exist
- dealer balances are visible
- bill/invoice/booking references appear across forms
- users need printable and spreadsheet reports

## Strong but not final hypotheses

- booking is converted/linked to later sale
- a specific bike unit is allocated after booking
- dealer sale is mainly a credit-account flow
- balance receipt settles outstanding sales/booking amounts
- PO is fulfilled by one or more inventory receipts
- registration starts after a sale/vehicle allocation
- source transactions feed a common ledger automatically

## Unknown and client-dependent

- approval workflows
- posting moment
- cancellation rules
- returns
- refund logic
- discount permissions
- tax formulas
- user roles
- stock warehouses
- dealer-credit controls
- exact Head TYPE mapping
- complete status dictionaries
- Bike/Parts technical/accounting boundary

---

# 21. Questions that must be answered before ERPNext planning is finalized

The highest-value questions are:

1. What exactly is a `Head` in business terms, and what TYPE values exist?
2. What is the exact difference between Dealer Sale and Dealer Customer Invoice?
3. What is the full advance-booking lifecycle from WAITING to final sale?
4. How is advance money accounted for and refunded/cancelled?
5. When is engine/chassis assigned to a booking?
6. Can one PO be received in multiple deliveries?
7. What stock locations/godowns exist?
8. What exactly does Stock Adjust allow?
9. What are the exact Sales Tax / N.E.V Levy / registration-charge rules?
10. What does Institutional Sale change?
11. What does FBR Amount mean in the old system?
12. What is Outdoor Registration?
13. What does EXC mean in registration statuses?
14. How do dealers pay outstanding balances?
15. What are the voucher/status abbreviations?
16. Which reports are actually used daily by management?
17. Why do Bike-side reports include Parts activity?
18. Are Bike and Parts separate databases, separate accounting books, separate companies, or separate interfaces over some shared data?
19. Which opening balances and historical records must move to the new ERP?
20. What role/permission restrictions exist for sales, purchasing, accounts, registration and reporting?

---

# 22. What we should NOT do yet

Before these questions are resolved, we should not:

- create custom DocTypes just because old screens existed
- copy Oracle Forms one-to-one
- build a parallel custom accounting engine
- assume every old report must be recreated exactly
- merge Bike and Parts accounting
- finalize role design
- finalize tax/FBR logic
- finalize deployment/payment-gating logic

Those are later decisions.

---

# 23. What this document enables next

This working model gives us a proper basis for the next phase:

1. validate ambiguous business rules
2. define the required business behavior
3. map each behavior to ERPNext standard functionality
4. identify true gaps
5. only then design custom forms/workflows
6. only then create the implementation plan

The intended replacement remains **ERPNext-first**:

> use standard ERPNext wherever it correctly represents the verified dealership process, and add custom wiring/forms/workflows only where the business genuinely requires them.

The immediate goal is therefore still **understanding**, not coding.
