# BIKE-BATCH-08 — Registration Tracking and Registration Receipt

## Batch scope

This batch proves registration is an operational workflow with chassis/engine tracking, letter/document statuses, agent handling and money receipt/payment fields—not merely an invoice charge.

---

# BIKE-022 — `registration_form.png`

- **Visible title:** REGISTRATION FORM
- **Type:** registration workflow tracker
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- LAST RECORD
- DELETE
- BACK
- DELETE CONFORM

## Visible grid/report columns

- Chassis no
- Engine no
- Date
- Customer Name
- Reg no
- Letter
- Letter Rec Date
- Letter Del Date
- Documents
- Documents Rec Date
- Documents Del Date
- Documents Receive Name
- Agent Name
- Agent Date
- Amount

## Direct evidence

- Registration is tracked per vehicle using chassis and engine number.
- Registration number, letter status/dates, document status/dates, receiving person, agent and amount are tracked.
- A status dropdown in the letter/document area visibly includes values such as RECEIVED, PENDING and delivery-related states.
- One visible delivery-related value is DELIVERED TO CUSTOMER/DEALER; another visible state is DELIVERED TO EXC.

## Inferences — not yet proven

- The workflow tracks handoff of registration letters/documents between dealership, external authority/agent and customer/dealer.

## Unknowns carried forward

- Exact status field ownership for every dropdown option
- Meaning of EXC
- Required transition order
- Whether Amount is charge/cost/receipt

---

# BIKE-023 — `registration_form_2.png`

- **Visible title:** REGISTRATION FORM
- **Type:** same registration workflow with alternate dropdown expanded
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- LAST RECORD
- DELETE
- BACK
- DELETE CONFORM

## Visible grid/report columns

- Chassis no
- Engine no
- Date
- Customer Name
- Reg no
- Letter
- Letter Rec Date
- Letter Del Date
- Documents
- Documents Rec Date
- Documents Del Date
- Documents Receive Name
- Agent Name
- Agent Date
- Amount

## Direct evidence

- The Letter field visibly shows PENDING in the captured row.
- A second status dropdown in the Documents area visibly exposes RECEIVED, DELIVERED and PENDING.
- Letter and document tracking are separate concepts with their own dates.

## Inferences — not yet proven

- The two screenshots were likely captured specifically to show different status dropdowns/options.

## Unknowns carried forward

- Complete status lists
- Automated date population
- Whether statuses are enforced sequentially

---

# BIKE-024 — `registration_recieve_voucher.png`

- **Visible title:** REGISTRATION RECEIVED VOUCHER
- **Type:** registration financial receipt/payment voucher
- **Confidence:** high

## Visible actions

- SAVE
- ADD NEW
- FIND
- VIEW
- LAST RECORD
- DELETE
- BACK

## Visible fields / filters

- Sr No
- Ref Inv
- Date
- Total

## Visible grid/report columns

- Rec From
- Ac Name
- Description
- Reg. Rec
- Reg. Pay

## Direct evidence

- Registration finance has dedicated received and paid amount columns.
- Voucher can reference an invoice through Ref Inv.
- Multiple lines and an overall total are supported.

## Inferences — not yet proven

- Registration profit can be derived from amounts received versus paid; later reports directly support this interpretation.

## Unknowns carried forward

- Whether Reg. Pay creates a payable/cash payment automatically
- Invoice eligibility
- Account selection semantics

---

## Cross-image findings

- Registration has both operational document/agent tracking and a separate financial voucher.
- The workflow is vehicle-specific via chassis/engine and separately tracks letter and document lifecycle.
- The later Registration Profit reports are consistent with Reg. Rec versus Reg. Pay captured here.

## Preliminary ERPNext relevance — non-final

- Registration likely needs a dedicated workflow/custom DocType linked to the sold vehicle and customer, while its monetary effects should still use standard ERPNext accounting documents where possible.

## Batch completion status

**BIKE-BATCH-08: ANALYZED**

All source screenshots were manually reviewed at full resolution. Visible UI is treated as authoritative; hidden rules are not invented.
