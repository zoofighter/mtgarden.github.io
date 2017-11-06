---
layout: post
title: '06 built-in-type'
tags: [Python]
---

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Built-in-Types">Built-in Types<a class="anchor-link" href="#Built-in-Types">&#182;</a></h1><ul>
<li><a href="https://docs.python.org/3/library/stdtypes.html">Built-in Types docs</a> 보면 다음과 같은 Python의 기본 자료형을 확인할 수 있다.<ol>
<li>Boolean Types: 참(True) 또는 거짓(False) 값 또는 1과 0의 숫자값으로도 표현</li>
<li>Numeric Types: int(정수), float(실수), complex(복소수)</li>
<li>Iterator Types: <strong>iter</strong>(), <strong>next</strong>()(컨테이너 또는 이터레이터에 대하여 반복</li>
<li>Sequence Types: list, tuple, range (산술연산, indexing 같은  Sequence Operations을 수행)</li>
<li>Text Sequence Type:str (String Methods를 수행)</li>
<li>Set Types:set, frozentset(정렬되지 않은 유일한 개체의 모음)</li>
<li>Mapping Types:dictionary(연관배열의 키와 값의 쌍의 집합형 자료형</li>
</ol>
</li>
</ul>
<ul>
<li>변경 가능형 : list, dict, set
변경 불가능형 : int, float, complex, bool, tuple, str</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Boolean-Types">Boolean Types<a class="anchor-link" href="#Boolean-Types">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="kc">True</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">a</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="n">a</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;bool&#39;&gt;
True
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">b</span> <span class="o">=</span> <span class="kc">False</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">b</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">bool</span><span class="p">(</span><span class="n">b</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;bool&#39;&gt;
False
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
<h2 id="Numeric-Types">Numeric Types<a class="anchor-link" href="#Numeric-Types">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Python에는 정수나 실수형도 객체로 인식한다.</span>
<span class="n">c</span> <span class="o">=</span> <span class="mi">3</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">c</span><span class="p">))</span>
<span class="n">d</span> <span class="o">=</span> <span class="mf">3.3</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">d</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;int&#39;&gt;
&lt;class &#39;float&#39;&gt;
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
<h2 id="Iterator-Types">Iterator Types<a class="anchor-link" href="#Iterator-Types">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">x</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">]</span>
<span class="nb">type</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="n">y</span> <span class="o">=</span> <span class="nb">iter</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">y</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="n">y</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="n">y</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="n">y</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;list_iterator&#39;&gt;
1
2
3
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
<h1 id="Sequence-Types">Sequence Types<a class="anchor-link" href="#Sequence-Types">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">6</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>[1, 2, 3, 4, 5]
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
<h1 id="Text-Sequence-Type">Text Sequence Type<a class="anchor-link" href="#Text-Sequence-Type">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="s1">&#39;abcde&#39;</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">a</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>a
b
c
d
e
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
<h1 id="Set-Type">Set Type<a class="anchor-link" href="#Set-Type">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">s</span> <span class="o">=</span> <span class="nb">set</span> <span class="p">(</span><span class="n">i</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">6</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>{1, 2, 3, 4, 5}
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
<h1 id="Mapping-Types">Mapping Types<a class="anchor-link" href="#Mapping-Types">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;k&#39;</span><span class="p">:</span><span class="s1">&#39;v&#39;</span><span class="p">,</span><span class="s1">&#39;k2&#39;</span><span class="p">:</span><span class="mi">3</span><span class="p">}</span>
<span class="n">a</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[8]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>dict_items([(&#39;k&#39;, &#39;v&#39;), (&#39;k2&#39;, 3)])</pre>
</div>

</div>

</div>
</div>

</div>
 

