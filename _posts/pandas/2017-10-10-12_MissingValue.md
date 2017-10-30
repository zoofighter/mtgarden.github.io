---
layout: post
title: '12 MissingValue'
tags: [Pandas]
---
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Missing-Data">Missing Data<a class="anchor-link" href="#Missing-Data">&#182;</a></h1><ul>
<li><p>Pandas에는 Database에서 Null과 유사한 NaN이 존재함.</p>
<ul>
<li>NaN은 Not a number라는 의미로, numpy에서의 개념이지만</li>
<li>Pandas에서는 존재할 수도 있지만 측정이 되지 않는 값임(not present for whatever reason  missing value)</li>
<li>pandas에서는 NaN을 숫자형에 가깝게 인식함, 참고로 oracle의 경우 컬럼에 null이 있으면 숫자형으로 정의할 수 있음.</li>
<li>' ' 이 Null에 더 가까운 개념임.</li>
</ul>
</li>
<li><p>NaN을 조회하는 메소드로는</p>
<ul>
<li>isnull(), notnull()</li>
<li>isnull().values.any()</li>
</ul>
</li>
<li>NaN을 처리하는 메소드로는 <ul>
<li>dropna(), fillna() </li>
</ul>
</li>
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
<span class="c1">#pandas를 사용하기 위해서 import함 </span>

<span class="n">data</span> <span class="o">=</span> <span class="p">[[</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span>  <span class="mi">2</span><span class="p">,</span>  <span class="mi">3</span><span class="p">]</span>
       <span class="p">,[</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span>  <span class="mi">6</span><span class="p">,</span>  <span class="mi">7</span><span class="p">]</span>
       <span class="p">,[</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">11</span><span class="p">]]</span>

<span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2002</span><span class="p">,</span> <span class="mi">2003</span><span class="p">,</span> <span class="mi">2004</span> <span class="p">]</span>
<span class="n">columns</span> <span class="o">=</span>  <span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">index</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>
<span class="c1">## DataFrame()  안에 data, index, columns은 생략 가능함</span>
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
2002        0       1        2        3
2003        4       5        6        7
2004        8       9       10       11
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># None을 사용해도 NaN으로 인식 </span>
<span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">NaN</span>
<span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
<span class="n">df</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[2]:</div>


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
      <th>2002</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>4.0</td>
      <td>5.0</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>8.0</td>
      <td>9.0</td>
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
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># &#39;&#39; 로 할당 </span>
<span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>
<span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>
<span class="n">df</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[3]:</div>


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
      <th>2002</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>4.0</td>
      <td>5.0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2004</th>
      <td>8.0</td>
      <td>9.0</td>
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
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#NaN의 경우는 count하지 않음 , &#39;&#39;의  경우은 할당함</span>
<span class="n">df</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[4]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>Arizona    2
Boston     2
Chicago    3
Detroit    3
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#NaN의 경우는 평균과 분산 값을 계산</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">mean</span><span class="p">())</span>
<span class="n">df</span><span class="o">.</span><span class="n">std</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Arizona    6.0
Boston     7.0
dtype: float64
</pre>
</div>
</div>

<div class="output_area">
<div class="prompt output_prompt">Out[5]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>Arizona    2.828427
Boston     2.828427
dtype: float64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># NaN으로 할당한 경우에는 숫자형이 었던 컬럼 타입이  변하지 않았지만 &#39;&#39; 로 변경된 타입은 숫자형이 Object 변경 되었음</span>
<span class="n">df</span><span class="o">.</span><span class="n">dtypes</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[6]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>Arizona    float64
Boston     float64
Chicago     object
Detroit     object
dtype: object</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># isnull() 메소드를 사용하여 컬럼을 기준으로 조회할 수 있음</span>
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">isnull</span><span class="p">()]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[7]:</div>


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
      <th>2002</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>3</td>
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
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># notnull() 메소드를 사용하여 컬럼을 기준으로 조회할 수 있음</span>
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">notnull</span><span class="p">()]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[16]:</div>


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
      <td>4.0</td>
      <td>5.0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2004</th>
      <td>8.0</td>
      <td>9.0</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># fillna메소드를 사용하여 NaN 값을 다른 값으로 대체할 수 있음</span>
<span class="n">df</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">mean</span><span class="p">())</span>
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
      <th>2002</th>
      <td>6.0</td>
      <td>7.0</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>4.0</td>
      <td>5.0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2004</th>
      <td>8.0</td>
      <td>9.0</td>
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
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># dropna메소드를 NaN 값을 제거할 수 있음</span>
<span class="n">df</span><span class="o">.</span><span class="n">dropna</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[10]:</div>


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
      <td>4.0</td>
      <td>5.0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>2004</th>
      <td>8.0</td>
      <td>9.0</td>
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
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># &#39;&#39; 값을 조회할 수 있는 방법</span>
<span class="n">df</span><span class="o">.</span><span class="n">applymap</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o">==</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[11]:</div>


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
      <th>2002</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
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
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#  컬럼 단위로 &#39;&#39; 값을 조회할 수 있는 방법</span>
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span> <span class="o">==</span><span class="s1">&#39;&#39;</span><span class="p">)]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[12]:</div>


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
      <td>4.0</td>
      <td>5.0</td>
      <td></td>
      <td></td>
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
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># replace 메소드로 &#39;&#39; 를 NaN으로 대체 할 수 있음</span>
<span class="n">df</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">,</span><span class="n">np</span><span class="o">.</span><span class="n">NaN</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[13]:</div>


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
      <th>2002</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>4.0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>8.0</td>
      <td>9.0</td>
      <td>10.0</td>
      <td>11.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
 

