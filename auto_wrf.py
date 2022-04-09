from jinja2 import Template
import sys
import os
from datetime import datetime as dt
import config as conf
import utils


mpinum = sys.argv[1]
start_date, end_date, wps_share_start_date, wps_share_end_date = utils.get_date(conf.START_DATE, conf.END_DATE)

data_wrf = {'start_year': start_date.year,
            'start_month': start_date.month,
            'start_day': start_date.day,
            'start_hour': conf.SIM_UTC,
            'end_year': end_date.year,
            'end_month': end_date.month,
            'end_day': end_date.day,
            'end_hour': conf.SIM_UTC,
            'interval_seconds': conf.INTERVAL_SECONDS,
            'input_from_file': conf.INPUT_FROM_FILE,
            'history_interval': conf.HISTORY_INTERVAL,
            'frames_per_outfile': conf.FRAMES_PER_OUTFILE,
            'restart': conf.RESTART,
            'restart_interval': conf.RESTART_INTERVAL,
            'io_form_history': conf.IO_FORM_HISTORY,
            'io_form_restart': conf.IO_FORM_RESTART,
            'io_form_input': conf.IO_FORM_INPUT,
            'io_form_boundary': conf.IO_FORM_BOUNDARY,
            'debug_level': conf.DEBUG_LEVEL,
            'time_step': conf.TIME_STEP,
            'time_step_fract_num': conf.TIME_STEP_FRACT_NUM,
            'time_step_fract_den': conf.TIME_STEP_FRACT_DEN,
            'max_dom': conf.MAX_DOM,
            'e_we': conf.E_WE,
            'e_sn': conf.E_SN,
            'e_vert': conf.E_VERT,
            'p_top_requested': conf.P_TOP_REQUESTED,
            'dx': conf.DX_WRF,
            'dy': conf.DY_WRF,
            'grid_id': conf.GRID_ID,
            'parent_id': conf.PARENT_ID,
            'i_parent_start': conf.I_PARENT_START,
            'j_parent_start': conf.J_PARENT_START,
            'parent_grid_ratio': conf.PARENT_GRID_RATIO,
            'parent_time_step_ratio': conf.PARENT_TIME_STEP_RATIO,
            'feedback': conf.FEEDBACK,
            'smooth_option': conf.SMOOTH_OPTION,
            }

if conf.AUTO:
    i_parent_start, j_parent_start = utils.get_parent_start(conf.WE_DISTANCE, conf.SN_DISTANCE, conf.PARENT_GRID_RATIO,
                                                            conf.DX_WPS / 1000, conf.DY_WPS / 1000)
    e_we, e_sn = utils.get_e_we_sn(conf.WE_DISTANCE, conf.SN_DISTANCE, conf.PARENT_GRID_RATIO, conf.DX_WPS / 1000,
                                   conf.DY_WPS / 1000)
    data_wrf["i_parent_start"] = i_parent_start
    data_wrf["j_parent_start"] = j_parent_start
    data_wrf["e_we"] = e_we
    data_wrf["e_sn"] = e_sn
    data_wrf["time_step"] = int(6*conf.DX_WPS / 1000)
    data_wrf["parent_time_step_ratio"] = conf.PARENT_GRID_RATIO
file_name = os.path.join(conf.OPT_OUTPUT_FROM_METGRID_PATH,
                         "met_em.d{:0>2d}.{}.nc".format(conf.MAX_DOM, wps_share_start_date))
num_metgrid_levels = utils.get_command_output(
    """ncdump -h {} | grep -i NUM_METGRID_LEVELS |grep -o '[0-9]*'""".format(file_name))
num_metgrid_soil_levels = utils.get_command_output(
    """ncdump -h {} | grep -i NUM_METGRID_SOIL_LEVELS |grep -o '[0-9]*'""".format(file_name))
data_wrf.update({"num_metgrid_levels": num_metgrid_levels, "num_metgrid_soil_levels": num_metgrid_soil_levels})
# enter WRF directory
utils.save_namelist("namelist.input", conf.NAMELIST_INPUT_T, data_wrf)
utils.run_command("mv namelist.input {}".format(conf.WRF_DIR + "/."))

utils.run_command("cp {} {}".format(os.path.join(conf.OPT_OUTPUT_FROM_METGRID_PATH, "*.nc"), os.path.join(conf.WRF_DIR, ".")))
os.chdir(conf.WRF_DIR)

utils.run_command(command="./real.exe")
utils.run_command(command="mpirun -np {} ./wrf.exe".format(mpinum))
utils.move_wrf_file(output_dir=conf.WRF_OUTPUT_DIR)
