# Quick Reference Guide - Dataset Access

This is a quick reference for accessing the main datasets. For complete details, see [DATASETS.md](../DATASETS.md).

## Essential Datasets

### 1. eBird Data (Bird Observations)

**What you need:** Migratory bird observation data

**Quick Access:**
```
1. Go to: https://ebird.org/data/download
2. Create account / Log in
3. Request "eBird Basic Dataset" access
4. Accept Data Use Agreement  
5. Download custom data request or full dataset
```

**Citation Required:** Yes - see DATASETS.md

---

### 2. MODIS NDVI (Vegetation/Food Availability)

**What you need:** Vegetation greenness data (250m resolution)

**Quick Access via Google Earth Engine:**
```python
import ee
ee.Initialize()

# Load MODIS NDVI
ndvi = ee.ImageCollection('MODIS/006/MOD13Q1').select('NDVI')

# Filter for spring migration (adjust dates as needed)
spring = ndvi.filterDate('2023-03-01', '2023-05-31')
```

**Alternative:** AppEEARS - https://appeears.earthdatacloud.nasa.gov/

**Citation Required:** Yes - see DATASETS.md

---

### 3. Important Bird Areas (Stopover Sites)

**What you need:** Known important stopover locations

**Quick Access:**
```
1. Go to: http://datazone.birdlife.org/site/search
2. Register for an account
3. Search by region or species
4. Download site data
```

**Citation Required:** Yes

---

## Account Setup Checklist

Create these accounts to access all datasets:

- [ ] **eBird** → https://ebird.org/home
- [ ] **NASA Earthdata** → https://urs.earthdata.nasa.gov/
- [ ] **Google Earth Engine** → https://earthengine.google.com/
- [ ] **BirdLife Data Zone** → http://datazone.birdlife.org/

---

## First-Time Setup

### Python Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Authenticate Earth Engine
python -c "import ee; ee.Authenticate()"
```

### Create Directory Structure
```bash
# Run the helper script
python datasets/download_helper.py
```

---

## Common Tasks

### Task 1: Get eBird data for a species
1. Go to eBird download page
2. Select species from dropdown
3. Choose date range (migration period)
4. Select geographic region
5. Submit request and download when ready

### Task 2: Extract NDVI for locations
Use the example in `download_helper.py` or Google Earth Engine Code Editor

### Task 3: Find stopover sites
1. Check BirdLife IBA database
2. Analyze eBird data for clustering
3. Look for high-abundance areas during migration

---

## Getting Help

- **eBird issues:** https://support.ebird.org/
- **Earth Engine forum:** https://groups.google.com/g/google-earth-engine-developers
- **Dataset details:** See [DATASETS.md](../DATASETS.md)

---

## Migration Periods (Northern Hemisphere)

Use these as default date ranges:

- **Spring Migration:** March 1 - May 31
- **Fall Migration:** August 1 - October 31

Adjust based on specific species and geographic region.

---

Last Updated: February 2026
