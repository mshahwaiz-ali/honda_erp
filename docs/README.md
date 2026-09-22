# Honda ERP Documentation

This directory is intentionally organized by business system and project phase.

## Current structure

```text
docs/
└── bike_erp/
    ├── README.md
    ├── 01_legacy_evidence/
    │   └── image_analysis/
    │       ├── README.md
    │       ├── analysis_schema.json
    │       ├── bike_image_manifest.json
    │       ├── generated_inventory.json
    │       ├── batches/
    │       └── refined/
    └── 02_system_understanding/
        └── BIKE_LEGACY_SYSTEM_WORKING_MODEL.md
```

## Documentation rule

The project progresses in this order:

1. collect and preserve legacy evidence
2. understand how the legacy business/software works
3. resolve unknown business rules
4. map verified requirements to ERPNext standard features
5. identify only the required customizations
6. create the implementation plan
7. implement and validate

Implementation planning must not replace or rewrite evidence.

The legacy Bike and Parts systems are treated as separate business systems unless later evidence explicitly proves a shared relationship. Parts documentation will be created separately when its analysis begins.
