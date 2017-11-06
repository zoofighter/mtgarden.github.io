---
layout: post
title: '05 build in function'
tags: [Python]
---

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Built_in-function">Built_in function<a class="anchor-link" href="#Built_in-function">&#182;</a></h1><ul>
<li>Python <a href="https://docs.python.org/3.6/library/functions.html">내장함수 docs</a>에서 알파벳 순으로 함수 목록을 확인할 수 있다.</li>
<li>속성별로 분류를 해보면<ul>
<li>산술연산함수:abs, bin, oct, hex, pow, round, divmod, hash</li>
<li>기본 타입/클래스 생성자:bool, bytearray, bytes, complex, dict, float, frozenset, int, list, memoryview, object, slice, str, tuple, zip</li>
<li>실행관련:complie, eval, exec</li>
<li>연속열/반복관련:all, any, enumrate, filter, iter, len, map, max, min, next, range reversed, sorted, sum, </li>
<li>문자열과 IO관련:ascii, chr, foramt, ord, repr, input, open,print</li>
<li>객체와 모듈관련:help, callable, delattr, dir, gettattr, globals, hasattr, id, isinstance, issubclass, locals, setattar, type, vars</li>
<li>그외:classmethod, staticmethod, property, supter, <em>import</em></li>
</ul>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="all">all<a class="anchor-link" href="#all">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">all</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">all</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">0</span><span class="p">]))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>True
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
<h2 id="enumerate">enumerate<a class="anchor-link" href="#enumerate">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">name</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">([</span><span class="s1">&#39;a&#39;</span><span class="p">,</span> <span class="s1">&#39;bc&#39;</span><span class="p">,</span> <span class="s1">&#39;dc&#39;</span><span class="p">]):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span>

    
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>0 a
1 bc
2 dc
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
<h2 id="ord,-char">ord, char<a class="anchor-link" href="#ord,-char">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">ord</span><span class="p">(</span><span class="s1">&#39;a&#39;</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">chr</span><span class="p">(</span><span class="mi">99</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>97
c
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
<h2 id="Sorted">Sorted<a class="anchor-link" href="#Sorted">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">sorted</span><span class="p">([</span><span class="s1">&#39;a&#39;</span><span class="p">,</span><span class="s1">&#39;c&#39;</span><span class="p">,</span><span class="s1">&#39;b&#39;</span><span class="p">]))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">sorted</span><span class="p">(</span><span class="s2">&quot;zero&quot;</span><span class="p">))</span>
<span class="c1">#리스트 자료형의 sort함수는 리스트 객체 그 자체를 소트할 뿐이지 소트된 결과를 리턴하지는 않는다.</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]
[&#39;e&#39;, &#39;o&#39;, &#39;r&#39;, &#39;z&#39;]
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
<h2 id="reversed">reversed<a class="anchor-link" href="#reversed">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="nb">reversed</span><span class="p">(</span><span class="s2">&quot;zero&quot;</span><span class="p">))</span>
<span class="c1">#In Python, reversed  returns a reverse iterator.</span>
<span class="n">rev_zero</span><span class="o">=</span> <span class="nb">reversed</span><span class="p">(</span><span class="s2">&quot;zero&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">rev_zero</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span> <span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">reversed</span><span class="p">(</span><span class="s1">&#39;abcde&#39;</span><span class="p">)))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;reversed object at 0x7f9418090860&gt;
[&#39;o&#39;, &#39;r&#39;, &#39;e&#39;, &#39;z&#39;]
edcba
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
<h2 id="Filter">Filter<a class="anchor-link" href="#Filter">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">positive</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">x</span> <span class="o">&gt;</span> <span class="mi">0</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="nb">filter</span><span class="p">(</span><span class="n">positive</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">3</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">])))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>[1, 2, 6]
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
<h2 id="Range">Range<a class="anchor-link" href="#Range">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">a</span><span class="p">))</span>
<span class="c1"># range() 함수의 결과는 반복가능(iterable) 함 </span>
<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">)))</span>
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
<pre>&lt;class &#39;range&#39;&gt;
[10, 8, 6, 4, 2]
10
8
6
4
2
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
<h1 id="zip">zip<a class="anchor-link" href="#zip">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">list1</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;one&#39;</span><span class="p">,</span> <span class="s1">&#39;two&#39;</span><span class="p">]</span>
<span class="n">list2</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;X&#39;</span><span class="p">,</span><span class="s1">&#39;Y&#39;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">list1</span><span class="p">,</span> <span class="n">list2</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">list1</span><span class="p">,</span> <span class="n">list2</span><span class="p">)))</span>
<span class="n">aa</span> <span class="o">=</span> <span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">list1</span><span class="p">,</span> <span class="n">list2</span><span class="p">))</span>
<span class="c1">#생성된 zip을 다시 분해 </span>
<span class="n">zip1</span><span class="p">,</span> <span class="n">zip2</span> <span class="o">=</span> <span class="nb">zip</span><span class="p">(</span><span class="o">*</span><span class="n">aa</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">zip1</span><span class="p">,</span> <span class="n">zip2</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;zip object at 0x7f941809b708&gt;
[(&#39;one&#39;, &#39;X&#39;), (&#39;two&#39;, &#39;Y&#39;)]
(&#39;one&#39;, &#39;two&#39;) (&#39;X&#39;, &#39;Y&#39;)
</pre>
</div>
</div>

</div>
</div>

</div>
 

