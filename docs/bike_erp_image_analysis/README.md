# Bike ERP Legacy Image Analysis

## Purpose

This folder is the durable evidence record for reconstructing the client's **legacy Bike system** before implementation begins.

The target replacement platform is **ERPNext/Frappe**. Standard ERPNext functionality should be reused wherever it matches the business requirement; custom DocTypes, fields, scripts, workflows, reports, print formats, or integrations should only be introduced where the legacy/business requirement genuinely needs them.

This folder is **analysis first, planning later**. The screenshots are treated as evidence of the old system, not as a design specification to copy blindly.

## Critical project context

- The client historically used **two parallel systems**:
  1. Bike system
  2. Parts system
- Their records/accounting were kept separately. Do not merge or cross-assume their ledgers, transactions, inventory, or workflows unless later evidence explicitly proves a shared relationship.
- This folder covers the **Bike system only**.
- Parts-system analysis will be performed separately later.
- FBR invoicing is an important future requirement, but it is intentionally **out of scope for the initial legacy-image reconstruction**. It will be designed after the core replacement ERP is understood and built.

## Source screenshots

Bike screenshots:

`client_old/software_images_bike/`

The original screenshots remain the source of truth. Analysis documents reference them rather than duplicating image files.

## Analysis method

Screenshots are reviewed in batches of **3 images** for accuracy.

For each image we record:

- screen/form/report title
- apparent screen type
- visible sections and tabs
- visible fields and labels
- tables and columns
- buttons/actions
- filters
- displayed statuses
- visible calculations/taxes/totals
- customer/dealer/vehicle/inventory/accounting concepts shown
- document or record references
- relationships visible between screens
- workflow evidence supported by the screenshot
- uncertainties and open questions
- confidence level

### Evidence discipline

Every observation should be classified mentally as one of:

- **Observed** — directly visible in the screenshot.
- **Inferred** — likely based on visible context, but not proven.
- **Unknown** — cannot be determined from the screenshot.

Do not invent hidden validation rules, database relationships, posting logic, or workflows.

## File strategy

- `bike_image_manifest.json` — all Bike screenshots and review batches.
- `analysis_schema.json` — normalized structure used for detailed image records.
- `batches/batch_XX.md` — human-readable analysis for each 3-image batch.
- `batches/batch_XX.json` — structured machine-readable evidence for the same batch.
- `refined/` — created only after all screenshots are analyzed.

After all Bike screenshots are reviewed, the raw evidence will be converted into a separate refined specification. That refined document will describe the business capabilities/workflows clearly enough to support ERPNext architecture and implementation planning without repeatedly re-reading screenshots.

## Final Bike outputs

The image-analysis phase should eventually produce:

1. complete screenshot evidence record
2. functional/module inventory
3. masters and transaction inventory
4. report inventory
5. accounting observations
6. stock/inventory observations
7. customer/dealer/booking/sales/registration observations
8. suspected workflow map with evidence/confidence
9. unresolved questions/gaps
10. refined Bike ERP functional specification
11. later: ERPNext standard-vs-custom mapping
12. later: implementation plan

The final ERPNext plan must be based on the refined evidence, not on screenshot filenames alone.

## Validated workflow

Batches 01 and 02 have been manually reviewed at full resolution. The inventory/batching helper is validated for the Bike screenshot set: 45 images, 15 logical batches of 3.

The per-batch ZIP exporter is **not part of the durable evidence format**. It was only a transport helper for getting binary screenshots into visual review. Reports are stored directly under `docs/bike_erp_image_analysis/batches/` as Markdown + JSON.

For the remaining Bike screenshots, the efficient workflow is to provide the remaining source images once, then analyze them internally in 3-image logical batches and write the reports directly to this folder. No separate ZIP needs to be retained in the repository.
