# Tte | fits4

观测期间每轨一个``fits``文件，记录每一个粒子入射事件，分别为``UTC+0``时间、能量、ADC Value值  
命名规则:``yymmddmmss_yymmddmmss.fits``，分别代表每一轨的起始时间与终止时间

### 单元列表

| No. |   Name  | Ver |     Type    | Cards | Dimensions |  Format   |
|:---:|:-------:|:---:|:-----------:|:-----:|:----------:|:---------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |     ()     |           |
|  1  |   T_E0  |  1  | BinTableHDU |   18  |   NR x 6C  | [D, D, J] |
|  2  |   T_E1  |  1  | BinTableHDU |   18  |   NR x 6C  | [D, D, J] |
|  3  |   T_E2  |  1  | BinTableHDU |   18  |   NR x 6C  | [D, D, J] |
|  4  |   T_E3  |  1  | BinTableHDU |   18  |   NR x 6C  | [D, D, J] |

### 主头文件

|  字段  | 值 |            说明            |
|:------:|:--:|:--------------------------:|
| SIMPLE | T  | conforms to FITS standard  |
| BITPIX | 8  | array data type            |
| NAXIS  | 0  | number of array dimensions |
| EXTEND | T  |                            |

### 扩展单元T_E头文件

|   字段   |     值    |            说明            |
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

### 字段说明

|    字段   |      含义      |    说明    |
|:---------:|:--------------:|:----------:|
|     t     |  入射事件时间  |            |
|     E     |  入射粒子能量  |            |
|   adcv    |   ADC value   |            |