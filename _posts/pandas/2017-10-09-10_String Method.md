---
layout: post
title: '10_문자함수'
tags: [Pandas]
---
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="&#47928;&#51088;&#54632;&#49688;">&#47928;&#51088;&#54632;&#49688;<a class="anchor-link" href="#&#47928;&#51088;&#54632;&#49688;">&#182;</a></h2><ul>
<li>Pandas에는 DataFrame에서는 직접 문자함수를 사용할 수 는 없고  Series로 변환후 문자 함수를 적용 할 수 있음.  </li>
<li><p><a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.html">Series.str docs</a>를 보면 Series.str 메소드을 사용하여  Series와 Index에 python의 문자열 함수를 사용할 수 있음 (Vectorized string functions for Series and Index)</p>
</li>
<li><p>대표적인 메소들들은 다음과 같다.</p>
<ul>
<li>str.len(): 문자의 길이를 반환</li>
<li>str[]: slicing을 적용(sql의 subsring 처럼 사용할 수 있음)</li>
<li>str.split(): 구분자에 의해 문자열을 분해</li>
<li>str.cat(): 문장열을 연결</li>
<li>str.get(): 위치에 따라 요소를 반환</li>
<li>str.replace(): 문자를 서로 치환</li>
<li>str.contains() : 문자가 포함 되어 있는지 boolean array를 반환</li>
<li>str.find(): 찾는 문자가 있으면 위치를 반환</li>
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
<span class="n">data</span>  <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">12</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">((</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>
<span class="c1">#data = np.random.randn(3,4)</span>

<span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2003</span><span class="p">,</span> <span class="mi">2004</span><span class="p">,</span> <span class="mi">2005</span> <span class="p">]</span>
<span class="n">columns</span><span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">data</span> <span class="o">=</span> <span class="p">([[</span> <span class="n">row</span> <span class="o">+</span> <span class="s1">&#39;_&#39;</span> <span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="n">col</span><span class="p">)</span> <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">]</span> <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">index</span><span class="p">])</span>
<span class="n">data</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[2]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>[[&#39;Arizona_2003&#39;, &#39;Boston_2003&#39;, &#39;Chicago_2003&#39;, &#39;Detroit_2003&#39;],
 [&#39;Arizona_2004&#39;, &#39;Boston_2004&#39;, &#39;Chicago_2004&#39;, &#39;Detroit_2004&#39;],
 [&#39;Arizona_2005&#39;, &#39;Boston_2005&#39;, &#39;Chicago_2005&#39;, &#39;Detroit_2005&#39;]]</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">index</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>
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
      <th>2003</th>
      <td>Arizona_2003</td>
      <td>Boston_2003</td>
      <td>Chicago_2003</td>
      <td>Detroit_2003</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>Arizona_2004</td>
      <td>Boston_2004</td>
      <td>Chicago_2004</td>
      <td>Detroit_2004</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>Arizona_2005</td>
      <td>Boston_2005</td>
      <td>Chicago_2005</td>
      <td>Detroit_2005</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#- str.len() 크기</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Boston&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">len</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[4]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2003    11
2004    11
2005    11
Name: Boston, dtype: int64</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># - str[]  문자열 slicing을 취함</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Boston&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="p">[</span><span class="mi">3</span><span class="p">:</span><span class="mi">9</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[5]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2003    ton_20
2004    ton_20
2005    ton_20
Name: Boston, dtype: object</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># split메소드를 사용하여 구분자 &#39;_&#39;에 따라 문장열을 분리</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;_&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[6]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2003    [Arizona, 2003]
2004    [Arizona, 2004]
2005    [Arizona, 2005]
Name: Arizona, dtype: object</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># split메소드 사용후 get메소드를 사용하면 요소를 반환할 수 있음</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;_&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[7]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2003    2003
2004    2004
2005    2005
Name: Arizona, dtype: object</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># cat을 사용하여 문자열 연결</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">cat</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Detroit&#39;</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[8]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2003    Arizona_2003Detroit_2003
2004    Arizona_2004Detroit_2004
2005    Arizona_2005Detroit_2005
Name: Arizona, dtype: object</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># replace을 사용하여 &#39;_&#39;를  &#39;Cups&#39;로 치환</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Chicago&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;_&#39;</span><span class="p">,</span> <span class="s1">&#39;Cups&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[9]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2003    ChicagoCups2003
2004    ChicagoCups2004
2005    ChicagoCups2005
Name: Chicago, dtype: object</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># contains 사용하여 &#39;2003&#39; 이 있는지 확인</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">contains</span><span class="p">(</span><span class="s1">&#39;2003&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[10]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2003     True
2004    False
2005    False
Name: Arizona, dtype: bool</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#find 위치를 반환, 없으면 -1을 반환</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s1">&#39;2003&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[11]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2003    8
2004   -1
2005   -1
Name: Arizona, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
 

