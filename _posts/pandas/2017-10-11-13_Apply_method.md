---
layout: post
title: '13 Apply Method'
tags: [Pandas]
---
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Apply--&#54632;&#49688;">Apply  &#54632;&#49688;<a class="anchor-link" href="#Apply--&#54632;&#49688;">&#182;</a></h2><ul>
<li>Apply 메소드는 DataFrame의 rows 나 columns(즉 1차원 어레이)을 인풋으로 하여 집합(그룹함수)를 처리할 수 있게 해 준다. <a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html">Apply docs.</a> 참조<ul>
<li>기본적으로 DataFrame의 축의 방향에 따라서 함수에 적용되는 인풋이 결정됨(즉. 열이나 행을 파라미터 값을 전달)(Applies function along input axis of DataFrame.)</li>
<li>아웃풋은 적용되는 함수(집합함수)에 결정됨( Return type depends on whether passed function aggregates)</li>
<li>참고로 R의 경우에는 apply() 함수는 배열 또는 행렬에 주어진 함수를 적용한 뒤 그 결과를 벡터, 배열 또는 리스트로 반환</li>
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
<span class="c1">#data  = np.random.randn(12).reshape((3, 4))</span>
<span class="n">data</span>  <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">12</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">((</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>
<span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>
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
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># apply가 DataFrame이 row의 array에 적용됨</span>
<span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="nb">max</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="o">-</span> <span class="nb">min</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[2]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>Arizona    8
Boston     8
Chicago    8
Detroit    8
dtype: int64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># axis = 1를 사용함으로 columns의 array에 적용됨</span>
<span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="nb">max</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="o">-</span> <span class="nb">min</span><span class="p">(</span><span class="n">x</span><span class="p">),</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[3]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>0    3
1    3
2    3
dtype: int64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span><span class="n">x</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span> <span class="c1"># 모든 rows 에 적용</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">rows</span><span class="p">:</span><span class="n">rows</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>   <span class="c1"># 첫번째 row에만 적용  </span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">columns</span><span class="p">:</span><span class="n">columns</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="n">axis</span> <span class="o">=</span><span class="mi">1</span><span class="p">))</span>  <span class="c1"># 마지막  columns 에만 적용  </span>
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
0        1       2        3        4
1        5       6        7        8
2        9      10       11       12
Arizona    1
Boston     2
Chicago    3
Detroit    4
dtype: int64
0     4
1     8
2    12
dtype: int64
</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># row 또는 columns별로 합계를 계산</span>
<span class="k">def</span> <span class="nf">add_all</span><span class="p">(</span><span class="n">row</span><span class="p">):</span>
    <span class="n">total</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">cell</span> <span class="ow">in</span> <span class="n">row</span><span class="p">:</span>
        <span class="n">total</span> <span class="o">+=</span> <span class="n">cell</span>
    <span class="k">return</span> <span class="n">total</span>

<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">add_all</span><span class="p">))</span>
<span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">add_all</span><span class="p">,</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Arizona    12
Boston     15
Chicago    18
Detroit    21
dtype: int64
</pre>
</div>
</div>

<div class="output_area">
<div class="prompt output_prompt">Out[5]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>0     6
1    22
2    38
dtype: int64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># DataFrame을 컬럼을 선택하여 범위를 정할 수 있음</span>
<span class="n">df</span><span class="p">[[</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">add_all</span><span class="p">,</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[6]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>0     3
1    11
2    19
dtype: int64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 결과 값으로  Array를 반환</span>
<span class="k">def</span> <span class="nf">add_plus_one</span><span class="p">(</span><span class="n">row</span><span class="p">):</span><span class="k">return</span> <span class="p">[</span><span class="n">cell</span> <span class="o">+</span> <span class="mi">1</span>  <span class="k">for</span> <span class="n">cell</span> <span class="ow">in</span> <span class="n">row</span><span class="p">]</span>
<span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">add_plus_one</span><span class="p">)</span>
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
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
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
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># row나 columns을 인풋으로 하여 사용자 함수에서 부분집합을 계산함</span>
<span class="k">def</span> <span class="nf">add_two</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>    
    <span class="k">return</span> <span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">+</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>  
<span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">add_two</span><span class="p">,</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[8]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>0     1
1     9
2    17
dtype: int64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># lambda를 사용하여 row나 columns 부분 집합을 인풋으로 사용함</span>
<span class="k">def</span> <span class="nf">add_xy</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">x</span> <span class="o">+</span> <span class="n">y</span>
<span class="n">df</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">row</span><span class="p">:</span> <span class="n">add_xy</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">],</span> <span class="n">row</span><span class="p">[</span><span class="s1">&#39;Chicago&#39;</span><span class="p">]),</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[9]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>0     2
1    10
2    18
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
 

