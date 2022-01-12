# Orbit monitor | fits5

During the observation period, a `fits` file is generated for each orbit. Each data point is separated by 1s. The recorded values are `UTC+0` timestamp, four-channel bias voltage(vop), four-channel label, four-channel temperature of SiPM , adc value of four-channel temperature , four-channel vmon, vout, four-channel iop, four-channel imon, temperature of mcu, anchor  
Naming rules : `yymmddmmss_yymmddmmss.fitsorb`, means the orbit start and end time

### HDU LIST

| No. |   Name  | Ver |     Type    | Cards | Dimensions |  Format   |
|:---:|:-------:|:---:|:-----------:|:-----:|:----------:|:---------:|
|  0  | PRIMARY |  1  |  PrimaryHDU |   4   |     ()     |           |
|  1  |  TEL_MO |  1  | BinTableHDU |  108  |  NR x 33C  | [K, J, D, D, D, D, I, I, I, I, D, D, D, D, I, I, I, I, D, D, D, D, D, D, D, D, D, I, I, I, I, I, I] |

### Primary Header

|Keyword | Value |         Description        |
|:------:|:-----:|:--------------------------:|
| SIMPLE |   T   | conforms to FITS standard  |
| BITPIX |   8   | array data type            |
| NAXIS  |   0   | number of array dimensions |
| EXTEND |   T   |                            |

### Extension Header : TEL_MO

| Keyword  |   Value    |       Description       |
|:--------:|:----------:|:-----------------------:|
| XTENSION |  BINTABLE  |   binarytableextension  |
|  BITPIX  |      8     |      arraydatatype      |
|   NAXIS  |      2     | numberofarraydimensions |
|  NAXIS1  |     176    |    lengthofdimension1   |
|  NAXIS2  |      N     |    lengthofdimension2   |
|  PCOUNT  |      0     | numberofgroupparameters |
|  GCOUNT  |      1     |      numberofgroups     |
|  TFIELDS |     33     |   numberoftablefields   |
|  EXTNAME |   TEL_MO   |      extensionname      |
|  TTYPE1  |  usc_recon |                         |
|  TFORM1  |      K     |                         |
|  TUNIT1  |      1     |                         |
|  TTYPE2  |  utc_recon |                         |
|  TFORM2  |      J     |                         |
|  TUNIT2  |      s     |                         |
|  TTYPE3  |    vop0    |                         |
|  TFORM3  |      D     |                         |
|  TUNIT3  |      V     |                         |
|  TTYPE4  |    vop1    |                         |
|  TFORM4  |      D     |                         |
|  TUNIT4  |      V     |                         |
|  TTYPE5  |    vop2    |                         |
|  TFORM5  |      D     |                         |
|  TUNIT5  |      V     |                         |
|  TTYPE6  |    vop3    |                         |
|  TFORM6  |      D     |                         |
|  TUNIT6  |      V     |                         |
|  TTYPE7  |   label0   |                         |
|  TFORM7  |      I     |                         |
|  TUNIT7  |      1     |                         |
|  TTYPE8  |   label1   |                         |
|  TFORM8  |      I     |                         |
|  TUNIT8  |      1     |                         |
|  TTYPE9  |   label2   |                         |
|  TFORM9  |      I     |                         |
|  TUNIT9  |      1     |                         |
|  TTYPE10 |   label3   |                         |
|  TFORM10 |      I     |                         |
|  TUNIT10 |      1     |                         |
|  TTYPE11 | sipm_temp0 |                         |
|  TFORM11 |      D     |                         |
|  TUNIT11 |      C     |                         |
|  TTYPE12 | sipm_temp1 |                         |
|  TFORM12 |      D     |                         |
|  TUNIT12 |      C     |                         |
|  TTYPE13 | sipm_temp2 |                         |
|  TFORM13 |      D     |                         |
|  TUNIT13 |      C     |                         |
|  TTYPE14 | sipm_temp3 |                         |
|  TFORM14 |      D     |                         |
|  TUNIT14 |      C     |                         |
|  TTYPE15 |  adc_temp0 |                         |
|  TFORM15 |      I     |                         |
|  TUNIT15 |      1     |                         |
|  TTYPE16 |  adc_temp1 |                         |
|  TFORM16 |      I     |                         |
|  TUNIT16 |      1     |                         |
|  TTYPE17 |  adc_temp2 |                         |
|  TFORM17 |      I     |                         |
|  TUNIT17 |      1     |                         |
|  TTYPE18 |  adc_temp3 |                         |
|  TFORM18 |      I     |                         |
|  TUNIT18 |      1     |                         |
|  TTYPE19 |    vmon0   |                         |
|  TFORM19 |      D     |                         |
|  TUNIT19 |      V     |                         |
|  TTYPE20 |    vmon1   |                         |
|  TFORM20 |      D     |                         |
|  TUNIT20 |      V     |                         |
|  TTYPE21 |    vmon2   |                         |
|  TFORM21 |      D     |                         |
|  TUNIT21 |      V     |                         |
|  TTYPE22 |    vmon3   |                         |
|  TFORM22 |      D     |                         |
|  TUNIT22 |      V     |                         |
|  TTYPE23 |    vout    |                         |
|  TFORM23 |      D     |                         |
|  TUNIT23 |      V     |                         |
|  TTYPE24 |    iop0    |                         |
|  TFORM24 |      D     |                         |
|  TUNIT24 |      A     |                         |
|  TTYPE25 |    iop1    |                         |
|  TFORM25 |      D     |                         |
|  TUNIT25 |      A     |                         |
|  TTYPE26 |    iop2    |                         |
|  TFORM26 |      D     |                         |
|  TUNIT26 |      A     |                         |
|  TTYPE27 |    iop3    |                         |
|  TFORM27 |      D     |                         |
|  TUNIT27 |      A     |                         |
|  TTYPE28 |    imon0   |                         |
|  TFORM28 |      I     |                         |
|  TUNIT28 |      1     |                         |
|  TTYPE29 |    imon1   |                         |
|  TFORM29 |      I     |                         |
|  TUNIT29 |      1     |                         |
|  TTYPE30 |    imon2   |                         |
|  TFORM30 |      I     |                         |
|  TUNIT30 |      1     |                         |
|  TTYPE31 |    imon3   |                         |
|  TFORM31 |      I     |                         |
|  TUNIT31 |      1     |                         |
|  TTYPE32 |  mcu_temp  |                         |
|  TFORM32 |      I     |                         |
|  TUNIT32 |      1     |                         |
|  TTYPE33 |   anchor   |                         |
|  TFORM33 |      I     |                         |
|  TUNIT33 |      1     |                         |

### Keyword Description

|  Keyword  |       Significance       | Remarks |
|:---------:|:------------------------:|:-------:|
| usc_recon |                          |         |
| utc_recon |      UTC-0 timestamp     |         |
|    vop    |       bias voltage       |         |
|   label   |                          |         |
| sipm_temp |    temperature of SiPM   |         |
|  adc_temp | adc value of temperature |         |
|    vmon   |                          |         |
|    vout   |                          |         |
|    iop    |                          |         |
|    imon   |                          |         |
|  mcu_temp |    temperature of MCU    |         |
|   anchor  |                          |         |