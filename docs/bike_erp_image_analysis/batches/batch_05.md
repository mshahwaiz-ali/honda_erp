# BIKE-BATCH-05 — Cash Sale, Dealer Sale, and Used-Bike Sale

## Batch scope

This batch defines three visibly different sales scenarios. Cash Sale captures consumer identity, booking reference, taxes/levies, registration charges and cash settlement; Dealer Sale is account/balance oriented; Used-Bike Sale uses account/customer plus stock-out rows.

---

# BIKE-013 — `cash_sale_invoice.png`

- **Visible title:** CASH SALE INVOICE
- **Type:** retail/cash bike sales invoice
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- LAST RECORD
- DELETE
- INVOICE PRINT
- RECEIPT PRINT
- BACK

## Visible fields / filters

- Sr No.
- REF No.
- INSTITUTIONAL SALES
- Sale Type
- Date
- Customer Name
- Father Name
- C.NIC
- Address
- Booking #
- City
- Company
- Mobile No.
- Discount
- Reg. Charges
- Net
- Cash Receive
- Balance
- FBR Amount

## Visible grid/report columns

- Chassis No.
- Engine No.
- Model
- Color
- Qty
- Sale Rate
- Sales Tax (18%)
- N.E.V.Levy (1%)
- Total

## Direct evidence

- Sale Type is visibly CASH in the captured screen.
- Institutional Sales is a selectable field and is visibly NO in the captured screen.
- A Booking # can be attached to a cash sale.
- The invoice records chassis and engine number, proving unit-specific bike sale.
- Sales Tax 18% and N.E.V. Levy 1% are separate line financial components.
- Discount, registration charges, net, cash received and balance are visible settlement fields.
- An FBR Amount field already exists in the legacy cash-sale UI.
- Separate Invoice Print and Receipt Print actions are available.

## Inferences — not yet proven

- Booking may be settled/converted through Cash Sale; the direct transition is not shown.

## Unknowns carried forward

- FBR Amount calculation/use
- Tax bases and formulas
- Whether cash received posts automatically
- How registration charges are accounted
- Institutional-sales behavior

---

# BIKE-014 — `dealer_sale_invoice.png`

- **Visible title:** DEALER SALE INVOICE
- **Type:** dealer/account bike sales invoice
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- LAST RECORD
- DELETE
- INVOICE PRINT
- BACK
- CASH RECEIVE

## Visible fields / filters

- Sr No.
- Bill No.
- Date
- A/c Code
- Prev Balance
- Dealers Name
- From
- To
- Current Balance

## Visible grid/report columns

- COMPANY
- INSTITUTIONAL SALE
- Chassis
- Engine No
- Model
- Colour
- Qty
- Retail
- Amount
- L
- x

## Direct evidence

- Dealer sale is explicitly account-based through A/c Code and Dealers Name.
- Previous Balance and Current Balance are visible on the sale form.
- A CASH RECEIVE action is embedded in the dealer-sale screen.
- Dealer-sale lines contain chassis/engine identity plus model, colour, quantity, retail and amount.
- Institutional Sale is captured per line.

## Inferences — not yet proven

- Dealer Sale likely supports credit/account receivables, given previous/current balance fields and a cash-receive action.

## Unknowns carried forward

- Meaning of Company field versus dealer account
- How previous/current balance is computed
- Cash Receive destination document
- Credit limits/terms
- Meaning of L control

---

# BIKE-015 — `used_bike_sale_invoice.png`

- **Visible title:** USED BIKE SALE INVOICE
- **Type:** used-bike stock-out/sales invoice
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- DELETE
- LAST RECORD
- PRINT
- BACK

## Visible fields / filters

- Sr No
- Ref No
- DATE
- Account Code
- Customer Name

## Visible grid/report columns

- CHASIS NO
- ENGINE NO
- CODE
- PRODUCT NAME
- BRAND
- OUT QTY
- RATE
- AMOUNT
- L
- X

## Direct evidence

- Used-bike sale is a dedicated form separate from normal Cash Sale.
- It uses an Account Code plus Customer Name.
- It records chassis and engine number and an explicit OUT QTY.
- Rate, amount, total quantity and total amount are visible.

## Inferences — not yet proven

- Used-bike inventory is likely tracked through explicit in/out quantity movements, reinforced by the matching purchase form in the next batch.

## Unknowns carried forward

- Tax handling
- Payment/receivable settlement
- Source of used-bike cost
- Whether each used bike is always quantity 1
- Meaning of L control

---

## Cross-image findings

- The legacy system deliberately separates cash retail, dealer/account, and used-bike sale flows.
- Cash Sale is the richest consumer-facing invoice: customer identity, booking, taxes/levy, registration charge, cash receipt, balance and FBR Amount are all on one form.
- Dealer Sale behaves more like an account/credit sale because balances are displayed before and after the transaction.
- All three sale types retain vehicle-unit identity through chassis/engine fields.

## Preliminary ERPNext relevance — non-final

- Do not automatically create three custom invoice DocTypes. Later determine whether standard Sales Invoice plus customer groups, payment behavior, vehicle-unit fields and workflow rules can represent the verified differences.
- Existing FBR Amount is evidence only; the future FBR integration remains a later phase after core ERP reconstruction.

## Batch completion status

**BIKE-BATCH-05: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
