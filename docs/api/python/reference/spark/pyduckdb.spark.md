---
# this file is GENERATED, regenerate it with scripts/generate_python_docs.py
layout: docu
title: Examples
---
<div class="documentwrapper">
<div class="bodywrapper">
<div class="body" role="main">

<dl class="py exception" id="module-pyduckdb.spark">
<dt class="sig sig-object py" id="pyduckdb.spark.ContributionsAcceptedError">
<em class="property"><span class="pre">exception</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pyduckdb.spark.</span></span><span class="sig-name descname"><span class="pre">ContributionsAcceptedError</span></span><a class="headerlink" href="#pyduckdb.spark.ContributionsAcceptedError" title="Link to this definition">&#182;</a>
</dt>
<dd>
<p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">NotImplementedError</span></code></p>
<p>This method is not planned to be implemented, if you would like to implement this method
or show your interest in this method to other members of the community,
feel free to open up a PR or a Discussion over on <a class="reference external" href="https://github.com/duckdb/duckdb">https://github.com/duckdb/duckdb</a></p>
</dd>
</dl>

<dl class="py class">
<dt class="sig sig-object py" id="pyduckdb.spark.DataFrame">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pyduckdb.spark.</span></span><span class="sig-name descname"><span class="pre">DataFrame</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">relation</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="../index.html#duckdb.DuckDBPyRelation" title="duckdb.duckdb.DuckDBPyRelation"><span class="pre">DuckDBPyRelation</span></a></span></em>, <em class="sig-param"><span class="n"><span class="pre">session</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pyduckdb.spark.SparkSession" title="pyduckdb.spark.SparkSession"><span class="pre">SparkSession</span></a></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pyduckdb.spark.DataFrame" title="Link to this definition">&#182;</a>
</dt>
<dd>
<p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.DataFrame.collect">
<span class="sig-name descname"><span class="pre">collect</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Row</span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#pyduckdb.spark.DataFrame.collect" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.DataFrame.createGlobalTempView">
<span class="sig-name descname"><span class="pre">createGlobalTempView</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.DataFrame.createGlobalTempView" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.DataFrame.createOrReplaceTempView">
<span class="sig-name descname"><span class="pre">createOrReplaceTempView</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.DataFrame.createOrReplaceTempView" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.DataFrame.printSchema">
<span class="sig-name descname"><span class="pre">printSchema</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pyduckdb.spark.DataFrame.printSchema" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.DataFrame.schema">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">schema</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">StructType</span></em><a class="headerlink" href="#pyduckdb.spark.DataFrame.schema" title="Link to this definition">&#182;</a>
</dt>
<dd>
<p>Returns the schema of this <a class="reference internal" href="#pyduckdb.spark.DataFrame" title="pyduckdb.spark.DataFrame"><code class="xref py py-class docutils literal notranslate"><span class="pre">DataFrame</span></code></a> as a <code class="xref py py-class docutils literal notranslate"><span class="pre">pyduckdb.spark.sql.types.StructType</span></code>.</p>
<div class="versionadded">
<p><span class="versionmodified added">New in version 1.3.0.</span></p>
</div>
<section id="examples">
<h1>Examples<a class="headerlink" href="#examples" title="Link to this heading">&#182;</a>
</h1>
<div class="doctest highlight-default notranslate">
<div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">df</span><span class="o">.</span><span class="n">schema</span>
<span class="go">StructType([StructField('age', IntegerType(), True),</span>
<span class="go">            StructField('name', StringType(), True)])</span>
</pre></div>
</div>
</section>
</dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.DataFrame.show">
<span class="sig-name descname"><span class="pre">show</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.DataFrame.show" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.DataFrame.toDF">
<span class="sig-name descname"><span class="pre">toDF</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="o"><span class="pre">*</span></span><span class="n"><span class="pre">cols</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.DataFrame" title="pyduckdb.spark.sql.dataframe.DataFrame"><span class="pre">DataFrame</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.DataFrame.toDF" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.DataFrame.write">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">write</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">DataFrameWriter</span></em><a class="headerlink" href="#pyduckdb.spark.DataFrame.write" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

</dd>
</dl>

<dl class="py class">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pyduckdb.spark.</span></span><span class="sig-name descname"><span class="pre">SparkConf</span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf" title="Link to this definition">&#182;</a>
</dt>
<dd>
<p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.contains">
<span class="sig-name descname"><span class="pre">contains</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">bool</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.contains" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.get">
<span class="sig-name descname"><span class="pre">get</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">defaultValue</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.get" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.getAll">
<span class="sig-name descname"><span class="pre">getAll</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Tuple</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.getAll" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.set">
<span class="sig-name descname"><span class="pre">set</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkConf" title="pyduckdb.spark.conf.SparkConf"><span class="pre">SparkConf</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.set" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.setAll">
<span class="sig-name descname"><span class="pre">setAll</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">pairs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Tuple</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkConf" title="pyduckdb.spark.conf.SparkConf"><span class="pre">SparkConf</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.setAll" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.setAppName">
<span class="sig-name descname"><span class="pre">setAppName</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkConf" title="pyduckdb.spark.conf.SparkConf"><span class="pre">SparkConf</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.setAppName" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.setExecutorEnv">
<span class="sig-name descname"><span class="pre">setExecutorEnv</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">pairs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">Tuple</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">,</span></span><span class="w"> </span><span class="pre">str</span><span class="p"><span class="pre">]</span></span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkConf" title="pyduckdb.spark.conf.SparkConf"><span class="pre">SparkConf</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.setExecutorEnv" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.setIfMissing">
<span class="sig-name descname"><span class="pre">setIfMissing</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkConf" title="pyduckdb.spark.conf.SparkConf"><span class="pre">SparkConf</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.setIfMissing" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.setMaster">
<span class="sig-name descname"><span class="pre">setMaster</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkConf" title="pyduckdb.spark.conf.SparkConf"><span class="pre">SparkConf</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.setMaster" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.setSparkHome">
<span class="sig-name descname"><span class="pre">setSparkHome</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkConf" title="pyduckdb.spark.conf.SparkConf"><span class="pre">SparkConf</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.setSparkHome" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkConf.toDebugString">
<span class="sig-name descname"><span class="pre">toDebugString</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkConf.toDebugString" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

</dd>
</dl>

<dl class="py class">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pyduckdb.spark.</span></span><span class="sig-name descname"><span class="pre">SparkContext</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">master</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pyduckdb.spark.SparkContext" title="Link to this definition">&#182;</a>
</dt>
<dd>
<p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.addArchive">
<span class="sig-name descname"><span class="pre">addArchive</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.addArchive" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.addFile">
<span class="sig-name descname"><span class="pre">addFile</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">recursive</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.addFile" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.addPyFile">
<span class="sig-name descname"><span class="pre">addPyFile</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.addPyFile" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.applicationId">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">applicationId</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pyduckdb.spark.SparkContext.applicationId" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.cancelAllJobs">
<span class="sig-name descname"><span class="pre">cancelAllJobs</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.cancelAllJobs" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.cancelJobGroup">
<span class="sig-name descname"><span class="pre">cancelJobGroup</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">groupId</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.cancelJobGroup" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.connection">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">connection</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><a class="reference internal" href="../index.html#duckdb.DuckDBPyConnection" title="duckdb.duckdb.DuckDBPyConnection"><span class="pre">DuckDBPyConnection</span></a></em><a class="headerlink" href="#pyduckdb.spark.SparkContext.connection" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.defaultMinPartitions">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">defaultMinPartitions</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span></em><a class="headerlink" href="#pyduckdb.spark.SparkContext.defaultMinPartitions" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.defaultParallelism">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">defaultParallelism</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span></em><a class="headerlink" href="#pyduckdb.spark.SparkContext.defaultParallelism" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.dump_profiles">
<span class="sig-name descname"><span class="pre">dump_profiles</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">path</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.dump_profiles" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.getCheckpointDir">
<span class="sig-name descname"><span class="pre">getCheckpointDir</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.getCheckpointDir" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.getConf">
<span class="sig-name descname"><span class="pre">getConf</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkConf" title="pyduckdb.spark.conf.SparkConf"><span class="pre">SparkConf</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.getConf" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.getLocalProperty">
<span class="sig-name descname"><span class="pre">getLocalProperty</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.getLocalProperty" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.getOrCreate">
<em class="property"><span class="pre">classmethod</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">getOrCreate</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">conf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pyduckdb.spark.SparkConf" title="pyduckdb.spark.conf.SparkConf"><span class="pre">SparkConf</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkContext" title="pyduckdb.spark.context.SparkContext"><span class="pre">SparkContext</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.getOrCreate" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.setCheckpointDir">
<span class="sig-name descname"><span class="pre">setCheckpointDir</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">dirName</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.setCheckpointDir" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.setJobDescription">
<span class="sig-name descname"><span class="pre">setJobDescription</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.setJobDescription" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.setJobGroup">
<span class="sig-name descname"><span class="pre">setJobGroup</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">groupId</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">description</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">interruptOnCancel</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.setJobGroup" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.setLocalProperty">
<span class="sig-name descname"><span class="pre">setLocalProperty</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.setLocalProperty" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.setLogLevel">
<span class="sig-name descname"><span class="pre">setLogLevel</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">logLevel</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.setLogLevel" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.setSystemProperty">
<em class="property"><span class="pre">classmethod</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">setSystemProperty</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.setSystemProperty" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.show_profiles">
<span class="sig-name descname"><span class="pre">show_profiles</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.show_profiles" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.sparkUser">
<span class="sig-name descname"><span class="pre">sparkUser</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">str</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.sparkUser" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.startTime">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">startTime</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pyduckdb.spark.SparkContext.startTime" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.stop">
<span class="sig-name descname"><span class="pre">stop</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkContext.stop" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.uiWebUrl">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">uiWebUrl</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pyduckdb.spark.SparkContext.uiWebUrl" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkContext.version">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">version</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pyduckdb.spark.SparkContext.version" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

</dd>
</dl>

<dl class="py class">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">pyduckdb.spark.</span></span><span class="sig-name descname"><span class="pre">SparkSession</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">context</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pyduckdb.spark.SparkContext" title="pyduckdb.spark.context.SparkContext"><span class="pre">SparkContext</span></a></span></em><span class="sig-paren">)</span><a class="headerlink" href="#pyduckdb.spark.SparkSession" title="Link to this definition">&#182;</a>
</dt>
<dd>
<p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py class">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.Builder">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">Builder</span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.Builder" title="Link to this definition">&#182;</a>
</dt>
<dd>
<p>Bases: <code class="xref py py-class docutils literal notranslate"><span class="pre">object</span></code></p>
<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.Builder.appName">
<span class="sig-name descname"><span class="pre">appName</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkSession.Builder" title="pyduckdb.spark.sql.session.SparkSession.Builder"><span class="pre">Builder</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.Builder.appName" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.Builder.config">
<span class="sig-name descname"><span class="pre">config</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">key</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">value</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">conf</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><a class="reference internal" href="#pyduckdb.spark.SparkConf" title="pyduckdb.spark.conf.SparkConf"><span class="pre">SparkConf</span></a><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkSession.Builder" title="pyduckdb.spark.sql.session.SparkSession.Builder"><span class="pre">Builder</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.Builder.config" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.Builder.enableHiveSupport">
<span class="sig-name descname"><span class="pre">enableHiveSupport</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkSession.Builder" title="pyduckdb.spark.sql.session.SparkSession.Builder"><span class="pre">Builder</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.Builder.enableHiveSupport" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.Builder.getOrCreate">
<span class="sig-name descname"><span class="pre">getOrCreate</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkSession" title="pyduckdb.spark.sql.session.SparkSession"><span class="pre">SparkSession</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.Builder.getOrCreate" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.Builder.master">
<span class="sig-name descname"><span class="pre">master</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkSession.Builder" title="pyduckdb.spark.sql.session.SparkSession.Builder"><span class="pre">Builder</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.Builder.master" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.Builder.remote">
<span class="sig-name descname"><span class="pre">remote</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">url</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkSession.Builder" title="pyduckdb.spark.sql.session.SparkSession.Builder"><span class="pre">Builder</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.Builder.remote" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

</dd>
</dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.builder">
<span class="sig-name descname"><span class="pre">builder</span></span><em class="property"><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">&lt;pyduckdb.spark.sql.session.SparkSession.Builder</span> <span class="pre">object&gt;</span></em><a class="headerlink" href="#pyduckdb.spark.SparkSession.builder" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.catalog">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">catalog</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Catalog</span></em><a class="headerlink" href="#pyduckdb.spark.SparkSession.catalog" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.conf">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">conf</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">RuntimeConfig</span></em><a class="headerlink" href="#pyduckdb.spark.SparkSession.conf" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.createDataFrame">
<span class="sig-name descname"><span class="pre">createDataFrame</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">data</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">PandasDataFrame</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">Iterable</span><span class="p"><span class="pre">[</span></span><span class="pre">Any</span><span class="p"><span class="pre">]</span></span></span></em>, <em class="sig-param"><span class="n"><span class="pre">schema</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">StructType</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">List</span><span class="p"><span class="pre">[</span></span><span class="pre">str</span><span class="p"><span class="pre">]</span></span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">samplingRatio</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">float</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">verifySchema</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">bool</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">True</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.DataFrame" title="pyduckdb.spark.sql.dataframe.DataFrame"><span class="pre">DataFrame</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.createDataFrame" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.getActiveSession">
<span class="sig-name descname"><span class="pre">getActiveSession</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkSession" title="pyduckdb.spark.sql.session.SparkSession"><span class="pre">SparkSession</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.getActiveSession" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.newSession">
<span class="sig-name descname"><span class="pre">newSession</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.SparkSession" title="pyduckdb.spark.sql.session.SparkSession"><span class="pre">SparkSession</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.newSession" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.range">
<span class="sig-name descname"><span class="pre">range</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">start</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">end</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">step</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">1</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">numPartitions</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">int</span><span class="w"> </span><span class="p"><span class="pre">|</span></span><span class="w"> </span><span class="pre">None</span></span><span class="w"> </span><span class="o"><span class="pre">=</span></span><span class="w"> </span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.DataFrame" title="pyduckdb.spark.sql.dataframe.DataFrame"><span class="pre">DataFrame</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.range" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.read">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">read</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">DataFrameReader</span></em><a class="headerlink" href="#pyduckdb.spark.SparkSession.read" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.readStream">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">readStream</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">DataStreamReader</span></em><a class="headerlink" href="#pyduckdb.spark.SparkSession.readStream" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.sparkContext">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">sparkContext</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><a class="reference internal" href="#pyduckdb.spark.SparkContext" title="pyduckdb.spark.context.SparkContext"><span class="pre">SparkContext</span></a></em><a class="headerlink" href="#pyduckdb.spark.SparkSession.sparkContext" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.sql">
<span class="sig-name descname"><span class="pre">sql</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sqlQuery</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">kwargs</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">Any</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.DataFrame" title="pyduckdb.spark.sql.dataframe.DataFrame"><span class="pre">DataFrame</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.sql" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.stop">
<span class="sig-name descname"><span class="pre">stop</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><span class="pre">None</span></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.stop" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.streams">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">streams</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Any</span></em><a class="headerlink" href="#pyduckdb.spark.SparkSession.streams" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py method">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.table">
<span class="sig-name descname"><span class="pre">table</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">tableName</span></span><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="n"><span class="pre">str</span></span></em><span class="sig-paren">)</span> <span class="sig-return"><span class="sig-return-icon">&#8594;</span> <span class="sig-return-typehint"><a class="reference internal" href="#pyduckdb.spark.DataFrame" title="pyduckdb.spark.sql.dataframe.DataFrame"><span class="pre">DataFrame</span></a></span></span><a class="headerlink" href="#pyduckdb.spark.SparkSession.table" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.udf">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">udf</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">UDFRegistration</span></em><a class="headerlink" href="#pyduckdb.spark.SparkSession.udf" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

<dl class="py property">
<dt class="sig sig-object py" id="pyduckdb.spark.SparkSession.version">
<em class="property"><span class="pre">property</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">version</span></span><em class="property"><span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span></em><a class="headerlink" href="#pyduckdb.spark.SparkSession.version" title="Link to this definition">&#182;</a>
</dt>
<dd></dd>
</dl>

</dd>
</dl>



<div class="clearer"></div>
</div>
</div>
</div>
