---
layout: post
title: 'Create DataFrame'
tags: [Pandas]
comments: true
---
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Create-DataFrame">Create DataFrame<a class="anchor-link" href="#Create-DataFrame">&#182;</a></h1><ul>
<li>Pandas에서는 Oracle의 테이블과 같은 자료구조를 DataFrame라고 함</li>
<li>DataFrame은 data, index, columns_index로 구성되어 있음<ul>
<li>data는 2차원 데이터 구조로 numpy의 ndarrary나 python의 dict 형태로 컬럼의 유형과 같은 순서로 숫자나 문자로 구성되어 있음</li>
<li>columns은 Oracle 컬럼과 유사함, 자료 구조 형이 있음  컬럼에는 문자나 숫자 같은 유형을 가질 수 있음</li>
<li>index는 생략할때가 많고 생략되어진다면 기본적으로 np.arange(n)로 표현됨(즉, 0에서 row 데이터수 -1 까지의 값을 가짐)</li>
</ul>
</li>
<li>DataFrame을 만드는 방법에는 DataFrame(), read_csv(), read_excel() 등 다수의 방법이 있음.</li>
<li>index, columns이라는 명칭보다는 rows_index, columns_index라는 명칭이 좀 더 의미를 파악하는데 도움이 됨</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="n">data</span>  <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">12</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">((</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>
<span class="c1">#로 표현 할 수 있음</span>


<span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2002</span><span class="p">,</span> <span class="mi">2003</span><span class="p">,</span> <span class="mi">2004</span> <span class="p">]</span>
<span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">index</span> <span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>      Arizona  Boston  Chicago  Detroit
2000        0       1        2        3
2001        4       5        6        7
2002        8       9       10       11
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
Int64Index: 3 entries, 2000 to 2002
Data columns (total 4 columns):
Arizona    3 non-null int64
Boston     3 non-null int64
Chicago    3 non-null int64
Detroit    3 non-null int64
dtypes: int64(4)
memory usage: 120.0 bytes
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>DataFrame 관련 <a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html" title="DataFrame 관련 Pandas Docs">Pandas Docs</a> 을 보면</p>
<ul>
<li>DataFrame 함수(객체함수)는 추가적으로 data, index, columns 뿐만 아니라 dtype, copy 파라미터를 추가적으로 입력받을 수 있음</li>
<li>dtype은 컬럼에서 유형을 명시적으로 선언할 수도 있음</li>
<li>선언이 되어 있지 않으면 Pandas가 알아서 columns의 타입을 결정함</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">columns</span>
<span class="c1"># 컬럼이름과 타입을 확인할 수</span>
<span class="n">df</span><span class="o">.</span><span class="n">dtypes</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[3]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>Arizona    int64
Boston     int64
Chicago    int64
Detroit    int64
dtype: object</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">index</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[3]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>Int64Index([2000, 2001, 2002], dtype=&#39;int64&#39;)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="DataFrame&#51012;-&#47564;&#46300;&#45716;-&#46608;-&#45796;&#47480;-&#48169;&#48277;">DataFrame&#51012; &#47564;&#46300;&#45716; &#46608; &#45796;&#47480; &#48169;&#48277;<a class="anchor-link" href="#DataFrame&#51012;-&#47564;&#46300;&#45716;-&#46608;-&#45796;&#47480;-&#48169;&#48277;">&#182;</a></h3><ul>
<li>data, columns, row_index를 각각 선언하지 않고 columns과 데이터를 딕셔너리를 구조로 하여 DataFrame을 만들 수 있음</li>
<li>간단히 데이터를 만들 때 선호되는 방식임</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dicts</span> <span class="o">=</span><span class="p">{</span><span class="s1">&#39;Arizona&#39;</span><span class="p">:[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">4</span> <span class="p">,</span><span class="mi">8</span> <span class="p">]</span>
      <span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">:</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">9</span><span class="p">]</span>
      <span class="p">,</span><span class="s1">&#39;Chicago&#39;</span><span class="p">:[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">10</span><span class="p">]</span>
      <span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">:[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">11</span><span class="p">]}</span>
<span class="n">df2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">dicts</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df2</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>   Arizona  Boston  Chicago  Detroit
0        0       1        2        3
1        4       5        6        7
2        8       9       10       11
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">==</span> <span class="n">df2</span>
<span class="p">(</span><span class="ne">ValueError</span><span class="p">:</span> <span class="n">Can</span> <span class="n">only</span> <span class="n">compare</span> <span class="n">identically</span><span class="o">-</span><span class="n">labeled</span> <span class="n">DataFrame</span> <span class="n">objects</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">ValueError</span>                                Traceback (most recent call last)
<span class="ansi-green-fg">&lt;ipython-input-11-9d01f1582091&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span><span class="ansi-blue-fg">()</span>
<span class="ansi-green-fg">----&gt; 1</span><span class="ansi-red-fg"> </span>df <span class="ansi-blue-fg">==</span> df2

<span class="ansi-green-fg">/home/bono/anaconda3/lib/python3.5/site-packages/pandas/core/ops.py</span> in <span class="ansi-cyan-fg">f</span><span class="ansi-blue-fg">(self, other)</span>
<span class="ansi-green-intense-fg ansi-bold">   1295</span>     <span class="ansi-green-fg">def</span> f<span class="ansi-blue-fg">(</span>self<span class="ansi-blue-fg">,</span> other<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">   1296</span>         <span class="ansi-green-fg">if</span> isinstance<span class="ansi-blue-fg">(</span>other<span class="ansi-blue-fg">,</span> pd<span class="ansi-blue-fg">.</span>DataFrame<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">:</span>  <span class="ansi-red-fg"># Another DataFrame</span>
<span class="ansi-green-fg">-&gt; 1297</span><span class="ansi-red-fg">             </span><span class="ansi-green-fg">return</span> self<span class="ansi-blue-fg">.</span>_compare_frame<span class="ansi-blue-fg">(</span>other<span class="ansi-blue-fg">,</span> func<span class="ansi-blue-fg">,</span> str_rep<span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">   1298</span>         <span class="ansi-green-fg">elif</span> isinstance<span class="ansi-blue-fg">(</span>other<span class="ansi-blue-fg">,</span> ABCSeries<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">   1299</span>             <span class="ansi-green-fg">return</span> self<span class="ansi-blue-fg">.</span>_combine_series_infer<span class="ansi-blue-fg">(</span>other<span class="ansi-blue-fg">,</span> func<span class="ansi-blue-fg">)</span>

<span class="ansi-green-fg">/home/bono/anaconda3/lib/python3.5/site-packages/pandas/core/frame.py</span> in <span class="ansi-cyan-fg">_compare_frame</span><span class="ansi-blue-fg">(self, other, func, str_rep)</span>
<span class="ansi-green-intense-fg ansi-bold">   3570</span>     <span class="ansi-green-fg">def</span> _compare_frame<span class="ansi-blue-fg">(</span>self<span class="ansi-blue-fg">,</span> other<span class="ansi-blue-fg">,</span> func<span class="ansi-blue-fg">,</span> str_rep<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">   3571</span>         <span class="ansi-green-fg">if</span> <span class="ansi-green-fg">not</span> self<span class="ansi-blue-fg">.</span>_indexed_same<span class="ansi-blue-fg">(</span>other<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">:</span>
<span class="ansi-green-fg">-&gt; 3572</span><span class="ansi-red-fg">             raise ValueError(&#39;Can only compare identically-labeled &#39;
</span><span class="ansi-green-intense-fg ansi-bold">   3573</span>                              &#39;DataFrame objects&#39;)
<span class="ansi-green-intense-fg ansi-bold">   3574</span>         <span class="ansi-green-fg">return</span> self<span class="ansi-blue-fg">.</span>_compare_frame_evaluate<span class="ansi-blue-fg">(</span>other<span class="ansi-blue-fg">,</span> func<span class="ansi-blue-fg">,</span> str_rep<span class="ansi-blue-fg">)</span>

<span class="ansi-red-fg">ValueError</span>: Can only compare identically-labeled DataFrame objects</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df2</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span><span class="n">row_index</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df2</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[8]:</div>


<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Arizona</th>
      <th>Boston</th>
      <th>Chicago</th>
      <th>Detroit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="p">(</span><span class="n">df</span> <span class="o">==</span> <span class="n">df2</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[9]:</div>


<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Arizona</th>
      <th>Boston</th>
      <th>Chicago</th>
      <th>Detroit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">s</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">poisson</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">10000</span><span class="p">)</span>
<span class="n">count</span><span class="p">,</span> <span class="n">bins</span><span class="p">,</span> <span class="n">ignored</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="mi">14</span><span class="p">,</span> <span class="n">normed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">NameError</span>                                 Traceback (most recent call last)
<span class="ansi-green-fg">&lt;ipython-input-10-2bc1820176ab&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span><span class="ansi-blue-fg">()</span>
<span class="ansi-green-intense-fg ansi-bold">      1</span> 
<span class="ansi-green-intense-fg ansi-bold">      2</span> s <span class="ansi-blue-fg">=</span> np<span class="ansi-blue-fg">.</span>random<span class="ansi-blue-fg">.</span>poisson<span class="ansi-blue-fg">(</span><span class="ansi-cyan-fg">5</span><span class="ansi-blue-fg">,</span> <span class="ansi-cyan-fg">10000</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-fg">----&gt; 3</span><span class="ansi-red-fg"> </span>count<span class="ansi-blue-fg">,</span> bins<span class="ansi-blue-fg">,</span> ignored <span class="ansi-blue-fg">=</span> plt<span class="ansi-blue-fg">.</span>hist<span class="ansi-blue-fg">(</span>s<span class="ansi-blue-fg">,</span> <span class="ansi-cyan-fg">14</span><span class="ansi-blue-fg">,</span> normed<span class="ansi-blue-fg">=</span><span class="ansi-green-fg">True</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      4</span> plt<span class="ansi-blue-fg">.</span>show<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">)</span>

<span class="ansi-red-fg">NameError</span>: name &#39;plt&#39; is not defined</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="&#51221;&#47532;">&#51221;&#47532;<a class="anchor-link" href="#&#51221;&#47532;">&#182;</a></h4><ol>
<li>DataFrame(data, cou)    DataFrame객체를 생성할 수 있다.</li>
<li>DataFrame.info() 함수를 사용하면 DataFrame 전체적인 정보를 확인할 수 있다.</li>
<li>index(이 블로그에서는 row_index라고 지칭) 생략해서 사용할 수 있다.</li>
<li>DataFrame을 만드는 또 다른 방법은 딕셔너리를 이용하면 됨</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">primt</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Viewing</span> <span class="n">Data</span>  
<span class="n">head</span><span class="p">()</span>
<span class="n">듣등</span>
<span class="mi">10</span> <span class="n">minute</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">pandas</span><span class="o">.</span><span class="n">pydata</span><span class="o">.</span><span class="n">org</span><span class="o">/</span><span class="n">pandas</span><span class="o">-</span><span class="n">docs</span><span class="o">/</span><span class="n">stable</span><span class="o">/</span><span class="n">generated</span><span class="o">/</span><span class="n">pandas</span><span class="o">.</span><span class="n">DataFrame</span><span class="o">.</span><span class="n">html</span>  <span class="mi">200</span><span class="n">개</span> <span class="n">메소드</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">### 데이터 프레임 조작..</span>

<span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">stackoverflow</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">questions</span><span class="o">/</span><span class="mi">12555323</span><span class="o">/</span><span class="n">adding</span><span class="o">-</span><span class="n">new</span><span class="o">-</span><span class="n">column</span><span class="o">-</span><span class="n">to</span><span class="o">-</span><span class="n">existing</span><span class="o">-</span><span class="n">dataframe</span><span class="o">-</span><span class="ow">in</span><span class="o">-</span><span class="n">python</span><span class="o">-</span><span class="n">pandas</span>
</pre></div>

</div>
</div>
</div>

</div>
 

