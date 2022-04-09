## Overview

auto_run_wrf is a toolkit for running WRF automatically. The package consists mainly of

- Create and plot WRF domain. The simulation area is located in the centre
- Move WRF files to the target directory
- Simplifying the writing of namelist
- auto-run WPS and WRF
- The file for download the FNL data and ERA data for WRF

### Method of running

1. Downloading FNL or ERA data using scripts in the download_data folder

2. Edit the **config.py**. Set the study area, time, directory and so on

3. Edit the **namelist.input.T** and set  the parameterisation scheme

4. Run WPS  and specify the data type(FNL or ERA)

   ```python
   python auto_wps.py fnl
   ```

5. Run wrf and specify the mpirun number(real.exe will be one process)

    ```python
    python auto_wrf.py mpinum  
    ```

6. If the WRF runs with an error, please check rsl.error file

### More information

1. This script calculates the starting point of the grid and the number of grids in each domain based on the distance of each  domain and the parent_grid_ratio of each domain. If set **AUTO=True** in **config.py**. The scripts will calculate the I_PARENT_START,J_PARENT_START,E_WE,E_SN,TIME_STEP automatically. The TIME_STEP  is 6 times of the dx.
2. [How to use the CDS API](https://cds.climate.copernicus.eu/api-how-to#install-the-cds-api-key)
3. [FNL data download](https://rda.ucar.edu/datasets/ds083.2/#!description)