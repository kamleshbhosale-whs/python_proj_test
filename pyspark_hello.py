import pkg_resources

pkg_resources.require("pyspark==2.4.0")
import pyspark

sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:////usr/share/doc/python/copyright')
print(txt.count())

python_lines = txt.filter(lambda line: 'python' in line.lower())
print(python_lines.count())
