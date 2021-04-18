# Telemetry | fits1
&emsp;&emsp;每个`raw.dat`对应一个`fits`文件，记录了探测器及卫星的工作状态等信息，用于清洗和筛选科学数据，是科学数据分析的基础。`raw.dat`可能混杂来自多天的数据。

&emsp;&emsp;命名规则:`telYYYYMMDD_H_unpack-YYYYMMDD-UTC_Count.fits`，文件名与`raw.dat`中日期相同，所以文件内可能混杂来自很多天的数据，而文件名与中数据归属日期无关。

### 单元列表

| No. |   Name  | Ver |     Type    | Cards | Dimensions |  Format   |
|:---:|:-------:|:---:|:-----------:|:-----:|:----------:|:---------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |     ()     |           |
|  1  | TEL_ORBIT |  1  | BinTableHDU |  15  |  2R x 2C  | [J, J] |
|  2  |  TEL_MO |  1  | BinTableHDU |  108  |  NR x 33C  | [K, J, D, D, D, D, I, I, I, I, D, D, D, D, I, I, I, I, D, D, D, D, D, D, D, D, D, I, I, I, I, I, I] |
|  3  | TEL_ORBIT_ALL |  1  | BinTableHDU |  15  |  2R x 2C  | [J, J] |
|  4  | TEL_UTC_ALL |  1  | BinTableHDU |  12  |  NR x 1C  | [D] |

### 主头文件

|  字段  | 值 |            说明            |
|:------:|:--:|:--------------------------:|
| SIMPLE | T  | conforms to FITS standard  |
| BITPIX | 8  | array data type            |
| NAXIS  | 0  | number of array dimensions |
| EXTEND | T  |                            |

### 扩展单元TEL_ORBIT头文件

|    字段   |          值         |               说明               |
|:---------:|:------------------:|:--------------------------------:|
| XTENSION  |      BINTABLE      |     binary table extension       |
|  BITPIX   |          8         |          array data type         |
|  NAXIS    |          2         |    number of array dimensions    |
|  NAXIS1   |          8         |    length of dimension 1         |
|  NAXIS2   |          2         |    length of dimension 2         |
|  PCOUNT   |          0         |    number of group parameters    |
|  GCOUNT   |          1         |          number of groups        |
|  TFIELDS  |          2         |    number of table fields        |
|  EXTNAME  |      TEL_ORBIT     |          extension name          |
|  TTYPE1   |   orbit_begin_pos  |                                  |
|  TFORM1   |          J         |                                  |
|  TUNIT1   |          s         |                                  |
|  TTYPE2   |    orbit_end_pos   |                                  |
|  TFORM2   |          J         |                                  |
|  TUNIT2   |          s         |                                  |

### 扩展单元TEL_MO头文件
&emsp;&emsp;同[fits5](/detail/fits5.html)

### 扩展单元TEL_ORBIT_ALL头文件

|   字段   |       值      |             说明             |
|:--------:|:-------------:|:----------------------------:|
| XTENSION |    BINTABLE   | binary table extension       |
|  BITPIX  |       8       |      array data type         |
|   NAXIS  |       2       | number of array dimensions   |
|  NAXIS1  |       8       |     length of dimension 1    |
|  NAXIS2  |       2       |     length of dimension 2    |
|  PCOUNT  |       0       | number of group parameters   |
|  GCOUNT  |       1       |      number of groups        |
|  TFIELDS |       2       | number of table fields       |
|  EXTNAME | TEL_ORBIT_ALL |      extension name          |
|  TTYPE1  | all_begin_pos |                              |
|  TFORM1  |       J       |                              |
|  TUNIT1  |       s       |                              |
|  TTYPE2  | all_end_pos   |                              |
|  TFORM2  |       J       |                              |
|  TUNIT2  |       s       |                              |

### 扩展单元TEL_UTC_ALL头文件

|   字段   |       值      |             说明             |
|:--------:|:-------------:|:----------------------------:|
| XTENSION |    BINTABLE   | binary table extension       |
|  BITPIX  |       8       |      array data type         |
|   NAXIS  |       2       | number of array dimensions   |
|  NAXIS1  |       8       |     length of dimension 1    |
|  NAXIS2  |       2       |     length of dimension 2    |
|  PCOUNT  |       0       | number of group parameters   |
|  GCOUNT  |       1       |      number of groups        |
|  TFIELDS |       2       | number of table fields       |
|  EXTNAME | TEL_ORBIT_ALL |      extension name          |
|  TTYPE1  | all_begin_pos |                              |
|  TFORM1  |       J       |                              |
|  TUNIT1  |       s       |                              |
|  TTYPE2  | all_end_pos   |                              |
|  TFORM2  |       J       |                              |
|  TUNIT2  |       s       |                              |

### 字段说明

|       字段      |        含义        | 说明 |
|:---------------:|:------------------:|:----:|
| orbit_begin_pos | 每一轨的起始 index |      |
|  orbit_end_pos  | 每一轨的终止 index |      |
|  all_begin_pos  |                    |      |
|   all_end_pos   |                    |      |
|     all_utc     |                    |      |