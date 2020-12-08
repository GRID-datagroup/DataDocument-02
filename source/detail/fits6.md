# Earth | fits6

每天一个``fits``文件，每10s记录一个数据点，分别为``UTC+0``时间、星下点纬度、星下点经度、探测器高度、天球坐标系下地球的`Ra&Dec`  
命名规则:``YYYYY_yymmddearth.fits``，前者为距**时间原点**天数，后者为日期

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

### 字段说明
