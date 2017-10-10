---
layout: post
title: '08_DataFrame 자료형'
tags: [Pandas]
layout: default
comments: true
---

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="DataFrame&#51032;-&#51088;&#47308;&#54805;">DataFrame&#51032; &#51088;&#47308;&#54805;<a class="anchor-link" href="#DataFrame&#51032;-&#51088;&#47308;&#54805;">&#182;</a></h1><ul>
<li>기본적으로 pandas는 데이터의 구조를 numpy의 ndarray를 사용하기 때문에 DataFrame의 자료형 역시 ndarray를 따른다. </li>
<li><p>기본적인 type을 보면</p>
<ul>
<li>float64: 실수형 자료형</li>
<li>int64: 정수형 자료형 </li>
<li>boolean: bool 자료형</li>
<li>object: 파이선의 객체형 자료형(문자형만 담을 수도 있고 또는  문자형과 숫자형을 같이, 또는 list형을 담을 수 도  있다. <ul>
<li>Pandas에서는 따로 독립적으로 문자형을 사용하지 않는데 그 이유는 numpy의 자료형을 그대로 사용하기 때문이다. numpy는 문자형을 Object형으로 인식함 </li>
</ul>
</li>
</ul>
</li>
<li><p>자료형 DataFrame에서 확인하기 위해서는 dtypes를 사용한다.</p>
</li>
<li><p>자료형 변환을 위해서는 astype()을 사용한다.</p>
<ul>
<li>만약 int형 자료형을 문자로 변환한다면  df['co1'].astype(str)  </li>
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

<span class="n">data</span>  <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">rand</span><span class="p">(</span><span class="mi">12</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">)</span>
<span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2000</span><span class="p">,</span> <span class="mi">2001</span><span class="p">,</span> <span class="mi">2002</span> <span class="p">]</span>
<span class="n">columns_index</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">index</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns_index</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#컬럼의 타입을 확인하면 float64인 것을 확인할 수 있다.</span>
<span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">dtypes</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[2]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>Arizona    float64
Boston     float64
Chicago    float64
Detroit    float64
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#인텍스를 컬럼으로 변경하여 타입을 확인해도 float64인 것을 확인할 수 있다.</span>
<span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">T</span><span class="o">.</span><span class="n">dtypes</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[3]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2000    float64
2001    float64
2002    float64
dtype: object</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># list를 사용하여 winnder라는 컬럼을 생성 </span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Winner&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span> <span class="s1">&#39;Boston&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>  
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span> 
<span class="c1"># 자료형은 확인하면 문자형 데이터를 이용하여  Winner 컬럼을 생성했기 때문에 Winner는 Object형임 </span>
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
<pre>       Arizona    Boston   Chicago   Detroit   Winner
2000  0.093597  0.406413  0.846233  0.812615  Arizona
2001  0.808303  0.733503  0.708402  0.367251   Boston
2002  0.269071  0.118879  0.392947  0.089479  Detroit
Arizona    float64
Boston     float64
Chicago    float64
Detroit    float64
Winner      object
dtype: object
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">T</span><span class="p">)</span> 
<span class="c1"># 인덱스를 컬럼으로 변경해 보면 역시 Object형으로 변형이 되어 있음을 확인 할 수 있음</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">T</span><span class="o">.</span><span class="n">dtypes</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>              2000      2001       2002
Arizona  0.0935974  0.808303   0.269071
Boston    0.406413  0.733503   0.118879
Chicago   0.846233  0.708402   0.392947
Detroit   0.812615  0.367251  0.0894788
Winner     Arizona    Boston    Detroit
2000    object
2001    object
2002    object
dtype: object
</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#list로 생성된 Winners 컬럼의 자료형 역시 Object 형임</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Winners&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;Winner&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;,&#39;</span><span class="p">)</span> 
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span> 
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
<pre>       Arizona    Boston   Chicago   Detroit   Winner    Winners
2000  0.093597  0.406413  0.846233  0.812615  Arizona  [Arizona]
2001  0.808303  0.733503  0.708402  0.367251   Boston   [Boston]
2002  0.269071  0.118879  0.392947  0.089479  Detroit  [Detroit]
Arizona    float64
Boston     float64
Chicago    float64
Detroit    float64
Winner      object
Winners     object
dtype: object
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#float형을 Object(문자형)으로 바꾸고 문자형 함수를 적용할 수 있음</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Boston&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;Boston&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Boston&#39;</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">dtypes</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Boston&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Boston&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>2000    0.406412994797
2001     0.73350284794
2002     0.11887913438
Name: Boston, dtype: object
Arizona    float64
Boston      object
Chicago    float64
Detroit    float64
Winner      object
Winners     object
dtype: object
</pre>
</div>
</div>

<div class="output_area">
<div class="prompt output_prompt">Out[7]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2000    14
2001    13
2002    13
Name: Boston, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
 

