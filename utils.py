from jinja2 import Template
import sys
import os
from datetime import datetime as dt
import config as conf
import numpy as np
from salem.utils import get_demo_file
from salem import geogrid_simulator


def render_template(template_file: str, data: dict) -> str:
    print('rendering template ', template_file)

    with open(template_file, 'r') as tf:
        template = Template(tf.read())
        return template.render(data)


def get_grib_file(dir_path):
    files = []
    for file in os.listdir(dir_path):
        files.append(file)
    return files


def get_date(start_date: str, end_date: str):
    """

    :param start_date:
    :param end_date:
    :return:
    """
    start_date = dt.strptime(start_date, '%Y%m%d')
    end_date = dt.strptime(end_date, '%Y%m%d')
    wps_share_start_date = start_date.strftime(conf.FULL_DATE_FMT(conf.SIM_UTC))
    wps_share_end_date = end_date.strftime(conf.FULL_DATE_FMT(conf.SIM_UTC))
    return start_date, end_date, wps_share_start_date, wps_share_end_date


def save_namelist(file_name: str, T_file: str, data: dict) -> int:
    """
    :param file_name: the file that you want to save
    :param file_name: T文_file
    :param data: the content
    :return:
    """
    with open(file_name, 'w') as wf:
        wf.write(render_template(T_file, data))
        return 0


def make_dir(dir_path):
    """
    make directory
    Parameters
    ----------
    dir_path the directory to make

    Returns
    -------

    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def run_command(command):
    """
    The function of running linux command
    Parameters
    ----------
    command

    Returns
    -------

    """
    flag = os.system(command)
    if flag != 0:
        print("{} Raise Error".format(command))
        quit()


def get_command_output(command):
    """

    Parameters
    ----------
    command the command of linux

    Returns the output of this command
    -------

    """
    run_command(command)  # wheter the command can operate
    return os.popen(command).read().strip()


def run_geogrid_metgrid(output_dir, command):
    """

    :param output_dir: output data path for geogrid or metgrid
    :return:
    """
    if "geogrid.exe" in command:
        make_dir(output_dir)
        run_command(command)
        print("geogrig well down")
    elif "metgrid.exe" in command:
        make_dir(output_dir)
        run_command(command)
        print("metgrid well down")
    else:
        raise ValueError("Please input correct command")


def run_ungrib(file_name, output_dir, file_data, surface=True, data_type="ERA"):
    """

    :param file_name:the ERA file
    :param output_dir: output data path for ungrib
    :param surface: True for surface, False for height
    note fgname higher data is former than surface data eg:fg_name = '../wps_data/ungrib/3D', '../wps_data/ungrib/SFC'
    if fg_name = '../wps_data/ungrib/SFC', '../wps_data/ungrib/3D' will raise error
    :return:
    """
    make_dir(output_dir)
    if data_type == "ERA":
        if surface:
            file_data.update({"prefix": conf.PREFIX_SFC, "fg_name2": conf.PREFIX_SFC})
            save_namelist("namelist.wps", conf.NAMELIST_WPS_T, file_data)
            run_command("ln -sf {} Vtable".format(os.path.join(conf.WPS_DIR, "ungrib/Variable_Tables/Vtable.ERA-interim.ml")))  # link Pressure Vtable
            run_command("{}".format(os.path.join(conf.WPS_DIR, "link_grib.csh ")) + file_name)
            run_command(os.path.join(conf.WPS_DIR, "ungrib.exe"))
            run_command("rm -rf ./GRIBFILE*")
            print("ungrib for surface well down")
        else:
            file_data.update({"prefix": conf.PREFIX_3D, "fg_name1": conf.PREFIX_3D})
            save_namelist("namelist.wps", conf.NAMELIST_WPS_T, file_data)
            run_command("ln -sf {} Vtable".format(os.path.join(conf.WPS_DIR, "ungrib/Variable_Tables/Vtable.ERA-interim.pl")))  # link Surface Vtable
            run_command("{}".format(os.path.join(conf.WPS_DIR, "link_grib.csh ")) + file_name)
            run_command(os.path.join(conf.WPS_DIR, "ungrib.exe"))
            run_command("rm -rf ./GRIBFILE*")
            print("ungrib for higher well down")
    else:
        file_data.update({"prefix": conf.PREFIX_3D, "fg_name1": conf.PREFIX_3D})
        save_namelist("namelist.wps", conf.NAMELIST_WPS_T, file_data)
        run_command("ln -sf {} ./Vtable".format(os.path.join(conf.WPS_DIR, "ungrib/Variable_Tables/Vtable.GFS")))  # link GFS Vtable
        run_command("{}".format(os.path.join(conf.WPS_DIR, "link_grib.csh ")) + file_name)
        run_command(os.path.join(conf.WPS_DIR, "ungrib.exe"))
        run_command("rm -rf ./GRIBFILE*")
        print("ungrib for fnl data well down")


def move_wrf_file(output_dir):
    """
    moving wrf output to the specify folder
    Parameters
    ----------
    output_dir

    Returns
    -------

    """
    make_dir(output_dir)
    run_command("mv wrfb* {}.".format(output_dir))  # mv wrfb* ../wrf_output/.
    run_command("mv wrfi* {}.".format(output_dir))
    run_command("mv wrfo* {}.".format(output_dir))
    run_command("mv rsl* {}.".format(output_dir))
    run_command("rm -rf met*")


def get_parent_start(we_distance, sn_distance, parent_grid_ratio, dx, dy):
    """

    Parameters
    ----------
    we_distance the distance of the west-east
    sn_distance the distance of the south-north
    parent_grid_ratio the ratio of the inner grid and outer grid
    dx the x distance of outer grid
    dy the y distance of outer grid

    Returns the i_parent_start, j_parent_start of namelist
    -------

    """
    i_parent_start = [1]
    j_parent_start = [1]
    for k in range(len(sn_distance) - 1):
        # wrf grid points start counting at 1, so 1 needs to be added
        i_parent_start.append(np.floor(
            we_distance[k] * ((we_distance[k] - we_distance[k + 1]) / (2 * we_distance[k])) / (
                    dx / np.prod(parent_grid_ratio[:k + 1]))).astype(int) + 1)
        j_parent_start.append(np.floor(
            sn_distance[k] * ((sn_distance[k] - sn_distance[k + 1]) / (2 * sn_distance[k])) / (
                    dy / np.prod(parent_grid_ratio[:k + 1]))).astype(int) + 1)
    return i_parent_start, j_parent_start


def get_e_we_sn(we_distance, sn_distance, parent_grid_ratio, dx, dy):
    """

    Parameters
    ----------
    we_distance the distance of the west-east
    sn_distance the distance of the south-north
    parent_grid_ratio the ratio of the inner grid and outer grid
    dx the x distance of outer grid
    dy the y distance of outer grid

    Returns the grid number of each domain
    -------

    """
    e_we = [np.ceil(we_distance[0] / dx).astype(int)]
    e_sn = [np.ceil(sn_distance[0] / dy).astype(int)]
    for k in range(len(we_distance) - 1):
        x = np.ceil(we_distance[k + 1] / (dx / np.prod(parent_grid_ratio[:k + 2])))
        e_we.append(
            [y + 1 for y in [x, x + 1, x + 2, x + 3, x + 4] if y % parent_grid_ratio[k + 1] == 0][0].astype(int))
        x = np.ceil(sn_distance[k + 1] / (dx / np.prod(parent_grid_ratio[:k + 2])))
        e_sn.append(
            [y + 1 for y in [x, x + 1, x + 2, x + 3, x + 4] if y % parent_grid_ratio[k + 1] == 0][0].astype(int))
    return e_we, e_sn


def plot_wrf_domain(namelist_wps_file="namelist.wps", title='Domains 1 to 3', output="./wrf_domain.png"):
    """
    This function to plot the wrf domain
    Parameters
    ----------
    namelist_wps_file
    title
    output

    Returns
    -------

    """
    g, maps = geogrid_simulator(namelist_wps_file)
    maps[0].set_rgb(natural_earth='lr')
    maps[0].visualize(title=title)
    plt.savefig(output)

