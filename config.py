import os
import utils


WPS_DIR = './WPS-4.2'
WPS_OUTPUT_DIR = './wps_output/'
WRF_OUTPUT_DIR = "./wrf_output/"  # Advise write absoulte path
WRF_DIR = "./WRF-4.2/run"

NAMELIST_WPS_T = "./FNLnamelist.wps.T"
NAMELIST_INPUT_T = "./namelist.input.T"
AUTO = True  # determin whether use we_distance and sn_distance to get parent_start
WE_DISTANCE = [1000, 600, 200]
SN_DISTANCE = [800, 480, 120]
#  share
MAX_DOM = 1
START_DATE = "20200101"
END_DATE = "20200102"
SIM_UTC = 00  # 00 or 12
INTERVAL_SECONDS = 21600
OPT_OUTPUT_FROM_GEOGRID_PATH = os.path.join(WPS_OUTPUT_DIR, 'geogrid/')

# geogrid
PARENT_GRID_RATIO = (1, 5, 5)
I_PARENT_START = (1, 25, 60)  # manual or auto
J_PARENT_START = (1, 21, 47)  # manual or auto

E_WE = (81, 161, 221)  # manual or auto
E_SN = (65, 121, 141)  # manual or auto
GEOG_DATA_RES = ("'10m'", "'2m'", "'30s'")
DX_WPS = 25000
DY_WPS = 25000
MAP_PROJ = 'lambert'
REF_LAT = 34.620412
REF_LON = 105.661397
TRUELAT1 = 30.0
TRUELAT2 = 60.0
STAND_LON = 105.661397
OPT_GEOGRID_TBL_PATH = os.path.join(WPS_DIR, 'geogrid')
GEOG_DATA_PATH = '/home/zhangby21/WPS_GEOG'


# ungrib
OUT_FORMAT = 'WPS'

PREFIX_SFC = os.path.join(WPS_OUTPUT_DIR, 'ungrib/SFC')  # ERA surface
PREFIX_3D = os.path.join(WPS_OUTPUT_DIR, 'ungrib/3D')  # ERA surface or fnl


ERA_SFC_filename = "./data/ERA5/20200325_20200101_sl.grib"  # ERA5 Filename for linkgrib.csh
ERA_3D_filename = "./data/ERA5/20200325_20200101_pl.grib"

FNL_filename = "./data/fnl_202001*"  # FNL Filename for linkgrib.csh

# metgrid
FG_NAME1 = PREFIX_SFC
FG_NAME2 = PREFIX_3D
OPT_OUTPUT_FROM_METGRID_PATH = os.path.join(WPS_OUTPUT_DIR, 'metgrid')
OPT_METGRID_TBL_PATH = os.path.join(WPS_DIR, 'metgrid')


IO_FORM_GEOGRID = 2
IO_FORM_METGRID = 2
WRF_CORE = "ARW"  # ARW or NMM
FULL_DATE_FMT = lambda sim_utc: f'%Y-%m-%d_{sim_utc:02d}:00:00'


# WRF namelist.input
# time_control
INPUT_FROM_FILE = ('.true.', '.true.', '.true.')
HISTORY_INTERVAL = (180, 60, 60)
FRAMES_PER_OUTFILE = (2400, 2400, 2400)
RESTART = '.false.'
RESTART_INTERVAL = 7200
IO_FORM_HISTORY = 2
IO_FORM_RESTART = 2
IO_FORM_INPUT = 2
IO_FORM_BOUNDARY = 2
DEBUG_LEVEL = 0

# domains
TIME_STEP = 180  # manual or auto 6*dx
TIME_STEP_FRACT_NUM = 0
TIME_STEP_FRACT_DEN = 1
E_VERT = (41, 41, 41)
P_TOP_REQUESTED = 5000
DX_WRF = (DX_WPS, int(DX_WPS/PARENT_GRID_RATIO[1]), int(DX_WPS/PARENT_GRID_RATIO[1]/PARENT_GRID_RATIO[2]))
DY_WRF = (DY_WPS, int(DY_WPS/PARENT_GRID_RATIO[1]), int(DY_WPS/PARENT_GRID_RATIO[1]/PARENT_GRID_RATIO[2]))
GRID_ID = (1, 2, 3)
PARENT_ID = (0, 1, 2)
PARENT_TIME_STEP_RATIO = (1, 5, 5)  # manual or auto PARENT_GRID_RATIO
FEEDBACK = 1
SMOOTH_OPTION = 0
