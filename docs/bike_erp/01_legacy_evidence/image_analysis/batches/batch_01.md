# BIKE-BATCH-01 — Legacy Bike ERP Menu Analysis

## Batch scope

This batch establishes the **top-level navigation and functional footprint** of the legacy Bike system. It contains three screenshots of the same Oracle Forms-style main menu at different scroll/expand states:

| Image ID | Source |
|---|---|
| BIKE-001 | `client_old/software_images_bike/menu.png` |
| BIKE-002 | `client_old/software_images_bike/menu_bike.png` |
| BIKE-003 | `client_old/software_images_bike/menu_bike_2.png` |

The screenshots are treated as **evidence of visible capabilities only**. Menu names do not by themselves prove database structure, accounting posting logic, validation rules, or exact workflow order.

---

## Cross-image conclusions

### 1. The Bike application is broader than a simple sales screen

**Observed with high confidence:** the visible navigation covers at least:

- bike inventory / purchasing / receiving
- quotations
- used-bike purchasing
- cash and dealer sales
- used-bike sales
- customer/dealer-oriented invoicing
- booking / advance-booking activity
- registration activity and registration receipts
- cash receipt and cash payment vouchers
- journal vouchers
- accounting/general/profit/bike reports
- item and account/head maintenance
- FIFO-oriented reporting

This is important for reconstruction: the Bike application appears to combine **operational bike dealership workflows and accounting/reporting functions in one legacy application**.

### 2. The menu is a hierarchical expandable tree

**Observed:** the left navigation uses parent menu groups with expandable/collapsible children. The three screenshots capture different expanded states and scroll positions rather than three independent applications.

Visible top-level groups include:

1. `BIKE INVENTORY MENU`
2. `ACCOUNTS MENU`
3. `REPORTS MENU`
4. `ADMIN MENU`
5. `SALES MENU`
6. `FIFO REPORTS`

### 3. The application identity is Bike-side dealership software

**Observed:**

- window title: `Computerized Accounts`
- dealership branding: `RAHMAN HONDA PALACE`
- Atlas Honda branding is shown in the main work area
- `ADMIN` appears as the current main-panel heading/user context

No conclusion is drawn here about the exact meaning of `ADMIN` beyond what is visible.

---

# BIKE-001 — `menu.png`

## Screen classification

- **Type:** main application menu / navigation screen
- **Confidence:** high
- **Purpose observed:** provides access to Bike inventory, accounting, reporting, administration, sales and FIFO-report areas.

## Visible global application chrome

The Oracle Forms-style frame visibly includes the global menus:

- Action
- Edit
- Query
- Block
- Record
- Field
- Help
- Window

A toolbar with standard legacy form/navigation icons is also visible.

These controls are framework-level UI, not evidence that every business screen uses every Oracle Forms action.

## Visible business navigation

### BIKE INVENTORY MENU

Observed child entries:

- `DEALER CUSTOMER INVOICE`
- `PURCHASE ORDER (BIKE)`
- `RECEIVE INVENTORY (BIKE)`
- `CASH BALANCE RECEIVE`
- `REGISTRATION FORMS`
- `BIKE QUOTATION`
- `USED BIKE PURCHASE`

### ACCOUNTS MENU

Observed child entries:

- `CASH RECEIVE VOUCHER`
- `CASH PAYMENT VOUCHER`
- `JV VOUCHER`
- `ADVANCE BOOKING CUSTOMER`
- `REGISTRATION RECEIVE VOUCHER`

### REPORTS MENU

The top-level report group is visible, but this screenshot does not expose all of its children clearly. BIKE-002 and BIKE-003 provide the expanded report menu.

### ADMIN MENU

Observed child entries:

- `ADD NEW ITEM`
- `ADD NEW HEAD`

### SALES MENU

Observed child entries:

- `CASH SALE`
- `DEALER SALE`
- `USED BIKE SALE`

### FIFO REPORTS

The `FIFO REPORTS` top-level group is visible near the lower edge. Its children are not visible in this screenshot.

## Evidence-level implications

### Inventory / stock

Observed menu names demonstrate dedicated functionality for:

- purchasing bikes
- receiving bike inventory
- used-bike purchasing
- item setup
- FIFO reports

This strongly supports the existence of stock/inventory concepts, but **does not yet prove** exact stock valuation rules, warehouses, serial-number behavior, or ledger posting.

### Sales

Observed menu names distinguish:

- cash sale
- dealer sale
- used-bike sale

The separation implies multiple sales scenarios in the legacy system. Their field differences and accounting effects must be verified from their own screenshots.

### Booking / receivables

`CASH BALANCE RECEIVE` and `ADVANCE BOOKING CUSTOMER` are visible as separate functions.

A likely relationship to customer balances, booking advances or later settlement exists, but that relationship is **inferred, not yet proven**.

### Registration

Two separate registration-related functions are visible:

- `REGISTRATION FORMS`
- `REGISTRATION RECEIVE VOUCHER`

This suggests that registration is not just a printed field on an invoice; the legacy system has dedicated registration processing and receipt functionality. Exact workflow remains unknown until registration screenshots are reviewed.

### Accounting

Dedicated voucher entries exist for:

- cash receipt
- cash payment
- journal voucher

This is direct evidence that the legacy Bike system contains accounting transaction entry points.

---

# BIKE-002 — `menu_bike.png`

## Screen classification

- **Type:** same main navigation screen, report section expanded
- **Confidence:** high

## Reconfirmed menu areas

The screenshot reconfirms:

- BIKE INVENTORY MENU
- ACCOUNTS MENU
- REPORTS MENU

The visible Bike Inventory and Accounts child entries match BIKE-001.

## Expanded REPORTS MENU

Observed child report groups:

- `ACCOUNTS REPORTS`
- `GENERAL REPORTS`
- `PROFIT REPORTS`
- `BIKE REPORTS MENU`

## Evidence-level implications

The report menu is itself hierarchical. This indicates the application likely has a significant report catalogue rather than one generic reporting screen.

Observed categories establish at least four report domains:

1. accounting
2. general/operational
3. profit
4. bike-specific

No specific report names should be inferred from these categories alone; later screenshots provide concrete report evidence.

---

# BIKE-003 — `menu_bike_2.png`

## Screen classification

- **Type:** same main navigation screen, lower portion visible with Admin and Sales expanded
- **Confidence:** high

## Reconfirmed REPORTS MENU

Visible report groups:

- `ACCOUNTS REPORTS`
- `GENERAL REPORTS`
- `PROFIT REPORTS`
- `BIKE REPORTS MENU`

## Expanded ADMIN MENU

Observed child entries:

- `ADD NEW ITEM`
- `ADD NEW HEAD`

### Interpretation

`ADD NEW ITEM` clearly indicates an item/master-maintenance capability.

`ADD NEW HEAD` very likely refers to an accounting head/account master in the context of the Accounts system, but the exact data model is **not proven by the menu alone**. BIKE-005 (`head_form.png`) is expected to provide direct evidence later.

## Expanded SALES MENU

Observed child entries:

- `CASH SALE`
- `DEALER SALE`
- `USED BIKE SALE`

### Interpretation

The legacy application intentionally distinguishes at least three sale transaction types. This distinction must be preserved as a **business requirement to investigate**, not automatically copied as three custom ERPNext DocTypes.

During later ERPNext design we should determine whether these are:

- one standard Sales Invoice flow with different customer/payment/stock behavior,
- different workflows around standard sales documents,
- or genuinely different transaction models requiring customization.

No decision is made at this analysis stage.

## FIFO REPORTS

The `FIFO REPORTS` parent group is visible and appears collapsed. Child report names are not visible in this batch.

---

# Consolidated menu inventory from Batch 01

| Area | Visible functions |
|---|---|
| Bike Inventory | Dealer Customer Invoice; Purchase Order (Bike); Receive Inventory (Bike); Cash Balance Receive; Registration Forms; Bike Quotation; Used Bike Purchase |
| Accounts | Cash Receive Voucher; Cash Payment Voucher; JV Voucher; Advance Booking Customer; Registration Receive Voucher |
| Reports | Accounts Reports; General Reports; Profit Reports; Bike Reports Menu |
| Admin | Add New Item; Add New Head |
| Sales | Cash Sale; Dealer Sale; Used Bike Sale |
| FIFO | FIFO Reports parent group visible; children not yet visible |

---

# Relationships suggested by the menu — not yet proven

The following are **working hypotheses only** and must be validated against later screenshots:

1. **Purchase Order (Bike) → Receive Inventory (Bike)** may represent the new-bike procurement/receipt chain.
2. **Bike Quotation → Cash Sale or Dealer Sale** may represent quotation-to-sale processing.
3. **Advance Booking Customer → later bike allocation/sale/balance receipt** may be part of a booking workflow.
4. **Cash Balance Receive** may settle an outstanding amount arising from booking or a sale.
5. **Registration Forms → Registration Receive Voucher** may separate operational registration processing from money collection.
6. **Used Bike Purchase → Used Bike Sale** likely forms a used-bike acquisition/resale lifecycle.
7. Voucher entry screens likely feed accounting reports and possibly the General Ledger, but that posting relationship must be confirmed from later evidence.

---

# Preliminary ERPNext relevance — intentionally non-final

This section is only a future-planning pointer. It is **not an implementation decision**.

Several visible legacy capabilities have obvious ERPNext concepts that should be evaluated before creating custom functionality:

- item master
- customer/dealer records
- purchase orders
- purchase receipts / stock receipts
- quotations
- sales invoices
- payment entries / receipts / payments
- journal entries
- general ledger and accounting reports
- stock valuation / stock reports

Potential areas that may need workflow customization or dedicated extensions, depending on later evidence:

- advance bike booking
- bike-specific balance collection
- registration workflow
- used-bike lifecycle
- dealer-sale differences
- FIFO-specific legacy reports
- dealership-specific profitability/reporting

The project rule remains: **use standard ERPNext where it correctly models the requirement; customize only the uncovered gaps.**

---

# Unknowns carried forward

Batch 01 does **not** establish:

- exact database entities or table relationships
- required fields
- numbering series
- approval states
- tax rules
- payment allocation logic
- stock valuation configuration
- serial/engine/chassis handling
- whether dealer customers use separate ledgers or customer groups
- whether booking creates accounting entries immediately
- whether registration charges are income, pass-through, receivable, payable, or another treatment
- exact relationship between `DEALER CUSTOMER INVOICE` and `DEALER SALE`
- exact meaning of `ADD NEW HEAD`
- contents of FIFO report submenus
- role/permission rules

These are deliberately left unresolved until supporting screenshots are analyzed.

---

# Batch completion status

**BIKE-BATCH-01: ANALYZED**

The three source screenshots have been visually reviewed at full resolution and their durable evidence has been recorded here and in `batch_01.json`.
