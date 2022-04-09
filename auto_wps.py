from jinja2 import Template
import sys
import os
from datetime import datetime as dt
import config as conf
import utils


data_type = sys.argv[1]
start_date, end_date, wps_share_start_date, wps_share_end_date = utils.get_date(conf.START_DATE, conf.END_DATE)
data_wps = {'wrf_core': conf.WRF_CORE,
            'start_date': wps_share_start_date,
            'max_dom': conf.MAX_DOM,
            'end_date': wps_share_end_date,
            'interval_seconds': conf.INTERVAL_SECONDS,
            'io_form_geogrid': conf.IO_FORM_GEOGRID,
            'opt_output_from_geogrid_path': conf.OPT_OUTPUT_FROM_GEOGRID_PATH,
            'parent_grid_ratio': conf.PARENT_GRID_RATIO,
            'i_parent_start': conf.I_PARENT_START,
            'j_parent_start': conf.J_PARENT_START,
            'e_we': conf.E_WE,
            'e_sn': conf.E_SN,
            'geog_data_res': conf.GEOG_DATA_RES,
            'dx': conf.DX_WPS,
            'dy': conf.DY_WPS,
            'map_proj': conf.MAP_PROJ,
            'ref_lon': conf.REF_LON,
            'ref_lat': conf.REF_LAT,
            'truelat1': conf.TRUELAT1,
            'truelat2': conf.TRUELAT2,
            'stand_lon': conf.STAND_LON,
            'geog_data_path': conf.GEOG_DATA_PATH,
            'opt_geogrid_tbl_path': conf.OPT_GEOGRID_TBL_PATH,
            'out_format': conf.OUT_FORMAT,
            'fgname1': conf.FG_NAME1,
            'io_form_metgrid': conf.IO_FORM_METGRID,
            'opt_output_from_metgrid_path': conf.OPT_OUTPUT_FROM_METGRID_PATH,
            'opt_metgrid_tbl_path': conf.OPT_METGRID_TBL_PATH
            }
if data_type == "ERA":
    data_wps["fgname2"] = conf.FG_NAME2
elif data_type == "FNL":
    data_wps = data_wps
else:
    raise ValueError("Please input ERA or FNL")
if conf.AUTO:
    i_parent_start, j_parent_start = utils.get_parent_start(conf.WE_DISTANCE, conf.SN_DISTANCE, conf.PARENT_GRID_RATIO,
                                                            conf.DX_WPS / 1000, conf.DY_WPS / 1000)
    e_we, e_sn = utils.get_e_we_sn(conf.WE_DISTANCE, conf.SN_DISTANCE, conf.PARENT_GRID_RATIO, conf.DX_WPS / 1000,
                                   conf.DY_WPS / 1000)
    data_wps["i_parent_start"] = i_parent_start
    data_wps["j_parent_start"] = j_parent_start
    data_wps["e_we"] = e_we
    data_wps["e_sn"] = e_sn
utils.save_namelist("namelist.wps", conf.NAMELIST_WPS_T, data_wps)
utils.run_geogrid_metgrid(output_dir=conf.OPT_OUTPUT_FROM_GEOGRID_PATH, command=os.path.join(conf.WPS_DIR, "geogrid.exe"))
if data_type == "ERA":
    utils.run_ungrib(conf.ERA_SFC_filename, file_data=data_wps, surface=True,
                     output_dir=os.path.join(conf.WPS_OUTPUT_DIR, 'ungrib/'))
    utils.run_ungrib(conf.ERA_3D_filename, file_data=data_wps, surface=False,
                     output_dir=os.path.join(conf.WPS_OUTPUT_DIR, 'ungrib/'))
elif data_type == "FNL":
    utils.run_ungrib(conf.FNL_filename, file_data=data_wps, data_type="FNL",
                     output_dir=os.path.join(conf.WPS_OUTPUT_DIR, 'ungrib/'))
else:
    raise ValueError("Please input ERA or FNL")
utils.run_geogrid_metgrid(output_dir=conf.OPT_OUTPUT_FROM_METGRID_PATH, command=os.path.join(conf.WPS_DIR, "metgrid.exe"))
