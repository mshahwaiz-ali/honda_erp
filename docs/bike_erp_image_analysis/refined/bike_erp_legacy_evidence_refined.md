# Bike ERP — Refined Legacy Evidence Specification

## Status

**Evidence phase complete: 45 / 45 Bike screenshots analyzed across 15 / 15 logical batches.**

This document is the consolidated business picture extracted from the legacy Bike-system screenshots. It is intentionally **not the implementation plan**. Its purpose is to provide a stable, evidence-based specification that can be used later for ERPNext planning without repeatedly re-reading screenshots.

Source-of-truth hierarchy:

1. original screenshots under `client_old/software_images_bike/`
2. per-batch evidence under `docs/bike_erp_image_analysis/batches/`
3. this refined consolidation

Where the evidence is incomplete, the gap is stated explicitly rather than filled with assumptions.

---

# 1. System boundary

The client historically ran a **Bike system** and a **Parts system** in parallel with separate records/accounting as the project baseline.

This document covers the **Bike system only**.

However, several Bike-side screenshots expose part-oriented content:

- a Bike Profit Report variant contains `Part No`
- Date Wise Profit output contains part/consumable-like item descriptions
- Daily Transaction includes `Market Purchase` and `Parts Sale Invoice` sections

These observations **do not prove** that Bike and Parts shared a database or accounting. They establish a boundary question that must be resolved with the client during later planning. Possible explanations include overlapping functionality, a shared report source, copied/reused reports, or partial integration.

Do not merge the two legacy systems solely because of these screenshots.

---

# 2. High-level functional footprint

The Bike system visibly contains:

- master data
- new-bike procurement
- inventory receiving
- vehicle-unit stock tracking
- quotations
- advance booking
- cash retail sales
- dealer/account sales
- used-bike purchasing
- used-bike sales
- customer/dealer transaction capture
- registration operations
- registration receipts/payments
- cash receipts
- cash payments
- journal vouchers
- balance collection
- account ledgers
- cash book
- general ledger
- expense/balance summaries
- purchase/order reports
- sales reports
- profit reports
- FIFO profit/stock-value reports
- consolidated daily transaction reporting

The application is therefore not just an invoice generator. It is a combined operational dealership + inventory + accounting/reporting system.

---

# 3. Core legacy masters

## 3.1 Head master

Visible Head fields include:

- Code
- Group Code
- Head Name
- TYPE
- Account Name
- City
- Area
- Address
- Cell 1
- Cell 2
- Fax
- Contact Person

### Evidence interpretation

The legacy `Head` record appears broader than a simple chart-of-accounts node because it combines account-style fields with contact/address details.

Possible business meanings include customer, dealer, supplier, ledger party, account, or multiple categories controlled by `TYPE` / `Group Code`.

**Not yet proven:** exact category model or one-to-one mapping to modern ERPNext masters.

---

## 3.2 Item master

Visible Item Registration fields include:

- Item Code
- Item
- Brand
- Catagory
- Barcode / QR Code
- Price
- Profit %
- Net Amount
- Purchase Rate
- Profit Amt
- Parts Sale Rate

### Evidence interpretation

The legacy item record stores both identification and commercial/pricing information.

The presence of `Parts Sale Rate` inside Bike evidence is another reason not to infer the Bike/Parts boundary solely from naming.

No pricing formula is proven by the blank screenshot.

---

# 4. Vehicle-unit identity

The Bike system repeatedly uses:

- Chassis No
- Engine No
- Model / Item
- Brand
- Colour
- Registration No

Vehicle identity is visible in:

- inventory receipt
- dealer-customer transaction
- cash sale
- dealer sale
- used-bike purchase
- used-bike sale
- registration tracking
- account/general ledger
- engine-wise stock report
- bike profit report
- sales reports

### Refined conclusion

A replacement must treat a motorcycle as more than a generic quantity item. The business needs a durable link between the ERP item/model and the physical bike unit identified by **engine + chassis**, with colour and registration-related context.

The exact ERPNext implementation is deliberately deferred.

---

# 5. New-bike procurement and stock receiving

## 5.1 Purchase Order

Visible header concepts:

- Sr No
- P.O No
- Date
- A/C Code
- account/name field
- From / To dates
- Ledger action

Visible line concepts:

- Code
- Product Name
- Part No
- Brand
- Colour
- Qty
- Rate
- Amount

## 5.2 Receive Inventory Bike

Visible header concepts:

- Sr No
- Date
- Delivery Order No
- Truck No

Visible line concepts:

- Qty
- P.O No
- Code
- Product Name
- Chassis No
- Engine No
- Colour
- Reg No
- Rate
- Amount

### Refined workflow evidence

The strongest supported procurement sequence is:

**Purchase Order → Receive Inventory Bike**

because receipt lines explicitly contain `P.O No`.

At receipt, the generic ordered bike/model becomes a physically identifiable unit through chassis and engine numbers.

### Still unknown

- whether a PO is mandatory for every receipt
- warehouse/godown structure
- supplier semantics of A/C Code
- approval/submission workflow
- stock/accounting posting timing
- chassis/engine uniqueness validation

---

# 6. Quotation

Quotation captures:

- Sr No
- M/S
- A/C
- Date
- Code
- Item
- Catagory
- Colours
- Qty
- Rate
- Registration Fee
- Amount
- Total

### Refined conclusion

The legacy system can quote a model/item, colour, quantity, rate and registration fee before sale.

A direct quotation-to-booking or quotation-to-sale conversion is **not proven**.

---

# 7. Advance booking workflow

## 7.1 Advance Booking Customer

Visible fields include:

- Delivery Date
- Invoice Date
- Sr No
- Bill No
- Customer Name
- Father Name
- CNIC
- Address
- Mobile No
- City
- District
- Remarks
- Item Code
- item lookup/description
- Colour
- Status
- Amount
- Advance
- Balance

Observed status:

- `WAITING`

## 7.2 Booking reports

Advance Booking Report exposes:

- Status filter
- Sr No
- Date / Received Date
- Issue Date
- CNIC
- Name
- Cell No
- Model
- Account No
- Amount

Rendered report confirms:

- WAITING-status filtering
- multiple waiting bookings
- amount total
- Issue Date may be blank for visible waiting records

## 7.3 Accounting references to booking

Cash Payment Voucher visibly contains:

- Booking #
- Ref Inv

Cash Sale Invoice visibly contains:

- Booking #

### Refined workflow hypothesis

The evidence supports this likely lifecycle:

**Advance booking → WAITING reservation → later bike allocation/sale → remaining balance settlement**

The booking form records model/item + colour but no visible chassis/engine, while completed sales use chassis/engine. This strongly suggests specific vehicle-unit allocation may happen later.

### Still unknown

- complete booking status list
- exact event that changes WAITING
- when chassis/engine is assigned
- cancellation/refund process
- whether Advance creates an automatic accounting entry
- whether Balance is collected specifically through Cash Balance Receive
- exact meaning of Issue Date / Account No

---

# 8. Cash retail sale

Cash Sale Invoice includes:

### Header / customer

- Sr No
- Ref No
- Institutional Sales
- Sale Type
- Date
- Customer Name
- Father Name
- CNIC
- Address
- Booking #
- City
- Company
- Mobile No

Observed:

- Sale Type = `CASH`
- Institutional Sales = `NO` in the captured form

### Vehicle / financial line

- Chassis No
- Engine No
- Model
- Color
- Qty
- Sale Rate
- Sales Tax 18%
- N.E.V Levy 1%
- Total

### Settlement

- Discount
- Reg. Charges
- Net
- Cash Receive
- Balance
- FBR Amount

### Output actions

- Invoice Print
- Receipt Print

### Refined conclusion

This is the main consumer-facing bike sale form and combines:

- customer identity
- booking reference
- physical bike identity
- tax/levy
- registration charge
- payment received
- remaining balance
- print outputs

An existing `FBR Amount` field is visible in the legacy form. This is evidence only; the new FBR integration remains intentionally deferred until the core ERP is built.

---

# 9. Dealer sale and dealer-customer flow

## 9.1 Dealer Sale Invoice

Header:

- Sr No
- Bill No
- Date
- A/c Code
- Previous Balance
- Dealer Name
- From / To
- Current Balance

Lines:

- Company
- Institutional Sale
- Chassis
- Engine No
- Model
- Colour
- Qty
- Retail
- Amount

Action:

- Cash Receive

### Refined conclusion

Dealer Sale is account/balance oriented and likely supports credit-style dealer transactions.

Previous and current balances are first-class form concepts.

## 9.2 Dealer Customer

Dealer Customer form captures:

- dealer code
- company
- item code
- engine
- chassis
- brand
- colour
- end-customer identity
- cost price
- Sales Tax 18%
- N.E.V Levy
- Net Price

### Critical unresolved distinction

The exact business difference between:

- `DEALER CUSTOMER INVOICE`
- `DEALER SALE INVOICE`

is not proven by screenshots.

This needs direct client clarification before implementation planning.

---

# 10. Used-bike lifecycle

## 10.1 Used Bike Purchase Invoice

Captures:

- account/customer
- product/code/brand
- engine no
- chassis no
- **IN QTY**
- rate
- amount

## 10.2 Used Bike Sale Invoice

Captures:

- account/customer
- chassis no
- engine no
- code/product/brand
- **OUT QTY**
- rate
- amount

### Refined conclusion

The screenshots establish a matched used-bike stock lifecycle:

**Used Bike Purchase = stock in**

**Used Bike Sale = stock out**

with engine/chassis identity retained.

### Still unknown

- seller-party semantics
- tax treatment
- ownership/inspection/document process
- valuation method
- refurbishment/expense handling
- payment settlement

---

# 11. Cash and voucher accounting

## 11.1 Cash Receive Voucher

Header:

- Sr No
- Ref Inv
- Date

Lines:

- Rec From
- A/c Name
- Description
- Amount

Total is visible.

## 11.2 Cash Payment Voucher

Header:

- Sr No
- Ref Inv
- Booking #
- Date
- Payment Type

Observed Payment Type:

- `CLEAR`

Lines:

- Pay To
- A/c Name
- Description
- Amount

## 11.3 Cash Balance Receive (Bike)

Header:

- Sr No
- Date
- Head of A/c
- Sub A/c

Lines:

- Bill No
- Customer Name
- Description
- Amount

### Refined conclusion

The legacy application distinguishes:

- generic receipt voucher
- generic payment voucher
- Bike-specific outstanding/bill balance receipt

Invoice and booking numbers are common accounting reference surfaces.

---

# 12. Journal voucher

JV Voucher includes:

- Voucher No
- Voucher Type
- Date
- Code
- A/C Name
- Narration
- Cheque No
- Pay Order
- DR/CR
- Debit
- Credit
- debit/credit totals

Additional actions include:

- Last Voucher
- All Vouchers
- Type Wise Report

### Refined conclusion

The Bike system contains a general manual journal-entry mechanism in addition to operational vouchers.

---

# 13. Accounting ledger structure

## 13.1 Cash Book

Rendered Cash Book shows:

- dedicated account `CASH IN HAND (BIKE)`
- opening balance
- Date
- Sr No
- Narration
- Status
- Debit
- Credit
- running Balance

Visible status examples include:

- ADV/BOOK
- C/P
- C/S

The exact abbreviations are not fully defined.

## 13.2 Accounts Ledger Form

Filters:

- branch
- from/to date
- A/c Name

Grid:

- Date
- Sr No
- Ref No
- Status
- Description
- Engine No
- Chassis No
- In Qty
- Out Qty
- Rate
- Debit
- Credit
- Balance

## 13.3 General Ledger output

Rendered GL includes the same operational + financial blend.

Visible sample statuses/descriptions include:

- SALE
- C/R
- CASH
- CHEQUE CLEAR
- DISCOUNT

### Refined conclusion

The legacy accounting layer is tightly coupled to source operational detail. Vehicle movement and accounting entries appear together in ledger reports.

For the replacement, this is evidence that users need traceability from accounting back to bike transactions—not evidence that a custom parallel GL should be built.

---

# 14. Registration workflow

Registration is a substantial sub-process.

## 14.1 Registration Form

Per vehicle, the tracker visibly includes:

- Chassis No
- Engine No
- Date
- Customer Name
- Reg No
- Letter status
- Letter Received Date
- Letter Delivered Date
- Documents status
- Documents Received Date
- Documents Delivered Date
- Documents Receive Name
- Agent Name
- Agent Date
- Amount

Observed status values across the screenshots include:

- PENDING
- RECEIVED
- DELIVERED
- DELIVERED TO EXC
- DELIVERED TO CUSTOMER/DEALER

The exact ownership of every option between Letter and Documents status is partly obscured by the open dropdowns, so it should be confirmed later.

## 14.2 Registration Received Voucher

Header:

- Sr No
- Ref Inv
- Date

Lines:

- Rec From
- A/c Name
- Description
- Reg. Rec
- Reg. Pay

## 14.3 Registration profitability

Two reports exist:

### Registration Profit Report

- Ref No
- Item Desc
- Name
- Received
- Pay Amt
- Profit

### Registration Profit Report (Outdoor)

- Item Name
- Reg Receive
- Reg Pay
- Net Profit

### Refined conclusion

Registration combines:

1. vehicle/document operational tracking
2. external-agent/process tracking
3. customer/dealer handoff
4. money received
5. money paid
6. profit reporting

`OUTDOOR` is a distinct business variant, but its exact definition remains unknown.

---

# 15. Purchase and stock reporting

## Pending Order Report

Filters:

- Order No
- Model

Columns:

- P.Order #
- Model Name
- Colour
- Order Qty
- Receive Qty
- Balance

This confirms fulfillment is monitored as ordered versus received quantity.

## Bike Purchase Order Report

Filters:

- Start Date
- End Date
- P.O No

Columns:

- Sr No
- Order Date
- P.O No
- Model Name
- Color
- Qty
- Rate
- Total

## Engine Wise Stock Report

Filters:

- Model
- Colour

Columns:

- Catagory
- Brand
- Chassis No
- Engine No
- Amount

Special action:

- `ONLY 30-JUN STOCK`

### Refined conclusion

The business requires both normal live stock reporting and a special 30-Jun stock view, likely connected to year-end reporting. Exact purpose must be confirmed.

---

# 16. Sales reporting

## Daily Cash Sale Report

Filters:

- date range
- model
- colour

Columns include:

- invoice/reference
- customer identity/contact
- item/model
- colour
- chassis
- amount

## Dealer Sale Report

Filters:

- date range
- dealer

Columns include:

- Comp No
- Reg No
- A/C Name
- model
- colour
- chassis
- engine
- amount

### Refined conclusion

Sales reporting is transaction-type-specific and strongly vehicle-unit-aware.

---

# 17. Profit and FIFO reporting

## 17.1 Bike Profit — vehicle view

Columns include:

- Date
- Type
- Item Name
- Engine No
- Chassis No
- Sale Rate
- Purchase Rate
- Qty
- Discount
- Profit Pcs
- Net Profit

## 17.2 Bike Profit — alternate item/part view

Columns include:

- Date
- Name
- Item Name
- Part No
- Qty
- Total Sale
- Total Purchase
- Net Profit

## 17.3 Date Wise Profit

Rendered output includes:

- Date
- Item Name
- Part No
- Qty
- Total Sale
- Total Purchase
- Net Profit

The visible data contains part/consumable-style items.

## 17.4 Item Wise FIFO — profit view

Filters:

- date range
- item code

Columns:

- Sale Qty
- Sale Rate
- Purchase Rate
- Total Sale
- Total Purchase
- Profit Qty
- Profit Amount

## 17.5 Item Wise FIFO — stock/value view

Columns:

- Date
- Item Name
- Part No
- In Qty
- Out Qty
- Stock
- Rate
- Value

### Refined conclusion

The legacy business depends on cost/profit and stock-value reporting, with the UI explicitly labelling some views FIFO.

The exact FIFO algorithm is not visible and should not be reverse-engineered from labels alone.

---

# 18. Balance and summary reporting

## Cash Book Report

- Date
- Sr No
- Narration
- Status
- Debit
- Credit
- Balance

## All Balance & Summary Report

Filter:

- Head Name
- date range

Columns:

- Account ID
- Name
- Area
- Opening Balance
- Debit
- Credit
- Balance

## Expense Summary Report

Filter:

- Head Name
- date range

Columns:

- Account ID
- Name
- Amount

## Cash Balance Report anomaly

The screen titled `CASH BALANCE REPORT` visibly contains:

- Bill No
- Name
- Cell No
- Reg Receive
- Reg Pay
- Net Profit

This resembles registration financial reporting more than a conventional cash-balance report.

### Refined conclusion

Legacy naming cannot be treated as a reliable specification. Business behavior and visible fields are more trustworthy.

---

# 19. Consolidated Daily Transaction report

The rendered `DAILY TRANSACTION` report is one of the strongest cross-module artifacts.

Visible sections include:

- Purchase
- Market Purchase
- Parts Sale Invoice
- Cash Sale Invoice Bike
- Dealers Sale Invoice Bike
- payment activity

It combines operational fields such as:

- invoice no
- delivery no
- PO/godown
- item code/name
- brand
- quantity
- sale rate
- chassis
- registration number
- customer detail

with payment/source information.

### Refined conclusion

Users likely rely on a single daily operational summary spanning multiple transaction categories.

This is a strong candidate requirement for a consolidated ERPNext report/dashboard later.

### Boundary caution

The presence of Parts Sale Invoice inside this Bike-side captured report is a **real evidence conflict** with the simplified idea of completely isolated functional domains. It must be clarified with the client; it is not permission to merge the two systems automatically.

---

# 20. Legacy report delivery behavior

Many interactive report forms provide:

- Refresh
- Report Run (RDF)
- Generate Sheet
- Back

The system therefore supports:

- on-screen table
- rendered/PDF-style Oracle report
- spreadsheet export

The replacement should preserve the business need for printable/exportable reporting, without copying Oracle-specific implementation.

---

# 21. Evidence-backed workflow map

The following is the strongest consolidated workflow map supported by the screenshots.

## Procurement / new stock

`Purchase Order`
→ `Receive Inventory Bike`
→ chassis/engine identified stock
→ stock/reporting
→ sale

## Advance booking

`Advance Booking Customer`
→ status `WAITING`
→ booking reports
→ likely later vehicle allocation
→ Cash Sale / another sale path
→ balance settlement

The middle/later transitions remain partly inferred.

## Cash sale

customer + booking reference if applicable
→ vehicle chassis/engine
→ rate/tax/levy
→ discount/registration charge
→ cash receive
→ balance
→ invoice/receipt print

## Dealer sale

dealer account
→ previous balance
→ vehicle sale lines
→ current balance
→ cash receive

## Used bike

`Used Bike Purchase` with IN QTY
→ used-bike stock
→ `Used Bike Sale` with OUT QTY

## Registration

sold/identified bike
→ registration row
→ letter/document statuses
→ agent/process dates
→ registration receipts/payments
→ registration profit reporting

## Accounting

operational transaction
→ receipt/payment/JV/balance collection
→ account ledger / cash book / general ledger
→ balance / expense / summary reports

---

# 22. Known statuses / classifications

Directly observed:

## Booking

- WAITING

## Registration area

- PENDING
- RECEIVED
- DELIVERED
- DELIVERED TO EXC
- DELIVERED TO CUSTOMER/DEALER

## Accounting/report examples

- SALE
- C/R
- ADV/BOOK
- C/P
- C/S
- CASH
- CHEQUE CLEAR
- DISCOUNT
- Payment Type: CLEAR

These values are evidence of legacy classifications, not yet a proposed new status model.

---

# 23. Critical unresolved questions

These should be answered before the final implementation architecture is locked.

## Business boundary

- Why do Bike-side reports contain Parts Sale / part-like items?
- Were Bike and Parts truly separate databases, separate companies, separate ledgers, or just separate applications/interfaces?
- Is any reporting expected to combine them in the replacement?

## Parties / accounts

- What exactly is a legacy `Head`?
- What values exist for Head TYPE and Group Code?
- Which Heads are customers, dealers, suppliers, expenses, cash/bank, etc.?
- What distinguishes Dealer Customer from Dealer Sale?

## Booking

- full booking status lifecycle
- cancellation/refund rules
- advance-accounting treatment
- when a chassis/engine is allocated
- how Balance is settled

## Procurement / inventory

- supplier/account relationship
- warehouse/godown needs
- PO-to-receipt validation
- chassis/engine uniqueness
- stock adjustment fields/rules
- purpose of 30-Jun stock

## Cash/dealer sales

- exact tax bases
- N.E.V Levy rules
- Institutional Sale behavior
- registration-charge accounting
- discount rules
- dealer credit/payment rules
- FBR Amount meaning

## Registration

- exact Letter and Documents status lists
- meaning of EXC
- definition of Outdoor
- agent workflow
- profit formula
- relationship to sale/customer/dealer

## Accounting

- full status/type code dictionary
- voucher types
- invoice/bill allocation rules
- cheque/pay-order behavior
- opening-balance migration requirements

## Profit / FIFO

- official business definition of profit
- cost source
- FIFO algorithm expectation
- treatment of discounts/taxes/registration
- whether part-style profit belongs to Bike or Parts

---

# 24. Preliminary ERPNext fit map — not the implementation plan

The evidence strongly suggests that many legacy functions should first be mapped to standard ERPNext rather than rebuilt as custom forms.

## Standard ERPNext concepts to evaluate first

- Item
- Brand
- Item Group
- Barcode
- Customer
- Supplier
- Address
- Contact
- Account / Chart of Accounts
- Quotation
- Purchase Order
- Purchase Receipt
- Stock Entry / Stock Reconciliation
- Sales Invoice
- Payment Entry
- Journal Entry
- General Ledger
- stock valuation
- receivable/payable and accounting reports

## Likely custom or extended business areas to evaluate

- physical bike-unit identity around Engine No + Chassis No
- advance booking lifecycle
- registration operational workflow
- dealer-specific credit/balance UX
- used-bike acquisition/resale details
- dealership-specific consolidated Daily Transaction report
- specialized 30-Jun stock view
- selected legacy profitability/FIFO report layouts where standard ERPNext reports do not meet the verified need

### Guiding rule

**Use ERPNext as the accounting and inventory backbone. Customization should represent verified dealership workflow gaps, not reproduce Oracle screens one-for-one.**

---

# 25. FBR scope

The legacy Cash Sale Invoice visibly contains an `FBR Amount` field.

The new project requirement is to add the proper FBR invoicing/integration after the core ERP is complete.

Therefore:

- FBR is recorded as a confirmed future requirement.
- It should not distort the initial reconstruction of sales, inventory, booking, registration and accounting.
- Final FBR design will be handled as a dedicated later phase.

---

# 26. Evidence anomalies and cautions

1. `booking.png` actually shows **CASH PAYMENT VOUCHER**.
2. `CASH BALANCE REPORT` displays registration receive/pay/profit columns.
3. Bike-side reports expose parts/part-number activity.
4. Different report variants share the same title while exposing different data.
5. Legacy spelling/labels are inconsistent.
6. Screenshots reveal UI and visible behavior, not server-side validation/database logic.

These inconsistencies are useful. They show why the new ERP should be based on **business requirements**, not copied screen-for-screen.

---

# 27. Final evidence-phase conclusion

The screenshot set is sufficient to construct a strong first-pass functional specification of the Bike business:

- vehicle procurement and receipt
- physical unit identification
- booking
- retail/dealer/used-bike sales
- registration
- payments/receipts
- accounting
- profitability and stock reporting

It is **not sufficient** to prove every hidden rule or exact posting formula.

The next project phase should use this refined document plus the unresolved-question list to produce the ERPNext architecture and implementation plan. Until that planning phase begins, no custom DocType or workflow should be considered mandatory solely because a similarly named legacy form existed.
