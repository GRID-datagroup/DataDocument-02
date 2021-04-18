# 数据规范

### 存储
&emsp;&emsp;文件按照[目录结构](./brief.html#id2)存储，全部为fits格式

### 时间
1. 存储的数据中的**所有**时间均为`UTC+0`
2. Mission Elapsed Time(MET)的**时间原点**为`2018.10.29.00:00UTC+0`

### 坐标系
&emsp;&emsp;轨道数据和日地位置涉及两个参考系：  
1. det : 探测器坐标系，固定法向为`[0, 0, -1]`
2. cel : 天球坐标系，近似认为探测器与地心重合

### 文件命名
##### 无时间信息
1. fits3：命名为`Observation_plan.fits`

##### 按照`raw.dat`文件存储
1. fits0：文件名与`raw.dat`中日期相同，所以fits0文件内可能混杂来自很多天的数据，而文件名与fits0中数据归属日期无关
2. fits1：同fits0

##### 基于数据中的时间按天(UTC+0)存储
1. fits2：文件名为`DDDDD_yymmdd`，前者为距**时间原点**天数，后者为日期
2. fits6：同fits2

##### 基于数据中的时间按轨(UTC+0)存储
1. fits5：文件夹名为该轨**起始时间**对应的日期，文件以每一轨的起始时间与终止时间命名
2. fits4：文件夹名为该轨**起始时间**对应的日期，文件以每一轨监测数据`orb_mon5.fits`的起始时间与终止时间命名

### 常用字段

| 字段        | struct format | FITS format code | minimum format |  
| :---------- | :------------ | :--------------- | :------------- |  
| utc         | L             | J                | int32          |  
| pps         | Q             | J                | int32          |  
| usc         | Q             | K                | int64          |  
| channel     | B             | I                | int16          |  
| adc_value   | H             | J                | int32          |  
| valid_count | L             | J                | int32          |  
| lost_count  | L             | J                | int32          |  
| sipm_temp   | H             | I                | int16          |  
| adc_temp    | H             | I                | int16          |  
| vmon        | H             | I                | int16          |  
| imon        | H             | I                | int16          |  
| mcu_temp    | H             | I                | int16          |  
| position    |               | J                | int32          |  
| label       |               | I                | int16          |  
| utc_recon   |               | J                | float64        |  
| iop         |               | D                | float64        |
| vop         |               | D                | float64        |
| vout        |               | D                | float64        |  
| t           |               | D                | float64        |  
| E           |               | D                | float64        |  
| ra          |               | D                | float64        |  
| dec         |               | D                | float64        |  
| xyz         |               | D                | float64        |