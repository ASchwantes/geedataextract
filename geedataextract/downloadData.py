#####Created by Amanda Schwantes on Jan 31 2018
#####Updated May 1 2019

"""
Functions for extracting data from GEE
"""

def GEEtcPts(ptsFile,yr,buf,poly,username,folderOut, scalePix = 30):
    """    
    Calculates tree cover % at point OR within buffer of point if buf > 0 OR within polygon if poly = 1

    Requires:
    
    ptsfile - file name of your uploaded shapefile to GEE

    yr - year of interest: options include 2001 or 2011

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive. 

    Optional parameters

    scalePix - scale/spatial resolution. Default: 30
    
    """
    # load required libraries
    import ee
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    #define landcover images
    tc = ee.Image("USGS/NLCD/NLCD" + str(yr)).select('percent_tree_cover')

    if buf > 0:
        bufL = [buf]
        def bufferPoly(feature):
            return feature.buffer(bufL[0])

        ptsB = pts1.map(bufferPoly)
        
        #reduce regions, filter out null values, remove geometry and export table
        table_tc_pts = tc.reduceRegions(collection = ptsB.select([ID_field]),
                                        reducer = ee.Reducer.mean(),
                                        scale = scalePix)
        task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                .filter(ee.Filter.neq('mean', None))
                                                .select(['.*'],None,False),
                                                description = 's_tc_'+str(yr)+'_ptsB',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()

        #print ("buffered pts by:" + str(buf))

    elif poly > 0:
                     
        #reduce regions, filter out null values, remove geometry and export table
        table_tc_pts = tc.reduceRegions(collection = pts1.select([ID_field]),
                                        reducer = ee.Reducer.mean(),
                                        scale = scalePix)
        task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                .filter(ee.Filter.neq('mean', None))
                                                .select(['.*'],None,False),
                                                description = 's_tc_'+str(yr)+'_poly1',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()

        #print ("spatial mean in poly: no buffer")

    else:
 
        #reduce regions, filter out null values, remove geometry and export table
        table_tc_pts = tc.reduceRegions(collection = pts1.select([ID_field]),
                                        reducer = ee.Reducer.mean(),
                                        scale = scalePix)
        task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                .filter(ee.Filter.neq('mean', None))
                                                .select(['.*'],None,False),
                                                description = 's_tc_'+str(yr)+'_pts1',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()

        #print("value at point: no buffer")

def GEEicPts(ptsFile,yr,buf,poly,username,folderOut, scalePix = 30):
    """    
    Calculates % impervious cover at point OR within buffer of point if buf > 0 OR within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE

    yr - year of interest: options include 2001, 2006, or 2011

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.
    
    Optional parameters    

    scalePix - scale/spatial resolution. Default: 30
    
    """
    # load required libraries
    import ee
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    #define landcover images
    tc = ee.Image("USGS/NLCD/NLCD" + str(yr)).select('impervious')

    if buf > 0:
        bufL = [buf]
        def bufferPoly(feature):
            return feature.buffer(bufL[0])

        ptsB = pts1.map(bufferPoly)
        
        #reduce regions, filter out null values, remove geometry and export table
        table_tc_pts = tc.reduceRegions(collection = ptsB.select([ID_field]),
                                        reducer = ee.Reducer.mean(),
                                        scale = scalePix)
        task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                .filter(ee.Filter.neq('mean', None))
                                                .select(['.*'],None,False),
                                                description = 's_ic_'+str(yr)+'_ptsB',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()

        #print ("buffered pts by:" + str(buf))

    elif poly > 0:
        
        #reduce regions, filter out null values, remove geometry and export table
        table_tc_pts = tc.reduceRegions(collection = pts1.select([ID_field]),
                                        reducer = ee.Reducer.mean(),
                                        scale = scalePix)
        task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                .filter(ee.Filter.neq('mean', None))
                                                .select(['.*'],None,False),
                                                description = 's_ic_'+str(yr)+'_poly1',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()

        #print ("spatial mean in poly: no buffer")

    else:
 
        #reduce regions, filter out null values, remove geometry and export table
        table_tc_pts = tc.reduceRegions(collection = pts1.select([ID_field]),
                                        reducer = ee.Reducer.mean(),
                                        scale = scalePix)
        task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                .filter(ee.Filter.neq('mean', None))
                                                .select(['.*'],None,False),
                                                description = 's_ic_'+str(yr)+'_pts1',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()

        #print("value at point: no buffer")

def GEElcPts(ptsFile,yr,buf,poly,username,folderOut, scalePix = 30):
    """    
    Calculates land cover at point OR histogram within buffer of point if buf > 0 OR within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    yr - year of interest: options include 2001, 2006, or 2011

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive. 
    
    Optional parameters    

    scalePix - scale/spatial resolution. Default: 30
    
    """
    
    # load required libraries
    import ee
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    #define landcover images
    tc = ee.Image("USGS/NLCD/NLCD" + str(yr)).select('landcover')

    if buf > 0:
        bufL = [buf]
        def bufferPoly(feature):
            return feature.buffer(bufL[0])

        ptsB = pts1.map(bufferPoly)
        
        #reduce regions, filter out null values, remove geometry and export table
        table_tc_pts = tc.reduceRegions(collection = ptsB.select([ID_field]),
                                        reducer = ee.Reducer.frequencyHistogram(),
                                        scale = scalePix)
        task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                .filter(ee.Filter.neq('histogram', None))
                                                .select(['.*'],None,False),
                                                description = 'f_lc_'+str(yr)+'_ptsB',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()

        #print ("buffered pts by:" + str(buf))

    elif poly > 0:
               
        #reduce regions, filter out null values, remove geometry and export table
        table_tc_pts = tc.reduceRegions(collection = pts1.select([ID_field]),
                                        reducer = ee.Reducer.frequencyHistogram(),
                                        scale = scalePix)
        task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                .filter(ee.Filter.neq('histogram', None))
                                                .select(['.*'],None,False),
                                                description = 'f_lc_'+str(yr)+'_poly1',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()

        #print ("spatial mean in poly: no buffer")

    else:
 
        #reduce regions, filter out null values, remove geometry and export table
        table_tc_pts = tc.reduceRegions(collection = pts1.select([ID_field]),
                                        reducer = ee.Reducer.mean(),
                                        scale = scalePix)
        task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                .filter(ee.Filter.neq('mean', None))
                                                .select(['.*'],None,False),
                                                description = 's_lc_'+str(yr)+'_pts1',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()

        #print("value at point: no buffer")


def GEEsoilPts(ptsFile,metric,buf,poly,username,folderOut, scalePix = 250):
    """    
    Calculates soil metrics at point OR within buffer of point if buf > 0 OR within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of metrics to include in output ['oc','ph','cec','sand','silt','cfrag','clay','bulkDensity','soilDepth','subordersUS','subgroupsWorld']
    
        'oc' = Soil organic carbon content (fine earth fraction) in g per kg
        'ph' = Soil pH x 10 in H2O
        'cec' = Cation exchange capacity of soil in cmolc/kg
        'sand' = Sand content (50-2000 micro meter) mass fraction in %
        'silt' = Silt content (2-50 micro meter) mass fraction in %
        'cfrag' = Coarse fragments volumetric in %
        'clay' = Clay content (0-2 micro meter) mass fraction in %
        'bulkDensity' = Bulk density (fine earth) in kg / cubic-meter
        'soilDepth' = Absolute depth to bedrock (in cm)
        'subordersUS' = Predicted USDA 2014 suborder classes (as integers)
        'subgroupsWorld' = Predicted WRB 2006 subgroup classes (as integers)
        
    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.
    
    Optional parameters

    scalePix - scale/spatial resolution. Default: 250
    
    """

    #define dictionary for raster random names
    soil_d = {}
    soil_d["soilDepth"] = "BDTICM_M_250m"
    soil_d["bulkDensity"] = "BLDFIE_I"
    soil_d["cec"] = "CECSOL_I"
    soil_d["clay"] = "CLYPPT_I"
    soil_d["cfrag"] = "CRFVOL_I"
    soil_d["ph"] = "PHIHOX_I"
    soil_d["silt"] = "SLTPPT_I"
    soil_d["sand"] = "SNDPPT_I"
    soil_d["oc"] = "ORCDRC_I"
    soil_d["subordersUS"] = "TAXOUSDA_250m"
    soil_d["subgroupsWorld"] = "TAXNWRB_250m"
    
        
    # load required libraries
    import ee
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    for met in metric:
        metL = [met]
    
        if buf > 0:
            bufL = [buf]
            def bufferPoly(feature):
                return feature.buffer(bufL[0])

            ptsB = pts1.map(bufferPoly)
        
            if any([(met == 'subgroupsWorld'),(met == 'subordersUS')]):

                soilImage = ee.Image("users/aschwantes/" + str(soil_d[met]))
                table_tc_pts = soilImage.reduceRegions(collection = ptsB.select([ID_field]),
                                                    reducer = ee.Reducer.mode(),
                                                    scale = scalePix)
                task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                        .filter(ee.Filter.neq('mode', None))
                                                        .select(['.*'],None,False),
                                                        description = 's_'+str(met)+'_soil_ptsB',
                                                        folder = folderOut,
                                                        fileFormat = 'CSV')
            
            elif met == 'soilDepth':

                soilImage = ee.Image("users/aschwantes/" + str(soil_d[met])).float()
                table_tc_pts = soilImage.reduceRegions(collection = ptsB.select([ID_field]),
                                                    reducer = ee.Reducer.mean(),
                                                    scale = scalePix)
                task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                        .filter(ee.Filter.neq('mean', None))
                                                        .select(['.*'],None,False),
                                                        description = 's_'+str(met)+'_soil_ptsB',
                                                        folder = folderOut,
                                                        fileFormat = 'CSV')
            else:

                soilImage = ee.Image("users/aschwantes/" + str(soil_d[met])).float().divide(100)
                table_tc_pts = soilImage.reduceRegions(collection = ptsB.select([ID_field]),
                                                    reducer = ee.Reducer.mean(),
                                                    scale = scalePix)
                task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                        .filter(ee.Filter.neq('mean', None))
                                                        .select(['.*'],None,False),
                                                        description = 's_'+str(met)+'_soil_ptsB',
                                                        folder = folderOut,
                                                        fileFormat = 'CSV')
            task_tc.start()

            #print ("buffered pts by:" + str(buf))

        elif poly > 0:

            if any([(met == 'subgroupsWorld'),(met == 'subordersUS')]):

                soilImage = ee.Image("users/aschwantes/" + str(soil_d[met]))
                table_tc_pts = soilImage.reduceRegions(collection = pts1.select([ID_field]),
                                            reducer = ee.Reducer.mode(),
                                            scale = scalePix)
                task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mode', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_'+str(met)+'_soil_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            
            elif met == 'soilDepth':

                soilImage = ee.Image("users/aschwantes/" + str(soil_d[met])).float()
                table_tc_pts = soilImage.reduceRegions(collection = pts1.select([ID_field]),
                                            reducer = ee.Reducer.mean(),
                                            scale = scalePix)
                task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_'+str(met)+'_soil_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            else:

                soilImage = ee.Image("users/aschwantes/" + str(soil_d[met])).float().divide(100)
                table_tc_pts = soilImage.reduceRegions(collection = pts1.select([ID_field]),
                                            reducer = ee.Reducer.mean(),
                                            scale = scalePix)
                task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_'+str(met)+'_soil_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            
            task_tc.start()

            #print ("spatial mean in poly: no buffer")

        else:

            if any([(met == 'subgroupsWorld'),(met == 'subordersUS')]):

                soilImage = ee.Image("users/aschwantes/" + str(soil_d[met]))
                table_tc_pts = soilImage.reduceRegions(collection = pts1.select([ID_field]),
                                            reducer = ee.Reducer.mode(),
                                            scale = scalePix)
                task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mode', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_'+str(met)+'_soil_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            
            elif met == 'soilDepth':

                soilImage = ee.Image("users/aschwantes/" + str(soil_d[met])).float()
                table_tc_pts = soilImage.reduceRegions(collection = pts1.select([ID_field]),
                                            reducer = ee.Reducer.mean(),
                                            scale = scalePix)
                task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_'+str(met)+'_soil_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            else:

                soilImage = ee.Image("users/aschwantes/" + str(soil_d[met])).float().divide(100)
                table_tc_pts = soilImage.reduceRegions(collection = pts1.select([ID_field]),
                                            reducer = ee.Reducer.mean(),
                                            scale = scalePix)
                task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_'+str(met)+'_soil_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            
            task_tc.start()

            #print("value at point: no buffer")

def GEEtopoPts(ptsFile,metric,buf,poly,username,folderOut, scalePix = 30):
    """    
    Calculates topography metrics at point OR within buffer of point if buf > 0 OR within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of metrics to include in output ['elev', 'slope', 'aspect']
        elev: elevation (meters)
        slope: (radians)
        aspect: (radians) unless spatial average then two outputs will be produced
            aspect_sin: Sum of the sin(aspect)
            aspect_cos: Sum of the cos(aspect)
            You can then later take the circular average using atan2(aspectSinSum, aspectCosSum)
       
    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.

    Optional parameters

    scalePix - scale/spatial resolution. Default: 30
    
    """
            
    # load required libraries
    import ee
    import math
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    #define topo images
    srtm = ee.Image('USGS/SRTMGL1_003')
    slopeI = ee.Terrain.slope(srtm).multiply(math.pi/180)
    aspectI = ee.Terrain.aspect(srtm).multiply(math.pi/180)

    aspectS = aspectI.sin();
    aspectC = aspectI.cos();
    
    if buf > 0:
        bufL = [buf]
        def bufferPoly(feature):
            return feature.buffer(bufL[0])

        ptsB = pts1.map(bufferPoly)
        
        #reduce regions, filter out null values, remove geometry and export table

        if 'elev' in metric:
            table_tc_pts = srtm.reduceRegions(collection = ptsB.select([ID_field]),
                                              reducer = ee.Reducer.mean(),
                                              scale = scalePix)
            task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_elev_topo_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()

        if 'slope' in metric:
            table_tc_pts = slopeI.reduceRegions(collection = ptsB.select([ID_field]),
                                              reducer = ee.Reducer.mean(),
                                              scale = scalePix)
            task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_slope_topo_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()

        if 'aspect' in metric:
            table_AS_pts = aspectS.reduceRegions(collection = ptsB.select([ID_field]),
                                                 reducer = ee.Reducer.sum(),
                                                 scale = scalePix)
            table_AC_pts = aspectC.reduceRegions(collection = ptsB.select([ID_field]),
                                                 reducer = ee.Reducer.sum(),
                                                 scale = scalePix)
            task_AS = ee.batch.Export.table.toDrive(collection = table_AS_pts
                                                    .filter(ee.Filter.neq('sum', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_aspect_sin_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_AC = ee.batch.Export.table.toDrive(collection = table_AC_pts
                                                    .filter(ee.Filter.neq('sum', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_aspect_cos_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_AS.start()
            task_AC.start()

        #print ("buffered pts by:" + str(buf))

    elif poly > 0:
        
        #reduce regions, filter out null values, remove geometry and export table

        if 'elev' in metric:
            table_tc_pts = srtm.reduceRegions(collection = pts1.select([ID_field]),
                                              reducer = ee.Reducer.mean(),
                                              scale = scalePix)
            task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_elev_topo_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()

        if 'slope' in metric:
            table_tc_pts = slopeI.reduceRegions(collection = pts1.select([ID_field]),
                                              reducer = ee.Reducer.mean(),
                                              scale = scalePix)
            task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_slope_topo_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()

        if 'aspect' in metric:
            table_AS_pts = aspectS.reduceRegions(collection = pts1.select([ID_field]),
                                                 reducer = ee.Reducer.sum(),
                                                 scale = scalePix)
            table_AC_pts = aspectC.reduceRegions(collection = pts1.select([ID_field]),
                                                 reducer = ee.Reducer.sum(),
                                                 scale = scalePix)
            task_AS = ee.batch.Export.table.toDrive(collection = table_AS_pts
                                                    .filter(ee.Filter.neq('sum', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_aspect_sin_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_AC = ee.batch.Export.table.toDrive(collection = table_AC_pts
                                                    .filter(ee.Filter.neq('sum', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_aspect_cos_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_AS.start()
            task_AC.start()

        #print ("spatial mean in poly: no buffer")

    else:

        if 'elev' in metric:
            table_tc_pts = srtm.reduceRegions(collection = pts1.select([ID_field]),
                                              reducer = ee.Reducer.mean(),
                                              scale = scalePix)
            task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_elev_topo_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
        if 'slope' in metric:
            table_tc_pts = slopeI.reduceRegions(collection = pts1.select([ID_field]),
                                              reducer = ee.Reducer.mean(),
                                              scale = scalePix)
            task_tc = ee.batch.Export.table.toDrive(collection = table_tc_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_slope_topo_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()

        if 'aspect' in metric:
            table_A_pts = aspectI.reduceRegions(collection = pts1.select([ID_field]),
                                                 reducer = ee.Reducer.mean(),
                                                 scale = scalePix)
            task_A = ee.batch.Export.table.toDrive(collection = table_A_pts
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 's_aspect_topo_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_A.start()
            
        #print("value at point: no buffer")

def GEEgridmetPtsAvg(ptsFile,metric,startYear,endYear,timeStep,buf,poly,username,folderOut, scalePix = 4000):
    """    
    Calculates climate temporal monthly averages at point OR within buffer of point if buf > 0 OR within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of metrics to include in output ['tmin', 'tmax', 'vpd']
        tmax: average maximum temperature (K)
        tmin: average minimum temperature (K)
        vpd: average vapor pressure deficit (kPa)

    startYear - The start of the time-series (year) 1979 is the earliest possible year

    endYear - The end of the time-series (year)

    timeStep - time step for temporal averaging, either 'month', 'year', or 'day'

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.

    Optional parameters

    scalePix - scale/spatial resolution. Default: 4000
    
    """
        
    # load required libraries
    import ee
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    lastImage = ee.Image(ee.ImageCollection('IDAHO_EPSCOR/GRIDMET')
                         .sort('system:time_start',False)
                         .first())
    lastImageDate = lastImage.get('system:index').getInfo()

    endYearReal = min((int(lastImageDate[0:4])-1),endYear)
    
    years = list(range(startYear, endYearReal + 1))

    if endYear > endYearReal:
        months = list(range(0,(12*len(years)+(int(lastImageDate[4:6])-1))))
    elif  endYear <= endYearReal:
        months = list(range(0,(12*len(years))))

    monthsEE = ee.List(months)
    yearsEE = ee.List(years)

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    ID_field = "geeID"

    time_d = {}
    time_d['month'] = 'cm'
    time_d['year'] = 'cy'
    time_d['day'] = 'cd'

    clim_d = {}
    clim_d['tmax'] = 'tmmx'
    clim_d['tmin'] = 'tmmn'
    clim_d['vpd'] = 'vpd'
    
    for met in metric:
        metL = [met]
        Gridmet_pr = ee.ImageCollection('IDAHO_EPSCOR/GRIDMET').select(clim_d[met])
        
        if timeStep == 'year':

            def map_m(i):
                i = ee.Number(i).int()
                image2 = (Gridmet_pr
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .first())
                filtered = (Gridmet_pr
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .mean()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col = ee.ImageCollection(yearsEE.map(map_m).flatten())

        elif timeStep == 'month':
            
            def map_m(i):
                i = ee.Number(i)
                y = i.divide(12).add(years[0]).int()
                m = i.mod(12).add(1)
                image2 = (Gridmet_pr
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .first())
                filtered = (Gridmet_pr
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .mean()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col = ee.ImageCollection(monthsEE.map(map_m).flatten())

        elif timeStep == 'day':

            img_col = Gridmet_pr.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))

        #else:
            #print("incorrect time step specified")

        if buf > 0:
            bufL = [buf]
            def bufferPoly(feature):
                return feature.buffer(bufL[0])

            ptsB = pts1.map(bufferPoly)
            def table_m(image):
                table = (image
                    .select(clim_d[metL[0]])
                    .reduceRegions(collection = ptsB.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = str(time_d[timeStep])+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('buffered pts by:' + str(buf) + ' for ' + met)

        elif poly > 0:
            
            def table_m(image):
                table = (image
                    .select(clim_d[metL[0]])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = str(time_d[timeStep])+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('spatial mean in poly: no buffer for ' + met)

        else:
            def table_m(image):
                table = (image
                    .select(clim_d[metL[0]])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = str(time_d[timeStep])+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
                
            #print('value at point: no buffer for ' + met)


def GEEgridmetPtsSum(ptsFile,metric,startYear,endYear,timeStep,buf,poly,username,folderOut, scalePix = 4000):
    """    
    Calculates climate temporal sums and spatial averages at point OR within buffer of point if buf > 0 OR within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of metrics to include in output ['eto', 'pr']
        pr: precipitation amount (mm, total sum)
        eto: Daily reference evapotranspiration (grass, mm, total sum)

    startYear - The start of the time-series (year) 1979 is the earliest possible year

    endYear - The end of the time-series (year) 2017 is the latest possible year

    timeStep - time step for temporal averaging, either 'month', 'year', or 'day'.

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.
    
    Optional parameters

    scalePix - scale/spatial resolution. Default: 4000
    
    """
        
    # load required libraries
    import ee
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    lastImage = ee.Image(ee.ImageCollection('IDAHO_EPSCOR/GRIDMET')
                         .sort('system:time_start',False)
                         .first())
    lastImageDate = lastImage.get('system:index').getInfo()

    endYearReal = min((int(lastImageDate[0:4])-1),endYear)
    
    years = list(range(startYear, endYearReal + 1))

    if endYear > endYearReal:
        months = list(range(0,(12*len(years)+(int(lastImageDate[4:6])-1))))
    elif  endYear <= endYearReal:
        months = list(range(0,(12*len(years))))

    monthsEE = ee.List(months)
    yearsEE = ee.List(years)

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    ID_field = "geeID"

    time_d = {}
    time_d['month'] = 'cm'
    time_d['year'] = 'cy'
    time_d['day'] = 'cd'
    #time_d['week'] = 'cw'

    #dt = datetime.datetime(1979, 1, 1)
    #end = datetime.datetime(2018, 1, 2)
    #step = datetime.timedelta(days=7)

    #result = []

    #while dt < end:
    #    result.append(dt.strftime('%Y-%m-%d'))
    #    dt += step

    #dateS = [num for num in result if int(num[0:4]) >= startYear and int(num[0:4]) <= endYear]
    #dateS1 = [[num for num in result if int(num[0:4]) == endYear+1][0]]
    #dateS.extend(list(dateS1))

    #dateSEE = ee.List(dateS[0:(len(dateS)-1)])
    #dateEEE = ee.List(dateS[1:len(dateS)])
                
    #weekEE = ee.List(list(range(0,(len(dateS)-1))))
    
    for met in metric:
        metL = [met]
        Gridmet_pr = ee.ImageCollection('IDAHO_EPSCOR/GRIDMET').select(met)
        
        if timeStep == 'year':

            def map_m(i):
                i = ee.Number(i).int()
                image2 = (Gridmet_pr
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .first())
                filtered = (Gridmet_pr
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .sum()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col = ee.ImageCollection(yearsEE.map(map_m).flatten())

        elif timeStep == 'month':
            
            def map_m(i):
                i = ee.Number(i)
                y = i.divide(12).add(years[0]).int()
                m = i.mod(12).add(1)
                image2 = (Gridmet_pr
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .first())
                filtered = (Gridmet_pr
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .sum()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col = ee.ImageCollection(monthsEE.map(map_m).flatten())

##        elif timeStep == 'week':
##
##            def map_m(i):
##                i = ee.Number(i).int()
##                
##                image2 = (Gridmet_pr
##                    .filterDate(dateSEE.get(i), dateEEE.get(i))
##                    .first())
##                filtered = (Gridmet_pr
##                    .filterDate(dateSEE.get(i), dateEEE.get(i))
##                    .sum()
##                    .copyProperties(image2,['system:time_start','system:time_end']))
##                return filtered
##
##            img_col = ee.ImageCollection(weekEE.map(map_m).flatten())

        elif timeStep == 'day':

            img_col = Gridmet_pr.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))

        #else:
            #print("incorrect time step specified")
            
        if buf > 0:
            bufL = [buf]
            def bufferPoly(feature):
                return feature.buffer(bufL[0])

            ptsB = pts1.map(bufferPoly)
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = ptsB.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = str(time_d[timeStep])+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('buffered pts by:' + str(buf) + ' for ' + met)

        elif poly > 0:
            
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = str(time_d[timeStep])+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('spatial mean in poly: no buffer for ' + met)

        else:
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = str(time_d[timeStep])+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
                
            #print('value at point: no buffer for ' + met)

def GEEphenMODIS(ptsFile,metric,startYear,endYear,buf,poly,username,folderOut, scalePix = 500):
    """    
    Calculates phenology metric at point OR mean within buffer of point if buf > 0 OR mean within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of metrics to include in output ['GreenInc', 'GreenMax', 'GreenDec','GreenMin']
        GreenInc: Days since Jan 1, 2000 that correspond to vegetation greenup, mode 1
        GreenMax: Days since Jan 1, 2000 that correspond to vegetation maturity, mode 1
        GreenDec: Days since Jan 1, 2000 that correspond to vegetation senescence, mode 1
        GreenMin: Days since Jan 1, 2000 that correspond to vegetation dormancy, mode 1

    startYear - The start of the time-series (year), data available starting 2001

    endYear - The end of the time-series (year), data available ending 2014

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.
    
    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.
    
    Optional parameters

    scalePix - scale/spatial resolution. Default: 500
    
    """
        
    # load required libraries
    import ee
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    years = ee.List(list(range(startYear, endYear + 1)))
    
    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    #define dictionary for raster random names
    phen_d = {}
    phen_d['GreenInc'] = 'Onset_Greenness_Increase1'
    phen_d['GreenMax'] = 'Onset_Greenness_Maximum1'
    phen_d['GreenDec'] = 'Onset_Greenness_Decrease1'
    phen_d['GreenMin'] = 'Onset_Greenness_Minimum1'

    for met in metric:

        modis1 = ee.ImageCollection('MODIS/MCD12Q2').select(phen_d[met])
        
        def map_m(i):
            i = ee.Number(i)
            filtered = (modis1
                .filter(ee.Filter.calendarRange(i, i, 'year'))
                .first())
            return filtered

        img_col = ee.ImageCollection(years.map(map_m).flatten())

        if buf > 0:
            bufL = [buf]
            def bufferPoly(feature):
                return feature.buffer(bufL[0])

            ptsB = pts1.map(bufferPoly)
            def table_m(image):
                table = (image
                    .select(phen_d[met])
                    .reduceRegions(collection = ptsB.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 'p_MCD12Q2_'+str(met)+'_'+str(startYear)+'_'+str(endYear)+'_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
            #print ('buffered pts by:' + str(buf) + ' for phen for ' + str(met))

        elif poly > 0:
            
            def table_m(image):
                table = (image
                    .select(phen_d[met])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 'p_MCD12Q2_'+str(met)+'_'+str(startYear)+'_'+str(endYear)+'_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
            #print ('spatial mean in poly: no buffer for phen for ' + str(met))

        else:
            def table_m(image):
                table = (image
                    .select(phen_d[met])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 'p_MCD12Q2_'+str(met)+'_'+str(startYear)+'_'+str(endYear)+'_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
                
            #print('value at point: no buffer for phen for ' + str(met))

def GEEviLandsat(ptsFile,metric,timeStep,sensor,buf,poly,username,folderOut, scalePix = 30):
    """    
    Calculates vegetation/water indices for Landsat at point OR mean within buffer of point if buf > 0 OR mean within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of metrics to include: ['NDVI', 'NDWI', 'NBR']
        'NDVI' = Normalized Difference Vegetation Index (NIR-RED)/(NIR+RED)
        'NDWI'; = Normalized Difference Water Index (NIR-SWIR1)/(NIR+SWIR1)
        'NBR'; = Normalized Difference Burn Ratio (NIR-SWIR2)/(NIR+SWIR2)

    timeStep - time step for temporal averaging, either 'lowest','month', OR 'year'

    sensor - list of Landsat sensors: separate files will be exported for each sensor specified ['L4','L5','L7','L8']
        L4: Landsat 4 images taken from Aug 22, 1982 to Dec 14, 1993
        L5: Landsat 5 images taken from Jan 1, 1984 to May 5, 2012
        L7: Landsat 7 images taken from Jan 1, 1999 to present
        L8: Landsat 8 images taken from Apr 11, 2013 to present

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.

    Optional parameters

    scalePix - scale/spatial resolution. Default: 30
    
    """
        
    # load required libraries
    import ee
    import math
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    #define dictionary for raster random names
    sensor_d = {}
    sensor_d['L4'] = 'LANDSAT/LT04/C01/T1_SR'
    sensor_d['L5'] = 'LANDSAT/LT05/C01/T1_SR'
    sensor_d['L7'] = 'LANDSAT/LE07/C01/T1_SR'
    sensor_d['L8'] = 'LANDSAT/LC08/C01/T1_SR'

    time_d = {}
    time_d['lowest'] = 'rl'
    time_d['month'] = 'rm'
    time_d['year'] = 'ry'
    
    
    #Computes the bits we need to extract.
    def getQABits(image, start, end, newName):
        pattern = 0
        listB = list(range(start, end+1))
        for one in listB:
            pattern += math.pow(2, one)
            pattern = int(pattern)
    
        return (image.select([0], [newName])
                  .bitwiseAnd(pattern)
                  .rightShift(start))
    
    for sen in sensor:
        LS = ee.ImageCollection(sensor_d[sen])
        #senL = [sen]
        
        def maskbyBits(img):
            QA = img.select('pixel_qa')
            QA1 = getQABits(QA, 3, 3, 'QA')
            QA2 = getQABits(QA, 5, 5, 'QA')

            mask = QA1.eq(0).And(QA2.eq(0))
            return img.updateMask(mask)
        
        LSm = LS.map(maskbyBits)
            
        lastImage = ee.Image(ee.ImageCollection(sensor_d[sen])
                         .sort('system:time_start',False)
                         .first())
        lastImageDate = lastImage.get('system:index').getInfo()

        firstImage = ee.Image(ee.ImageCollection(sensor_d[sen])
                         .sort('system:time_start',True)
                         .first())
        firstImageDate = firstImage.get('system:index').getInfo()
      
        startYear = int(firstImageDate[(len(firstImageDate)-8):(len(firstImageDate)-4)])
        endYear = int(lastImageDate[(len(lastImageDate)-8):(len(lastImageDate)-4)])
        startMonth = int(firstImageDate[(len(firstImageDate)-4):(len(firstImageDate)-2)])
        endMonth = int(lastImageDate[(len(lastImageDate)-4):(len(lastImageDate)-2)])-1
        startYearAll = startYear + 1
        endYearAll = endYear - 1
                        
        years = list(range(startYear, endYearAll + 1))
        monthsEE = ee.List(list(range(startMonth,(12*len(years)+endMonth))))
        yearsEE = ee.List(list(range(startYearAll, endYearAll + 1)))
              
        for met in metric:
           # metL = [met]

            if (sen == 'L8' and met == "NDVI"):
                bands = ['B5', 'B4']
            elif (sen != 'L8' and met == "NDVI"):
                bands = ['B4', 'B3']
            elif (sen == 'L8' and met == "NDWI"):
                bands = ['B5', 'B6']
            elif (sen != 'L8' and met == "NDWI"):
                bands = ['B4', 'B5']
            elif (sen == 'L8' and met == "NBR"):
                bands = ['B5', 'B7']
            elif (sen != 'L8' and met == "NBR"):
                bands = ['B4', 'B7']
            #else:
                  #print("wrong metric specified")
                   
            def addVI(image):
                vi = (image.normalizedDifference(bands)
                    .rename('VI'))
                return image.addBands(vi)

            withVI = LSm.map(addVI)

            VI_col = withVI.select('VI')

            if timeStep == 'year':

                def map_m(i):
                    i = ee.Number(i).int()
                    image2 = (VI_col
                        .filter(ee.Filter.calendarRange(i, i, 'year'))
                        .first())
                    filtered = (VI_col
                        .filter(ee.Filter.calendarRange(i, i, 'year'))
                        .mean()
                        .copyProperties(image2,['system:time_start','system:time_end']))
                    return filtered

                img_col = ee.ImageCollection(yearsEE.map(map_m).flatten())

            elif timeStep == 'month':
            
                def map_m(i):
                    i = ee.Number(i)
                    y = i.divide(12).add(years[0]).int()
                    m = i.mod(12).add(1)
                    image2 = (VI_col
                        .filter(ee.Filter.calendarRange(m, m, 'month'))
                        .filter(ee.Filter.calendarRange(y, y, 'year'))
                        .first())
                    filtered = (VI_col
                        .filter(ee.Filter.calendarRange(m, m, 'month'))
                        .filter(ee.Filter.calendarRange(y, y, 'year'))
                        .mean()
                        .copyProperties(image2,['system:time_start','system:time_end']))
                    return filtered

                img_col = ee.ImageCollection(monthsEE.map(map_m).flatten())

            elif timeStep == 'lowest':

                img_col = VI_col

            #else:
                  #print("incorrect time step specified")
            
            if buf > 0:
                bufL = [buf]
                def bufferPoly(feature):
                    return feature.buffer(bufL[0])

                ptsB = pts1.map(bufferPoly)
                def table_m(image):
                    table = (image
                        .select('VI')
                        .reduceRegions(collection = ptsB.select([ID_field]),
                                        reducer = ee.Reducer.mean(),
                                        scale = scalePix))
                        
                    def table_add_date(f):
                        return f.set('startDate', ee.Date(image.get('system:time_start')))

                    return table.map(table_add_date)

                triplets = img_col.map(table_m).flatten()

                task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = str(time_d[timeStep])+'_'+str(sen)+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
                task_tc.start()
    
    
                #print ('buffered pts by:' + str(buf) + ' for Landsat: ' + sen + '_' + met)

            elif poly > 0:
                
                def table_m(image):
                    table = (image
                        .select('VI')
                        .reduceRegions(collection = pts1.select([ID_field]),
                                        reducer = ee.Reducer.mean(),
                                        scale = scalePix))
                            
                    def table_add_date(f):
                        return f.set('startDate', ee.Date(image.get('system:time_start')))

                    return table.map(table_add_date)

                triplets = img_col.map(table_m).flatten()

                task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                        .filter(ee.Filter.neq('mean', None))
                                                        .select(['.*'],None,False),
                                                        description = str(time_d[timeStep])+'_'+str(sen)+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                        folder = folderOut,
                                                        fileFormat = 'CSV')
                task_tc.start()
        
        
                #print ('spatial mean in poly: no buffer for Landsat: ' + sen + '_' + met)

            else:
                def table_m(image):
                    table = (image
                        .select('VI')
                        .reduceRegions(collection = pts1.select([ID_field]),
                                        reducer = ee.Reducer.mean(),
                                        scale = scalePix))
                            
                    def table_add_date(f):
                        return f.set('startDate', ee.Date(image.get('system:time_start')))

                    return table.map(table_add_date)

                triplets = img_col.map(table_m).flatten()

                task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                        .filter(ee.Filter.neq('mean', None))
                                                        .select(['.*'],None,False),
                                                        description = str(time_d[timeStep])+'_'+str(sen)+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                        folder = folderOut,
                                                        fileFormat = 'CSV')
                task_tc.start()
                    
                #print('value at point: no buffer for Landsat: ' + sen + '_' + met)

def GEElaiMODIS(ptsFile,metric,timeStep,buf,poly,QC,username,folderOut, scalePix = 500,startYear = None,endYear = None):
    """    
    Calculates LAI and fpar at point OR mean within buffer of point if buf > 0 OR mean within polygon if poly = 1
    
    Calculates all available years
    
    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list can include: ['Fpar', 'Lai']
        Fpar: 'FPAR absorbed by the green elements of a vegetation canopy' 400-700 nm wavelength
        Lai: 'One-sided green leaf area per unit ground area'

    timeStep - time step for temporal averaging, either 'lowest','month', OR 'year'
        
    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.
    
    QC - define which poor-quality pixels should be masked
        None: no masking of poor quality data
        Op1: We only included pixels that satisfied the following conditions: (1) 'Main (RT) method used with no saturation, best result possible', (2) 'Significant clouds NOT present (clear)', and (3) 'No or low atmospheric aerosol levels detected',
        Op2: We only included pixels that were of good quality
        Op3: We only included pixels that satisfied the following conditions: (1) Main (RT) method used with or without saturation, (2) 'Significant clouds NOT present (clear)'

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.

    Optional parameters

    scalePix - scale/spatial resolution. Default: 500
    
    startYear - The start of the time-series (year)

    endYear - The end of the time-series (year)
    
    If you don't specify the startYear and endYear the default is to download the entire time-series
    
    """
        
    # load required libraries
    import ee
    import math
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))
    
    lai_d = {}
    lai_d['Lai'] = 0.1
    lai_d['Fpar'] = 0.01
    
    #Computes the bits we need to extract.
    def getQABits(image, start, end, newName):
        pattern = 0
        listB = list(range(start, end+1))
        for one in listB:
            pattern += math.pow(2, one)
            pattern = int(pattern)
    
        return (image.select([0], [newName])
                  .bitwiseAnd(pattern)
                  .rightShift(start))

    lastImage = ee.Image(ee.ImageCollection('MODIS/006/MCD15A3H')
                         .sort('system:time_start',False)
                         .first())
    lastImageDate = lastImage.get('system:index').getInfo()

    firstImage = ee.Image(ee.ImageCollection('MODIS/006/MCD15A3H')
                         .sort('system:time_start',True)
                         .first())
    firstImageDate = firstImage.get('system:index').getInfo()
      
    if all([startYear is None,endYear is None]):
        startYear = int(firstImageDate[0:4])
        endYear = int(lastImageDate[0:4])
        startMonth = int(firstImageDate[5:7])
        endMonth = int(lastImageDate[5:7])-1
        startYearAll = startYear + 1
        endYearAll = endYear - 1
                        
        years = list(range(startYear, endYearAll + 1))
        monthsEE = ee.List(list(range(startMonth,(12*len(years)+endMonth))))
        yearsEE = ee.List(list(range(startYearAll, endYearAll + 1)))
        
    elif all([startYear >= 0,endYear >= 0]):
        startYearReal = int(firstImageDate[0:4])
        endYearReal = int(lastImageDate[0:4]) 
        
        years = list(range(max(startYearReal,startYear), (min(endYearReal,endYear) + 1)))
    
        if endYear >= endYearReal:
            endMonth = int(lastImageDate[5:7])-1
            endYearReal2 = endYearReal-1
            years2 = len(years)-1
        elif endYear < endYearReal:
            endMonth = 0
            endYearReal2 = endYearReal
            years2 = len(years)
            
        if startYear <= startYearReal:
            startMonth = int(firstImageDate[5:7])
            startYearReal2 = startYearReal+1
        elif startYear > startYearReal:
            startMonth = 0
            startYearReal2 = startYearReal
        
        monthsEE = ee.List(list(range(startMonth,(12*years2+endMonth))))
        yearsEE = ee.List(list(range(max(startYearReal2,startYear), (min(endYearReal2,endYear) + 1))))

    time_d = {}
    time_d['lowest'] = 'rl'
    time_d['month'] = 'rm'
    time_d['year'] = 'ry'
    
    for met in metric:
        modisLAI = ee.ImageCollection('MODIS/006/MCD15A3H')
        metL = [met]
##        def maskbyBits(img):
##            QA = img.select('FparLai_QC')
##            QA1 = getQABits(QA, 0, 0, 'QA')
##            QA2 = getQABits(QA, 3, 4, 'QA')
##            QA3 = getQABits(QA, 5, 7, 'QA')
##
##            mask = QA1.eq(0).And(QA2.neq(1)).And(QA3.neq(4))
##            return img.updateMask(mask)
        def maskbyBits1(img):
            QA = img.select('FparLai_QC')
            QAextra = img.select('FparExtra_QC')
            QA1 = getQABits(QA, 0, 0, 'QA')
            QA2 = getQABits(QA, 3, 4, 'QA')
            QA3 = getQABits(QA, 5, 7, 'QA')
            QA4 = getQABits(QAextra, 3, 3, 'QA')
            mask = QA1.eq(0).And(QA2.eq(0)).And(QA3.eq(0)).And(QA4.eq(0))
            return img.updateMask(mask)
        
        def maskbyBits2(img):
            QA = img.select('FparLai_QC')
            QA1 = getQABits(QA, 0, 0, 'QA')
            mask = QA1.eq(0)
            return img.updateMask(mask)
        
        def maskbyBits3(img):
            QA = img.select('FparLai_QC')
            QA2 = getQABits(QA, 3, 4, 'QA')
            QA3 = getQABits(QA, 5, 7, 'QA')
            mask = QA2.eq(0).And(QA3.lt(2))
            return img.updateMask(mask)
        
        if QC == 'None':
            modisLAIn = modisLAI.select(met)
        elif QC == 'Op1':
            modisLAIn = modisLAI.map(maskbyBits1).select(met)
        elif QC == 'Op2':
            modisLAIn = modisLAI.map(maskbyBits2).select(met)
        elif QC == 'Op3':
            modisLAIn = modisLAI.map(maskbyBits3).select(met)

        def scale1(img):
            return (img.select(metL[0])
                    .float()
                    .multiply(lai_d[metL[0]])
                    .copyProperties(img,['system:time_start','system:time_end']))

        if timeStep == 'year':

            def map_m(i):
                i = ee.Number(i).int()
                image2 = (modisLAIn
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .first())
                filtered = (modisLAIn
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .mean()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col1 = ee.ImageCollection(yearsEE.map(map_m).flatten())

        elif timeStep == 'month':
            
            def map_m(i):
                i = ee.Number(i)
                y = i.divide(12).add(years[0]).int()
                m = i.mod(12).add(1)
                image2 = (modisLAIn
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .first())
                filtered = (modisLAIn
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .mean()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col1 = ee.ImageCollection(monthsEE.map(map_m).flatten())
            
        elif all([timeStep == 'lowest',endYear is None, startYear is None]):

            img_col1 = modisLAIn
            
        elif all([timeStep == 'lowest',endYear > 0, startYear > 0]):

            img_col1 = modisLAIn.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))

        #else:
            #print("incorrect time step specified")
        
        img_col = img_col1.map(scale1)
        
        if buf > 0:
            bufL = [buf]
            def bufferPoly(feature):
                return feature.buffer(bufL[0])

            ptsB = pts1.map(bufferPoly)
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = ptsB.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = time_d[timeStep]+'_MCD15A3H_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('buffered pts by:' + str(buf) + ' for: ' + met)

        elif poly > 0:
            
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = time_d[timeStep]+'_MCD15A3H_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('spatial mean in poly: no buffer for: ' + met)

        else:
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = time_d[timeStep]+'_MCD15A3H_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
                
            #print('value at point: no buffer for: ' + met)

def GEElstMODIS(ptsFile,metric,timeStep,buf,poly,QC,username,folderOut, scalePix = 1000,startYear = None,endYear = None):
    """    
    Calculates land surface temperature at point OR mean within buffer of point if buf > 0 OR mean within polygon if poly = 1
    Calculates all available years
    
    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of time of day to include: ['day1030', 'day1330', 'night2230','night0130']
        'day1030' = Land surface temperature at ~1030 local time from Terra (MOD)
        'day1330' = Land surface temperature at ~1330 local time from Aqua (MYD)
        'night2230' = Land surface temperature at ~2230 local time from Terra (MOD)
        'night0130' = Land surface temperature at ~0130 local time from Aqua (MYD)

    timeStep - time step for temporal averaging, either 'lowest','month', OR 'year'
        
    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    QC - define which poor-quality pixels should be masked
        'None': no masking of poor quality data
        'Op1': We only included pixels that satisfied the following conditions: (1) 'LST produced, good quality', (2) 'Good data quality', (3) 'Average emissivity error ≤ 0.02', and (4) 'Average LST error ≤ 2K'

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.
    
    Optional parameters

    scalePix - scale/spatial resolution. Default: 1000
    
    startYear - The start of the time-series (year)

    endYear - The end of the time-series (year)
    
    If you don't specify the startYear and endYear the default is to download the entire time-series
    
    """
        
    # load required libraries
    import ee
    import math
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))
    
    #define dictionary for raster random names
    lst_d = {}
    lst_d['day1030'] = 'LST_Day_1km'
    lst_d['day1330'] = 'LST_Day_1km'
    lst_d['night2230'] = 'LST_Night_1km'
    lst_d['night0130'] = 'LST_Night_1km'

    lst_q = {}
    lst_q['day1030'] = 'QC_Day'
    lst_q['day1330'] = 'QC_Day'
    lst_q['night2230'] = 'QC_Night'
    lst_q['night0130'] = 'QC_Night'

    lst_s = {}
    lst_s['day1030'] = 'MODIS/006/MOD11A2'
    lst_s['day1330'] = 'MODIS/006/MYD11A2'
    lst_s['night2230'] = 'MODIS/006/MOD11A2'
    lst_s['night0130'] = 'MODIS/006/MYD11A2'

    lst_n = {}
    lst_n['day1030'] = 'MOD11A2'
    lst_n['day1330'] = 'MYD11A2'
    lst_n['night2230'] = 'MOD11A2'
    lst_n['night0130'] = 'MYD11A2'
    
    #Computes the bits we need to extract.
    def getQABits(image, start, end, newName):
        pattern = 0
        listB = list(range(start, end+1))
        for one in listB:
            pattern += math.pow(2, one)
            pattern = int(pattern)
    
        return (image.select([0], [newName])
                  .bitwiseAnd(pattern)
                  .rightShift(start))

    time_d = {}
    time_d['lowest'] = 'rl'
    time_d['month'] = 'rm'
    time_d['year'] = 'ry'
    
    for met in metric:
        modisLST = ee.ImageCollection(lst_s[met])
        metL = [met]
        def maskbyBits1(img):
            QA = img.select(lst_q[metL[0]])
            QA1 = getQABits(QA, 0, 1, 'QA')
            QA2 = getQABits(QA, 2, 3, 'QA')
            QA3 = getQABits(QA, 4, 5, 'QA')
            QA4 = getQABits(QA, 6, 7, 'QA')
            mask = QA1.eq(0).And(QA2.eq(0)).And(QA3.lt(2)).And(QA4.lt(2))
            return img.updateMask(mask)
        
        if QC == 'None':
            modisLSTn = modisLST.select(lst_d[met])
        elif QC == 'Op1':
            modisLSTn = modisLST.map(maskbyBits1).select(lst_d[met])

        def KtoC(img):
            return (img.select(lst_d[metL[0]])
                    .float()
                    .multiply(0.02)
                    .subtract(273.15)
                    .copyProperties(img,['system:time_start','system:time_end']))

        lastImage = ee.Image(ee.ImageCollection(lst_s[met])
                         .sort('system:time_start',False)
                         .first())
        lastImageDate = lastImage.get('system:index').getInfo()

        firstImage = ee.Image(ee.ImageCollection(lst_s[met])
                         .sort('system:time_start',True)
                         .first())
        firstImageDate = firstImage.get('system:index').getInfo()

        if all([startYear is None,endYear is None]):
            startYear = int(firstImageDate[0:4])
            endYear = int(lastImageDate[0:4])
            startMonth = int(firstImageDate[5:7])
            endMonth = int(lastImageDate[5:7])-1
            startYearAll = startYear + 1
            endYearAll = endYear - 1

            years = list(range(startYear, endYearAll + 1))
            monthsEE = ee.List(list(range(startMonth,(12*len(years)+endMonth))))
            yearsEE = ee.List(list(range(startYearAll, endYearAll + 1)))
            
        elif all([startYear >= 0,endYear >= 0]):
            startYearReal = int(firstImageDate[0:4])
            endYearReal = int(lastImageDate[0:4]) 
            
            years = list(range(max(startYearReal,startYear), (min(endYearReal,endYear) + 1)))
        
            if endYear >= endYearReal:
                endMonth = int(lastImageDate[5:7])-1
                endYearReal2 = endYearReal-1
                years2 = len(years)-1
            elif endYear < endYearReal:
                endMonth = 0
                endYearReal2 = endYearReal
                years2 = len(years)
                
            if startYear <= startYearReal:
                startMonth = int(firstImageDate[5:7])
                startYearReal2 = startYearReal+1
            elif startYear > startYearReal:
                startMonth = 0
                startYearReal2 = startYearReal
            
            monthsEE = ee.List(list(range(startMonth,(12*years2+endMonth))))
            yearsEE = ee.List(list(range(max(startYearReal2,startYear), (min(endYearReal2,endYear) + 1))))


        if timeStep == 'year':

            def map_m(i):
                i = ee.Number(i).int()
                image2 = (modisLSTn
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .first())
                filtered = (modisLSTn
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .mean()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col1 = ee.ImageCollection(yearsEE.map(map_m).flatten())

        elif timeStep == 'month':
            
            def map_m(i):
                i = ee.Number(i)
                y = i.divide(12).add(years[0]).int()
                m = i.mod(12).add(1)
                image2 = (modisLSTn
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .first())
                filtered = (modisLSTn
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .mean()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col1 = ee.ImageCollection(monthsEE.map(map_m).flatten())
          
        elif all([timeStep == 'lowest',endYear is None, startYear is None]):

            img_col1 = modisLSTn
            
        elif all([timeStep == 'lowest',endYear > 0, startYear > 0]):

            img_col1 = modisLSTn.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))

        #else:
            #print("incorrect time step specified")
        
        img_col = img_col1.map(KtoC)
        
        if buf > 0:
            bufL = [buf]
            def bufferPoly(feature):
                return feature.buffer(bufL[0])

            ptsB = pts1.map(bufferPoly)
            def table_m(image):
                table = (image
                    .select(lst_d[metL[0]])
                    .reduceRegions(collection = ptsB.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = time_d[timeStep]+'_'+lst_n[metL[0]]+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('buffered pts by:' + str(buf) + ' for LST: ' + met)

        elif poly > 0:
            
            def table_m(image):
                table = (image
                    .select(lst_d[metL[0]])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = time_d[timeStep]+'_'+lst_n[metL[0]]+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('spatial mean in poly: no buffer for LST: ' + met)

        else:
            def table_m(image):
                table = (image
                    .select(lst_d[metL[0]])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = time_d[timeStep]+'_'+lst_n[metL[0]]+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
                
            #print('value at point: no buffer for LST: ' + met)

def GEEviMODIS(ptsFile,metric,timeStep,buf,poly,QC, username,folderOut, scalePix = 250,startYear = None,endYear = None):
    """    
    Calculates NDVI or EVI at point OR mean within buffer of point if buf > 0 OR mean within polygon if poly = 1
    Calculates all available years.
    
    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of metrics to include: ['NDVI', 'EVI']
        'NDVI' = Normalized Difference Vegetation Index
        'EVI' = Enhanced Vegetation Index

    timeStep - time step for temporal averaging, either 'lowest','month', OR 'year'
        
    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.
    
    QC - define which poor-quality pixels should be masked
        'None': no masking of poor quality data
        'Op1': We only included pixels that satisfied the following conditions: (1) quality = good or other, (2) usefulness < 12 (3)  Aerosol Quantity equal to low or intermediate and (4) zero for the following flags: Adjacent cloud, Mixed clouds, & Possible shadow.
        'Op2': We only included pixels that were of good quality

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.
    
    Optional parameters

    scalePix - scale/spatial resolution. Default: 250
    
    startYear - The start of the time-series (year)

    endYear - The end of the time-series (year)
    
    If you don't specify the startYear and endYear the default is to download the entire time-series
    
    """
        
    # load required libraries
    import ee
    import math
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))
    
    #Computes the bits we need to extract.
    def getQABits(image, start, end, newName):
        pattern = 0
        listB = list(range(start, end+1))
        for one in listB:
            pattern += math.pow(2, one)
            pattern = int(pattern)
    
        return (image.select([0], [newName])
                  .bitwiseAnd(pattern)
                  .rightShift(start))

    time_d = {}
    time_d['lowest'] = 'rl'
    time_d['month'] = 'rm'
    time_d['year'] = 'ry'

    lastImage = ee.Image(ee.ImageCollection('MODIS/006/MOD13Q1')
                         .sort('system:time_start',False)
                         .first())
    lastImageDate = lastImage.get('system:index').getInfo()

    firstImage = ee.Image(ee.ImageCollection('MODIS/006/MOD13Q1')
                         .sort('system:time_start',True)
                         .first())
    firstImageDate = firstImage.get('system:index').getInfo()
    
    if all([startYear is None,endYear is None]):
        startYear = int(firstImageDate[0:4])
        endYear = int(lastImageDate[0:4])
        startMonth = int(firstImageDate[5:7])
        endMonth = int(lastImageDate[5:7])-1
        startYearAll = startYear + 1
        endYearAll = endYear - 1

        years = list(range(startYear, endYearAll + 1))
        monthsEE = ee.List(list(range(startMonth,(12*len(years)+endMonth))))
        yearsEE = ee.List(list(range(startYearAll, endYearAll + 1)))
        
    elif all([startYear >= 0,endYear >= 0]):
        startYearReal = int(firstImageDate[0:4])
        endYearReal = int(lastImageDate[0:4]) 
        
        years = list(range(max(startYearReal,startYear), (min(endYearReal,endYear) + 1)))
    
        if endYear >= endYearReal:
            endMonth = int(lastImageDate[5:7])-1
            endYearReal2 = endYearReal-1
            years2 = len(years)-1
        elif endYear < endYearReal:
            endMonth = 0
            endYearReal2 = endYearReal
            years2 = len(years)
            
        if startYear <= startYearReal:
            startMonth = int(firstImageDate[5:7])
            startYearReal2 = startYearReal+1
        elif startYear > startYearReal:
            startMonth = 0
            startYearReal2 = startYearReal
        
        monthsEE = ee.List(list(range(startMonth,(12*years2+endMonth))))
        yearsEE = ee.List(list(range(max(startYearReal2,startYear), (min(endYearReal2,endYear) + 1))))
    
    for met in metric:
        modisVI = ee.ImageCollection('MODIS/006/MOD13Q1')
        metL = [met]
        def maskbyBits1(img):
            QA = img.select('DetailedQA')
            QA1 = getQABits(QA, 0, 1, 'QA')
            QA2 = getQABits(QA, 2, 5, 'QA')
            QA3 = getQABits(QA, 6, 7, 'QA')
            QA4 = getQABits(QA, 8, 8, 'QA')
            QA5 = getQABits(QA, 10, 10, 'QA')
            QA6 = getQABits(QA, 15, 15, 'QA')
            mask = QA1.lt(2).And(QA2.lt(12)).And(QA3.neq(3)).And(QA3.neq(0)).And(QA4.eq(0)).And(QA5.eq(0)).And(QA6.eq(0))
            return img.updateMask(mask)
        
        def maskbyBits2(img):
            QA = img.select('DetailedQA')
            QA1 = getQABits(QA, 0, 1, 'QA')
            mask = QA1.eq(0)
            return img.updateMask(mask)
        
        if QC == 'None':
            modisVIn = modisVI.select(met)
        elif QC == 'Op1':
            modisVIn = modisVI.map(maskbyBits1).select(met)
        elif QC == 'Op2':            
            modisVIn = modisVI.map(maskbyBits2).select(met)

        def scale1(img):
            return (img.select(metL[0])
                    .float()
                    .multiply(0.0001)
                    .copyProperties(img,['system:time_start','system:time_end']))

        if timeStep == 'year':

            def map_m(i):
                i = ee.Number(i).int()
                image2 = (modisVIn
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .first())
                filtered = (modisVIn
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .mean()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col1 = ee.ImageCollection(yearsEE.map(map_m).flatten())

        elif timeStep == 'month':
            
            def map_m(i):
                i = ee.Number(i)
                y = i.divide(12).add(years[0]).int()
                m = i.mod(12).add(1)
                image2 = (modisVIn
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .first())
                filtered = (modisVIn
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .mean()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col1 = ee.ImageCollection(monthsEE.map(map_m).flatten())
        
        elif all([timeStep == 'lowest',endYear is None, startYear is None]):

            img_col1 = modisVIn
            
        elif all([timeStep == 'lowest',endYear > 0, startYear > 0]):

            img_col1 = modisVIn.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))

        #else:
            #print("incorrect time step specified")
        
        img_col = img_col1.map(scale1)
        
        if buf > 0:
            bufL = [buf]
            def bufferPoly(feature):
                return feature.buffer(bufL[0])

            ptsB = pts1.map(bufferPoly)
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = ptsB.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = time_d[timeStep]+'_MOD13Q1_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('buffered pts by:' + str(buf) + ' for: ' + met)

        elif poly > 0:
            
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = time_d[timeStep]+'_MOD13Q1_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('spatial mean in poly: no buffer for: ' + met)

        else:
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = time_d[timeStep]+'_MOD13Q1_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
                
            #print('value at point: no buffer for: ' + met)

def GEEsmos(ptsFile,metric,timeStep,buf,poly,username,folderOut, scalePix = 25000,startYear = None,endYear = None):
    """    
    Calculates soil moisture at point OR mean within buffer of point if buf > 0 OR mean within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - surface or subsurface soil moisture: ['ssm', 'susm','smp']
        'ssm' = Surface soil moisture (mm)
        'susm' = Subsurface soil moisture (mm)
        'smp' = Soil moisture profile (fraction, 0-1)

    timeStep - time step for temporal averaging, either 'lowest','month', OR 'year'
    
    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.
    
    Optional parameters    

    scalePix - scale/spatial resolution. Default: 25000
    
    startYear - The start of the time-series (year)

    endYear - The end of the time-series (year)
    
    If you don't specify the startYear and endYear the default is to download the entire time-series
    
    """
        
    # load required libraries
    import ee
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    time_d = {}
    time_d['lowest'] = 'rl'
    time_d['month'] = 'rm'
    time_d['year'] = 'ry'

    lastImage = ee.Image(ee.ImageCollection('NASA_USDA/HSL/soil_moisture')
                         .sort('system:time_start',False)
                         .first())
    lastImageDate = lastImage.get('system:index').getInfo()

    firstImage = ee.Image(ee.ImageCollection('NASA_USDA/HSL/soil_moisture')
                         .sort('system:time_start',True)
                         .first())
    firstImageDate = firstImage.get('system:index').getInfo()
     
    #startMonth - 1, because time-series starts on Jan 1
    #startYearAll: did't add one, for same reason
    if all([startYear is None,endYear is None]):
        startYear = int(firstImageDate[(len(firstImageDate)-8):(len(firstImageDate)-4)])
        endYear = int(lastImageDate[(len(lastImageDate)-8):(len(lastImageDate)-4)])
        startMonth = int(firstImageDate[(len(firstImageDate)-4):(len(firstImageDate)-2)])-1
        endMonth = int(lastImageDate[(len(lastImageDate)-4):(len(lastImageDate)-2)])-1
        startYearAll = startYear
        endYearAll = endYear - 1
        
        years = list(range(startYear, endYearAll + 1))
        monthsEE = ee.List(list(range(startMonth,(12*len(years)+endMonth))))
        yearsEE = ee.List(list(range(startYearAll, endYearAll + 1)))
        
    elif all([startYear >= 0,endYear >= 0]):
        startYearReal = int(firstImageDate[(len(firstImageDate)-8):(len(firstImageDate)-4)])
        endYearReal = int(lastImageDate[(len(lastImageDate)-8):(len(lastImageDate)-4)]) 
        
        years = list(range(max(startYearReal,startYear), (min(endYearReal,endYear) + 1)))
    
        if endYear >= endYearReal:
            endMonth = int(lastImageDate[(len(lastImageDate)-4):(len(lastImageDate)-2)])-1
            endYearReal2 = endYearReal-1
            years2 = len(years)-1
        elif endYear < endYearReal:
            endMonth = 0
            endYearReal2 = endYearReal
            years2 = len(years)
            
        if startYear <= startYearReal:
            startMonth = int(firstImageDate[(len(firstImageDate)-4):(len(firstImageDate)-2)])-1
        elif startYear > startYearReal:
            startMonth = 0
        
        monthsEE = ee.List(list(range(startMonth,(12*years2+endMonth))))
        yearsEE = ee.List(list(range(max(startYearReal,startYear), (min(endYearReal2,endYear) + 1))))
    
    for met in metric:
        SMOS = ee.ImageCollection('NASA_USDA/HSL/soil_moisture').select(met)
        metL = [met]
        
        if timeStep == 'year':

            def map_m(i):
                i = ee.Number(i).int()
                image2 = (SMOS
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .first())
                filtered = (SMOS
                    .filter(ee.Filter.calendarRange(i, i, 'year'))
                    .mean()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col = ee.ImageCollection(yearsEE.map(map_m).flatten())

        elif timeStep == 'month':
            
            def map_m(i):
                i = ee.Number(i)
                y = i.divide(12).add(years[0]).int()
                m = i.mod(12).add(1)
                image2 = (SMOS
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .first())
                filtered = (SMOS
                    .filter(ee.Filter.calendarRange(m, m, 'month'))
                    .filter(ee.Filter.calendarRange(y, y, 'year'))
                    .mean()
                    .copyProperties(image2,['system:time_start','system:time_end']))
                return filtered

            img_col = ee.ImageCollection(monthsEE.map(map_m).flatten())

        elif all([timeStep == 'lowest',endYear is None, startYear is None]):

            img_col = SMOS
            
        elif all([timeStep == 'lowest',endYear > 0, startYear > 0]):

            img_col = SMOS.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))

        #else:
            #print("incorrect time step specified")
       
        if buf > 0:
            bufL = [buf]
            def bufferPoly(feature):
                return feature.buffer(bufL[0])

            ptsB = pts1.map(bufferPoly)
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = ptsB.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = str(time_d[timeStep])+'_SMOS_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('buffered pts by:' + str(buf) + ' for SMOS: ' + met)

        elif poly > 0:
            
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = str(time_d[timeStep])+'_SMOS_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('spatial mean in poly: no buffer for SMOS: ' + met)

        else:
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = str(time_d[timeStep])+'_SMOS_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
                
            #print('value at point: no buffer for SMOS: ' + met)
            
def GEEterraClimatePtsAvgMonth(ptsFile,metric,startYear,endYear,buf,poly,username,folderOut, scalePix = 4000):
    """    
    Calculates global climate temporal monthly averages at point OR within buffer of point if buf > 0 OR within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of metrics to include in output ['aet','def','pdsi','pet','pr','ro','soil','srad','swe','tmmn','tmmx','vap','vpd','vs']
        aet: Actual evapotranspiration (mm)
        def: climatic water deficit (mm)
        pdsi: Palmer Drought Severity Index
        pet: reference evapotranspiration (penman-montieth, mm)
        pr: precipitation (mm)
        ro: runoff (mm)
        soil: soil moisture (mm)
        srad: Downward surface shortwave radiation (W/m2)
        swe: snow water equivalent (mm)
        tmmn: min temperature (deg C)
        tmmx: max temperature (deg C)
        vap: vapor pressure (kPa)
        vpd: vapor pressure deficit(kPa)
        vs: Wind-speed at 10m (m/s)
        
    startYear - The start of the time-series (year) 1958 is the earliest possible year

    endYear - The end of the time-series (year)

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile is a polygon, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.

    Optional parameters

    scalePix - scale/spatial resolution. Default: 4000
    
    """
        
    # load required libraries
    import ee
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    years = list(range(startYear, endYear + 1))

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    ID_field = "geeID"

    scale_d = {}
    scale_d['aet'] = 0.1
    scale_d['def'] = 0.1
    scale_d['pdsi'] = 0.01
    scale_d['pet'] = 0.1
    scale_d['soil'] = 0.1
    scale_d['srad'] = 0.1
    scale_d['tmmn'] = 0.1
    scale_d['tmmx'] = 0.1
    scale_d['vap'] = 0.001
    scale_d['vpd'] = 0.01
    scale_d['vs'] = 0.01
    
    for met in metric:
        metL = [met]
        Gridmet_pr = ee.ImageCollection('IDAHO_EPSCOR/TERRACLIMATE').select(met)
        
        img_col0 = Gridmet_pr.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))

        if any([(met == 'pr'),(met == 'ro'),(met == 'swe')]):

            img_col = img_col0
            
        else:

            def Scale1(img):
                return (img.float()
                        .multiply(scale_d[metL[0]])
                        .copyProperties(img,['system:time_start','system:time_end']))

            img_col = img_col0.map(Scale1)
        
        if buf > 0:
            bufL = [buf]
            def bufferPoly(feature):
                return feature.buffer(bufL[0])

            ptsB = pts1.map(bufferPoly)
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = ptsB.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 'tcy'+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
            #print ('buffered pts by:' + str(buf) + ' for ' + met)

        elif poly > 0:
            
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 'tcy'+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('spatial mean in poly: no buffer for ' + met)

        else:
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 'tcy'+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
                
            #print('value at point: no buffer for ' + met)


def GEEnasaNEXGDDP(ptsFile,metric,timeStep,startYear,endYear,scenarios,buf,poly,username,folderOut,models = ['ACCESS1-0', 'bcc-csm1-1', 'BNU-ESM',
        'CanESM2', 'CCSM4', 'CESM1-BGC', 'CNRM-CM5', 'CSIRO-Mk3-6-0',
        'GFDL-CM3', 'GFDL-ESM2G', 'GFDL-ESM2M', 'inmcm4', 'IPSL-CM5A-LR',
        'IPSL-CM5A-MR', 'MIROC-ESM', 'MIROC-ESM-CHEM', 'MIROC5', 'MPI-ESM-LR',
        'MPI-ESM-MR', 'MRI-CGCM3', 'NorESM1-M'], scalePix = 25000):

    """    
    Calculates future climate projections at point OR mean within buffer of point if buf > 0 OR mean within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - precipitation and temperature: ['pr', 'tasmin','tasmax']
        'pr' = sum of precipitation, liquid and solid phases (kg/(m^2*s))
        'tasmin' = mean daily min near surface air temperature (K)
        'tasmax' = mean daily max near surface air temperature (K)

    timeStep - time step for temporal averaging, either 'day','month', OR 'year'

    startYear - First year of time series: 1950-2006 for 'historical' scenario and 2006-2099 for future climate change scenarios

    endYear - Last year of time series: 1950-2006 for 'historical' scenario or 2006-2099 for future climate change scenarios
    
    scenarios - CMIP5 scenario: choices are ['historical', 'rcp45', 'rcp85']

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.

    Optional parameters

    models - If you are not aggregating, CMIP5 model choices are ['ACCESS1-0', 'bcc-csm1-1', 'BNU-ESM',
        'CanESM2', 'CCSM4', 'CESM1-BGC', 'CNRM-CM5', 'CSIRO-Mk3-6-0',
        'GFDL-CM3', 'GFDL-ESM2G', 'GFDL-ESM2M', 'inmcm4', 'IPSL-CM5A-LR',
        'IPSL-CM5A-MR', 'MIROC-ESM', 'MIROC-ESM-CHEM', 'MIROC5', 'MPI-ESM-LR',
        'MPI-ESM-MR', 'MRI-CGCM3', 'NorESM1-M']. Default is all models.

    scalePix - scale/spatial resolution. Default: 25000
    
    """
        
    # load required libraries
    import ee

    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    time_d = {}
    time_d['day'] = 'projd'
    time_d['month'] = 'projm'
    time_d['year'] = 'projy'
    
    for met in metric:

        for scenario in scenarios:

                for model in models:

                    NEX = (ee.ImageCollection('NASA/NEX-GDDP')
                        .select(met)
                        .filterMetadata('model', 'equals', model)
                        .filterMetadata('scenario', 'equals', scenario))

                    metL = [met]
                    
                    years = list(range(startYear, endYear + 1))
                    monthsEE = ee.List(list(range(0,(12*len(years)))))
                    yearsEE = ee.List(years)

######Turned off unit conversion, because it fails when there are too many pts
##                    if (met == 'pr'):
##
##                        def Scale1(img):
##                            return (img.float()
##                                    .multiply(86400)
##                                    .copyProperties(img,['system:time_start','system:time_end']))
##
##                        NEX = NEX0.map(Scale1)
##                        
##                    elif any([(met == 'tasmin'),(met == 'tasmax')]):
##
##                        def KtoC(img):
##                            return (img.float()
##                                .subtract(273.15)
##                                .copyProperties(img,['system:time_start','system:time_end']))
##
##                        NEX = NEX0.map(KtoC)
                    
                    if all([(timeStep == 'year'),any([(met == 'tasmin'),(met == 'tasmax')])]):

                        def map_m(i):
                            i = ee.Number(i).int()
                            image2 = (NEX
                                .filter(ee.Filter.calendarRange(i, i, 'year'))
                                .first())
                            filtered = (NEX
                                .filter(ee.Filter.calendarRange(i, i, 'year'))
                                .mean()
                                .copyProperties(image2,['system:time_start','system:time_end']))
                            return filtered

                        img_col = ee.ImageCollection(yearsEE.map(map_m).flatten())

                    elif all([(timeStep == 'month'),any([(met == 'tasmin'),(met == 'tasmax')])]):
                        
                        def map_m(i):
                            i = ee.Number(i)
                            y = i.divide(12).add(years[0]).int()
                            m = i.mod(12).add(1)
                            image2 = (NEX
                                .filter(ee.Filter.calendarRange(m, m, 'month'))
                                .filter(ee.Filter.calendarRange(y, y, 'year'))
                                .first())
                            filtered = (NEX
                                .filter(ee.Filter.calendarRange(m, m, 'month'))
                                .filter(ee.Filter.calendarRange(y, y, 'year'))
                                .mean()
                                .copyProperties(image2,['system:time_start','system:time_end']))
                            return filtered

                        img_col = ee.ImageCollection(monthsEE.map(map_m).flatten())

                    elif all([(timeStep == 'year'),(met == 'pr')]):

                        def map_m(i):
                            i = ee.Number(i).int()
                            image2 = (NEX
                                .filter(ee.Filter.calendarRange(i, i, 'year'))
                                .first())
                            filtered = (NEX
                                .filter(ee.Filter.calendarRange(i, i, 'year'))
                                .sum()
                                .copyProperties(image2,['system:time_start','system:time_end']))
                            return filtered

                        img_col = ee.ImageCollection(yearsEE.map(map_m).flatten())

                    elif all([(timeStep == 'month'),(met == 'pr')]):
                        
                        def map_m(i):
                            i = ee.Number(i)
                            y = i.divide(12).add(years[0]).int()
                            m = i.mod(12).add(1)
                            image2 = (NEX
                                .filter(ee.Filter.calendarRange(m, m, 'month'))
                                .filter(ee.Filter.calendarRange(y, y, 'year'))
                                .first())
                            filtered = (NEX
                                .filter(ee.Filter.calendarRange(m, m, 'month'))
                                .filter(ee.Filter.calendarRange(y, y, 'year'))
                                .sum()
                                .copyProperties(image2,['system:time_start','system:time_end']))
                            return filtered

                        img_col = ee.ImageCollection(monthsEE.map(map_m).flatten())

                    elif timeStep == 'day':

                        img_col = NEX.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))

                    #else:
                        #print("incorrect time step specified")
                   
                    if buf > 0:
                        bufL = [buf]
                        def bufferPoly(feature):
                            return feature.buffer(bufL[0])

                        ptsB = pts1.map(bufferPoly)
                        def table_m(image):
                            table = (image
                                .select(metL[0])
                                .reduceRegions(collection = ptsB.select([ID_field]),
                                                reducer = ee.Reducer.mean(),
                                                scale = scalePix))
                                    
                            def table_add_date(f):
                                return f.set('startDate', ee.Date(image.get('system:time_start')))

                            return table.map(table_add_date)

                        triplets = img_col.map(table_m).flatten()

                        task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                                .filter(ee.Filter.neq('mean', None))
                                                                .select(['.*'],None,False),
                                                                description = str(time_d[timeStep])+'_NEX_'+str(met)+'_'+scenario+'_'+model+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                                folder = folderOut,
                                                                fileFormat = 'CSV')
                        task_tc.start()
                
                
                        #print ('buffered pts by:' + str(buf) + ' for NEX: ' + met + ' ' + scenario + ' ' + model)

                    elif poly > 0:
                        
                        def table_m(image):
                            table = (image
                                .select(metL[0])
                                .reduceRegions(collection = pts1.select([ID_field]),
                                                reducer = ee.Reducer.mean(),
                                                scale = scalePix))
                                    
                            def table_add_date(f):
                                return f.set('startDate', ee.Date(image.get('system:time_start')))

                            return table.map(table_add_date)

                        triplets = img_col.map(table_m).flatten()

                        task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                                .filter(ee.Filter.neq('mean', None))
                                                                .select(['.*'],None,False),
                                                                description = str(time_d[timeStep])+'_NEX_'+str(met)+'_'+scenario+'_'+model+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                                folder = folderOut,
                                                                fileFormat = 'CSV')
                        task_tc.start()
                
                
                        #print ('spatial mean in poly: no buffer for NEX: ' + met + ' ' + scenario + ' ' + model)

                    else:
                        def table_m(image):
                            table = (image
                                .select(metL[0])
                                .reduceRegions(collection = pts1.select([ID_field]),
                                                reducer = ee.Reducer.mean(),
                                                scale = scalePix))
                                    
                            def table_add_date(f):
                                return f.set('startDate', ee.Date(image.get('system:time_start')))

                            return table.map(table_add_date)

                        triplets = img_col.map(table_m).flatten()

                        task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                                .filter(ee.Filter.neq('mean', None))
                                                                .select(['.*'],None,False),
                                                                description = str(time_d[timeStep])+'_NEX_'+str(met)+'_'+scenario+'_'+model+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                                folder = folderOut,
                                                                fileFormat = 'CSV')
                        task_tc.start()
                            
                        #print('value at point: no buffer for NEX: ' + met + ' ' + scenario + ' ' + model)

###This almost always fails, maybe turn this option off
# =============================================================================
#             if (aggregate == 1):
# 
#                 NEX = (ee.ImageCollection('NASA/NEX-GDDP')
#                     .select(met)
#                     .filterMetadata('scenario', 'equals', scenario))
# 
#                 metL = [met]
#                 
#                 years = list(range(startYear, endYear + 1))
#                 monthsEE = ee.List(list(range(0,(12*len(years)))))
#                 yearsEE = ee.List(years)
# 
# ##                if (met == 'pr'):
# ##
# ##                    def Scale1(img):
# ##                        return (img.float()
# ##                                .multiply(86400)
# ##                                .copyProperties(img,['system:time_start','system:time_end']))
# ##
# ##                    NEX = NEX0.map(Scale1)
# ##                    
# ##                elif any([(met == 'tasmin'),(met == 'tasmax')]):
# ##
# ##                    def KtoC(img):
# ##                        return (img.float()
# ##                            .subtract(273.15)
# ##                            .copyProperties(img,['system:time_start','system:time_end']))
# ##
# ##                    NEX = NEX0.map(KtoC)
#                 
#                 if all([(timeStep == 'year'),any([(met == 'tasmin'),(met == 'tasmax')])]):
# 
#                     def map_m(i):
#                         i = ee.Number(i).int()
#                         image2 = (NEX
#                             .filter(ee.Filter.calendarRange(i, i, 'year'))
#                             .first())
#                         filtered = (NEX
#                             .filter(ee.Filter.calendarRange(i, i, 'year'))
#                             .mean()
#                             .copyProperties(image2,['system:time_start','system:time_end']))
#                         return filtered
# 
#                     img_col = ee.ImageCollection(yearsEE.map(map_m).flatten())
# 
#                 elif all([(timeStep == 'month'),any([(met == 'tasmin'),(met == 'tasmax')])]):
#                     
#                     def map_m(i):
#                         i = ee.Number(i)
#                         y = i.divide(12).add(years[0]).int()
#                         m = i.mod(12).add(1)
#                         image2 = (NEX
#                             .filter(ee.Filter.calendarRange(m, m, 'month'))
#                             .filter(ee.Filter.calendarRange(y, y, 'year'))
#                             .first())
#                         filtered = (NEX
#                             .filter(ee.Filter.calendarRange(m, m, 'month'))
#                             .filter(ee.Filter.calendarRange(y, y, 'year'))
#                             .mean()
#                             .copyProperties(image2,['system:time_start','system:time_end']))
#                         return filtered
# 
#                     img_col = ee.ImageCollection(monthsEE.map(map_m).flatten())
# 
#                 elif all([(timeStep == 'year'),(met == 'pr')]):
# 
#                     def map_m(i):
#                         i = ee.Number(i).int()
#                         image2 = (NEX
#                             .filter(ee.Filter.calendarRange(i, i, 'year'))
#                             .first())
#                         filtered = (NEX
#                             .filter(ee.Filter.calendarRange(i, i, 'year'))
#                             .sum()
#                             .divide(21.0)
#                             .copyProperties(image2,['system:time_start','system:time_end']))
#                         return filtered
# 
#                     img_col = ee.ImageCollection(yearsEE.map(map_m).flatten())
# 
#                 elif all([(timeStep == 'month'),(met == 'pr')]):
#                     
#                     def map_m(i):
#                         i = ee.Number(i)
#                         y = i.divide(12).add(years[0]).int()
#                         m = i.mod(12).add(1)
#                         image2 = (NEX
#                             .filter(ee.Filter.calendarRange(m, m, 'month'))
#                             .filter(ee.Filter.calendarRange(y, y, 'year'))
#                             .first())
#                         filtered = (NEX
#                             .filter(ee.Filter.calendarRange(m, m, 'month'))
#                             .filter(ee.Filter.calendarRange(y, y, 'year'))
#                             .sum()
#                             .divide(21.0)
#                             .copyProperties(image2,['system:time_start','system:time_end']))
#                         return filtered
# 
#                     img_col = ee.ImageCollection(monthsEE.map(map_m).flatten())
# 
#                 else:
#                     #print("incorrect time step specified. When aggregating, options only exist for month or year")
#                
#                 if buf > 0:
#                     bufL = [buf]
#                     def bufferPoly(feature):
#                         return feature.buffer(bufL[0])
# 
#                     ptsB = pts1.map(bufferPoly)
#                     def table_m(image):
#                         table = (image
#                             .select(metL[0])
#                             .reduceRegions(collection = ptsB.select([ID_field]),
#                                             reducer = ee.Reducer.mean(),
#                                             scale = scalePix))
#                                 
#                         def table_add_date(f):
#                             return f.set('startDate', ee.Date(image.get('system:time_start')))
# 
#                         return table.map(table_add_date)
# 
#                     triplets = img_col.map(table_m).flatten()
# 
#                     task_tc = ee.batch.Export.table.toDrive(collection = triplets
#                                                             .filter(ee.Filter.neq('mean', None))
#                                                             .select(['.*'],None,False),
#                                                             description = str(time_d[timeStep])+'_NEX_'+str(met)+'_'+scenario+'_'+'Agg21GCM'+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
#                                                             folder = folderOut,
#                                                             fileFormat = 'CSV')
#                     task_tc.start()
#             
#             
#                     #print ('buffered pts by:' + str(buf) + ' for NEX: ' + met + ' ' + scenario + ' ' + 'Agg21GCM')
# 
#                 elif poly > 0:
#                     
#                     def table_m(image):
#                         table = (image
#                             .select(metL[0])
#                             .reduceRegions(collection = pts1.select([ID_field]),
#                                             reducer = ee.Reducer.mean(),
#                                             scale = scalePix))
#                                 
#                         def table_add_date(f):
#                             return f.set('startDate', ee.Date(image.get('system:time_start')))
# 
#                         return table.map(table_add_date)
# 
#                     triplets = img_col.map(table_m).flatten()
# 
#                     task_tc = ee.batch.Export.table.toDrive(collection = triplets
#                                                             .filter(ee.Filter.neq('mean', None))
#                                                             .select(['.*'],None,False),
#                                                             description = str(time_d[timeStep])+'_NEX_'+str(met)+'_'+scenario+'_'+'Agg21GCM'+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
#                                                             folder = folderOut,
#                                                             fileFormat = 'CSV')
#                     task_tc.start()
#             
#             
#                     #print ('spatial mean in poly: no buffer for NEX: ' + met + ' ' + scenario + ' ' + 'Agg21GCM')
# 
#                 else:
#                     def table_m(image):
#                         table = (image
#                             .select(metL[0])
#                             .reduceRegions(collection = pts1.select([ID_field]),
#                                             reducer = ee.Reducer.mean(),
#                                             scale = scalePix))
#                                 
#                         def table_add_date(f):
#                             return f.set('startDate', ee.Date(image.get('system:time_start')))
# 
#                         return table.map(table_add_date)
# 
#                     triplets = img_col.map(table_m).flatten()
# 
#                     task_tc = ee.batch.Export.table.toDrive(collection = triplets
#                                                             .filter(ee.Filter.neq('mean', None))
#                                                             .select(['.*'],None,False),
#                                                             description = str(time_d[timeStep])+'_NEX_'+str(met)+'_'+scenario+'_'+'Agg21GCM'+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
#                                                             folder = folderOut,
#                                                             fileFormat = 'CSV')
#                     task_tc.start()
#                         
#                     #print('value at point: no buffer for NEX: ' + met + ' ' + scenario + ' ' + 'Agg21GCM')
# =============================================================================

def GEEmonthTRMM(ptsFile,startYear,endYear,buf,poly,username,folderOut, scalePix = 25000):
    """    
    Calculates global average precipitation rate (mm/hr) per month at point OR within buffer of point if buf > 0 OR within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    startYear - The start of the time-series (year) 1998 is the earliest possible year

    endYear - The end of the time-series (year)

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile is a polygon, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.

    Optional parameters

    scalePix - scale/spatial resolution. Default: 25000
    
    """
        
    # load required libraries
    import ee

    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    years = list(range(startYear, endYear + 1))

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    ID_field = "geeID"
              
    TRMM = ee.ImageCollection('TRMM/3B43V7').select('precipitation')
        
    img_col = TRMM.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))
        
    if buf > 0:
        bufL = [buf]
        def bufferPoly(feature):
            return feature.buffer(bufL[0])

        ptsB = pts1.map(bufferPoly)
        def table_m(image):
            table = (image
                .select('precipitation')
                .reduceRegions(collection = ptsB.select([ID_field]),
                                reducer = ee.Reducer.mean(),
                                scale = scalePix))
                        
            def table_add_date(f):
                return f.set('startDate', ee.Date(image.get('system:time_start')))

            return table.map(table_add_date)

        triplets = img_col.map(table_m).flatten()

        task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                .filter(ee.Filter.neq('mean', None))
                                                .select(['.*'],None,False),
                                                description = 'rm_TRMM_pr_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()
    
        #print ('buffered pts by:' + str(buf) + ' for TRMM')

    elif poly > 0:
            
        def table_m(image):
            table = (image
                .select('precipitation')
                .reduceRegions(collection = pts1.select([ID_field]),
                                reducer = ee.Reducer.mean(),
                                scale = scalePix))
                        
            def table_add_date(f):
                return f.set('startDate', ee.Date(image.get('system:time_start')))

            return table.map(table_add_date)

        triplets = img_col.map(table_m).flatten()

        task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                .filter(ee.Filter.neq('mean', None))
                                                .select(['.*'],None,False),
                                                description = 'rm_TRMM_pr_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()
    
    
        #print ('spatial mean in poly: no buffer for TRMM')

    else:
        def table_m(image):
            table = (image
                .select('precipitation')
                .reduceRegions(collection = pts1.select([ID_field]),
                                reducer = ee.Reducer.mean(),
                                scale = scalePix))
                        
            def table_add_date(f):
                return f.set('startDate', ee.Date(image.get('system:time_start')))

            return table.map(table_add_date)

        triplets = img_col.map(table_m).flatten()

        task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                .filter(ee.Filter.neq('mean', None))
                                                .select(['.*'],None,False),
                                                description = 'rm_TRMM_pr_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                folder = folderOut,
                                                fileFormat = 'CSV')
        task_tc.start()
                
        #print('value at point: no buffer for TRMM')


def GEEprismPtsAvgMonth(ptsFile,metric,startYear,endYear,buf,poly,username,folderOut, scalePix = 4000):
    """    
    Calculates PRISM climate temporal monthly averages at point OR within buffer of point if buf > 0 OR within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of metrics to include in output ['ppt','tmean','tmin','tmax','tdmean','vpdmin','vpdmax']
        ppt: "Monthly total precipitation (including rain and melted snow)" (mm)
        tmean: "Monthly average of daily mean temperature" (deg C)
        tmin: "Monthly minimum temperature" (deg C)
        tmax: "Monthly average of daily maximum temperature" (deg C)
        tdmean: "Monthly average of daily mean dew point temperature" (deg C) 
        vpdmin: "Monthly average of daily minimum vapor pressure deficit" (hPa)	
        vpdmax: "Monthly average of daily maximum vapor pressure deficit" (hPa)

    startYear - The start of the time-series (year) 1895 is the earliest possible year

    endYear - The end of the time-series (year)

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    username - Specify your GEE username as a string.
    
    folderOut - Output folder name on google drive.

    Optional parameters

    scalePix - scale/spatial resolution. Default: 4000
    
    """
        
    # load required libraries
    import ee

    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    years = list(range(startYear, endYear + 1))

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    ID_field = "geeID"
    
    for met in metric:
        metL = [met]
        Gridmet_pr = ee.ImageCollection('OREGONSTATE/PRISM/AN81m').select(met)
        
        img_col = Gridmet_pr.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))
        
        if buf > 0:
            bufL = [buf]
            def bufferPoly(feature):
                return feature.buffer(bufL[0])

            ptsB = pts1.map(bufferPoly)
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = ptsB.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 'pri'+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
            #print ('buffered pts by:' + str(buf) + ' for ' + met)

        elif poly > 0:
            
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 'pri'+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
    
    
            #print ('spatial mean in poly: no buffer for ' + met)

        else:
            def table_m(image):
                table = (image
                    .select(metL[0])
                    .reduceRegions(collection = pts1.select([ID_field]),
                                    reducer = ee.Reducer.mean(),
                                    scale = scalePix))
                        
                def table_add_date(f):
                    return f.set('startDate', ee.Date(image.get('system:time_start')))

                return table.map(table_add_date)

            triplets = img_col.map(table_m).flatten()

            task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                    .filter(ee.Filter.neq('mean', None))
                                                    .select(['.*'],None,False),
                                                    description = 'pri'+'_'+str(met)+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                    folder = folderOut,
                                                    fileFormat = 'CSV')
            task_tc.start()
                
            #print('value at point: no buffer for ' + met)

def GEEmacaGCMs(ptsFile,metric,timeStep,startYear,endYear,scenarios,buf,poly,models,
                username,folderOut, scalePix = 4000):
    """    
    Calculates MACA future climate projections at point OR mean within buffer of point if buf > 0 OR mean within polygon if poly = 1

    Requires:
    
    ptsfile - file name of uploaded shapefile to GEE.

    metric - list of metrics to include in output : ['tasmax','tasmin','huss','pr','rsds','was']
        tasmax: 'Monthly average of maximum daily temperature near surface' (K)
        tasmin: 'Monthly average of minimum daily temperature near surface' (K)
        huss: 'Monthly average of mean daily specific humidity near surface' (kg/kg)
        pr: 'Total monthly precipitation amount at surface' (mm)
        rsds: 'Monthly average of mean daily downward shortwave radiation at surface' (W/m^2)	
        was: 'Monthly average of mean daily near surface wind speed' (m/s)	

    timeStep - time step for temporal averaging, either 'month', OR 'year'

    startYear - First year of time series: options include 1950-2005 for 'historical' scenario and 2006-2099 for future climate change scenarios

    endYear - Last year of time series: options include 1950-2005 for 'historical' scenario or 2006-2099 for future climate change scenarios
    
    scenarios - CMIP5 scenarios: choices are ['rcp85', 'rcp45', or 'historical']

    buf - specifies the radius of the buffer (meters) to add around each point. For no buffer, use buf = 0. 

    poly - If your ptsfile contains polygons, then specify poly = 1; otherwise use poly = 0.

    models - CMIP5 model choices are
                ['bcc-csm1-1','bcc-csm1-1-m','BNU-ESM','CanESM2','CCSM4','CNRM-CM5','CSIRO-Mk3-6-0',
                'GFDL-ESM2M','GFDL-ESM2G','HadGEM2-ES365','HadGEM2-CC365','inmcm4','IPSL-CM5A-LR','IPSL-CM5A-MR',
                'IPSL-CM5B-LR','MIROC5','MIROC-ESM','MIROC-ESM-CHEM','MRI-CGCM3','NorESM1-M']

    username - Specify your GEE username as a string.

    folderOut - Output folder name on google drive.

    Optional parameters

    scalePix - scale/spatial resolution. Default: 4000
    
    """
        
    # load required libraries
    import ee
    
    # Initialize the Earth Engine object, using the authentication credentials.
    ee.Initialize()

    ID_field = "geeID"

    #load pts or poly file
    pts1 = ee.FeatureCollection('users/' + username + '/' + str(ptsFile))

    time_d = {}
    time_d['month'] = 'projm'
    time_d['year'] = 'projy'
    
    for met in metric:

        for scenario in scenarios:

            for model in models:

                MACA = (ee.ImageCollection('IDAHO_EPSCOR/MACAv2_METDATA_MONTHLY')
                        .select(met)
                        .filterMetadata('model', 'equals', model)
                        .filterMetadata('scenario', 'equals', scenario))

                metL = [met]
                    
                years = list(range(startYear, endYear + 1))
                yearsEE = ee.List(years)
                    
                if all([(timeStep == 'year'),any([(met == 'tasmin'),(met == 'tasmax'),
                                                      (met == 'huss'),(met == 'rsds'),
                                                      (met == 'was')])]):

                    def map_m(i):
                        i = ee.Number(i).int()
                        image2 = (MACA
                                .filter(ee.Filter.calendarRange(i, i, 'year'))
                                .first())
                        filtered = (MACA
                                .filter(ee.Filter.calendarRange(i, i, 'year'))
                                .mean()
                                .copyProperties(image2,['system:time_start','system:time_end']))
                        return filtered

                    img_col = ee.ImageCollection(yearsEE.map(map_m).flatten())

                elif (timeStep == 'month'):
                        
                    img_col = MACA.filter(ee.Filter.calendarRange(startYear, endYear, 'year'))

                elif all([(timeStep == 'year'),(met == 'pr')]):

                    def map_m(i):
                        i = ee.Number(i).int()
                        image2 = (MACA
                                .filter(ee.Filter.calendarRange(i, i, 'year'))
                                .first())
                        filtered = (MACA
                                .filter(ee.Filter.calendarRange(i, i, 'year'))
                                .sum()
                                .copyProperties(image2,['system:time_start','system:time_end']))
                        return filtered

                    img_col = ee.ImageCollection(yearsEE.map(map_m).flatten())

                #else:
                    #print("incorrect time step specified")
                   
                if buf > 0:
                    bufL = [buf]
                    def bufferPoly(feature):
                        return feature.buffer(bufL[0])

                    ptsB = pts1.map(bufferPoly)
                    def table_m(image):
                        table = (image
                                .select(metL[0])
                                .reduceRegions(collection = ptsB.select([ID_field]),
                                                reducer = ee.Reducer.mean(),
                                                scale = scalePix))
                                    
                        def table_add_date(f):
                            return f.set('startDate', ee.Date(image.get('system:time_start')))

                        return table.map(table_add_date)

                    triplets = img_col.map(table_m).flatten()

                    task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                                .filter(ee.Filter.neq('mean', None))
                                                                .select(['.*'],None,False),
                                                                description = str(time_d[timeStep])+'_MACA_'+str(met)+'_'+scenario+'_'+model+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_ptsB',
                                                                folder = folderOut,
                                                                fileFormat = 'CSV')
                    task_tc.start()
                
                
                    #print ('buffered pts by:' + str(buf) + ' for MACA: ' + met + ' ' + scenario + ' ' + model)

                elif poly > 0:
                        
                    def table_m(image):
                        table = (image
                                .select(metL[0])
                                .reduceRegions(collection = pts1.select([ID_field]),
                                                reducer = ee.Reducer.mean(),
                                                scale = scalePix))
                                    
                        def table_add_date(f):
                            return f.set('startDate', ee.Date(image.get('system:time_start')))

                        return table.map(table_add_date)

                    triplets = img_col.map(table_m).flatten()

                    task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                                .filter(ee.Filter.neq('mean', None))
                                                                .select(['.*'],None,False),
                                                                description = str(time_d[timeStep])+'_MACA_'+str(met)+'_'+scenario+'_'+model+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_poly1',
                                                                folder = folderOut,
                                                                fileFormat = 'CSV')
                    task_tc.start()
                
                
                    #print ('spatial mean in poly: no buffer for MACA: ' + met + ' ' + scenario + ' ' + model)

                else:
                    def table_m(image):
                        table = (image
                                .select(metL[0])
                                .reduceRegions(collection = pts1.select([ID_field]),
                                                reducer = ee.Reducer.mean(),
                                                scale = scalePix))
                                    
                        def table_add_date(f):
                            return f.set('startDate', ee.Date(image.get('system:time_start')))

                        return table.map(table_add_date)

                    triplets = img_col.map(table_m).flatten()

                    task_tc = ee.batch.Export.table.toDrive(collection = triplets
                                                                .filter(ee.Filter.neq('mean', None))
                                                                .select(['.*'],None,False),
                                                                description = str(time_d[timeStep])+'_MACA_'+str(met)+'_'+scenario+'_'+model+'_'+str(years[0])+'_'+str(years[len(years)-1])+'_pts1',
                                                                folder = folderOut,
                                                                fileFormat = 'CSV')
                    task_tc.start()
                            
                    #print('value at point: no buffer for MACA: ' + met + ' ' + scenario + ' ' + model)
