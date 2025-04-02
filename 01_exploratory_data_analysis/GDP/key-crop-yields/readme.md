# Crop yields - Data package

This data package contains the data that powers the chart ["Crop yields"](https://ourworldindata.org/grapher/key-crop-yields?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The remaining columns are the data columns, each of which is a time series. If the CSV data is downloaded using the "full data" option, then each column corresponds to one time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data columns are transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

### How we process data at Our World In Data
All data and visualizations on Our World in Data rely on data sourced from one or several original data providers. Preparing this original data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/)

## Detailed information about each time series


## Wheat yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Wheat yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Wheat
Description: Wheat

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


## Rice yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Rice yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Rice
Description: Rice

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


## Banana yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Banana yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Bananas
Description: Bananas This subclass includes: - sweet/dessert bananas, Musa sapientum, M. cavendishii, M. nana, i.e. bananas that can be eaten without further preparation This subclass does not include: -  plantains, cooking bananas, Musa paradisiaca, cf. 01313

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


## Maize yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Maize yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Maize
Description: Maize (corn) This class includes: -  maize harvested for their dry grains only

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


## Soybean yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Soybean yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Soybeans
Description: Soya beans

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


## Potato yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Potato yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Potatoes
Description: Potatoes This subclass is defined through the following headings/subheadings of the HS 2007: 0701.

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


## Bean yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Bean yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Beans, dry
Description: Beans, dry This subclass includes: -  beans, species of Phaseolus (vulgaris, lunatus, angularis, aureus, etc.) -  beans, species of Vigna (angularis, mungo, radiata, unguiculata, etc.) This subclass does not include: - soya beans, cf. 0141 - green beans, cf. 01241 - lentils, green, cf. 01249 -  bean shoots and sprouts, cf. 01290 - locust beans (carobs), cf. 01356 - castor beans, cf. 01449 -  broad beans and horse beans, dry, cf. 01702 - garbanzo beans (chickpeas), dry, cf. 01703 - lentils, dry, cf. 01704

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


## Pea yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Pea yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Peas, dry
Description: Peas, dry This subclass is defined through the following headings/subheadings of the HS 2007: 0713.10.

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


## Cassava yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Cassava yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Cassava
Description: Cassava, species of Manihot esculenta; Manihot utilissima (manioc, mandioca, yuca) and Manihot palmata; Manihot dulcis (yuca dulce), fresh, chilled, frozen, is a semi-permanent highly perishable tuberous crop grown in tropical and subtropical regions. Sometimes bitter and sweet cassavas are referred to as separate species, the former being M. esculenta and the latter M. palmata, but this is incorrect since the toxicity varies according to location. Cassava is the staple food in many tropical countries. It is not traded internationally in its fresh state because tubers deteriorate very rapidly. (Unofficial definition)

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


## Cocoa bean yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Cocoa bean yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Cocoa beans
Description: Cocoa beans This subclass is defined through the following headings/subheadings of the HS 2007: 1801.

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


## Barley yields – FAO
Last updated: March 14, 2024  
Next update: March 2025  
Date range: 1961–2022  
Unit: tonnes per hectare  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data

#### Full citation
Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World in Data. “Barley yields – FAO” [dataset]. Food and Agriculture Organization of the United Nations, “Production: Crops and livestock products” [original data].
Source: Food and Agriculture Organization of the United Nations (2023) – with major processing by Our World In Data

### What you should know about this data

### How is this data described by its producer - Food and Agriculture Organization of the United Nations (2023)?
Item: Barley
Description: Barley

Metric: Yield
Description: Harvested production per unit of harvested area for crop products. In most of the cases yield data are not recorded but obtained by dividing the production data by the data on area harvested. Data on yields of permanent crops are not as reliable as those for temporary crops either because most of the area information may correspond to planted area, as for grapes, or because of the scarcity and unreliability of the area figures reported by the countries, as for example for cocoa and coffee. Source: FAO Statistics Division

### Source

#### Food and Agriculture Organization of the United Nations – Production: Crops and livestock products
Retrieved on: 2024-03-14  
Retrieved from: http://www.fao.org/faostat/en/#data/QCL  


    