&share
 wrf_core = '{{wrf_core}}',
 max_dom = {{max_dom}},
 start_date = '{{start_date}}','{{start_date}}','{{start_date}}',
 end_date   = '{{end_date}}','{{end_date}}','{{end_date}}',
 interval_seconds = {{interval_seconds}},
 io_form_geogrid = {{io_form_geogrid}},
 opt_output_from_geogrid_path = '{{opt_output_from_geogrid_path}}',
/

&geogrid
 parent_id         =   1, 1, 2,  
 parent_grid_ratio =   {{parent_grid_ratio|join(', ')}},
 i_parent_start    =   {{i_parent_start|join(', ')}}, 
 j_parent_start    =   {{j_parent_start|join(', ')}},
 e_we              =   {{e_we|join(', ')}},
 e_sn              =   {{e_sn|join(', ')}}, 
 !
 !!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT NOTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!
 ! The default datasets used to produce the MAXSNOALB and ALBEDO12M
 ! fields have changed in WPS v4.0. These fields are now interpolated
 ! from MODIS-based datasets.
 !
 ! To match the output given by the default namelist.wps in WPS v3.9.1,
 ! the following setting for geog_data_res may be used:
 !
 ! geog_data_res = 'maxsnowalb_ncep+albedo_ncep+default', 'maxsnowalb_ncep+albedo_ncep+default', 
 !
 !!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT NOTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!
 !
 geog_data_res = {{geog_data_res|join(', ')|safe}},
 dx = {{dx}},
 dy = {{dy}},
 map_proj = '{{map_proj}}',
 ref_lat   =  {{ref_lat}},
 ref_lon   = {{ref_lon}},
 truelat1  =  {{truelat1}},
 truelat2  =  {{truelat2}},
 stand_lon = {{stand_lon}},
 geog_data_path = '{{geog_data_path}}',
 opt_geogrid_tbl_path = '{{opt_geogrid_tbl_path}}',
/

&ungrib
 out_format = '{{out_format}}',
 prefix = '{{prefix}}',
/

&metgrid
 fg_name = '{{fg_name1}}', '{{fg_name2}}'
 io_form_metgrid = {{io_form_metgrid}}, 
 opt_output_from_metgrid_path = '{{opt_output_from_metgrid_path}}'
 opt_metgrid_tbl_path = '{{opt_metgrid_tbl_path}}',
/

