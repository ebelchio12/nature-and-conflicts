## Joining gridded geospatial data with country-specific data
The gridded data is obtained from [the CRU TS dataset](https://crudata.uea.ac.uk/cru/data/hrg/). Other helper datasets are obtained from different sources, as detailed in the [Jupyter notebook](rainfall.ipynb).

### Setting up environment to run the notebook
The following sets up a conda environment that allows for running the Jupyter notebook
```
conda env create -f environment.yml
```

The helper scripts have unit tests implemented in [tests](tests). To run the tests after creating the conda environment:
```
conda activate nature-and-conflicts-irem
cd tests
python -m pytest
```

### Helper scripts

The following helper scripts allow for parsing information from different sources more easily.
- `grid_data.py` defines a base class `GridData` to deal with gridded datasets from CRU TS. Two variations of this exist to deal with the rainfall (`Rainfall`) and surface temperature (`SurfaceTemperature`) data.
- `csv_fetcher.py` makes it easier to fetch a `csv` file from a URL and return as a `pandas` data frame.
- `missing_value_handler.py` contains functions to create rows for countries with years missing in datasets, and to fill missing values based on a defined strategy.
- `world.py` contains the class `World` that allows for looking up country names from geographical coordinates.
- `utils.py` contains very simple array-based functions to make data processing easier.