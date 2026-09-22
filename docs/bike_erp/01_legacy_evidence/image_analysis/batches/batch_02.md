# BIKE-BATCH-02 — Legacy Bike ERP Menu, Head Master, and Item Master Analysis

## Batch scope

This batch contains three Bike-system screenshots:

| Image ID | Source |
|---|---|
| BIKE-004 | `client_old/software_images_bike/menu_bike_3.png` |
| BIKE-005 | `client_old/software_images_bike/head_form.png` |
| BIKE-006 | `client_old/software_images_bike/item_registration_form.png` |

The batch extends the menu evidence from Batch 01 and gives the first direct evidence for two administrative/master-data forms.

---

# BIKE-004 — `menu_bike_3.png`

## Screen classification

- **Type:** main navigation / lower menu state
- **Confidence:** high
- **Purpose observed:** exposes the lower part of the Bike-system menu tree, including FIFO reports and additional operational entries.

## Visible menu structure

The screenshot reconfirms these groups and entries:

### REPORTS MENU

Visible children:

- `ACCOUNTS REPORTS`
- `GENERAL REPORTS`
- `PROFIT REPORTS`
- `BIKE REPORTS MENU`

### ADMIN MENU

Visible children:

- `ADD NEW ITEM`
- `ADD NEW HEAD`

### SALES MENU

Visible children:

- `CASH SALE`
- `DEALER SALE`
- `USED BIKE SALE`

### FIFO REPORTS

This screenshot resolves an open question from Batch 01. The visible FIFO-report children are:

- `DATE WISE PROFIT`
- `ITEM WISE PROFIT`
- `STOCK VALUE`

### Additional visible top-level entries

Below the FIFO report group, two additional entries are visible at the same general navigation level:

- `STOCK ADJUST`
- `DAILY TRANSACTION`

`DAILY TRANSACTION` is visibly selected/highlighted in the screenshot.

## Evidence-level implications

### FIFO/profit/valuation reporting

The legacy system explicitly exposes:

- date-wise profit reporting
- item-wise profit reporting
- stock-value reporting

This is stronger evidence than the generic `FIFO REPORTS` label alone. It suggests the legacy system reports inventory profitability/value using FIFO-oriented logic, but the exact valuation algorithm, layer mechanics, cost source, and accounting treatment remain unproven until report screenshots are analyzed.

### Stock adjustment

`STOCK ADJUST` is a distinct visible menu entry.

This directly establishes that the legacy Bike system has a stock-adjustment operation. The screenshot does not establish whether adjustment creates accounting entries, requires approval, or records reasons/warehouses.

### Daily transaction

`DAILY TRANSACTION` is a distinct visible menu entry.

Its exact content is not shown here. It could be an operational/accounting report or transaction view, but that classification is not yet proven from this screenshot alone.

---

# BIKE-005 — `head_form.png`

## Screen classification

- **Type:** master-data maintenance form
- **Likely domain:** account/head/party-style master
- **Confidence:** high for visible fields; medium for business semantics

The form is reached conceptually from the visible `ADD NEW HEAD` admin menu entry, but this batch does not prove the exact launch path through an interaction trace.

## Visible actions

Top action bar:

- `SAVE`
- `ADD NEW`
- `VIEW`
- `FIND`
- `DELETE`
- `VIEW ALL`
- `LAST`
- `BACK`

These show standard create/search/browse/delete/navigation behavior around the master.

## Visible fields

The screenshot visibly contains:

| Field | Visible UI characteristic |
|---|---|
| Code | text/input field |
| Group Code | long selection/input field with dropdown/list control visible |
| Head Name | text/input field |
| TYPE | selection/dropdown field |
| Account Name | text/input field |
| CITY NAME | text/input field |
| AREA | text/input field |
| Address | long text/input field |
| CELL 1 | text/input field |
| CELL 2 | text/input field |
| FAX NO | text/input field |
| Cont. Person | text/input field |

A vertical scrollbar is visible inside the form, so additional fields may exist outside the captured viewport. Only the fields above are treated as observed.

## Important structural observation

This form is **not just a simple account-code/name form**. Alongside Code, Group Code, Head Name and Account Name, it stores party/contact-style information:

- city
- area
- address
- two cell numbers
- fax
- contact person

Therefore, `Head` in the legacy system appears to be a richer business/account master than a bare Chart-of-Accounts node.

However, the screenshot does **not** prove whether a Head represents:

- customer
- dealer
- supplier
- expense/income account
- bank/cash account
- a generic ledger party
- several of these categories selected by `TYPE`

The `TYPE` and `Group Code` fields may control such classification, but their option values are not visible.

## ERPNext relevance — non-final

This is a key area where the replacement should **not blindly recreate the legacy Head table**.

Later evidence should determine whether legacy Head records map to standard ERPNext masters such as:

- Customer
- Supplier
- Account
- Address
- Contact
- or another standard party/master

The visible contact fields strongly suggest that one legacy entity may be combining concerns that ERPNext normally separates into linked standard DocTypes.

No mapping decision is locked at this stage.

---

# BIKE-006 — `item_registration_form.png`

## Screen classification

- **Type:** item/master registration form
- **Visible title:** `ITEM REGISTRATION FORM`
- **Confidence:** high

This is direct evidence for the legacy Bike system's item master/registration capability.

## Visible actions

Top action bar:

- `SAVE`
- `ADD NEW`
- `FIND`
- `VIEW`
- `VIEW ALL`
- `LAST`
- `DELETE`
- `BACK`

## Visible fields

| Field | Observed |
|---|---|
| Item Code | yes |
| Item | yes |
| Brand | yes |
| Catagory | yes — spelling appears exactly this way in the legacy UI |
| Barcode / Qr Code | yes |
| Price | yes |
| Profit % | yes |
| Net Amount | yes |
| Purchase Rate | yes |
| Profit Amt | yes |
| Parts Sale Rate | yes |

A vertical scrollbar is visible, so uncaptured fields may exist beyond this viewport.

## Pricing/profit evidence

The form visibly stores or displays several pricing/profit concepts together:

- Price
- Purchase Rate
- Profit %
- Profit Amt
- Net Amount
- Parts Sale Rate

This is significant because the legacy item master appears to contain pricing and profitability fields rather than only descriptive item attributes.

No formula can be proven because the screenshot shows blank fields. For example, we must **not assume** that `Profit Amt` or `Net Amount` is automatically calculated from `Price`, `Purchase Rate`, and `Profit %` until a populated form or actual behavior confirms it.

## Barcode/QR evidence

`Barcode / Qr Code` is directly visible.

This proves that the legacy item master has a place for barcode/QR-style identification. It does not prove that the old workflow actually used a scanner or QR scanning hardware.

## Important cross-system caution

The field `Parts Sale Rate` is visible inside this Bike-system screenshot.

That fact is recorded exactly as observed, but it **does not prove** that the Bike and Parts systems shared:

- the same database,
- the same item master,
- the same accounting,
- or synchronized records.

The project baseline remains that Bike and Parts were operated as separate parallel systems unless later evidence proves a shared data relationship.

## ERPNext relevance — non-final

Much of this master likely overlaps standard ERPNext Item capabilities:

- item code/name
- brand
- item group/category
- barcode
- purchasing/selling rates through standard pricing mechanisms

The profit/net/parts-sale-rate fields require later workflow evidence before deciding whether they should be:

- standard price lists,
- calculated report values,
- custom fields,
- or omitted because ERPNext derives the value elsewhere.

---

# Consolidated new evidence from Batch 02

## Newly proven functions

Batch 02 adds direct evidence for:

1. FIFO/date-wise profit report entry
2. FIFO/item-wise profit report entry
3. stock-value report entry
4. stock-adjust operation
5. daily-transaction entry
6. Head master maintenance
7. Item Registration master maintenance

## Master-data observations

### Head master

Visible evidence suggests a combined ledger/business-contact record with:

- classification/grouping
- naming
- account-name information
- address/contact details

### Item master

Visible evidence includes:

- identification/classification
- barcode/QR
- purchase/sale-related rates
- profit-related fields

---

# Cross-batch resolutions

Batch 01 left the child entries under `FIFO REPORTS` unknown.

Batch 02 resolves the visible child entries as:

- Date Wise Profit
- Item Wise Profit
- Stock Value

Batch 02 also reveals two additional navigation entries not captured clearly in Batch 01:

- Stock Adjust
- Daily Transaction

---

# Unknowns carried forward

The following remain unresolved:

- options/meaning of `Group Code`
- options/meaning of `TYPE`
- whether Head is a generic party ledger or a narrower account master
- whether Head records map one-to-one to customers/dealers/suppliers/accounts
- any additional off-screen fields in Head form
- any additional off-screen fields in Item Registration form
- formulas behind Price / Purchase Rate / Profit % / Profit Amt / Net Amount / Parts Sale Rate
- whether Parts Sale Rate is actually used in the Bike application workflow
- barcode/QR scanning behavior
- exact Stock Adjust fields and posting behavior
- exact Daily Transaction screen/report
- exact FIFO valuation/profit calculation mechanics

---

# Batch completion status

**BIKE-BATCH-02: ANALYZED**

The three source screenshots were manually reviewed at full resolution. Findings are stored in this Markdown report and in the paired structured `batch_02.json`.
