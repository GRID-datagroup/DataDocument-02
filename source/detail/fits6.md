# Earth | fits6

每天一个`fits`文件，每10s记录一个数据点，分别为`UTC+0`时间、星下点纬度、星下点经度、探测器高度、天球坐标系下地球的`Ra&Dec`  
命名规则:`YYYYY_yymmddearth.fits`，前者为距**时间原点**天数，后者为日期

### 单元列表

| No. |   Name  | Ver |     Type    | Cards | Dimensions |       Format       |
|:---:|:-------:|:---:|:-----------:|:-----:|:----------:|:------------------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |     ()     |                    |
|  1  |  RADEC  |  1  | BinTableHDU |   27  | 8640R x 6C | [D, D, D, D, D, D] |

### 主头文件

|  字段  | 值 |            说明            |
|:------:|:--:|:--------------------------:|
| SIMPLE | T  | conforms to FITS standard  |
| BITPIX | 8  | array data type            |
| NAXIS  | 0  | number of array dimensions |
| EXTEND | T  |                            |

### 扩展单元Ra&Dec头文件

|   字段   |     值    |            说明            |
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

### 字段说明

|    字段   |      含义      |    说明    |
|:---------:|:--------------:|:----------:|
|     t     |    UTC-0时间   |            |
|  Latitude |   星下点纬度   |            |
| Longitude |   星下点经度   |            |
|  Altitude | 探测器高度(km) |            |
|  e_Ra_cel |    地球赤经    | 天球坐标系  |
| e_Dec_cel |    地球赤纬    |            |