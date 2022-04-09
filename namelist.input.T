 &time_control
 run_days                            = 0,
 run_hours                           = 0,
 run_minutes                         = 0,
 run_seconds                         = 0,
 start_year                          = {{ start_year }}, {{ start_year }},  {{ start_year }},
 start_month                         = {{ '%02d' % start_month }}, {{ '%02d' % start_month }}, {{ '%02d' % start_month }},
 start_day                           = {{ '%02d' % start_day }}, {{ '%02d' % start_day }}, {{ '%02d' % start_day }},
 start_hour                          = {{ '%02d' % start_hour}}, {{ '%02d' % start_hour}}, {{ '%02d' % start_hour}},
 end_year                            = {{ end_year }}, {{ end_year }}, {{ end_year }},
 end_month                           = {{ '%02d' % end_month }}, {{ '%02d' % end_month }}, {{ '%02d' % end_month }},
 end_day                             = {{ '%02d' % end_day }}, {{ '%02d' % end_day }}, {{ '%02d' % end_day }},
 end_hour                            = {{ '%02d' % end_hour }}, {{ '%02d' % end_hour }}, {{ '%02d' % end_hour }},
 interval_seconds                    = {{interval_seconds}}
 input_from_file                     = {{input_from_file|join(', ')}},
 history_interval                    = {{history_interval|join(', ')}}, 
 frames_per_outfile                  = {{frames_per_outfile|join(', ')}},
 restart                             = {{restart}},
 restart_interval                    = {{restart_interval}},
 io_form_history                     = {{io_form_history}}
 io_form_restart                     = {{io_form_restart}}
 io_form_input                       = {{io_form_input}}
 io_form_boundary                    = {{io_form_boundary}}
 debug_level                         = {{debug_level}}
 /

 &domains
 time_step                           = {{time_step}},
 time_step_fract_num                 = {{time_step_fract_num}},
 time_step_fract_den                 = {{time_step_fract_den}},
 max_dom                             = {{max_dom}},
 e_we                                = {{e_we|join(', ')}},
 e_sn                                = {{e_sn|join(', ')}},
 e_vert                              = {{e_vert|join(', ')}},
 p_top_requested                     = {{p_top_requested}},
 num_metgrid_levels                  = {{num_metgrid_levels}},
 num_metgrid_soil_levels             = {{num_metgrid_soil_levels}},
 dx                                  = {{dx|join(', ')}},
 dy                                  = {{dy|join(', ')}},
 grid_id                             = {{grid_id|join(', ')}},
 parent_id                           = {{parent_id|join(', ')}},
 i_parent_start                      = {{i_parent_start|join(', ')}},
 j_parent_start                      = {{j_parent_start|join(', ')}},
 parent_grid_ratio                   = {{parent_grid_ratio|join(', ')}},
 parent_time_step_ratio              = {{parent_time_step_ratio|join(', ')}},
 feedback                            = {{feedback}},
 smooth_option                       = {{smooth_option}}
 /

 &physics
 physics_suite                       = 'CONUS'
 mp_physics                          = 2,     2,     2,
 ra_lw_physics                       = 1,     1,     1,
 ra_sw_physics                       = 1,     1,     1,
 radt                                = 25,    5,     1,
 sf_sfclay_physics                   = 1,     1,     1,
 sf_surface_physics                  = 1,     1,     1,
 bl_pbl_physics                      = 1,     1,     1,
 bldt                                = 0,     0,     0,
 cu_physics                          = 1,     1,     0,
 cudt                                = 5,     5,     5,
 isfflx                              = 1,
 ifsnow                              = 1,
 icloud                              = 1,
 surface_input_source                = 1,
 num_soil_layers                     = 5,
 num_land_cat                        = 21,
 sf_urban_physics                    = 0,     0,     0,
 /

 &fdda
 /

 &dynamics
 w_damping                           = 0,
 diff_opt                            = 1,      1,      1,
 km_opt                              = 4,      4,      4,
 diff_6th_opt                        = 0,      0,      0,
 diff_6th_factor                     = 0.12,   0.12,   0.12,
 base_temp                           = 290.
 damp_opt                            = 0,
 zdamp                               = 5000.,  5000.,  5000.,
 dampcoef                            = 0.2,    0.2,    0.2
 khdif                               = 0,      0,      0,
 kvdif                               = 0,      0,      0,
 non_hydrostatic                     = .true., .true., .true.,
 moist_adv_opt                       = 1,      1,      1,
 scalar_adv_opt                      = 1,      1,      1,
 /

 &bdy_control
 spec_bdy_width                      = 5,
 spec_zone                           = 1,
 relax_zone                          = 4,
 specified                           = .true., .false.,.false.,
 nested                              = .false., .true., .true.,
 /

 &grib2
 /

 &namelist_quilt
 nio_tasks_per_group = 0,
 nio_groups = 1,
 /

