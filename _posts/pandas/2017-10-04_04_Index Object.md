---
layout: post
title: '04_Index Object'
tags: [Pandas]
---
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Index-Objects">Index Objects<a class="anchor-link" href="#Index-Objects">&#182;</a></h2><ul>
<li>Index Objects은 Index와 columns의 label과 메타정보를 저장하는 객체이다(The basic object storing axis labels for all pandas objects)</li>
<li>Series나 DataFrame을 생성할 때 label의 array는 자동적으로 Index 객체으로 변환되어 매핑된다. </li>
<li>순위가 있고 slicing이 가능한 arary (Immutable ndarray implementing an ordered, sliceable set)<ul>
<li>Index Object의 slicing을 가능하게 하는 index key(location)와 이에 대응하는 label이 있다. </li>
<li>label은 array로 표현되고 label이 유니크할 필요는 없다.</li>
</ul>
</li>
<li>Index 객체는 Pandas에서 가장 어려운 개념에 속한다. Python for Data Analysis에 대부분에 독자는 Index객체에 대해 자세히 몰라도 되지만 Index 객체는 pandas의 데이터 모델 중에서 중요한 부분이라 노트 표시 되어 있다.</li>
<li><p><a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Index.html">Index Objects docs</a>를 보면 Index  Objects 역시 여러가지의 메소드와 속성을 가지고 있는데 DataFrame 또는 Series의 그것들과 유사함을 확인할 수 있다.</p>
</li>
<li><p>주요 메소드과 속성을 살펴 보면</p>
<ul>
<li>Index(): Index객체를 생성함</li>
<li>df.index: DataFrame내의 index객체를 반환</li>
<li>df.columns: DataFrame내의 columns Index객체를 반환 </li>
<li>get_loc:Label의 index key(위치, position)를 반환</li>
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
<span class="n">data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">16</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">((</span><span class="mi">4</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>
<span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>
<span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2003</span><span class="p">,</span>  <span class="mi">2004</span><span class="p">,</span> <span class="mi">2005</span><span class="p">,</span> <span class="mi">2006</span><span class="p">]</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">index</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># DataFrame을 생성하 때 자동으로 index 객체가 생성이 된다.</span>
<span class="c1"># index와 columns 함수는 DataFrame에서 index Object를 반환하는 함수 있다.  </span>
<span class="n">obj1</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">index</span>
<span class="nb">print</span><span class="p">(</span><span class="n">obj1</span><span class="p">)</span>
<span class="n">obj2</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">columns</span>
<span class="nb">print</span><span class="p">(</span><span class="n">obj2</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Int64Index([2003, 2004, 2005, 2006], dtype=&#39;int64&#39;)
Index([&#39;Arizona&#39;, &#39;Boston&#39;, &#39;Chicago&#39;, &#39;Detroit&#39;], dtype=&#39;object&#39;)
</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Index 함수를 사용하여 생성함. 라벨의 중복을 허용함</span>

<span class="n">obj3</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Index</span><span class="p">([</span><span class="s1">&#39;Pari&#39;</span><span class="p">,</span> <span class="s1">&#39;Roma&#39;</span><span class="p">,</span> <span class="s1">&#39;Seoul&#39;</span><span class="p">,</span><span class="s1">&#39;Pari&#39;</span><span class="p">])</span>
<span class="n">obj3</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[3]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>Index([&#39;Pari&#39;, &#39;Roma&#39;, &#39;Seoul&#39;, &#39;Pari&#39;], dtype=&#39;object&#39;)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#index key로 indexing 하여 대응되는 label을 반환 </span>
<span class="n">obj3</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[4]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>&#39;Pari&#39;</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#index key로 slicing 하여 대응되는 label을 반환</span>
<span class="n">obj3</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">3</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[5]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>Index([&#39;Roma&#39;, &#39;Seoul&#39;], dtype=&#39;object&#39;)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># index와 columns에 직접 index객체를 넣어 생성함.</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">obj3</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">obj3</span><span class="p">)</span>

<span class="n">df</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[6]:</div>


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
      <th>Pari</th>
      <th>Roma</th>
      <th>Seoul</th>
      <th>Pari</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Pari</th>
      <td>0.790148</td>
      <td>0.520752</td>
      <td>1.509777</td>
      <td>-0.934555</td>
    </tr>
    <tr>
      <th>Roma</th>
      <td>-0.828068</td>
      <td>-0.019791</td>
      <td>-0.209718</td>
      <td>1.839801</td>
    </tr>
    <tr>
      <th>Seoul</th>
      <td>-2.189928</td>
      <td>0.003347</td>
      <td>0.809648</td>
      <td>-0.094232</td>
    </tr>
    <tr>
      <th>Pari</th>
      <td>-1.349733</td>
      <td>-0.222871</td>
      <td>0.150734</td>
      <td>-2.098341</td>
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
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">obj3</span><span class="o">.</span><span class="n">get_slice_bound</span><span class="p">(</span><span class="s1">&#39;Seoul&#39;</span><span class="p">,</span> <span class="s1">&#39;left&#39;</span><span class="p">,</span> <span class="s1">&#39;loc&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[7]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Label의 index key(위치, position)를 반환</span>
<span class="n">obj3</span><span class="o">.</span><span class="n">get_loc</span><span class="p">(</span><span class="s1">&#39;Seoul&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[8]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Label의 index key(위치, position)를 반환, label 이 중복인 경우 boolean array를 반환</span>
<span class="n">obj3</span><span class="o">.</span><span class="n">get_loc</span><span class="p">(</span><span class="s1">&#39;Pari&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[9]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>array([ True, False, False,  True], dtype=bool)</pre>
</div>

</div>

</div>
</div>

</div>
 

