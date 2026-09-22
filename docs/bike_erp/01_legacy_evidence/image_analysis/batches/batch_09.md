# BIKE-BATCH-09 — Advance Booking, Pending Orders, and Purchase Order Reports

## Batch scope

This batch documents operational reporting around bookings and procurement. All three reports have in-app filters plus RDF/PDF-style report execution and spreadsheet generation.

---

# BIKE-025 — `advance_booking_report.png`

- **Visible title:** ADVANCE BOOKING REPORT
- **Type:** booking status/report view
- **Confidence:** high

## Visible actions

- REFRESH
- REPORT RUN (RDF)
- GENERATE SHEET
- BACK

## Visible fields / filters

- Branch
- User
- Status

## Visible grid/report columns

- Sr No
- Date
- Issue Date
- CNIC
- Name
- Cell No
- Model
- Ac No
- Amount

## Direct evidence

- Advance bookings can be filtered by Status.
- Report rows include booking dates, customer identity/contact, model, account number and amount.
- The application supports both rendered RDF report and spreadsheet output.

## Inferences — not yet proven

- Issue Date likely represents completion/allocation/delivery-related date, but exact meaning is not shown.

## Unknowns carried forward

- Status value set
- Meaning of Ac No
- Issue Date business event

---

# BIKE-026 — `pending_order_report.png`

- **Visible title:** PENDING ORDER REPORT
- **Type:** purchase-order fulfillment report
- **Confidence:** high

## Visible actions

- REFRESH
- REPORT RUN (RDF)
- GENERATE SHEET
- BACK

## Visible fields / filters

- Branch
- User
- Order No
- Model

## Visible grid/report columns

- P.Order #
- Model Name
- Colour
- Order Qty
- Receive Qty
- Balance

## Direct evidence

- Pending purchase orders are measured by ordered quantity, received quantity and remaining balance.
- Report can filter by order number and model.

## Inferences — not yet proven

- Balance is likely Order Qty minus Receive Qty; the formula is strongly implied but not directly demonstrated with populated rows.

## Unknowns carried forward

- Whether cancelled quantities affect balance
- Whether receipts are linked strictly by P.O. number

---

# BIKE-027 — `bike_purchase_order_report.png`

- **Visible title:** BIKE PURCHASE ORDER REPORT
- **Type:** purchase-order report
- **Confidence:** high

## Visible actions

- REFRESH
- REPORT RUN (RDF)
- GENERATE SHEET
- BACK

## Visible fields / filters

- Branch
- User
- Start Date
- End Date
- P.O. NO.

## Visible grid/report columns

- Sr No
- Order Date
- P.O NO
- Model Name
- Color
- Qty
- Rate
- Total

## Direct evidence

- Purchase orders can be reported by date range and optional P.O. number.
- Model, colour, quantity, rate and total are the core reported dimensions.

## Unknowns carried forward

- Supplier/account is not visible in this report grid
- Whether one PO can contain multiple models/colours in report grouping

---

## Cross-image findings

- Pending Order Report directly ties purchasing to receiving through ordered versus received quantities.
- Advance Booking Report is customer/model/amount/status oriented, while procurement reports are model/colour/quantity oriented.
- Legacy reporting commonly offers both RDF output and Generate Sheet.

## Preliminary ERPNext relevance — non-final

- Most procurement reporting should be evaluated against standard ERPNext Purchase Order/Purchase Receipt analytics before custom reports are planned.
- Advance-booking reporting will depend on the final booking workflow/model.

## Batch completion status

**BIKE-BATCH-09: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
