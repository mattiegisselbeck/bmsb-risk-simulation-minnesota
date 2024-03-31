# Data Extraction via Minnesota Geospatial Geocommons

# Set URLs
$mnNLCDURL = "https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dnr/biota_landcover_nlcd_mn_2019/tif_biota_landcover_nlcd_mn_2019.zip"
$mnDEMURL = "https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dnr/elev_30m_digital_elevation_model/fgdb_elev_30m_digital_elevation_model.zip"
$mnCityTerritoryURL = "https://resources.gisdata.mn.gov/pub/gdrs/data/pub/us_mn_state_dot/bdry_mn_city_township_unorg/shp_bdry_mn_city_township_unorg.zip"

# Set Directory Paths
$wd = pwd
$DataDir = Join-Path -Path $wd -ChildPath "data"
$mnNLCDDir = Join-Path -Path $DataDir -ChildPath "mnNLCD"
$mnDEMDir = Join-Path -Path $DataDir -ChildPath "mnDEM"
$mnCityTerritoryDir = Join-Path -Path $DataDir -ChildPath "mnCityTerritory"

$mnNLCDZip = Join-Path -Path $mnNLCDDir -ChildPath "mnNLCD.zip"
$mnDEMZip = Join-Path -Path $mnDEMDir -ChildPath "mnDEM.zip"
$mnCityTerritoryZip = Join-Path -Path $mnCityBoundariesDir -ChildPath "mnCityTerritory.zip"

# Create Directories
New-Item -Path $mnNLCDDir -ItemType Directory
New-Item -Path $mnDEMDir -ItemType Directory
New-Item -Path $mnCityTerritoryDir -ItemType Directory

# Download NLCD 2019 Land Cover, Minnesota
Write-Host "Downloading NLCD 2019 Land Cover, Minnesota..."
Invoke-WebRequest -Uri $mnNLCDURL -OutFile $mnNLCDZip
Write-Host "NLCD 2019 Land Cover, Minnesota..."
Expand-Archive $mnNLCDZip -DestinationPath $mnNLCDDir -Force

# Download Minnesota Digital Elevation Model - 30 Meter Resolution
Write-Host "Downloading Minnesota Digital Elevation Model - 30 Meter Resolution..."
Invoke-WebRequest -Uri $mnDEMURL -OutFile $mnDEMZip
Write-Host "Unzipping Minnesota Digital Elevation Model - 30 Meter Resolution..."
Expand-Archive $mnDEMZip -DestinationPath $mnDEMDir -Force

# Download City, Township, and Unorganized Territory in Minnesota
Write-Host "Downloading City, Township, and Unorganized Territory in Minnesota..."
Invoke-WebRequest -Uri $mnCityTerritoryURL -OutFile $mnCityTerritoryZip
Write-Host "Unzipping City, Township, and Unorganized Territory in Minnesota..."
Expand-Archive $mnCityTerritoryZip -DestinationPath $mnCityTerritoryDir -Force
