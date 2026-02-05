# Migratory Bird Food Prediction

## Project Overview

This project aims to develop a **Migratory Bird Stopover Quality Index** by analyzing eBird migratory species data and NDVI (Normalized Difference Vegetation Index) greenness at stopover sites. The goal is to quantify food and habitat availability during peak migration months and identify declining stopover zones, with a focus on understudied regions in global migration maps.

## Problem Statement

Use eBird migratory species data and NDVI greenness at stopover sites to:
- Quantify food and habitat availability during peak migration months
- Identify declining stopover zones
- Focus on understudied areas in global migration maps

## Datasets

This project requires several datasets from online sources:

1. **eBird Migratory Species Data** - Bird observation and migration patterns
2. **NDVI Greenness Data** - Vegetation indices for food availability
3. **Stopover Site Habitat Data** - Geographic and environmental data

**For detailed information about datasets, sources, and download instructions, see [DATASETS.md](DATASETS.md).**

### Quick Start

1. Review [DATASETS.md](DATASETS.md) for comprehensive dataset information
2. Create necessary accounts (eBird, NASA Earthdata, Google Earth Engine)
3. Download datasets to the `datasets/` directory following the structure in `datasets/README.md`
4. Follow data processing guidelines in [DATASETS.md](DATASETS.md)

## Data Sources Summary

- **eBird Basic Dataset**: https://ebird.org/data/download
- **MODIS NDVI**: https://lpdaac.usgs.gov/products/mod13q1v006/
- **Important Bird Areas**: http://datazone.birdlife.org/
- **Additional sources**: See [DATASETS.md](DATASETS.md)

## Repository Structure

```
.
├── README.md              # This file
├── DATASETS.md            # Comprehensive dataset documentation
├── datasets/              # Dataset storage directory (data not in git)
│   └── README.md         # Dataset directory structure
└── independent/           # Independent project materials
    └── problem_statement.txt
```

## Getting Started

1. **Set up accounts**: Create accounts for eBird, NASA Earthdata, and Google Earth Engine
2. **Install tools**: Install Python/R packages for data processing (see DATASETS.md)
3. **Download data**: Follow instructions in DATASETS.md
4. **Process data**: Use the recommended workflows in DATASETS.md

## License

Please ensure compliance with all dataset licenses and terms of use. See DATASETS.md for citation requirements.

## Contributing

When contributing:
- Do not commit large data files (see .gitignore)
- Follow the data structure outlined in datasets/README.md
- Cite all data sources appropriately
- Document any new datasets in DATASETS.md