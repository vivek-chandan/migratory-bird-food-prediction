# Datasets for Migratory Bird Food Prediction

This document provides comprehensive information about the datasets needed for the Migratory Bird Stopover Quality Index project, including sources, descriptions, and access methods.

## Overview

The project requires three main types of datasets:
1. **eBird Migratory Species Data** - Bird observation and migration data
2. **NDVI Greenness Data** - Vegetation indices indicating habitat quality and food availability
3. **Stopover Site Habitat Data** - Geographic and environmental data for stopover locations

---

## 1. eBird Migratory Species Data

### eBird Basic Dataset (EBD)

**Source:** Cornell Lab of Ornithology - eBird

**Website:** https://ebird.org/data/download

**Description:** The eBird Basic Dataset contains global bird observation data collected by birdwatchers worldwide. It includes species, location, date, time, and observation counts.

**Key Features:**
- Global coverage with millions of bird observations
- Species-specific migration patterns
- Temporal data (dates, times) for tracking migration periods
- Geographic coordinates for stopover site identification
- Observer effort data

**Access Method:**
1. Create a free eBird account at https://ebird.org
2. Request access to the Basic Dataset at https://ebird.org/data/download/ebd
3. Accept the Data Use Agreement
4. Download the full EBD or custom filtered datasets

**File Format:** Tab-delimited text files (can be large, 100+ GB for global data)

**Relevant Fields:**
- `COMMON NAME`, `SCIENTIFIC NAME` - Species identification
- `OBSERVATION DATE` - For migration timing
- `LATITUDE`, `LONGITUDE` - Stopover location
- `OBSERVATION COUNT` - Bird abundance
- `PROTOCOL TYPE`, `DURATION MINUTES` - Observation effort

**Citation:**
```
eBird Basic Dataset. Version: EBD_relXXX_XXXX. Cornell Lab of Ornithology, Ithaca, New York. 
Available: https://ebird.org/data/download (Accessed: [Date])
```

### eBird Status and Trends

**Source:** eBird Science

**Website:** https://science.ebird.org/en/status-and-trends

**Description:** Modeled estimates of bird abundance and distribution throughout the year, ideal for understanding migration patterns.

**Key Features:**
- Weekly abundance estimates
- Range maps for migration routes
- Seasonal trends
- Stopover site importance metrics

**Access Method:**
- Download via R package `ebirdst`
- Web interface for visualization and data export

**File Format:** GeoTIFF rasters, CSV summaries

**R Package Installation:**
```R
install.packages("ebirdst")
```

---

## 2. NDVI Greenness Data

### MODIS NDVI (MOD13Q1)

**Source:** NASA Earth Observing System

**Website:** https://lpdaac.usgs.gov/products/mod13q1v006/

**Description:** The MODIS Vegetation Indices (MOD13Q1) product provides 16-day composite NDVI at 250m resolution, ideal for monitoring vegetation greenness and food availability.

**Key Features:**
- 250m spatial resolution
- 16-day temporal resolution
- Global coverage
- Quality assurance flags
- Time series from 2000 to present

**Access Methods:**

1. **AppEEARS (Application for Extracting and Exploring Analysis Ready Samples)**
   - Website: https://appeears.earthdatacloud.nasa.gov/
   - Allows point, area, and time series extraction
   - Free registration required

2. **NASA Earthdata Search**
   - Website: https://search.earthdata.nasa.gov/
   - Direct download of MODIS tiles
   - Requires NASA Earthdata account

3. **Google Earth Engine**
   - Dataset ID: `MODIS/006/MOD13Q1`
   - Free for research and education
   - Python/JavaScript API access

**File Format:** HDF-EOS, GeoTIFF (via processing)

**Relevant Bands:**
- `250m 16 days NDVI` - Primary vegetation index
- `250m 16 days EVI` - Enhanced vegetation index
- `250m 16 days VI Quality` - Data quality flags

**Google Earth Engine Example:**
```python
import ee
ee.Initialize()

# Load MODIS NDVI
ndvi = ee.ImageCollection('MODIS/006/MOD13Q1').select('NDVI')

# Filter by date range (migration period)
ndvi_migration = ndvi.filterDate('2020-03-01', '2020-05-31')
```

**Citation:**
```
Didan, K. (2015). MOD13Q1 MODIS/Terra Vegetation Indices 16-Day L3 Global 250m SIN Grid V006. 
NASA EOSDIS Land Processes DAAC. doi: 10.5067/MODIS/MOD13Q1.006
```

### Landsat NDVI

**Source:** USGS/NASA

**Website:** https://earthexplorer.usgs.gov/

**Description:** Higher spatial resolution (30m) NDVI from Landsat satellites, useful for detailed stopover site analysis.

**Key Features:**
- 30m spatial resolution
- 16-day revisit time (with Landsat 8 and 9)
- Historical data from 1984 (Landsat 5)

**Access Method:**
- USGS EarthExplorer: https://earthexplorer.usgs.gov/
- Google Earth Engine: `LANDSAT/LC08/C02/T1_L2`

### Sentinel-2 NDVI

**Source:** European Space Agency (ESA)

**Website:** https://scihub.copernicus.eu/

**Description:** High-resolution (10m) vegetation indices from Sentinel-2 satellites.

**Key Features:**
- 10m spatial resolution
- 5-day revisit time
- Data from 2015 to present

**Access Method:**
- Copernicus Open Access Hub: https://scihub.copernicus.eu/
- Google Earth Engine: `COPERNICUS/S2_SR`

---

## 3. Stopover Site and Habitat Data

### Important Bird Areas (IBA) Database

**Source:** BirdLife International

**Website:** http://datazone.birdlife.org/site/search

**Description:** Global database of sites critical for bird conservation, including many important stopover sites.

**Key Features:**
- Site boundaries and coordinates
- Habitat descriptions
- Species lists
- Conservation status

**Access Method:**
- Search and download via BirdLife Data Zone
- Requires registration for bulk downloads

### Global Land Cover Data

**Source:** ESA Climate Change Initiative

**Website:** https://www.esa-landcover-cci.org/

**Description:** Annual global land cover maps at 300m resolution.

**Key Features:**
- Land cover classification (22 classes)
- Annual updates
- Global coverage from 1992 to present

**Access Method:**
- Direct download from ESA CCI website
- Also available via Google Earth Engine: `ESA/WorldCover/v100`

### WorldClim - Climate Data

**Source:** WorldClim

**Website:** https://www.worldclim.org/

**Description:** Historical and future climate data at various spatial resolutions.

**Key Features:**
- Temperature and precipitation data
- Bioclimatic variables
- Multiple spatial resolutions (30 seconds to 10 minutes)

**Access Method:**
- Direct download from WorldClim website
- Available in GeoTIFF format

---

## 4. Additional Relevant Datasets

### GBIF (Global Biodiversity Information Facility)

**Source:** GBIF

**Website:** https://www.gbif.org/

**Description:** Global biodiversity database including bird occurrence records.

**Access Method:**
- Web interface with filtering options
- API access for programmatic downloads
- R package: `rgbif`

### Protected Planet - WDPA

**Source:** UNEP-WCMC

**Website:** https://www.protectedplanet.net/

**Description:** World Database on Protected Areas, useful for understanding conservation status of stopover sites.

**Access Method:**
- Download via Protected Planet website
- Requires registration

---

## Data Processing Recommendations

### Tools and Libraries

**Python:**
```python
# Essential libraries
import pandas as pd
import geopandas as gpd
import rasterio
import earthengine as ee
import numpy as np
from auk import auk  # eBird data processing
```

**R:**
```R
# Essential packages
library(auk)        # eBird data
library(sf)         # Spatial data
library(raster)     # Raster processing
library(terra)      # Modern raster processing
library(ebirdst)    # eBird Status and Trends
```

### Workflow

1. **Download eBird data** for target migratory species and regions
2. **Filter observations** to migration periods (spring/fall)
3. **Identify stopover sites** using clustering or hotspot analysis
4. **Extract NDVI values** at stopover locations during migration periods
5. **Calculate stopover quality metrics** based on NDVI, habitat type, and bird abundance
6. **Analyze temporal trends** to identify declining stopover zones

---

## Data Storage Structure

Recommended directory structure:
```
datasets/
├── ebird/
│   ├── raw/              # Raw EBD data
│   ├── filtered/         # Filtered migration data
│   └── processed/        # Cleaned and processed data
├── ndvi/
│   ├── modis/           # MODIS NDVI data
│   ├── landsat/         # Landsat NDVI data
│   └── processed/       # Processed time series
├── habitat/
│   ├── iba/             # Important Bird Areas
│   ├── landcover/       # Land cover data
│   └── climate/         # Climate data
└── derived/
    └── stopover_quality/  # Final stopover quality indices
```

---

## Data Use and Citations

**Important Notes:**
- Always check and comply with data usage licenses and terms
- Cite all data sources in publications
- eBird data requires acceptance of Data Use Agreement
- NASA data is freely available for research
- Some datasets may have restrictions on commercial use

**General Citation Format:**
Include dataset name, version, provider, URL, and access date in all publications.

---

## Getting Started

### Quick Start Steps:

1. **Create accounts:**
   - eBird account: https://ebird.org
   - NASA Earthdata: https://urs.earthdata.nasa.gov/
   - Google Earth Engine: https://earthengine.google.com/

2. **Install necessary tools:**
   ```bash
   # Python environment
   pip install pandas geopandas rasterio earthengine-api
   
   # R packages
   R -e "install.packages(c('auk', 'sf', 'terra', 'ebirdst'))"
   ```

3. **Request dataset access:**
   - Submit eBird data request
   - Authenticate Earth Engine
   - Test data access with small samples

4. **Start with pilot data:**
   - Select a small geographic region
   - Download 1-2 years of data
   - Develop and test processing pipeline
   - Scale up to full dataset

---

## Support and Resources

- **eBird Help:** https://support.ebird.org/
- **NASA Earthdata Help:** https://earthdata.nasa.gov/support
- **Google Earth Engine Documentation:** https://developers.google.com/earth-engine/
- **eBird R Package Tutorial:** https://cornelllabofornithology.github.io/auk/

---

Last Updated: February 2026
