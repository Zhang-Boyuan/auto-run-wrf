import cdsapi


start_date = ["20200101"]
end_date = ["20200102"]


c = cdsapi.Client()


for i, j in zip(start_date, end_date):
    c.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'product_type': 'reanalysis',
            'format': 'grib',
            'variable':[
                'geopotential', 'relative_humidity', 'specific_humidity',
                'temperature', 'u_component_of_wind', 'v_component_of_wind'
            ],


            'date': "{}/{}".format(i, j),
            'area': [
                45, 70, 18,
                128,
            ],
            'pressure_level': [
                '1', '2', '3',
                '5', '7', '10',
                '20', '30', '50',
                '70', '100', '125',
                '150', '175', '200',
                '225', '250', '300',
                '350', '400', '450',
                '500', '550', '600',
                '650', '700', '750',
                '775', '800', '825',
                '850', '875', '900',
                '925', '950', '975',
                '1000',
            ],


            'time': [
                '00:00', '03:00', '06:00',
                '09:00', '12:00', '15:00',
                '18:00', '21:00',
            ],
        },
        i+"_" +j+"_pl.grib")


for i, j in zip(start_date, end_date):
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'grib',
            'variable': [
                '10m_u_component_of_wind','10m_v_component_of_wind','2m_dewpoint_temperature',
                '2m_temperature','land_sea_mask','mean_sea_level_pressure',
                'sea_ice_cover','orography','sea_surface_temperature','skin_temperature',
                'snow_depth','snow_density','soil_temperature_level_1','soil_temperature_level_2',
                'soil_temperature_level_3','soil_temperature_level_4','surface_pressure',
                'volumetric_soil_water_layer_1','volumetric_soil_water_layer_2','volumetric_soil_water_layer_3',
                'volumetric_soil_water_layer_4'
            ],
            'date':  "{}/{}".format(i, j),
            'area': [
                45, 70, 18,
                128,
            ],


            'time': [
                '00:00', '03:00', '06:00',
                '09:00', '12:00', '15:00',
                '18:00', '21:00',
            ],
        },
        i+"_" +j+"_sl.grib")