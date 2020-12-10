# Tte | fits4

During the observation period, a `fits` file is generated for each orbit, and each particle incident event is recorded. The recorded values are `UTC+0` timestamp, energy, ADC Value  
Naming rules : `yymmddmmss_yymmddmmss.fits`, means the orbit start and end time

### HDU LIST

| No. |   Name  | Ver |     Type    | Cards | Dimensions |  Format   |
|:---:|:-------:|:---:|:-----------:|:-----:|:----------:|:---------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |     ()     |           |
|  1  |   T_E0  |  1  | BinTableHDU |   18  |   NR x 6C  | [D, D, J] |
|  2  |   T_E1  |  1  | BinTableHDU |   18  |   NR x 6C  | [D, D, J] |
|  3  |   T_E2  |  1  | BinTableHDU |   18  |   NR x 6C  | [D, D, J] |
|  4  |   T_E3  |  1  | BinTableHDU |   18  |   NR x 6C  | [D, D, J] |

### Primary Header

|Keyword | Value |         Description        |
|:------:|:-----:|:--------------------------:|
| SIMPLE |   T   | conforms to FITS standard  |
| BITPIX |   8   | array data type            |
| NAXIS  |   0   | number of array dimensions |
| EXTEND |   T   |                            |

### Extension Header : T_E

| Keyword  |   Value   |        Description         |
|:--------:|:---------:|:--------------------------:|
| XTENSION |  BINTABLE |   binary table extension   |
|  BITPIX  |     8     |       array data type      |
|   NAXIS  |     2     | number of array dimensions |
|  NAXIS1  |     20    |    length of dimension1    |
|  NAXIS2  |      N    |    length of dimension2    |
|  PCOUNT  |     0     | number of group parameters |
|  GCOUNT  |     1     |      number of groups      |
|  TFIELDS |     3     |   number of table fields   |
|  EXTNAME |    T_E    |       extension name       |
|  TTYPE1  |     t     |                            |
|  TFORM1  |     D     |                            |
|  TUNIT1  |     s     |                            |
|  TTYPE2  |     E     |                            |
|  TFORM2  |     D     |                            |
|  TUNIT2  |    keV    |                            |
|  TTYPE3  |   adcv    |                            |
|  TFORM3  |     J     |                            |
|  TUNIT3  |     1     |                            |

### Keyword Description

| Keyword |         Significance        | Remarks |
|:-------:|:---------------------------:|:-------:|
|    t    |  time of particle incidence |         |
|    E    | energy of incident particle |         |
|   adcv  |     ADC value of energy     |         |