"""
Data Download Helper Script for Migratory Bird Food Prediction Project

This script provides helper functions and examples for downloading datasets
from various sources. Users should review DATASETS.md for full details.

Requirements:
    pip install earthengine-api requests pandas geopandas
"""

import os
from pathlib import Path


def setup_directories():
    """Create the recommended directory structure for datasets."""
    base_dir = Path("datasets")
    
    directories = [
        "ebird/raw",
        "ebird/filtered", 
        "ebird/processed",
        "ndvi/modis",
        "ndvi/landsat",
        "ndvi/processed",
        "habitat/iba",
        "habitat/landcover",
        "habitat/climate",
        "derived/stopover_quality"
    ]
    
    for directory in directories:
        dir_path = base_dir / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path}")
    
    print("\n✓ Directory structure created successfully!")
    print("\nNext steps:")
    print("1. Review DATASETS.md for dataset sources")
    print("2. Create required accounts (eBird, NASA Earthdata, Google Earth Engine)")
    print("3. Download datasets following the instructions in DATASETS.md")


def check_earth_engine_auth():
    """Check if Google Earth Engine is authenticated."""
    try:
        import ee
        try:
            ee.Initialize()
            print("✓ Google Earth Engine is authenticated")
            return True
        except Exception as e:
            print("✗ Google Earth Engine not authenticated")
            print("\nTo authenticate, run:")
            print("  import ee")
            print("  ee.Authenticate()")
            print("  ee.Initialize()")
            return False
    except ImportError:
        print("✗ earthengine-api package not installed")
        print("\nTo install, run:")
        print("  pip install earthengine-api")
        return False


def example_modis_ndvi_download():
    """
    Example code for downloading MODIS NDVI data using Google Earth Engine.
    
    Note: This is a template. Users need to:
    1. Authenticate with Google Earth Engine first
    2. Define their area of interest
    3. Specify the date range for migration periods
    """
    example_code = """
# Example: Download MODIS NDVI for a specific location and time period
import ee

# Initialize Earth Engine (run ee.Authenticate() first if needed)
ee.Initialize()

# Define area of interest (example: coordinates for a stopover site)
# Replace with your actual coordinates
aoi = ee.Geometry.Point([-95.0, 40.0]).buffer(50000)  # 50km radius

# Define time period (example: spring migration)
start_date = '2023-03-01'
end_date = '2023-05-31'

# Load MODIS NDVI collection
modis_ndvi = ee.ImageCollection('MODIS/006/MOD13Q1') \\
    .select('NDVI') \\
    .filterDate(start_date, end_date) \\
    .filterBounds(aoi)

# Calculate mean NDVI over time period
mean_ndvi = modis_ndvi.mean()

# Export to Google Drive
task = ee.batch.Export.image.toDrive(
    image=mean_ndvi,
    description='MODIS_NDVI_Spring_Migration',
    folder='MigratoryBird_NDVI',
    region=aoi.getInfo()['coordinates'],
    scale=250,  # MODIS resolution
    crs='EPSG:4326'
)

# Start the export
task.start()
print('Export task started. Check Google Earth Engine Tasks tab for progress.')
"""
    print("\n" + "="*70)
    print("EXAMPLE: MODIS NDVI Download via Google Earth Engine")
    print("="*70)
    print(example_code)
    print("="*70)
    print("\nNote: Save this code to a script and customize for your needs.")


def print_dataset_checklist():
    """Print a checklist of datasets to download."""
    checklist = """
    
DATASET DOWNLOAD CHECKLIST
===========================

□ eBird Data
  □ Created eBird account: https://ebird.org
  □ Requested EBD access: https://ebird.org/data/download/ebd
  □ Accepted Data Use Agreement
  □ Downloaded dataset or set up custom data request
  
□ NDVI Data
  □ Created NASA Earthdata account: https://urs.earthdata.nasa.gov/
  □ Selected NDVI source (MODIS/Landsat/Sentinel-2)
  □ Set up Google Earth Engine (optional): https://earthengine.google.com/
  □ Downloaded NDVI data for migration periods
  
□ Habitat Data
  □ Registered at BirdLife Data Zone: http://datazone.birdlife.org/
  □ Downloaded Important Bird Areas data
  □ Downloaded land cover data (ESA CCI or similar)
  
□ Additional Data (optional)
  □ Downloaded WorldClim climate data: https://www.worldclim.org/
  □ Downloaded Protected Planet data: https://www.protectedplanet.net/
  
□ Data Organization
  □ Placed datasets in correct directories
  □ Documented dataset versions and download dates
  □ Verified data integrity

For detailed instructions, see DATASETS.md
"""
    print(checklist)


def main():
    """Main function to help users get started with data download."""
    print("="*70)
    print("MIGRATORY BIRD FOOD PREDICTION - DATA SETUP HELPER")
    print("="*70)
    print("\nThis script helps you set up the project data structure.")
    print("For complete dataset information, please review DATASETS.md")
    print()
    
    # Setup directories
    response = input("Create directory structure? (y/n): ").strip().lower()
    if response == 'y':
        setup_directories()
    
    print()
    
    # Check Earth Engine
    response = input("Check Google Earth Engine authentication? (y/n): ").strip().lower()
    if response == 'y':
        check_earth_engine_auth()
    
    print()
    
    # Show example
    response = input("Show MODIS NDVI download example? (y/n): ").strip().lower()
    if response == 'y':
        example_modis_ndvi_download()
    
    print()
    
    # Show checklist
    response = input("Show dataset download checklist? (y/n): ").strip().lower()
    if response == 'y':
        print_dataset_checklist()
    
    print("\n" + "="*70)
    print("For more information, see DATASETS.md in the root directory.")
    print("="*70)


if __name__ == "__main__":
    main()
