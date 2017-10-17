---
layout: post
title: '14 Index, Column Method'
tags: [Pandas]
---
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Index,-Column-Method">Index, Column Method<a class="anchor-link" href="#Index,-Column-Method">&#182;</a></h1><ul>
<li>Pandas에서는 Index와 Columns이 객체임으로 객체 안에 중요한 정보를 다루기 위한 메소들이 존재함</li>
<li>대표적인 방법들 정리해 보면<ol>
<li>Reset_index: index를 columns의 하나로 변형시키고 0부터 n-1 까지 새로운 index를 추가</li>
<li>Setindex: reset_index와는 반대로 columns 중에 하나를 index로 변경</li>
<li>drop([row]) : index의 row를 삭제함 </li>
<li>drop([col], axis=1): 컬럼을 삭제</li>
<li>df[df.name != 'Tina']: 특정컬럼의 조건 로우만 삭제</li>
<li>컬럼이름 변경: df.rename</li>
<li>컬럼 Slicing을 통한 DagaFrame내 컬럼 내 위치변경</li>
</ol>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="n">data</span>  <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">12</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">((</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>

<span class="n">index</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2002</span><span class="p">,</span> <span class="mi">2003</span><span class="p">,</span> <span class="mi">2004</span><span class="p">]</span>
<span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">index</span> <span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># index에 &#39;Year&#39;라는 이름을 부여함</span>
<span class="n">df</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="s1">&#39;Year&#39;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">index</span><span class="p">)</span>
<span class="n">df</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># reset_index를 사용하여 &#39;Year&#39;가 하나의 컬럼으로 변경됨</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
<span class="n">df</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 컬럼 &#39;Arizona&#39;  set_index()메소드를 사용하여 index로 변경</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s1">&#39;Arizona&#39;</span><span class="p">)</span>
<span class="n">df</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#index를 인풋으로 drop메소드 사용 </span>
<span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">4</span><span class="p">])</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># drop메소드 사용시 columm이 인풋이면 axis = 1를 추가 해야 함</span>
<span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span><span class="s1">&#39;Year&#39;</span><span class="p">],</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 특정컬럼의 조건만 삭제</span>
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Boston&#39;</span><span class="p">]</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">]</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 컬럼이름 변경</span>

<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;Year&#39;</span><span class="p">:</span> <span class="s1">&#39;Arizona&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">:</span> <span class="s1">&#39;Chicago2&#39;</span><span class="p">})</span>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># 컬럼 Slicing을 통한 DagaFrame 위치변경</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">index</span> <span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>
<span class="n">cols</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span>
<span class="n">cols</span> <span class="o">=</span> <span class="n">cols</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">:]</span> <span class="o">+</span> <span class="n">cols</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="n">cols</span><span class="p">]</span>
<span class="n">df</span>
</pre></div>

</div>
</div>
</div>

</div>
 

