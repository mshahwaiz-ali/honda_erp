# BIKE-BATCH-14 — Daily Transaction, Expense Summary, and General Ledger

## Batch scope

This batch contains some of the strongest architectural evidence. The Daily Transaction output consolidates several transaction classes, while the General Ledger shows sales and cash-receipt entries with vehicle quantities and running financial balances.

---

# BIKE-040 — `daily_transection_report.png`

- **Visible title:** DAILY TRANSACTION
- **Type:** rendered consolidated daily transaction report
- **Confidence:** high

## Visible fields / filters

- From Date
- To Date

## Visible grid/report columns

- Multiple section-specific column sets

## Direct evidence

- The rendered report is sectioned by transaction type.
- Visible sections include Purchase, Market Purchase, Parts Sale Invoice, Cash Sale Invoice Bike, Dealers Sale Invoice Bike, and a payment-style section at the bottom.
- Purchase/Market Purchase sections carry invoice/type/delivery/P.O-or-godown/item/brand/quantity/rate/net dimensions.
- Cash Sale Invoice Bike carries customer detail, type, item code/name, brand, quantity, sale rate and net/received-amount style fields.
- Dealers Sale Invoice Bike carries customer detail, type, chassis number, registration number, item code/name, quantity, sale rate and net amount.
- A payment row shows Type PAY and Payment Type CLEAR in the captured output.
- The screenshot contains real party names/details; they are intentionally not reproduced here.

## Inferences — not yet proven

- The report acts as a consolidated daily activity journal across operational modules.
- Parts-related sections appearing in Bike evidence may indicate shared reporting, overlapping functionality, or a combined source; it does not by itself prove the two legacy systems shared accounting/database.

## Unknowns carried forward

- Exact data-source boundary between Bike and Parts
- Meaning of every section-specific field
- Whether report includes all transaction types
- Why purchase and market purchase are separate

---

# BIKE-041 — `expense_sumary_report.png`

- **Visible title:** EXPENSE SUMMARY REPORT
- **Type:** expense-by-account/head summary
- **Confidence:** high

## Visible actions

- REFRESH
- REPORT RUN (RDF)
- GENERATE SHEET
- BACK

## Visible fields / filters

- Branch
- User
- From Date
- To Date
- Head Name

## Visible grid/report columns

- Id Ac
- Name
- Amount

## Direct evidence

- Expenses can be summarized by account/head over a date range.
- Head Name is an optional filter.
- Account ID, name and amount are reported.

## Unknowns carried forward

- Which account groups qualify as expense
- Whether amount is debit net of credits

---

# BIKE-042 — `GL.png`

- **Visible title:** General Ledger
- **Type:** rendered account general ledger
- **Confidence:** high

## Visible fields / filters

- A/c code and account name
- FROM DATE
- TO DATE
- report date/page

## Visible grid/report columns

- DATE
- SRNO
- REF NO
- STATUS
- DESCRIPTION
- ENG NO
- CH NO
- IN
- OUT
- RATE
- DEBIT
- CREDIT
- BALANCE

## Direct evidence

- The ledger mixes financial debit/credit/balance with engine/chassis, in/out quantity and rate.
- Visible sample statuses include SALE and C/R.
- Visible sample descriptions include CASH, CHEQUE CLEAR and DISCOUNT.
- Running balance changes across sales and receipts are visible.
- The screenshot contains real account/party information; values are not repeated here.

## Inferences — not yet proven

- C/R likely denotes cash receipt, consistent with Cash Receive Voucher.
- Operational sales and receipt documents feed a common account ledger/reporting layer.

## Unknowns carried forward

- Full status mapping
- Whether discounts post through separate receipt/journal lines
- Exact source-document linkage

---

## Cross-image findings

- Daily Transaction demonstrates a consolidated reporting surface across purchase, parts sale, bike cash sale, bike dealer sale and payment activity.
- General Ledger confirms that sale and receipt activity converge into debit/credit running balances.
- The evidence strongly supports using ERPNext's native accounting ledger as the replacement backbone rather than reproducing this legacy ledger engine.

## Preliminary ERPNext relevance — non-final

- Daily Transaction can later become a consolidated query/report across standard ERPNext documents and any verified custom workflow records.
- Expense Summary and GL should primarily use ERPNext accounting data.

## Batch completion status

**BIKE-BATCH-14: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
