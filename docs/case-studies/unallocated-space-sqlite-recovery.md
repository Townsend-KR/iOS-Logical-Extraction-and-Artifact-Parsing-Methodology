# Unallocated-Space SQLite Recovery: An Unresolved Observation

## Status

**Unresolved / documentation recovery pending**

This note intentionally records an observation without presenting an unverified explanation as a forensic conclusion.

## Observation

During earlier examination of secondary storage, Messages-related SQLite material was reportedly recovered from unallocated space on a 64 GB USB device. The recovery was associated with a substantially larger `chat.db` dataset and appeared, during examination, to expose additional forensic information.

The original acquisition/recovery records needed to establish the precise mechanism have not yet been relocated. For that reason, this repository does **not** currently assert how the material came to reside on the USB device or why the recovered examination produced the observed result.

## Working Hypothesis

One possible explanation is that an earlier attempt to copy a substantially larger Messages database dataset to the USB device failed because the destination lacked sufficient capacity, while some database bytes or fragments were nevertheless written before the transfer terminated. Those remnants may later have been recoverable from unallocated space.

This is a hypothesis only.

Other explanations remain possible, including differences in carving, filesystem allocation, sparse/logical-size reporting, independently recovered SQLite pages, associated WAL material, or the examination process itself.

## Hash Constraint

If two complete files have the same byte length and the same SHA-256 digest, they should be treated as byte-identical for practical forensic comparison. One such file cannot contain additional bytes absent from the other.

Accordingly, any remembered difference in recoverable information must be reconciled against the original records. Potential sources include material outside the file itself, separately carved regions, sidecar data, recovery output, or comparison against a different logical database state.

## Required Validation

Before this observation is promoted to a completed case study, the following should be recovered or independently re-established where available:

- source-media image or preserved recovery set;
- acquisition and carving logs;
- filesystem metadata for the USB device;
- reported logical and allocated sizes of relevant artifacts;
- SHA-256 manifests;
- recovered `chat.db`, WAL, SHM, or carved SQLite regions;
- tool/version information and recovery parameters; and
- output demonstrating the reportedly additional information.

## Reporting Principle

The absence of the original documentation is itself a limitation and is reported as such.

This case study remains intentionally unresolved because a plausible explanation is not the same thing as a demonstrated one. That distinction is part of the forensic methodology being demonstrated by this repository.
