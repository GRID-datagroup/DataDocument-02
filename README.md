# 天格计划说明文档

## 介绍
本项目是为了帮助使用天格计划相关产品而编写，正在不断完善中；如果在使用过程中遇到任何问题或者有建议，请联系GRID Team

## 环境
本项目使用Sphinx生成，支持markdown文件，使用ReadtheDocs进行托管  

#### 开发环境
```
Python 3.9.1rc1
Sphinx 
```

#### 依赖包
```
sphinx
sphinx-autobuild
sphinx_rtd_theme
recommonmark
sphinx-markdown-tables
```

#### 配置
* `conf.py` :
```python
extensions = ['sphinx_markdown_tables', 'recommonmark']
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
```

以下操作将支持本地中文搜索：
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

#### 本地试运行
* `Server` : 使用`en/zh_server.py`，采用`Flask`库
* `Makefile` : 自定义`make html`命令

## 目录
1. 科学数据产品文档

## 参考资料
* [使用ReadtheDocs托管文档](https://www.xncoding.com/2017/01/22/fullstack/readthedoc.html)
* [ReadthrDocs](https://docs.readthedocs.io/en/stable/index.html)
* [Sphinx](https://www.sphinx-doc.org/en/master/)