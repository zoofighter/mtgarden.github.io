---
layout: post
title: '02_Create DataFrame'
tags: [Pandas]
layout: default
comments: true
---
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Create-DataFrame">Create DataFrame<a class="anchor-link" href="#Create-DataFrame">&#182;</a></h1><ul>
<li>Pandas에서는 DataBase의 테이블과 비슷한 자료구조를 DataFrame라고 함</li>
<li>DataFrame은 data, index, columns_index로 구성되어 있음<ul>
<li>data는 2차원 데이터 구조로 numpy의 ndarrary나 python의 dict, list 형태로 숫자나 문자로 구성되어 있음</li>
<li>columns은 DataBase의 컬럼 처럼 자료 구조 형이 있음.  컬럼에는 문자나 숫자 같은 유형을 가질 수 있음</li>
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
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="n">data</span>  <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">12</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">((</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>
<span class="c1">#로 표현 할 수 있음</span>


<span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2003</span><span class="p">,</span> <span class="mi">2004</span><span class="p">,</span> <span class="mi">2005</span> <span class="p">]</span>
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
2003        0       1        2        3
2004        4       5        6        7
2005        8       9       10       11
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#df.info를 사용하면 DataFrame의 정보를 확인할 수 있음</span>
<span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
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
Int64Index: 3 entries, 2003 to 2005
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
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>DataFrame 관련 <a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html">Pandas Docs</a> 을 보면</p>
<ul>
<li>DataFrame 메소드는는 추가적으로 data, index, columns 뿐만 아니라 dtype, copy 파라미터를 추가적으로 입력받을 수 있음</li>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 컬럼이름과 타입을 확인할 수</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">dtypes</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Index([&#39;Arizona&#39;, &#39;Boston&#39;, &#39;Chicago&#39;, &#39;Detroit&#39;], dtype=&#39;object&#39;)
Arizona    int64
Boston     int64
Chicago    int64
Detroit    int64
dtype: object
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 인덱스의 이름을 확인할 수 있음</span>
<span class="n">df</span><span class="o">.</span><span class="n">index</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[4]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>Int64Index([2003, 2004, 2005], dtype=&#39;int64&#39;)</pre>
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
<h3 id="Dictionary&#47484;-&#51060;&#50857;&#54616;&#50668;-DataFrame&#51012;-&#47564;&#46300;&#45716;--&#48169;&#48277;">Dictionary&#47484; &#51060;&#50857;&#54616;&#50668; DataFrame&#51012; &#47564;&#46300;&#45716;  &#48169;&#48277;<a class="anchor-link" href="#Dictionary&#47484;-&#51060;&#50857;&#54616;&#50668;-DataFrame&#51012;-&#47564;&#46300;&#45716;--&#48169;&#48277;">&#182;</a></h3><ul>
<li>data, columns, index를 각각 선언하지 않고 columns과 데이터를 딕셔너리를 구조로 하여 DataFrame을 만들 수 있음</li>
<li>간단히 데이터를 만들 때 선호되는 방식임</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
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
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#data, columns, index를 사용하여 만든 df와 비교</span>
<span class="c1">#Data와 Column은 같으나 Index가 다르기 때문에 비교 할 수 었음</span>
<span class="c1">#df == df2</span>
<span class="c1">#(ValueError: Can only compare identically-labeled DataFrame objects)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#index를 df2.index에 할당</span>
<span class="n">df2</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="n">index</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#index와 columns, data 가 같기 때문에 비교 가능함</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df2</span><span class="p">)</span>
<span class="p">(</span><span class="n">df</span> <span class="o">==</span> <span class="n">df2</span><span class="p">)</span>
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
2003        0       1        2        3
2004        4       5        6        7
2005        8       9       10       11
</pre>
</div>
</div>

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
      <th>2003</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2005</th>
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
 

