# BIKE-BATCH-11 — Bike Profit Reports and Date-Wise Profit Launcher

## Batch scope

This batch proves multiple profitability views: unit-level bike profit with engine/chassis, a second item/part-number profit view, and a date-wise profit report launcher.

---

# BIKE-031 — `bike_profit_report.png`

- **Visible title:** BIKE PROFIT REPORT
- **Type:** vehicle-level profitability report
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
- Type
- Item Name
- Eng No
- Ch No
- Sale Rate
- Pur Rate
- Qty
- Discount
- Profit Pcs
- Net Profit

## Direct evidence

- Profitability is reported using sale rate, purchase rate, quantity, discount, profit pieces and net profit.
- Engine and chassis numbers are retained in the profit report.
- A transaction Type dimension is visible.

## Inferences — not yet proven

- Net profit likely derives from sale versus purchase value adjusted by discount, but exact formula is not shown.

## Unknowns carried forward

- Definition of Profit Pcs
- Cost source/Pur Rate source
- Treatment of taxes and registration charges
- Type values

---

# BIKE-032 — `bike_profit_report2.png`

- **Visible title:** BIKE PROFIT REPORT
- **Type:** alternate item-level profitability report
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
- Name
- Item Name
- Part No
- Qty
- Total Sale
- Total Pur
- Net Profit

## Direct evidence

- A second Bike Profit Report variant summarizes item/part-number profitability.
- It reports quantity, total sale, total purchase and net profit.
- A Name column is present in addition to Item Name and Part No.

## Inferences — not yet proven

- This may be an item/parts-oriented profit view used from within the Bike application/report catalogue.

## Unknowns carried forward

- Meaning of Name
- Why Part No is present in Bike Profit Report
- Whether this report includes spare parts, service items, or all inventory

---

# BIKE-033 — `data_wise_profit_report_1.png`

- **Visible title:** DATE WISE PROFIT REPORT
- **Type:** report parameter/launcher form
- **Confidence:** high

## Visible actions

- RUN REPORT
- EXIT FORM

## Visible fields / filters

- FROM DATE
- TO DATE
- ADMIN
- REHMAN HONDA

## Direct evidence

- Date Wise Profit Report has a simple date-range launcher separate from the rendered output.
- The next batch contains the rendered result for this report.

## Unknowns carried forward

- Whether additional hidden parameters exist
- Exact data source until output is reviewed

---

## Cross-image findings

- Profit reporting exists at both vehicle-unit and item/part-number levels.
- The system retains explicit purchase-rate/cost information in profit reporting rather than showing only revenue.
- Batch 12 output is required to understand what Date Wise Profit actually contains.

## Preliminary ERPNext relevance — non-final

- Profitability should ultimately be derived from ERPNext stock valuation/accounting where possible rather than storing independent profit fields.
- Legacy report layouts can be recreated only after agreeing which profit definitions remain business requirements.

## Batch completion status

**BIKE-BATCH-11: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
