---
layout: post
title: '07_select rows from columns value'
tags: [Pandas]
layout: default
comments: true
---
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="select-rows-from-where-columns-condition">select rows from where columns condition<a class="anchor-link" href="#select-rows-from-where-columns-condition">&#182;</a></h2><ul>
<li>Pandas에서도 sql처럼 특정 columns의 값들을 조건을 기반으로 row를 조회하고 싶어 한다.  <ul>
<li>즉, select * from table where colume_name = some_value 같은 형태를 의미한다.</li>
</ul>
</li>
<li>위의 표현식을 dataframe을 사용할 경우에는 다음과 같이 표현 할 수 있다.  <ul>
<li>df.loc[df['column_name'] == some_value] </li>
<li>df.loc[df['column_name'] != some_value]     -- <strong> not 조건 </strong></li>
</ul>
</li>
<li>sql의 In 처럼 여러개의 값(multiple_values)을 선택하려면 isin을 사용한다. <ul>
<li>df.loc[df['column_name'].isin(multiple_values)]   </li>
<li>df.loc[~df['column_name'].isin(multiple_values)]    -- <strong> isin을 사용할 경우 부정은 앞에 ~를 사용   </strong> </li>
<li>loc[]의 인자로 boolean 값이 들어가는 boolean indexing의 형태임.</li>
</ul>
</li>
<li>만약에 조건이 2개 이상이면 &amp; 연산자를 다음과 같이 사용한다.<ul>
<li>df.loc[(df['column_name1'] == some_value1) &amp; (df['column_name2'] == some_value2)]</li>
<li>df.loc[(df['column_name'] == some_value) &amp; df['other_column'].isin(multiple_values)]</li>
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

<span class="n">data</span>  <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">12</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">((</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>

<span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2003</span><span class="p">,</span> <span class="mi">2004</span><span class="p">,</span> <span class="mi">2005</span> <span class="p">]</span>
<span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">index</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 컬럼 조건이 하나일 경우</span>
<span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">]</span>  <span class="c1"># &lt;--  df.loc[df.loc[:,&#39;Arizona&#39;] == 0] 와 같은 의미</span>
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
      <th>2003</th>
      <td>0</td>
      <td>1</td>
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
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># .loc[] 를 생략할 수 있음</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">])</span> 
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#  not 조건이면  &#39;==&#39; 대신에 &#39;!= &#39;를 사용한다.</span>
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[4]:</div>


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
      <th>2004</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2005</th>
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
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 조건에 컬럼 비교를 위해 부등호를 넣을 수 있다.</span>
<span class="n">data</span>  <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">)</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">index</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>                        
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>       Arizona    Boston   Chicago   Detroit
2003  0.907345  0.240986 -0.895304 -2.057843
2004  0.865341 -1.170443 -1.138361  0.100939
2005 -0.076767 -1.259515 -0.717019  1.686924
</pre>
</div>
</div>

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
      <th>2003</th>
      <td>0.907345</td>
      <td>0.240986</td>
      <td>-0.895304</td>
      <td>-2.057843</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>0.865341</td>
      <td>-1.170443</td>
      <td>-1.138361</td>
      <td>0.100939</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#applymap과 lambda를 사용하여 숫자를 문자로 치환함</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">applymap</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="s1">&#39;Win&#39;</span> <span class="k">if</span> <span class="n">x</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="k">else</span> <span class="s1">&#39;Final&#39;</span> <span class="k">if</span>  <span class="n">x</span> <span class="o">&gt;</span> <span class="mi">0</span>   <span class="k">else</span> <span class="s1">&#39;Lose&#39;</span><span class="p">)</span> 
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
<pre>     Arizona Boston Chicago Detroit
2003   Final  Final    Lose    Lose
2004   Final   Lose    Lose   Final
2005    Lose   Lose    Lose     Win
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 조건에 문자열 </span>
<span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span><span class="o">==</span><span class="s1">&#39;Lose&#39;</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[15]:</div>


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
      <th>2005</th>
      <td>Lose</td>
      <td>Lose</td>
      <td>Lose</td>
      <td>Win</td>
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
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 조건에 여러개의 값은 isin을 사용</span>
<span class="n">some_values</span>  <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Win&#39;</span><span class="p">,</span><span class="s1">&#39;Final&#39;</span><span class="p">]</span>
<span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">isin</span><span class="p">(</span><span class="n">some_values</span><span class="p">)]</span>  
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[14]:</div>


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
      <td>Final</td>
      <td>Final</td>
      <td>Lose</td>
      <td>Lose</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>Final</td>
      <td>Lose</td>
      <td>Lose</td>
      <td>Final</td>
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
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># isin의 부정 조건 </span>
<span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="o">~</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">isin</span><span class="p">([</span><span class="s1">&#39;Win&#39;</span><span class="p">])]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[19]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>[2003    True
 2004    True
 2005    True
 Name: Arizona, dtype: bool]</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#만약에 조건이 2인 경우에 &amp; 연산자를 사용.</span>
<span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;Final&#39;</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Boston&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;Final&#39;</span><span class="p">)]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[20]:</div>


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
      <td>Final</td>
      <td>Final</td>
      <td>Lose</td>
      <td>Lose</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
 

