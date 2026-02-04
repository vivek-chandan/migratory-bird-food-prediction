# Datasets Directory

This directory is designated for storing datasets used in the Migratory Bird Stopover Quality Index project.

## Quick Reference

For detailed information about all available datasets, see [DATASETS.md](../DATASETS.md) in the root directory.

## Required Datasets

1. **eBird Data** - Store in `ebird/` subdirectory
2. **NDVI Data** - Store in `ndvi/` subdirectory  
3. **Habitat Data** - Store in `habitat/` subdirectory

## Directory Structure

```
datasets/
├── README.md           # This file
├── ebird/             # eBird migratory species data
│   ├── raw/          # Raw downloaded data
│   ├── filtered/     # Filtered migration data
│   └── processed/    # Cleaned and processed data
├── ndvi/             # NDVI greenness data
│   ├── modis/       # MODIS NDVI
│   ├── landsat/     # Landsat NDVI
│   └── processed/   # Processed time series
├── habitat/          # Stopover site habitat data
│   ├── iba/         # Important Bird Areas
│   ├── landcover/   # Land cover data
│   └── climate/     # Climate data
└── derived/          # Derived data products
    └── stopover_quality/  # Final stopover quality indices
```

## Data Not Included in Repository

Due to file size limitations, actual datasets are **not** stored in this Git repository. 

Please download datasets following the instructions in [DATASETS.md](../DATASETS.md).

## .gitignore

Large data files are excluded from version control. Only scripts and small reference files should be committed.

Excluded patterns:
- `*.hdf`
- `*.tif`
- `*.tiff`
- `*.nc`
- `*.csv` (large files)
- `*.txt` (large data files)
- `*.zip`
- Raw data directories

## Getting Data

See [DATASETS.md](../DATASETS.md) for:
- Dataset sources and URLs
- Access instructions
- Download methods
- Data processing recommendations
- Citation requirements
