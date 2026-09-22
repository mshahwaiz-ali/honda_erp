# BIKE-BATCH-12 — Date-Wise Profit Output and Registration Profit Reports

## Batch scope

This batch resolves the Date Wise Profit output and proves two distinct registration-profit views. It also exposes a significant cross-domain anomaly: the rendered date-wise report contains part-like inventory items even though it is stored with the Bike evidence.

---

# BIKE-034 — `data_wise_profit_report_2.png`

- **Visible title:** Date Wise Profit Report
- **Type:** rendered profitability report
- **Confidence:** high

## Visible fields / filters

- From
- To
- Report run on
- Page

## Visible grid/report columns

- Sr #
- Srno
- Date
- Name
- Item Name
- Part No
- Qty
- Tot Sale
- Tot Pur
- Net Profit

## Direct evidence

- Rendered output reports item/part-number profitability with quantity, total sale, total purchase and net profit.
- The sample rows visibly contain part/consumable-like item descriptions rather than complete motorcycles.
- The report has a total row for quantity, sales, purchases and net profit.
- Actual customer/party values are present in the screenshot but are intentionally not reproduced in this evidence document.

## Inferences — not yet proven

- This report may cover spare-parts/item activity accessible from the Bike-side application or a shared reporting layer.

## Unknowns carried forward

- Whether Bike and Parts systems share any database/reporting source
- Why this report appears in Bike evidence
- Exact FIFO/costing basis

---

# BIKE-035 — `registration_profit_report.png`

- **Visible title:** REGISTRATION PROFIT REPORT
- **Type:** registration profitability report
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

- Sr No
- Date
- Ref No
- Item Desc
- Name
- Received
- Pay Amt
- Profit

## Direct evidence

- Registration profit is reported as received versus paid amount with a profit column.
- Reference number, item description and name are retained.
- Bottom totals are visible for the monetary columns.

## Inferences — not yet proven

- Profit is likely Received minus Pay Amt, but no populated row is shown here to verify arithmetic.

## Unknowns carried forward

- Meaning of Item Desc in registration context
- Whether received/pay values originate solely from Registration Received Voucher

---

# BIKE-036 — `registration_profit_report_outdoor.png`

- **Visible title:** REGISTRATION PROFIT REPORT (OUTDOOR)
- **Type:** outdoor registration profitability report
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

- Sr No
- Date
- Item Name
- Reg Receive
- Reg Pay
- Net Profit

## Direct evidence

- A distinct OUTDOOR registration profit report exists.
- It reports registration received, registration paid and net profit by item/date.

## Inferences — not yet proven

- Outdoor likely refers to registration work not following the normal in-house/sold-bike path, but exact business meaning is not shown.

## Unknowns carried forward

- Definition of Outdoor
- How outdoor registration records are created
- Relationship to Registration Form

---

## Cross-image findings

- Registration clearly has its own revenue/cost/profit model: receive, pay and profit are repeatedly exposed.
- The Date Wise Profit output confirms item/part-number profitability reporting, not only motorcycle-unit profit.
- The appearance of part-like items within Bike evidence conflicts with a simplistic assumption of completely isolated functional domains; this must be clarified without assuming shared accounting/database.

## Preliminary ERPNext relevance — non-final

- Registration revenue/cost should later be modeled with standard accounting entries plus a workflow record, not a separate unofficial profit ledger.
- The Bike-versus-Parts boundary needs explicit client confirmation before deciding company/site/accounting separation.

## Batch completion status

**BIKE-BATCH-12: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
