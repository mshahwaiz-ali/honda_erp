# BIKE-BATCH-10 — Cash Sale, Dealer Sale, and Engine-Wise Stock Reports

## Batch scope

This batch proves the operational report dimensions used for retail sales, dealer sales and available vehicle stock. The reports consistently preserve model/colour and vehicle-unit identifiers.

---

# BIKE-028 — `daily_cash_sale_report.png`

- **Visible title:** DAILY CASH SALE REPORT
- **Type:** cash-sale operational report
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
- MODEL
- COLOUR

## Visible grid/report columns

- Inv No
- Ref No
- Date
- CNIC
- Coustomer Name
- Cell No
- Item Name
- Colour
- Chassis No
- Amount

## Direct evidence

- Cash sales can be filtered by date range, model and colour.
- Report includes invoice/reference identifiers, customer identity/contact, item/model, colour, chassis and amount.
- Engine number is not visible in this particular cash-sale report grid.

## Inferences — not yet proven

- The report is intended for daily/period retail bike-sale tracking rather than full accounting detail.

## Unknowns carried forward

- Whether all sale lines appear or one row per invoice
- Treatment of multi-bike invoices
- Tax/discount columns are not shown here

---

# BIKE-029 — `dealer_sale_report.png`

- **Visible title:** DEALER SALE REPORT
- **Type:** dealer sales report
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
- DEALERS

## Visible grid/report columns

- Comp No
- Reg No
- Date
- A/C Name
- Model No
- Colour
- Chassis No
- Engine No
- Amount

## Direct evidence

- Dealer sales can be filtered by dealer and date range.
- Account name, model, colour, chassis, engine and amount are reported.
- Comp No and Reg No are explicit report columns.

## Inferences — not yet proven

- Comp No may represent company/commission/complaint or another internal identifier; the screenshot does not define it.

## Unknowns carried forward

- Meaning of Comp No
- Meaning/source of Reg No
- Whether Amount is gross or net

---

# BIKE-030 — `engine_wise_stock_report.png`

- **Visible title:** ENGINE WISE STOCK REPORT
- **Type:** vehicle-unit stock report
- **Confidence:** high

## Visible actions

- REFRESH
- REPORT RUN (RDF)
- GENERATE SHEET
- ONLY 30-JUN STOCK
- GENERATE SHEET
- BACK

## Visible fields / filters

- Branch
- User
- Model
- Colour

## Visible grid/report columns

- Catagory
- Brand
- Chassic No
- Engine No
- Amount

## Direct evidence

- Available stock is reportable at chassis/engine-unit level.
- Model and colour filters are provided.
- Category, brand, chassis, engine and amount are the visible stock dimensions.
- A special ONLY 30-JUN STOCK action exists with an adjacent Generate Sheet action.

## Inferences — not yet proven

- The 30-Jun-specific view may support fiscal year-end stock reporting/valuation.

## Unknowns carried forward

- Meaning of Amount in stock report
- 30-Jun calculation basis
- Whether sold/reserved units are excluded
- Warehouse dimension is absent

---

## Cross-image findings

- Cash-sale, dealer-sale and stock reports all retain vehicle-unit identity, confirming chassis/engine tracking is central to the Bike system.
- Dealer Sale report includes both chassis and engine; Cash Sale report exposes chassis but not engine in this view.
- The dedicated 30-Jun stock action is likely a statutory/year-end operational reporting requirement and should be investigated before replacement.

## Preliminary ERPNext relevance — non-final

- Standard ERPNext serial-number/stock reporting should be evaluated for chassis/engine tracking.
- Custom reports may still be needed for dealership-specific filters and year-end stock formats.

## Batch completion status

**BIKE-BATCH-10: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
