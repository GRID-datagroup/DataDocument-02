# Orbit monitor | fits5

观测期间每轨一个``fits``文件，每秒记录一次探测器信息，分别为``UTC+0``时间、四通道偏压、四通道label、四通道SiPM温度、四通道SiPM温度adc值、四通道vmon、vout、四通道leaki、四通道imon、mcu温度、anchor  
命名规则:``yymmddmmss_yymmddmmssorb.fits``，分别代表每一轨的起始时间与终止时间

### 单元列表

| No. |   Name  | Ver |     Type    | Cards | Dimensions |  Format   |
|:---:|:-------:|:---:|:-----------:|:-----:|:----------:|:---------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |     ()     |           |
|  1  |  TEL_MO |  1  | BinTableHDU |  108  |  NR x 33C  | [K, J, D, D, D, D, I, I, I, I, D, D, D, D, I, I, I, I, D, D, D, D, D, D, D, D, D, I, I, I, I, I, I] |

### 主头文件

### 扩展单元Ra&Dec头文件

### 字段说明