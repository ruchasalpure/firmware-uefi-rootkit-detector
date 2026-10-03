# Duties and Responsibilities for Firmware UEFI Rootkit Detector Agent

## Dual-Control Architecture
Maker:
firmware-volume-parser

Checker:
bootkit-signature-checker

## Operational Workflow
1. The Maker (firmware-volume-parser) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (bootkit-signature-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
