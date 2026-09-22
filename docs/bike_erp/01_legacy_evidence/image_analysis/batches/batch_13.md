# BIKE-BATCH-13 — Cash Balance, Cash Book, and All-Balance Summary Reports

## Batch scope

This batch covers balance-oriented reporting. One screen has a title/content mismatch that must be preserved as evidence rather than normalized away.

---

# BIKE-037 — `cash_balance_report.png`

- **Visible title:** CASH BALANCE REPORT
- **Type:** balance/profit-style report with registration columns
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

## Visible grid/report columns

- Bill No
- Name
- Cell No
- Reg Receive
- Reg Pay
- Net Profit

## Direct evidence

- Despite the title CASH BALANCE REPORT, the visible grid is registration-style: Reg Receive, Reg Pay and Net Profit.
- Bill number, party name and cell number are also included.

## Inferences — not yet proven

- The screen may be misnamed, reused, or represent a specialized registration/cash-balance report.

## Unknowns carried forward

- Why title and columns differ
- Whether this is the report for Cash Balance Receive (Bike)
- Profit formula

---

# BIKE-038 — `cash_book_report.png`

- **Visible title:** CASH BOOK REPORT
- **Type:** interactive cash-book report
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

## Visible grid/report columns

- Date
- Sr No
- Nerration
- Status
- Debit
- Credit
- Balanace

## Direct evidence

- Cash Book Report exposes date, serial number, narration, status, debit, credit and balance.
- Debit and credit totals are visible at the bottom.
- Legacy spelling in labels is preserved as observed.

## Unknowns carried forward

- Account selector is not visible here
- Status-code mapping

---

# BIKE-039 — `all_balabnce_summary_report.png`

- **Visible title:** ALL BALANCE & SUMMARY REPORT
- **Type:** account/party balance summary
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
- Area
- Opb
- Debit
- Credit
- Balance

## Direct evidence

- The report summarizes accounts/heads with area, opening balance, debit, credit and closing/current balance.
- Head Name is a filter.
- Bottom totals are visible for financial columns.

## Inferences — not yet proven

- Opb likely means opening balance.

## Unknowns carried forward

- Which Head types are included
- Area source
- Whether zero-balance heads are excluded

---

## Cross-image findings

- Balance reporting uses the same Head/account concepts observed in the Head master and Account Ledger.
- The Cash Balance Report title/content mismatch is a concrete legacy inconsistency; replacement requirements should be based on business need, not legacy naming alone.

## Preliminary ERPNext relevance — non-final

- Standard ERPNext General Ledger, Trial Balance, Party Ledger and Receivable/Payable reporting should be evaluated before custom balance reports are recreated.

## Batch completion status

**BIKE-BATCH-13: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
