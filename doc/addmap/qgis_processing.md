# Guide to processing maps from GADM using QGIS

- [Step 1: Download your map from GADM](#step-1-download-your-map-from-gadm)
- [Step 2: Process your map in QGIS](#step-2-process-your-map-in-qgis)
  * [Step 2.1: Importing](#step-21-importing)
  * [Step 2.2: Projection](#step-22-projection)
  * [Step 2.3: Simplification](#step-23-simplification)
  * [Step 2.4: Exporting](#step-24-exporting)

## Step 1: Download your map from GADM
Vist https://gadm.org. Select "Data", "country", your desired country from the dropdown menu, and "Shapefile". Unzip the Shapefile into your preferred directory.

## Step 2: Process your map in QGIS
You will now process your map in QGIS.

### Step 2.1: Importing
Open QGIS and in the main toolbar, select `Project` > `Open...`, navigate to the directory containing the Shapefiles, and open the `.shp` file.

### Step 2.2: Projection
Note: Be sure to have the GRASS plugin shown on QGIS. To show it, go to Plugins > Manage and install plugins, and tick the box that says GRASS 7

First, we need to create a mapset to process the world map. 
Go to Plugins > GRASS > New mapset, and follow the steps provided. 

On the window titled "GRASS Database", simply decide where to store your map data
On the window titled "GRASS Location", create a new location called "World"
On the window titled "Projection", locate and select the coordinate reference system WGS 84, which can be found by typing "4326" in the filter box
On the window titled "Default GRASS region", enter the extent coordinates as North: 90, South: -90, East: 180, West: -180
On the window titled "Mapset", name your mapset

Once you are done creating your mapeset, go to Plugins > GRASS > Open mapset, and select the mapset that you created. A red bounding box should display.
Finally, open your map in QGIS by dragging the GeoJSON file into the QGIS work space. It should display within the bounds of the red bounding box

Now, we must load the data into the GRASS mapset

In the third toolbox row in QGIS, click the first icon of tools and grass. This opens the GRASS toolbox.
In the modules tab, search for v.in.ogr.qgis.
In the v.in.ogr.qgis tab, select the layer that you have just loaded into QGIS and name your output vector map. 
Once you are done, click "Run", and once it is finished click "View output". A new layer should appear under "Layers"

### Step 2.3: Simplification
Now that we have the world map in QGIS, we can begin simplification. 

### Step 2.4: Exporting
Under your `Layers` panel, right-click on your final layer, `Export` > `Save As...`.
