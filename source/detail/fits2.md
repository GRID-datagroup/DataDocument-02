# Sun | fits2

每天一个`fits`文件，每10s记录一个数据点，分别为`UTC+0`时间、姿态四元数、探测器坐标系下太阳的笛卡尔坐标以及`Ra&Dec`、天球坐标系下的探测器指向和太阳的笛卡尔坐标以及`Ra&Dec`  
命名规则:`YYYYY_yymmddsun.fits`，前者为距**时间原点**天数，后者为日期

### 单元列表

| No. |   Name  | Ver |     Type    | Cards |  Dimensions  |                            Format                            |
|:---:|:-------:|:---:|:-----------:|:-----:|:------------:|:------------------------------------------------------------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |      ()      |                                                              |
|  1  |  RADEC  |  1  | BinTableHDU |   69  |   NR x 20C   | [D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D] |

### 主头文件


|  字段  | 值 |            说明            |
|:------:|:--:|:--------------------------:|
| SIMPLE | T  | conforms to FITS standard  |
| BITPIX | 8  | array data type            |
| NAXIS  | 0  | number of array dimensions |
| EXTEND | T  |                            |

### 扩展单元Ra&Dec头文件

|   字段   |      值     |            说明            |
|:--------:|:-----------:|:--------------------------:|
| XTENSION | BINTABLE    | binary table extension     |
| BITPIX   | 8           | array data type            |
| NAXIS    | 2           | number of array dimensions |
| NAXIS1   | 160         | length of dimension 1      |
| NAXIS2   | N           | length of dimension 2      |
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

### 字段说明

|    字段   |       含义     |     备注      |
|:---------:|:--------------:|:------------:|
|     t     |    UTC-0时间   |              |
|     Q0    |        qw      |  姿态四元数   |
|     Q1    |        qx      |              |
|     Q2    |        qy      |              |
|     Q3    |        qz      |              |
|  g_X_cel  | 探测器指向x坐标 |  天球坐标系   |
|  g_Y_cel  | 探测器指向y坐标 |              |
|  g_Z_cel  | 探测器指向z坐标 |              |
|  g_Ra_cel |  探测器指向赤经 |              |
| g_Dec_cel |  探测器指向赤纬 |              |
|  s_X_cel  |    太阳x坐标    |              |
|  s_Y_cel  |    太阳y坐标    |              |
|  s_Z_cel  |    太阳z坐标    |              |
|  s_Ra_cel |     太阳赤经    |              |
| s_Dec_cel |     太阳赤纬    |              |
|  s_X_det  |    太阳x坐标    | 探测器坐标系  |
|  s_Y_det  |    太阳y坐标    |              |
|  s_Z_det  |    太阳z坐标    |              |
|  s_Ra_det |     太阳赤经    |              |
| s_Dec_det |     太阳赤纬    |              |