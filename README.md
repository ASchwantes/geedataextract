# **geedataextract**

This package includes functions to download environmental and remote sensing data from Google Earth Engine, using the GEE python API. Environmental data can be extracted at the nearest pixel to a point or spatially averaged over pixels around a buffer from a point or within a polygon. Shapefiles of points or polygons must be [uploaded to GEE](https://developers.google.com/earth-engine/importing) in your [assets folder](https://code.earthengine.google.com/). Data tables will be automatically downloaded to your Google Drive. Functions exist for downloading environmental data related to land cover, topograpy, soil condition, climate, soil moisture (SMOS), and landsat & MODIS vegetation indices/products. A complete tutorial in jupyter notebooks can be found [here](https://www.pbgjam.org/products#Tutorials/). This package was developed under the support of the National Aeronautics and Space Administration's Advanced Information Systems Technology Program [(award number AIST-16-0052)](https://esto.nasa.gov/files/solicitations/AIST_16/ROSES2016_AIST_A41_awards.html#swenson) and the National Science Foundation [(award number 1754443)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1754443&HistoricalAwards=false). This package is still preliminary; we are constantly making updates and improvements. Please email me with any comments or suggestions at aschwantes@gmail.com.

> suggested citation: Schwantes, Amanda M., Chase Nuñez. (2019). geeDataExtract. Python package version 0.0.1.

### Download the GEE API
To use these functions you must [install the GEE python API](https://github.com/earthlab/tutorials/blob/master/documentation/intro-google-earth-engine-python-api.md). We recommend first installing [Anaconda Python 3.7](https://www.anaconda.com/distribution/) and registering for a [Google Earth Engine account](https://signup.earthengine.google.com/#!/). Then run the following commands from the Command Prompt (windows), the Terminal (mac), or the "Anaconda Prompt". Examples below are for Anaconda, but you can also use pip.

1. Install the python API client
```
conda install -c conda-forge google-api-python-client
```
2. Install the Earth Engine Python Library
```
conda install -c conda-forge earthengine-api
```
3.  Initialize the API and verify your account settings. This will open a web-browser. Login to your gmail account and copy/paste the key from the web-browser into the Command Promt. You will need to login to the gmail account that you
used to sign up for Google Earth Engine.
```
earthengine authenticate
```
4. Verify that the GEE API is working. You should not get an error by running this command.
```
python -c "import ee; ee.Initialize()"
```

### Important next steps
* **Add a new folder to your google drive.** You will need to specify this folder name using the parameter folderOut in each function. CSV files will be downloaded in this folder.  


* **How to use your own data?** To extract values at your points/polygons of interest, you will need to upload a shapefile to your assets folder in GEE; instructions __[here](https://developers.google.com/earth-engine/importing)__.

  + Add an ID column to your shapefile with the name "geeID" before you upload your file to your assets folder.  
  + Each row must have a unique ID.  
  + Each row/geeID should be unique through space. Do not include duplicate points through time; time-series data will be downloaded for each unique geeID.
  + To reduce the file size of the output tables, location information is removed. The geeID field is required to restore location information.


* **Set your username**. Each function has a parameter called "username", which must be specified. Your GEE username is typically your gmail adress. Look in the asset folder under users to verify [here](https://code.earthengine.google.com/).


* **To obtain data at points or spatial averages within polygons use the parameters buf and poly.** If you want the nearest pixel to an uploaded shapefile of points, then set buf = 0 and poly = 0. If you want a spatial average from a buffer around each point, then specify a value for buf in meters. For example, poly = 0 and buf = 1000, would give a spatial average of the pixels within a 1000 m radius circle around each point in your uploaded shapefile. If you want a spatial average within polygons for an uploaded shapefile of polygons, then set buf = 0 and poly = 1.


* **Consider using the 'scalePix' parameter**.

  + If you need to take a spatial average across a plot, then you will need to consider the scale of the imagery. If the size of your plot/polygon is much smaller than the spatial resolution of your imagery (scale) then reduce the scale, by using the optional parameter 'scalePix'. Or provide centroids for your plots instead of taking a spatial average. GEE functions take the weighted average within a polygon; however any pixels that are not 50% within the polygon are not included in the averaging. If your scale is much larger than your plot, all your output tables will be full of NAs.
  + Similiarly, to take a value at a point, for environmental data at fine-scales, we'd recommend reducing the 'scalePix'. If the scalepix is set to the resolution of the environmental data (the default in our functions), GEE functions will often give a value of a point that is shifted by up to the value of scalePix. Therefore, if you want to avoid a point shift, then reduce 'scalePix' to a value less than the spatial resolution of the dataset (the default in our functions).

### Below we provide descriptions for downloading data as well as suggested citations

When using this python package, we have tried to include suggested citations for each of the data products. GEE is simply hosting publically available data; therefore if you use one of these functions to download a dataset you should properly give credit to the authors who created the dataset. We have provided suggested citations; however, please refer to the original websites/links to metadata for each dataset to confirm that these suggested citations are current.

Furthermore, when using GEE, see this [link](https://earthengine.google.com/faq/) for a suggested citation. Currently, GEE suggests the following:

> Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., & Moore, R. (2017). Google Earth Engine: Planetary-scale geospatial analysis for everyone. Remote Sensing of Environment.

## Land cover

The source data for these functions is from the USGS National Land Cover Database (NLCD). The GEE ImageCollection ID is
"USGS/NLCD".

__GEEtcPts()__ calculates percent tree cover  
__GEEicPts()__ calculates percent impervious cover  
__GEElcPts()__ calculates land cover value at a point or a frequency table of land cover types within a polygon or buffer from a point

Land cover classes can be found __[here](https://www.mrlc.gov/data/legends/national-land-cover-database-2011-nlcd2011-legend)__, and more info on the products can be found __[here](https://www.mrlc.gov/data)__.

Proper citations depend on the NLCD product:  
> _NLCD 2001 citation:_ Homer, C., Dewitz, J., Fry, J., Coan, M., Hossain, N., Larson, C., Herold, N., McKerrow, A., VanDriel, J.N., and Wickham, J. 2007. Completion of the 2001 National Land Cover Database for the Conterminous United States. Photogrammetric Engineering and Remote Sensing, Vol. 73, No. 4, pp 337-341.  

> _NLCD 2006 citation:_ Fry, J., Xian, G., Jin, S., Dewitz, J., Homer, C., Yang, L., Barnes, C., Herold, N., and Wickham, J., 2011. Completion of the 2006 National Land Cover Database for the Conterminous United States, PE&RS, Vol. 77(9):858-864.  

> _NLCD 2011 citation:_ Homer, C.G., Dewitz, J.A., Yang, L., Jin, S., Danielson, P., Xian, G., Coulston, J., Herold, N.D., Wickham, J.D., and Megown, K., 2015, Completion of the 2011 National Land Cover Database for the conterminous United States-Representing a decade of land cover change information. Photogrammetric Engineering and Remote Sensing, v. 81, no. 5, p. 345-354  

## Topography

Source data is from the SRTM Digital Elevation Data 30m product. More info found __[here](https://www2.jpl.nasa.gov/srtm/)__. The GEE ImageCollection ID is 'USGS/SRTMGL1_003'.


The function __GEEtopoPts()__ calculates topograpy metrics:
> elevation (meters)  
> slope (radians)  
> aspect (radians)  

When calculating aspect at a point, the output will include only one value of aspect (in radians). When taking a spatial average of aspect within a plot or buffer, two metrics are computed: (1) aspect_sin: aspectSinSum and (2) aspect_cos: aspectCosSum. The circular average of aspect can then be calculated using: atan2(aspectSinSum, aspectCosSum), as described __[here](https://en.wikipedia.org/wiki/Mean_of_circular_quantities)__.

Citation:  
> Farr, Tom G., et al. "The shuttle radar topography mission." Reviews of geophysics 45.2 (2007).


# Soil metrics

Source data from SoilGrids250, downloaded from ftp://ftp.soilgrids.org/data/recent/

The function __GEEsoilPts()__ calculates soil metrics (depth weighted averages to 1-m) for the following:

> 'oc' = Soil organic carbon content (fine earth fraction) in g per kg  
> 'ph' = Soil pH x 10 in H2O  
> 'cec' = Cation exchange capacity of soil in cmolc/kg  
> 'sand' = Sand content (50-2000 micro meter) mass fraction in %  
> 'silt' = Silt content (2-50 micro meter) mass fraction in %  
> 'cfrag' = Coarse fragments volumetric in %  
> 'clay' = Clay content (0-2 micro meter) mass fraction in %  
> 'bulkDensity' = Bulk density (fine earth) in kg / cubic-meter  
> 'soilDepth' = Absolute depth to bedrock (in cm)  

Suborder classes for the USDA and WRB classifications are also available. Specifyng these metrics will calculate suborder class at a point or the mode within a polygon or buffer around a point. The legends for the USDA 2014 suborder classes can be found here: ftp://ftp.soilgrids.org/legends/TAXOUSDA.txt and the WRB 2006 subgroup classes can be found here: ftp://ftp.soilgrids.org/legends/TAXNWRB.txt.

> 'subordersUS' = Predicted USDA 2014 suborder classes (as integers)  
> 'subordersWorld' = Predicted WRB 2006 subgroup classes (as integers)  

Citation:
> Hengl, T., Mendes de Jesus, J., Heuvelink, G. B.M., Ruiperez Gonzalez, M., Kilibarda, M. et al. (2017) SoilGrids250m: global gridded soil information based on Machine Learning. PLoS ONE 12(2): e0169748. doi:10.1371/journal.pone.0169748.


# Climate: daily, monthly, or annual average

Source data from GRIDMET: University of Idaho Gridded Surface Meteorological Dataset. More info about this dataset can be found __[here](https://climate.northwestknowledge.net/METDATA/)__. The GEE ImageCollection ID is "IDAHO_EPSCOR/GRIDMET".

The function __GEEgridmetPtsAvg()__ calculates temporal daily, monthly, or annual averages as well as a spatial average either at a single point, within a buffer from a point or within a polygon.

#### Metrics include:
> tmax: average maximum temperature (K)  
> tmin: average minimum temperature (K)  
> vpd: average vapor pressure deficit (kPa)

#### timeStep options include:
> year: annual averages  
> month: monthly averages  
> day: daily averages  

Best practice when averaging across days/months is to only output 10 years at a time. Otherwise you will get a "Computation timed out" error message on GEE, because you're requesting to process too much data at one time.

Suggested citation(s):  
> Abatzoglou J.T. and Brown T.J., A comparison of statistical downscaling methods suited for wildfire applications, International Journal of Climatology(2012) doi: http://dx.doi.org/10.1002/joc.2312.

> Abatzoglou J. T., Development of gridded surface meteorological data for ecological applications and modelling, International Journal of Climatology. (2012) doi: http://dx.doi.org/10.1002/joc.3413


# Climate: daily, monthly or annual sum

Source data from GRIDMET: University of Idaho Gridded Surface Meteorological Dataset. More info about this dataset can be found __[here](https://climate.northwestknowledge.net/METDATA/)__. The GEE ImageCollection ID is "IDAHO_EPSCOR/GRIDMET".

The function __GEEgridmetPtsSum()__ calculates the temporal daily, monthly, or annual sum as well as a spatial average either at a single point, within a buffer from a point or within a polygon.

#### Metrics include:  
> pr: precipitation amount (mm, total sum)   
> eto: Daily reference evapotranspiration (grass, mm, total sum)  

#### timeStep options include:
> year: annual sum  
> month: monthly sum  
> day: daily sum  

Best practice when summing across months is to only output 10 years at a time. Otherwise you will get a "Computation timed out" error message on GEE, because you're requesting to process too much data at one time.

Suggested citation(s):  
> Abatzoglou J.T. and Brown T.J., A comparison of statistical downscaling methods suited for wildfire applications, International Journal of Climatology(2012) doi: http://dx.doi.org/10.1002/joc.2312.  

> Abatzoglou J. T., Development of gridded surface meteorological data for ecological applications and modelling, International Journal of Climatology. (2012) doi: http://dx.doi.org/10.1002/joc.3413

# Global climate: monthly average

Source data from TERRACLIMATE. More info about this dataset can be found __[here](http://www.climatologylab.org/terraclimate.html)__. The GEE ImageCollection ID is "IDAHO_EPSCOR/TERRACLIMATE".

The function __GEEterraClimatePtsAvgMonth()__ calculates the temporal monthly average as well as a spatial average either at a single point, within a buffer from a point or within a polygon.

#### Metrics include:
> aet: Actual evapotranspiration (mm)  
> def: climatic water deficit (mm)  
> pdsi: Palmer Drought Severity Index  
> pet: reference evapotranspiration (penman-montieth, mm)  
> pr: precipitation (mm)  
> ro: runoff (mm)  
> soil: soil moisture (mm)  
> srad: Downward surface shortwave radiation (W/m2)  
> swe: snow water equivalent (mm)  
> tmmn: min temperature (deg C)  
> tmmx: max temperature (deg C)  
> vap: vapor pressure (kPa)  
> vpd: vapor pressure deficit (kPa)  
> vs: Wind-speed at 10m (m/s)  

Best practice when averaging across months is to only output 10 years at a time. Otherwise you will get a "Computation timed out" error message on GEE, because you're requesting to process too much data at one time.

Suggested citation(s):  
> Abatzoglou, J.T., S.Z. Dobrowski, S.A. Parks, K.C. Hegewisch, 2018, Terraclimate, a high-resolution global dataset of monthly climate and climatic water balance from 1958-2015, Scientific Data,

# Contiguous US climate (PRISM): monthly average

Source data from PRISM. More info about this dataset can be found __[here](http://www.prism.oregonstate.edu/documents/PRISM_datasets.pdf)__. The GEE ImageCollection ID is "OREGONSTATE/PRISM/AN81m".

The function __GEEprismPtsAvgMonth()__ calculates the temporal monthly average as well as a spatial average either at a single point, within a buffer from a point or within a polygon.

#### Metrics include:

> ppt: "Monthly total precipitation (including rain and melted snow)" (mm)  
> tmean: "Monthly average of daily mean temperature" (deg C)  
> tmin: "Monthly minimum temperature" (deg C)  
> tmax: "Monthly average of daily maximum temperature" (deg C)  
> tdmean: "Monthly average of daily mean dew point temperature" (deg C)   
> vpdmin: "Monthly average of daily minimum vapor pressure deficit" (hPa)  	
> vpdmax: "Monthly average of daily maximum vapor pressure deficit" (hPa)  

#### Suggested citation(s):

> Daly, C., Halbleib, M., Smith, J.I., Gibson, W.P., Doggett, M.K., Taylor, G.H., Curtis, J., and Pasteris, P.A. 2008. Physiographically-sensitive mapping of temperature and precipitation across the conterminous United States. International Journal of Climatology, 28: 2031-2064  

> Daly, C., J.I. Smith, and K.V. Olson. 2015. Mapping atmospheric moisture climatologies across the conterminous United States. PloS ONE 10(10):e0141140. doi:10.1371/journal.pone.0141140.

# Remote Sensing Data

All the functions below can be used to download remote sensing data. Unless otherwise specified, each function has a parameter called timeStep, where you can specify the type of temporal averaging. Options include:  

    'lowest' for no temporal averaging
    'month' for monthly time-step
    'year' for annual time-steps

Caution, if you select 'lowest' for no temporal averaging then it may take a very long time to calculate your time-series.

Also, if you take monthly or annual averages, we are not interpolating before averaging. Therefore, in cloudy areas, this may not be good practise. Instead, use the lowest or monthly time-step for averaging and either exclude data points when there is too much missing data, and/or take averages after interpolating the missing data.

## Soil Moisture from SMOS

Source data from: NASA-USDA Global Soil Moisture Data. The GEE ImageCollection ID is "NASA_USDA/HSL/soil_moisture".

The __GEEsmos()__ function calculates the temporal average as well as a spatial average either at a single point, within a buffer from a point or within a polygon.

#### Metrics include the following: [links provide variable descriptions]  
> 'ssm' = __[Surface soil moisture (mm)](https://ipad.fas.usda.gov/cropexplorer/description.aspx?legendid=352)__  
> 'susm' = __[Subsurface soil moisture (mm)](https://ipad.fas.usda.gov/cropexplorer/description.aspx?legendid=353)__  
> 'smp' = __[Soil moisture profile (fraction, 0-1)](https://ipad.fas.usda.gov/cropexplorer/description.aspx?legendid=354)__

#### Suggested citation(s)

> I. E. Mladenova, J.D. Bolten, W.T. Crow, M.C. Anderson, C.R. Hain, D.M. Johnson, R. Mueller(2017). Intercomparison of Soil Moisture, Evaporative Stress, and Vegetation Indices for Estimating Corn and Soybean Yields Over the U.S., IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, vol. 10, no. 4, pp. 1328-1343, doi: 10.1109/JSTARS.2016.2639338.

> Bolten, J., and W. T. Crow (2012). Improved prediction of quasi-global vegetation conditions using remotely-sensed surface soil moisture, Geophysical Research Letters, 39 (L19406).

> Bolten, J., W.T. Crow, X. Zhan, T.J. Jackson, and C.A. Reynolds (2010). Evaluating the Utility of Remotely Sensed Soil Moisture Retrievals for Operational Agricultural Drought Monitoring IEEE Trans. Geosci. Remote Sens., 3(1), 57-66.  

## Landsat Vegetation Indices

Source data from: USGS Landsat 4,5,7,& 8 Surface Reflectance Tier 1 products. The GEE ImageCollection ID is 'LANDSAT/LT04/C01/T1_SR' (Landsat 4), 'LANDSAT/LT05/C01/T1_SR' (Landsat 5), 'LANDSAT/LE07/C01/T1_SR' (Landsat 7), and 'LANDSAT/LC08/C01/T1_SR' (Landsat 8).  Please see landsat surface reflectance product guides for [Landsat 4-7](https://www.usgs.gov/media/files/landsat-4-7-surface-reflectance-code-ledaps-product-guide) and [Landsat 8](https://www.usgs.gov/media/files/landsat-8-surface-reflectance-code-lasrc-product-guide).

The __GEEviLandsat()__ function calculates the temporal average as well as a spatial average either at a single point, within a buffer from a point or within a polygon.

#### The following vegetation indices can be selected:

> 'NDVI' = Normalized Difference Vegetation Index (NIR-RED)/(NIR+RED)  
> 'NDWI'; = Normalized Difference Water Index (NIR-SWIR)/(NIR+SWIR)  
> 'NBR'; = Normalized Difference Burn Ratio (NIR-SWIR)/(NIR+SWIR)

This function relies on data from the surface reflectance product (atmospheric correction has already been applied). Pixels that have clouds or cloud shadows are removed before temporal averaging, using the QC layer specific to each pixel within an image in the time series.

The following Landsat satellites can be selected. Remember, each sensor has a unique time-period:  

> L4: Landsat 4 images taken from Aug 22, 1982 to Dec 14, 1993    
> L5: Landsat 5 images taken from Jan 1, 1984 to May 5, 2012    
> L7: Landsat 7 images taken from Jan 1, 1999 to present  
> L8: Landsat 8 images taken from Apr 11, 2013 to present  

Suggested citations:

> Landsat Surface Reflectance products courtesy of the U.S. Geological Survey Earth Resources Observation and Science Center.   

> Masek, J.G., Vermote, E.F., Saleous N.E., Wolfe, R., Hall, F.G., Huemmrich, K.F., Gao, F., Kutler, J., and Lim, T-K. (2006). A Landsat surface reflectance dataset for North America, 1990–2000. IEEE Geoscience and Remote Sensing Letters 3(1):68-72. http://dx.doi.org/10.1109/LGRS.2005.857030.

## MODIS Phenology

Source data from NASA's MCD12Q2.005 Land Cover Dynamics Yearly L3 Global 500 m product. More info can be found __[here](https://lpdaac.usgs.gov/products/mcd12q2v005/)__. The GEE ImageCollection ID is "MODIS/MCD12Q2".

The function __GEEphenMODIS__ calculates the spatial average either at a single point, within a buffer from a point or within a polygon. This product has an annual time-step so no temporal averaging can be specified. Also, we have not removed poor quality data using the QC layer, because the layer is "not performing as intended". Data is currently available from 2001-2014.  

#### The following metrics can be selected:

> GreenInc: Days since Jan 1, 2000 that correspond to vegetation greenup  
> GreenMax: Days since Jan 1, 2000 that correspond to vegetation maturity  
> GreenDec: Days since Jan 1, 2000 that correspond to vegetation senescence  
> GreenMin: Days since Jan 1, 2000 that correspond to vegetation dormancy  

Suggested citation:
> Friedl, M., Gray, J., Sulla-Menashe, D. (2009). MCD12Q2 MODIS/Terra+Aqua Land Cover Dynamics Yearly L3 Global 500m SIN Grid V005. NASA EOSDIS Land Processes DAAC.

Also, click __[here](https://lpdaac.usgs.gov/citing_our_data)__ for additional suggestions on how to cite this product.

## MODIS LAI and FPAR

Source data from NASA's MCD15A3H.006 MODIS Leaf Area Index/FPAR 4-Day Global 500m product. This product considerers data from both sensors Terra and Aqua. More info can be found __[here](https://lpdaac.usgs.gov/products/mcd15a3hv006/)__. The GEE ImageCollection ID is "MODIS/006/MCD15A3H".

The function __GEElaiMODIS()__, calculates the temporal average of LAI and fpar as well as a spatial average either at a single point, within a buffer from a point or within a polygon.

#### The following metrics can be selected:
> Fpar: 'FPAR absorbed by the green elements of a vegetation canopy' 400-700 nm wavelength  
> Lai: 'One-sided green leaf area per unit ground area'  

Use the QC parameter to specify if only good quality pixels should be included in averaging using the QC flags specific for each pixel within an image.

> None: no masking of poor quality data

> Op1: We only included pixels that satisfied the following conditions: (1) 'Main (RT) method used with no saturation, best result possible', (2) 'Significant clouds NOT present (clear)', and (3) 'No or low atmospheric aerosol levels detected', following the suggested filtering steps from __[Ma et al, _RSE_, 2014](https://www.sciencedirect.com/science/article/pii/S0034425714003228)__.

> Op2: We only included pixels that were of good quality, following __[Li et al, RSE, 2018](https://www.sciencedirect.com/science/article/pii/S0034425717304467)__.  

> Op3: We only included pixels that satisfied the following conditions: (1) Main (RT) method used with or without saturation, (2) 'Significant clouds NOT present (clear)', following, __[Hovi et al, 2017](https://www.sciencedirect.com/science/article/pii/S0168192317302770)__.  


Click __[here](https://lpdaac.usgs.gov/citing_our_data)__ for suggestions on how to cite this product.

# MODIS NDVI and EVI

Source data from NASA's MOD13Q1.006 Terra Vegetation Indices 16-Day Global 250m product. This product considerers data only from the Terra sensor. More info can be found __[here](https://lpdaac.usgs.gov/products/mod13q1v006/)__.  The GEE ImageCollection ID is "MODIS/006/MOD13Q1".

The function __GEEviMODIS()__ calculates the temporal average of NDVI and EVI as well as a spatial average either at a single point, within a buffer from a point or within a polygon.

#### The following metrics can be selected:

> 'NDVI' = Normalized Difference Vegegation Index  
> 'EVI' = Enhanced Vegetation Index

Use the QC parameter to specify if only good quality pixels should be included in averaging using the QC flags specific for each pixel within an image.

> None: no masking of poor quality data

> Op1: We only included pixels that satisfied the following conditions: (1) quality = good or other, (2) usefulness < 12 (3)  Aerosol Quantity equal to low or intermediate and (4) zero for the following flags: Adjacent cloud, Mixed clouds, & Possible shadow. We followed the filtering recommendations of __[Samanda et al, _GRL_ 2010](https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2009GL042154)__ and __[Fensholt & Proud, _RSE_, 2012](https://www.sciencedirect.com/science/article/pii/S003442571200003X)__.

> Op2: We only included pixels that were of good quality, following __[Li et al, RSE, 2018](https://www.sciencedirect.com/science/article/pii/S0034425717304467)__.  

Click __[here](https://lpdaac.usgs.gov/citing_our_data)__ for suggestions on how to cite this product.

# MODIS LST

Source data from NASA's MOD11A2.006 Terra Land Surface Temperature and Emissivity 8-day Global 1km and MYD11A1.006 Aqua Land Surface Temperature and Emissivity 8-day Global 1km products. More information can be found __[here](https://lpdaac.usgs.gov/products/mod11a2v006/)__ for MOD11A2 and __[here](https://lpdaac.usgs.gov/products/myd11a2v006/)__ for MYD11A2. The GEE ImageCollection IDs are "MODIS/006/MOD11A2" and "MODIS/006/MYD11A2".

The function __GEElstMODIS()__ calculates the temporal average of Land Surface Temperature (LST) as well as a spatial average either at a single point, within a buffer from a point or within a polygon.

#### The following metrics can be selected:

> 'day1030' = Land surface temperature at ~1030 local time from Terra (MOD)  
> 'day1330' = Land surface temperature at ~1330 local time from Aqua (MYD)  
> 'night2230' = Land surface temperature at ~2230 local time from Terra (MOD)  
> 'night0130' = Land surface temperature at ~0130 local time from Aqua (MYD)  

Use the QC parameter to specify if only good quality pixels should be included in averaging using the QC flags specific for each pixel within an image.

> None: no masking of poor quality data

> Op1:  We only included pixels that satisfied the following conditions: (1) 'LST produced, good quality', (2) 'Good data quality', (3) 'Average emissivity error ≤ 0.02', and (4) 'Average LST error ≤ 2K', following the suggested filtering steps from __[Ma et al, _RSE_, 2014](https://www.sciencedirect.com/science/article/pii/S0034425714003228)__.

Click __[here](https://lpdaac.usgs.gov/citing_our_data)__ for suggestions on how to cite this product.

# TRMM 3B43: Monthly Precipitation Estimates

The function __GEEmonthTRMM()__ calculates global average precipitation rate (mm/hr) per month, taking a spatial average either at a single point, within a buffer from a point or within a polygon. More information can be found __[here](https://trmm.gsfc.nasa.gov/3b43.html)__. The GEE ImageCollection ID is "TRMM/3B43V7".

Citations:

> Adler, R.F., G.J. Huffman, A. Chang, R. Ferraro, P. Xie, J. Janowiak, B. Rudolf, U. Schneider, S. Curtis, D. Bolvin, A. Gruber, J. Susskind, P. Arkin, E.J. Nelkin, 2003: The Version 2 Global Precipitation Climatology Project (GPCP) Monthly Precipitation Analysis (1979-Present). J. Hydrometeor., 4(6), 1147-1167.  

> Huffman, G.J., 1997: "Estimates of Root-Mean-Square Random Error for Finite Samples of Estimated Precipitation", J. Appl. Meteor., 1191-1201.  

> Huffman, G.J., 2012:  Algorithm Theoretical Basis Document (ATBD) Version 3.0 for the NASA Global Precipitation Measurement (GPM) Integrated Multi-satellitE Retrievals for GPM (I-MERG).  GPM Project, Greenbelt, MD, 29 pp.  

> Huffman, G.J., R.F. Adler, P. Arkin, A. Chang, R. Ferraro, A. Gruber, J. Janowiak, A. McNab, B. Rudolph, U. Schneider, 1997: The Global Precipitation Climatology Project (GPCP) Combined Precipitation Dataset, Bul. Amer. Meteor. Soc., 78, 5-20.  

> Huffman, G.J., R.F. Adler, D.T. Bolvin, G. Gu, E.J. Nelkin, K.P. Bowman, Y. Hong, E.F. Stocker, D.B. Wolff, 2007: The TRMM Multi-satellite Precipitation Analysis: Quasi-Global, Multi-Year, Combined-Sensor Precipitation Estimates at Fine Scale. J. Hydrometeor.,8 (1), 38-55.  

> Huffman, G.J., R.F. Adler, B. Rudolph, U. Schneider, P. Keehn, 1995: Global Precipitation Estimates Based on a Technique for Combining Satellite-Based Estimates, Rain Gauge Analysis, and NWP Model Precipitation Information, J. Clim., 8, 1284-1295.  

# NEX-GDDP: NASA Earth Exchange Global Daily Downscaled Climate Projections

Global downscaled climate scenarios for 21 General Circulation Models (GCMs) from CMIP5. Emission scenarios include options for representative concentration pathways (RCPs) 4.5 and 8.5 from 2006-2099, as well as historical retrospective model runs from 1950-2006. More info can be found __[here](https://nex.nasa.gov/nex/projects/1356/)__. The GEE ImageCollection ID is "NASA/NEX-GDDP".

The function __GEEnasaNEXGDDP()__ provides future climate projections for precipitation and temperature (~25-km spatial resolution) as well as a spatial average either at a single point, within a buffer from a point or within a polygon.

The following metrics can be selected:

> 'pr' = sum of precipitation, liquid and solid phases (kg/(m^2*s))  
> 'tasmin' = mean daily min near surface air temperature (K)  
> 'tasmax' = mean daily max near surface air temperature (K)  

The following scenarios can be selected:

> 'historical'  
> 'rcp45'  
> 'rcp85'  

The following models can be selected:

> 'ACCESS1-0'  
> 'bcc-csm1-1'  
> 'BNU-ESM'  
> 'CanESM2'  
> 'CCSM4'  
> 'CESM1-BGC'  
> 'CNRM-CM5'  
> 'CSIRO-Mk3-6-0'  
> 'GFDL-CM3'  
> 'GFDL-ESM2G'  
> 'GFDL-ESM2M'  
> 'inmcm4'  
> 'IPSL-CM5A-LR'  
> 'IPSL-CM5A-MR'  
> 'MIROC-ESM'  
> 'MIROC-ESM-CHEM'  
> 'MIROC5'  
> 'MPI-ESM-LR'  
> 'MPI-ESM-MR'  
> 'MRI-CGCM3'  
> 'NorESM1-M'  

Best practice when averaging across months is to only output 10 years at a time. Otherwise you will get a "Computation timed out" error message on GEE, because you're requesting to process too much data at one time.

Suggested Citations:

> Thrasher, B., Maurer, E. P., McKellar, C., & Duffy, P. B., 2012: Technical Note: Bias correcting climate model simulated daily temperature extremes with quantile mapping. Hydrology and Earth System Sciences, 16(9), 3309-3314.  

Suggested acknowledgement

> Climate scenarios used were from the NEX-GDDP dataset, prepared by the Climate Analytics Group and NASA Ames Research Center using the NASA Earth Exchange, and distributed by the NASA Center for Climate Simulation (NCCS).

# Downscaled Climate Models for United States- Multivariate Adaptive Constructed Analogs (MACAv2-METDATA ):

Downscaled climate scenarios for 20 Global Climate Models (GCMs) from CMIP5 for the contiguous US. Emission scenarios include options for representative concentration pathways (RCPs) 4.5 and 8.5 from 2006-2099, as well as historical retrospective model runs from 1950-2005. More info can be found __[here](https://climate.northwestknowledge.net/MACA/index.php)__. The GEE ImageCollection ID is "IDAHO_EPSCOR/MACAv2_METDATA_MONTHLY".

The function __GEEmacaGCMs()__ provides future climate projections (~4-km spatial resolution) across the continental US as well as a spatial average either at a single point, within a buffer from a point or within a polygon.


The following metrics can be selected:
> tasmax: 'Monthly average of maximum daily temperature near surface' (K)  
> tasmin: 'Monthly average of minimum daily temperature near surface' (K)  
> huss: 'Monthly average of mean daily specific humidity near surface' (kg/kg)  
> pr: 'Total monthly precipitation amount at surface' (mm)  
> rsds: 'Monthly average of mean daily downward shortwave radiation at surface' (W/m^2)  	
> was: 'Monthly average of mean daily near surface wind speed' (m/s)  

The following scenarios can be selected:
> rcp85  
> rcp45  
> historical  

The following models can be selected:
> bcc-csm1-1  
> bcc-csm1-1-m  
> BNU-ESM  
> CanESM2  
> CCSM4  
> CNRM-CM5  
> CSIRO-Mk3-6-0  
> GFDL-ESM2M  
> GFDL-ESM2G  
> HadGEM2-ES365  
> HadGEM2-CC365  
> inmcm4  
> IPSL-CM5A-LR  
> IPSL-CM5A-MR  
> IPSL-CM5B-LR  
> MIROC5  
> MIROC-ESM  
> MIROC-ESM-CHEM  
> MRI-CGCM3  
> NorESM1-M  

Best practice when averaging across months is to only output 10 years at a time. Otherwise you will get a "Computation timed out" error message on GEE, because you're requesting to process too much data at one time.

Citations:

> Abatzoglou J.T. and Brown T.J., A comparison of statistical downscaling methods suited for wildfire applications, International Journal of Climatology(2012) doi: https://doi.org/10.1002/joc.2312.  
