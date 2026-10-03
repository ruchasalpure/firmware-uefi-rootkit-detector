# Multi-Agent Coordination Specification

## Assigned Roles
Maker:
firmware-volume-parser

Checker:
bootkit-signature-checker

## Coordination Protocol
- **Primary Agent**: firmware-uefi-rootkit-detector
- **Governance Standard**: OpenGAP Dual-Agent Control Framework v0.1.0
- **Consensus Threshold**: 100% agreement between Maker and Checker before state mutations.
- **Fail-safe Mode**: If verification fails, transaction rolls back and alerts human supervisor.
