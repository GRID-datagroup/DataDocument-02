# Observation plan | fits3
&emsp;&emsp;观测期间总计一个`fits`文件，记录了每一轨的计划时间戳起点和终点和定姿态观测中的计划四元数姿态，在文件末尾累加。

&emsp;&emsp;命名规则:`Observation_plan.fits`。

### 单元列表

| No. |   Name  | Ver |     Type    | Cards | Dimensions |  Format   |
|:---:|:-------:|:---:|:-----------:|:-----:|:----------:|:---------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |     ()     |           |
|  1  |  TEL_MO |  1  | BinTableHDU |  27  |  NR x 6C  | [D, D, D, D, D, D] |

### 主头文件

|  字段  | 值 |            说明            |
|:------:|:--:|:--------------------------:|
| SIMPLE | T  | conforms to FITS standard  |
| BITPIX | 8  | array data type            |
| NAXIS  | 0  | number of array dimensions |
| EXTEND | T  |                            |

### 扩展单元Ra&Dec头文件

|   字段   |     值     |           说明          |
|:--------:|:----------:|:-----------------------:|
| XTENSION |  BINTABLE  |   binarytableextension  |
|  BITPIX  |      8     |      arraydatatype      |
|   NAXIS  |      2     | numberofarraydimensions |
|  NAXIS1  |     48     |    lengthofdimension1   |
|  NAXIS2  |      N     |    lengthofdimension2   |
|  PCOUNT  |      0     | numberofgroupparameters |
|  GCOUNT  |      1     |      numberofgroups     |
|  TFIELDS |     6      |   numberoftablefields   |
|  EXTNAME |    PLAN    |      extensionname      |
|  TTYPE1  |Orbit_begin_time|                     |                                                    
|  TFORM1  |    D       |                         |                                                            
|  TUNIT1  |    s       |                         |                                                            
|  TTYPE2  |Orbit_end_time|                       |                                                      
|  TFORM2  |    D       |                         |                                                            
|  TUNIT2  |    s       |                         |                                                            
|  TTYPE3  |    Q0      |                         |                                                            
|  TFORM3  |    D       |                         |                                                            
|  TUNIT3  |    V       |                         |                                                            
|  TTYPE4  |    Q1      |                         |                                                            
|  TFORM4  |    D       |                         |                                                            
|  TUNIT4  |    V       |                         |                                                            
|  TTYPE5  |    Q2      |                         |                                                            
|  TFORM5  |    D       |                         |                                                            
|  TUNIT5  |    V       |                         |                                                            
|  TTYPE6  |    Q3      |                         |                                                            
|  TFORM6  |    D       |                         |                                                            
|  TUNIT6  |    V       |                         |

### 字段说明

|        字段      |      含义     | 说明 |
|:----------------:|:-------------:|:----:|
| Orbit_begin_time | 本轨的开始时间 |      |
| Orbit_end_time   | 本轨的结束时间 |      |
|        Q0        |               | 姿态四元数 |
|        Q1        |               |      |
|        Q2        |               |      |
|        Q3        |               |      |