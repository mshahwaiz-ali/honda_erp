# BIKE-BATCH-15 — FIFO Profit/Stock Views and Rendered Waiting-Booking Report

## Batch scope

The final batch resolves the FIFO report family and validates the rendered output for advance bookings in WAITING status.

---

# BIKE-043 — `item_wise_fifo_report.png`

- **Visible title:** ITEM WISE FIFO REPORT
- **Type:** item profitability/FIFO report view
- **Confidence:** high

## Visible actions

- REFRESH
- RUN REPORT (RDF)
- GENERATE SHEET
- BACK

## Visible fields / filters

- Branch
- User
- Start Date
- End Date
- Item Code
- adjacent item lookup/name field

## Visible grid/report columns

- Sr No
- Date
- Name
- Sale Qty
- Sale Rate
- Pur Rate
- Total Sale
- Total Pur
- Profit Qty
- Profit Amount

## Direct evidence

- The report can filter a specific item over a date range.
- It exposes sale quantity/rate, purchase rate, total sale, total purchase and profit quantity/amount.
- The report is explicitly labelled FIFO.

## Inferences — not yet proven

- FIFO cost layers may be used to derive purchase cost/profit, but the computation is not visible.

## Unknowns carried forward

- Meaning of Profit Qty
- Exact FIFO layer algorithm
- Handling of returns/adjustments

---

# BIKE-044 — `item_wise_fifo_report_2.png`

- **Visible title:** ITEM WISE FIFO REPORT
- **Type:** stock movement/value FIFO view
- **Confidence:** high

## Visible actions

- REFRESH
- RUN REPORT (RDF)
- GENERATE SHEET
- BACK

## Visible fields / filters

- Branch
- User

## Visible grid/report columns

- Date
- Item Name
- Part No
- In Qty
- Out Qty
- Stock
- Rate
- Value

## Direct evidence

- A second FIFO view reports stock movement and value rather than sales profit.
- It contains in quantity, out quantity, remaining stock, rate and value.
- Item Name and Part No are explicit columns.

## Inferences — not yet proven

- This may correspond to the Stock Value child entry seen under FIFO Reports, despite the screen title remaining Item Wise FIFO Report.

## Unknowns carried forward

- How this mode is selected
- Whether Value equals Stock × Rate for each FIFO layer or aggregated item
- Date/item filters may be outside the captured viewport or omitted

---

# BIKE-045 — `report.png`

- **Visible title:** Status : WAITING
- **Type:** rendered advance-booking report output
- **Confidence:** high

## Visible fields / filters

- Status = WAITING

## Visible grid/report columns

- Srno
- Rec. Date
- Issue Date
- Cnic
- Name
- Cell No
- Model
- Acno
- Amount

## Direct evidence

- This is a rendered output matching the Advance Booking Report field set.
- The report is filtered to WAITING status.
- Multiple waiting bookings are listed and an Amount total is shown.
- Issue Date and Acno can be blank in visible rows.
- The screenshot contains real customer identity/contact data; those values are intentionally not reproduced.

## Inferences — not yet proven

- Blank Issue Date is consistent with WAITING bookings not yet issued/completed.

## Unknowns carried forward

- Whether every waiting record must have blank Issue Date
- Meaning of Acno
- What event fills Issue Date

---

## Cross-image findings

- The FIFO family contains at least two distinct analytical views: profitability and stock movement/value.
- Rendered booking output validates the in-app Advance Booking Report design and the WAITING status used on the booking form.
- The final screenshot closes the evidence loop between Advance Booking entry, Advance Booking Report screen and rendered report output.

## Preliminary ERPNext relevance — non-final

- ERPNext perpetual inventory/valuation should be the first source for FIFO stock value and profit calculations; recreate only dealership-specific presentation gaps.
- Booking remains a likely custom workflow because its waiting/issue lifecycle is not a standard sales document by itself.

## Batch completion status

**BIKE-BATCH-15: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
