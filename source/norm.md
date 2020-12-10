# Data specification

### Stored
All files save as `fits` format (Please refer to [Category](./brief.html#category))

### Time
1. All timestamps in stored data refer to `UTC-0` time  
2. The **time origin** of Mission Elapsed Time (MET) is`2018.10.29.00:00UTC+0`

### Coordinate System
The orbit data and position of sun and earth involve two coordinate systems:   
1. det : Detector , the fixed normal direction is`[0, 0, -1]`
2. cel : Celestial, approximately considered that the detector coincides with the center of earth

### File Name
##### No Time Information
1. fits3：`Observation_plan.fits`

##### Store as `raw.dat` file
1. fits0：The file name is date in `raw.dat`, so fits0 file may be mixed with data from several days, and the file name has nothing to do with the date of the data in fits0
2. fits1：the same as fits0

##### Stored by day(UTC+0) based on the time in the data
1. fits2：The file name is `DDDDD_yymmdd`. The former is the number of days from **time origin**, the latter is date
2. fits6：the same as fits2

##### Stored by orbit start and end time(UTC+0) based on the time in the data
1. fits5：The folder name is date corresponding to orbit **start time**, the file is named by start time and end time of each orbit
2. fits4：The folder name is date corresponding to orbit **start time**, the file is named by start time and end time of monitoring data (`orb_mon5.fits`) of each orbit

### Common Keywords

| Keyword     | struct format | FITS format code | minimum format |  
| :---------- | :------------ | :--------------- | :------------- |  
| utc         | L             | J                | int32          |  
| pps         | Q             | J                | int32          |  
| usc         | Q             | K                | int64          |  
| channel     | B             | I                | int16          |  
| adc_value   | H             | J                | int32          |  
| valid_count | L             | J                | int32          |  
| lost_count  | L             | J                | int32          |  
| sipm_temp   | H             | I                | int16          |  
| adc_temp    | H             | I                | int16          |  
| vmon        | H             | I                | int16          |  
| imon        | H             | I                | int16          |  
| mcu_temp    | H             | I                | int16          |  
| position    |               | J                | int32          |  
| label       |               | I                | int16          |  
| utc_recon   |               | J                | float64        |  
| leaki       |               | D                | float64        |  
| vover       |               | D                | float64        |  
| vout        |               | D                | float64        |  
| t           |               | D                | float64        |  
| E           |               | D                | float64        |  
| ra          |               | D                | float64        |  
| dec         |               | D                | float64        |  
| xyz         |               | D                | float64        |