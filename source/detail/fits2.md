# Sun | fits2

A `fits` file is generated every day. Each data point is separated by 10s. The recorded values are `UTC+0` timestamp, attitude quaternion, Cartesian coordinates and `Ra&Dec` of sun in detector coordinate system, detector pointing, Cartesian coordinates and `Ra&Dec` of sun in celestial coordinate system  
Naming rules : `YYYYY_yymmddsun.fits`. The former is the number of days from **time origin**, the latter is date

### HDU LIST

| No. |   Name  | Ver |     Type    | Cards |  Dimensions  |                            Format                            |
|:---:|:-------:|:---:|:-----------:|:-----:|:------------:|:------------------------------------------------------------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |      ()      |                                                              |
|  1  |  RADEC  |  1  | BinTableHDU |   69  | 1964R x 20C  | [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D] |

### Primary Header

|Keyword | Value |         Description        |
|:------:|:-----:|:--------------------------:|
| SIMPLE |   T   | conforms to FITS standard  |
| BITPIX |   8   | array data type            |
| NAXIS  |   0   | number of array dimensions |
| EXTEND |   T   |                            |

### Extension Header : Ra&Dec

| Keyword  |     Value   |        Description         |
|:--------:|:-----------:|:--------------------------:|
| XTENSION | BINTABLE    | binary table extension     |
| BITPIX   | 8           | array data type            |
| NAXIS    | 2           | number of array dimensions |
| NAXIS1   | 160         | length of dimension 1      |
| NAXIS2   | 1964        | length of dimension 2      |
| PCOUNT   | 0           | number of group parameters |
| GCOUNT   | 1           | number of groups           |
| TFIELDS  | 20          | number of table fields     |
| EXTNAME  |  RADEC      | extension name             |
| TTYPE1   |  t          |                            |
| TFORM1   |  D          |                            |
| TUNIT1   |  s          |                            |
| TTYPE2   |  Q0         |                            |
| TFORM2   |  D          |                            |
| TUNIT2   |  1          |                            |
| TTYPE3   |  Q1         |                            |
| TFORM3   |  D          |                            |
| TUNIT3   |  1          |                            |
| TTYPE4   |  Q2         |                            |
| TFORM4   |  D          |                            |
| TUNIT4   |  1          |                            |
| TTYPE5   |  Q3         |                            |
| TFORM5   |  D          |                            |
| TUNIT5   |  1          |                            |
| TTYPE6   |  g_X_cel    |                            |
| TFORM6   |  D          |                            |
| TUNIT6   |  1          |                            |
| TTYPE7   |  g_Y_cel    |                            |
| TFORM7   |  D          |                            |
| TUNIT7   |  1          |                            |
| TTYPE8   |  g_Z_cel    |                            |
| TFORM8   |  D          |                            |
| TUNIT8   |  1          |                            |
| TTYPE9   |  g_Ra_cel   |                            |
| TFORM9   |  D          |                            |
| TUNIT9   |  rad        |                            |
| TTYPE10  |  g_Dec_cel  |                            |
| TFORM10  |  D          |                            |
| TUNIT10  |  rad        |                            |
| TTYPE11  |  s_X_cel    |                            |
| TFORM11  |  D          |                            |
| TUNIT11  |  1          |                            |
| TTYPE12  |  s_Y_cel    |                            |
| TFORM12  |  D          |                            |
| TUNIT12  |  1          |                            |
| TTYPE13  |  s_Z_cel    |                            |
| TFORM13  |  D          |                            |
| TUNIT13  |  1          |                            |
| TTYPE14  |  s_Ra_cel   |                            |
| TFORM14  |  D          |                            |
| TUNIT14  |  rad        |                            |
| TTYPE15  |  s_Dec_cel  |                            |
| TFORM15  |  D          |                            |
| TUNIT15  |  rad        |                            |
| TTYPE16  |  s_X_det    |                            |
| TFORM16  |  D          |                            |
| TUNIT16  |  1          |                            |
| TTYPE17  |  s_Y_det    |                            |
| TFORM17  |  D          |                            |
| TUNIT17  |  1          |                            |
| TTYPE18  |  s_Z_det    |                            |
| TFORM18  |  D          |                            |
| TUNIT18  |  1          |                            |
| TTYPE19  |  s_Ra_det   |                            |
| TFORM19  |  D          |                            |
| TUNIT19  |  rad        |                            |
| TTYPE20  |  s_Dec_det  |                            |
| TFORM20  |  D          |                            |
| TUNIT20  |  rad        |                            |

### Keyword Description

|  Keyword  |             Significance             |           Remarks           |
|:---------:|:------------------------------------:|:---------------------------:|
|     t     |            UTC-0 timestamp           |                             |
|     Q0    |                  qw                  |     Attitude quaternion     |
|     Q1    |                  qx                  |                             |
|     Q2    |                  qy                  |                             |
|     Q3    |                  qz                  |                             |
|  g_X_cel  |   x coordinate of detector pointing  | Celestial coordinate system |
|  g_Y_cel  |   y coordinate of detector pointing  |                             |
|  g_Z_cel  |   z coordinate of detector pointing  |                             |
|  g_Ra_cel | Right ascension of detector pointing |                             |
| g_Dec_cel |   Declination of detector pointing   |                             |
|  s_X_cel  |          x coordinate of sun         |                             |
|  s_Y_cel  |          y coordinate of sun         |                             |
|  s_Z_cel  |          z coordinate of sun         |                             |
|  s_Ra_cel |   Right ascension coordinate of sun  |                             |
| s_Dec_cel |     Declination coordinate of sun    |                             |
|  s_X_det  |          x coordinate of sun         |  Detector coordinate system |
|  s_Y_det  |          y coordinate of sun         |                             |
|  s_Z_det  |          z coordinate of sun         |                             |
|  s_Ra_det |   Right ascension coordinate of sun  |                             |
| s_Dec_det |     Declination coordinate of sun    |                             |