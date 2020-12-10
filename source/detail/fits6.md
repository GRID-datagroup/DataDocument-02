# Earth | fits6

A `fits` file is generated every day. Each data point is separated by 10s. The recorded values are `UTC+0` timestamp, latitude and longitude  of subsatellite point, altitude of detector, `Ra&Dec` of earth in celestial coordinate system  
Naming rules : `YYYYY_yymmddearth.fits`. The former is the number of days from **time origin**, the latter is date

### HDU LIST

| No. |   Name  | Ver |     Type    | Cards | Dimensions |       Format       |
|:---:|:-------:|:---:|:-----------:|:-----:|:----------:|:------------------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |     ()     |                    |
|  1  |  RADEC  |  1  | BinTableHDU |   27  | 8640R x 6C | [D, D, D, D, D, D] |

### Primary Header

|Keyword | Value |         Description        |
|:------:|:-----:|:--------------------------:|
| SIMPLE |   T   | conforms to FITS standard  |
| BITPIX |   8   | array data type            |
| NAXIS  |   0   | number of array dimensions |
| EXTEND |   T   |                            |

### Extension Header : Ra&Dec

| Keyword  |   Value   |         Description        |
|:--------:|:---------:|:--------------------------:|
| XTENSION |  BINTABLE |   binary table extension   |
|  BITPIX  |     8     |       array data type      |
|   NAXIS  |     2     | number of array dimensions |
|  NAXIS1  |     48    |    length of dimension1    |
|  NAXIS2  |    8640   |    length of dimension2    |
|  PCOUNT  |     0     | number of group parameters |
|  GCOUNT  |     1     |      number of groups      |
|  TFIELDS |     6     |   number of table fields   |
|  EXTNAME |   RADEC   |       extension name       |
|  TTYPE1  |     t     |                            |
|  TFORM1  |     D     |                            |
|  TUNIT1  |     s     |                            |
|  TTYPE2  |  Latitude |                            |
|  TFORM2  |     D     |                            |
|  TUNIT2  |    deg    |                            |
|  TTYPE3  | Longitude |                            |
|  TFORM3  |     D     |                            |
|  TUNIT3  |    deg    |                            |
|  TTYPE4  |  Altitude |                            |
|  TFORM4  |     D     |                            |
|  TUNIT4  |     km    |                            |
|  TTYPE5  |  e_Ra_cel |                            |
|  TFORM5  |     D     |                            |
|  TUNIT5  |    deg    |                            |
|  TTYPE6  | e_Dec_cel |                            |
|  TFORM6  |     D     |                            |
|  TUNIT6  |    deg    |                            |

### Keyword Description

|  Keyword  |            Significance           |           Remarks           |
|:---------:|:---------------------------------:|:---------------------------:|
|     t     |          UTC-0 timestamp          |                             |
|  Latitude |              Latitude             |      subsatellite point     |
| Longitude |             Longitude             |                             |
|  Altitude |              Altitude             |    Detector or Satellite    |
|  e_Ra_cel | Right ascension coordinate of sun | Celestial coordinate system |
| e_Dec_cel |   Declination coordinate of sun   |                             |