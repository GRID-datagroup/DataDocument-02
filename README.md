# 天格计划说明文档

## 介绍
&emsp;&emsp;本项目是为了帮助使用天格计划相关产品而编写，正在不断完善中；如果在使用过程中遇到任何问题或者有建议，请联系GRID Team。

## 分支
&emsp;&emsp;本仓库中所有分支的命名为`GRID-id-lang`，表示不同卫星对应的不同语言的文档。

### 版本号
&emsp;&emsp;本文档版本号命名规则为`X.Y.Z`：
* X：主版本号，代表卫星编号，以最小编号为准，例如GRID-02、GRID-04文档版本号均为`2.X.X`
* Y：次版本号，新增或弃用了内容
* Z：修订号，对内容进行了修正

## 环境
&emsp;&emsp;本项目使用Sphinx生成，使用ReadtheDocs进行托管。

### 开发环境
```
Python 3.9.1rc1
Sphinx 
```

### 依赖包
```
sphinx
sphinx-autobuild
sphinx_rtd_theme
```

### 配置

#### 支持markdown编写
* `conf.py` :
```python
extensions = ['sphinx_markdown_tables', 'recommonmark']
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
```

* `requirements.txt`:
```
recommonmark
sphinx-markdown-tables
```

#### 本地中文搜索：
* `jieba package` :
```python
pip3 install jieba
```
* `zh_CN.py` : 将`zh_CN.py`文件放置在`sphinx/search`目录下
* `sphinx/search/__init.py__` :
```python
from sphinx.search import en, ja, zh_CN
languages = {
    'en': en.SearchEnglish,
    'zh_CN': zh_CN.SearchChinese
}
```

### 本地试运行
* `Server` : 使用`en/zh_server.py`，采用`Flask`库
* `Makefile` : 自定义`make html`命令

## 参考资料
* [使用ReadtheDocs托管文档](https://www.xncoding.com/2017/01/22/fullstack/readthedoc.html)
* [ReadthrDocs](https://docs.readthedocs.io/en/stable/index.html)
* [Sphinx](https://www.sphinx-doc.org/en/master/)