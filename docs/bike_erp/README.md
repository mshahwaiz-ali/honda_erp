# Bike ERP Documentation

## Purpose

This folder contains the Bike-system reconstruction work that will later drive the ERPNext implementation.

The current phase is **understanding the client's existing software and business workflow**, not designing custom DocTypes or coding the replacement.

## Phase folders

### `01_legacy_evidence/`

Immutable/traceable evidence derived from the legacy screenshots.

The screenshot-analysis evidence is under:

`01_legacy_evidence/image_analysis/`

It contains:

- 45 screenshot inventory entries
- 15 logical analysis batches
- Markdown evidence reports
- structured JSON evidence
- a refined evidence consolidation

### `02_system_understanding/`

The human-readable operating model of how the Bike software appears to work end-to-end.

Primary document:

`02_system_understanding/BIKE_LEGACY_SYSTEM_WORKING_MODEL.md`

This is the document to refine **before implementation planning**.

## Later phases

Future documentation will be added only when the current understanding is mature:

- business requirements / client decisions
- ERPNext standard-vs-custom mapping
- architecture
- implementation plan
- deployment / operations

## Core principle

ERPNext will be the backbone of the replacement.

That does **not** mean copying every old Oracle Forms screen into a custom DocType. First understand the business behavior, then map it to standard ERPNext, and customize only the verified gaps.
