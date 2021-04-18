# Science | fits0
&emsp;&emsp;每个`raw.dat`对应一个`fits`文件，记录了探测器的科学观测数据，是`tte|fits4`的原始数据文件之一。`raw.dat`可能混杂来自多天的数据。

&emsp;&emsp;命名规则:`sciYYYYMMDD_H_unpack-YYYYMMDD-UTC_Count.fits`，文件名与`raw.dat`中日期相同，所以文件内可能混杂来自很多天的数据，而文件名与中数据归属日期无关。

### 单元列表

| No. |   Name  | Ver |     Type    | Cards | Dimensions |  Format   |
|:---:|:-------:|:---:|:-----------:|:-----:|:----------:|:---------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |     ()     |           |
|  1  | SCI_ORB_T |  1  | BinTableHDU |  15  |  NR x 2C  | [J, J] |
|  2  |  SCI |  1  | BinTableHDU |  108  |  NR x 3C  | [K, I, J] |
|  3  | SCI_COUNT |  1  | BinTableHDU |  15  |  NR x 2C  | [J, J] |

### 主头文件

|  字段  | 值 |            说明            |
|:------:|:--:|:--------------------------:|
| SIMPLE | T  | conforms to FITS standard  |
| BITPIX | 8  | array data type            |
| NAXIS  | 0  | number of array dimensions |
| EXTEND | T  |                            |

### 扩展单元SCI_ORB_T头文件

|   字段   |     值    |            说明            |
|:--------:|:---------:|:--------------------------:|
| XTENSION |  BINTABLE |   binary table extension   |
|  BITPIX  |     8     |       array data type      |
|   NAXIS  |     2     | number of array dimensions |
|  NAXIS1  |     8     |    length of dimension 1   |
|  NAXIS2  |     N     |    length of dimension 2   |
|  PCOUNT  |     0     | number of group parameters |
|  GCOUNT  |     1     |      number of groups      |
|  TFIELDS |     2     |   number of table fields   |
|  EXTNAME | SCI_ORB_T |       extension name       |
|  TTYPE1  |    UTC    |                            |
|  TFORM1  |     J     |                            |
|  TUNIT1  |     s     |                            |
|  TTYPE2  |    PPS    |                            |
|  TFORM2  |     J     |                            |
|  TUNIT2  |     s     |                            |

### 扩展单元SCI头文件

|   字段   |    值    |            说明            |
|:--------:|:--------:|:--------------------------:|
| XTENSION | BINTABLE |   binary table extension   |
|  BITPIX  |     8    |       array data type      |
|   NAXIS  |     2    | number of array dimensions |
|  NAXIS1  |    14    |    length of dimension 1   |
|  NAXIS2  |     N    |    length of dimension 2   |
|  PCOUNT  |     0    | number of group parameters |
|  GCOUNT  |     1    |      number of groups      |
|  TFIELDS |     3    |   number of table fields   |
|  EXTNAME |    SCI   |       extension name       |
|  TTYPE1  |  uScount |                            |
|  TFORM1  |     K    |                            |
|  TUNIT1  |     1    |                            |
|  TTYPE2  |  Channel |                            |
|  TFORM2  |     I    |                            |
|  TUNIT2  |     1    |                            |
|  TTYPE3  | ADCvalue |                            |
|  TFORM3  |     J    |                            |
|  TUNIT3  |     1    |                            |

### 扩展单元SCI_COUNT头文件

|   字段   |      值     |            说明            |
|:--------:|:-----------:|:--------------------------:|
| XTENSION |   BINTABLE  |   binary table extension   |
|  BITPIX  |      8      |       array data type      |
|   NAXIS  |      2      | number of array dimensions |
|  NAXIS1  |      8      |    length of dimension 1   |
|  NAXIS2  |      N      |    length of dimension 2   |
|  PCOUNT  |      0      | number of group parameters |
|  GCOUNT  |      1      |      number of groups      |
|  TFIELDS |      2      |   number of table fields   |
|  EXTNAME |  SCI_COUNT  |       extension name       |
|  TTYPE1  | Valid_count |                            |
|  TFORM1  |      J      |                            |
|  TUNIT1  |      1      |                            |
|  TTYPE2  |  Lost_count |                            |
|  TFORM2  |      J      |                            |
|  TUNIT2  |      1      |                            |

### 字段说明

|     字段    |       含义       |               说明               |
|:-----------:|:----------------:|:--------------------------------:|
|     UTC     |     UTC-0时间    |                                  |
|     PPS     |      秒脉冲      |         pulse per second         |
|   uScount   |     晶振计数     | count of crystal oscillator, usc |
|   Channel   |    探测器通道    |                0~3               |
|   ADCValue  |     ADC通道值    |                                  |
| Valid_count |     有效计数     |                                  |
|  Lost_count | 因错误的丢失计数 |                                  |