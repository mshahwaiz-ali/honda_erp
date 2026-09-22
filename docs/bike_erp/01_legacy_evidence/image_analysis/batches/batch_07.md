# BIKE-BATCH-07 — Journal Voucher, Cash Book, and Account Ledger

## Batch scope

This batch proves the Bike system has a double-entry-style voucher and ledger/reporting layer, while also carrying operational vehicle quantity and engine/chassis information into account ledgers.

---

# BIKE-019 — `jv_voucher.png`

- **Visible title:** JV VOUCHER
- **Type:** journal voucher / accounting entry
- **Confidence:** high

## Visible actions

- ADD NEW
- FIND
- VIEW
- LAST VOUCHER
- ALL VOUCHERS
- TYPE WISE REPORT
- DELETE
- BACK
- SAVE

## Visible fields / filters

- VOUCHER NO
- VOUCHER TYPE
- USER
- BRANCH

## Visible grid/report columns

- DATE
- CODE
- A/C NAME
- NARRATION
- CH NO.
- PAY ORD
- DR/CR
- DEBIT
- CREDIT

## Direct evidence

- Journal Voucher supports multiple accounting rows and separate debit/credit totals.
- Voucher Type is selectable.
- Cheque No. and Pay Order fields are built into journal rows.
- DR/CR is a row-level selection.

## Inferences — not yet proven

- The form is a generic manual accounting adjustment/transfer mechanism.

## Unknowns carried forward

- Voucher Type values
- Balancing validation
- Account restrictions
- Cheque/pay-order workflow

---

# BIKE-020 — `cash_book.png`

- **Visible title:** CASH BOOK
- **Type:** rendered cash-book report
- **Confidence:** high

## Visible fields / filters

- A/C
- From Date
- To Date

## Visible grid/report columns

- DATE
- Sr No
- NARRATION
- STATUS
- DEBIT
- CREDIT
- BALANCE

## Direct evidence

- The rendered report identifies a dedicated cash account labelled CASH IN HAND (BIKE).
- An opening-balance row is present.
- Debit, credit and running balance are reported.
- Visible status codes include ADV/BOOK, C/P and C/S in the sample.
- The report shows debit/credit totals.

## Inferences — not yet proven

- Status codes likely classify source transaction types; exact mappings require confirmation.

## Unknowns carried forward

- Full status-code dictionary
- Whether cash book is generated from one account only or configurable
- Period opening/closing rules

---

# BIKE-021 — `accounts_ledger_form.png`

- **Visible title:** ACCOUNTS LEDGER FORM
- **Type:** interactive general/account ledger view
- **Confidence:** high

## Visible actions

- REFRESH
- LEDGER NEW (PDF)
- GENERATE SHEET
- BACK

## Visible fields / filters

- Branch
- User
- From Date
- To Date
- A/c Name

## Visible grid/report columns

- Date
- Sr No
- Ref No
- Status
- Description
- Eng No
- Ch No
- In Qty
- Out Qty
- Rate
- Debit
- Credit
- Balance

## Direct evidence

- Ledger rows combine financial columns with engine/chassis and inventory in/out quantities.
- The ledger can be filtered by account and date range.
- PDF and spreadsheet outputs are available.
- Debit, credit and balance totals are shown.

## Inferences — not yet proven

- The legacy ledger/reporting model blends party/account activity with operational vehicle/stock detail.

## Unknowns carried forward

- Whether all account types show Eng/Ch/In/Out data
- Source/status mapping
- Account master relationship to Head form

---

## Cross-image findings

- The Bike application has a clear accounting backbone: JV, cash book, account ledger, debit/credit and running balances.
- Accounting reports retain source-operation context through status/reference plus vehicle/quantity fields.
- The dedicated CASH IN HAND (BIKE) label is strong evidence that Bike cash accounting was separated from other business activity.

## Preliminary ERPNext relevance — non-final

- Use ERPNext accounting ledgers as the canonical accounting layer rather than recreating a parallel debit/credit engine.
- Vehicle-specific context should be linked to standard accounting source documents, not embedded into a replacement GL schema unless a verified gap demands it.

## Batch completion status

**BIKE-BATCH-07: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
