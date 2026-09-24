# Secondary-Storage Recovery Methodology

## Scope

A separate component of the broader authorized examination involved secondary-storage media containing both allocated and unallocated data.

The workflow included source-media preservation, raw imaging, filesystem-layout examination, strings/signature review, and file carving with PhotoRec. Recovered material included technical documents as well as SQLite-related artifacts relevant to the broader Apple/iOS examination.

## Preservation

Historical examination notes document unmounting source media before acquisition, creation of raw images with `dd`, verification of image creation, and cryptographic hashing as part of the preservation process. Subsequent recovery work was performed against forensic images rather than treating the physical media as a disposable working copy.

Where a contemporaneous digest is private or unnecessary for public verification, this repository documents that hashing occurred without publishing the evidentiary value.

## Recovery and Interpretation

File carving was used to recover data no longer represented by active filesystem entries. A carved file demonstrates that recoverable byte sequences consistent with that file existed in the examined data source.

It does **not**, without supporting metadata or independent artifacts, establish the file's original name, path, owner, acquisition method, or whether a user opened it.

Recovered SQLite material is therefore identified and validated structurally. Filename and extension are treated as clues, not conclusions.

## Relationship to the iOS Project

Secondary-storage recovery is documented separately from backup-derived logical data so that acquisition provenance remains clear. A database recovered from secondary storage may subsequently be parsed with the same SQLite methodology used for an iOS backup artifact, but that does not transform its acquisition path into a logical extraction.

See [Unallocated-Space Messages SQLite Recovery](case-studies/unallocated-space-sqlite-recovery.md) for the Messages-related example.
