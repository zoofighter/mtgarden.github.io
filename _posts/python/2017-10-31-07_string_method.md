---
layout: post
title: '07 string mehtod'
tags: [Python]
---

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="String-Method">String Method<a class="anchor-link" href="#String-Method">&#182;</a></h1><ul>
<li>파이썬의 string은 객체이므로 문자를 다루는 여러 메소드들이 존재함</li>
<li>중요 메소드들을 살펴보면 다음과 같다.<ul>
<li>문자열의 변환: upper(), lower(), swapcase(), capitalize(), title()</li>
<li>문자열의 검색: count(), find(), index(), startwitch()</li>
<li>분리, 결합, 치환:split(),splitlines(),join(), replace(), strip()</li>
<li>문자열 판별:isdigit(), isalpha(), isspace()</li>
<li>정렬과 채움:center(), rjust(), ljust(), zfill()</li>
</ul>
</li>
<li>파이썬에서 String은 객체이므로 dir(str) 명령어를 입력하면 사용가능함 메소드들을 확인할 수 있다.</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="&#47928;&#51088;&#50676;&#51032;-&#48320;&#54872;">&#47928;&#51088;&#50676;&#51032; &#48320;&#54872;<a class="anchor-link" href="#&#47928;&#51088;&#50676;&#51032;-&#48320;&#54872;">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[54]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Bother Sister&quot;</span><span class="o">.</span><span class="n">upper</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Bother Sister&quot;</span><span class="o">.</span><span class="n">capitalize</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;bother sister&quot;</span><span class="o">.</span><span class="n">title</span><span class="p">())</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>BOTHER SISTER
Bother sister
Bother Sister
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
<h2 id="&#47928;&#51088;&#50676;-&#48516;&#47532;,-&#44208;&#54633;,-&#52824;&#54872;">&#47928;&#51088;&#50676; &#48516;&#47532;, &#44208;&#54633;, &#52824;&#54872;<a class="anchor-link" href="#&#47928;&#51088;&#50676;-&#48516;&#47532;,-&#44208;&#54633;,-&#52824;&#54872;">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[49]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;---split---&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;010-12x4-56y8&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;-&#39;</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;010-12x4-56y8&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;-&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">a</span> <span class="o">=</span> <span class="s1">&#39;010-12x4-56y8&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;-&#39;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;---join---&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">a</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot; &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">a</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;-&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">a</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;---strip---&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;---010 12x4 56y8--&#39;</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s1">&#39;-&#39;</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;uu010 12x4 56y8UU&#39;</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s1">&#39;uu&#39;</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;---replace---&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;---010-12x4-56y8--&#39;</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;-&#39;</span><span class="p">,</span><span class="s1">&#39;&#39;</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;---010-12x4-56y8--&#39;</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;-&#39;</span><span class="p">,</span><span class="s1">&#39;**&#39;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>---split---
[&#39;010&#39;, &#39;12x4&#39;, &#39;56y8&#39;]
[&#39;010&#39;, &#39;12x4-56y8&#39;]
[&#39;010&#39;, &#39;12x4&#39;, &#39;56y8&#39;]
---join---
01012x456y8
010 12x4 56y8
010-12x4-56y8
---strip---
010 12x4 56y8
010 12x4 56y8UU
---replace---
01012x456y8
******010**12x4**56y8****
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
<h2 id="&#47928;&#51088;&#50676;&#51032;-&#44160;&#49353;">&#47928;&#51088;&#50676;&#51032; &#44160;&#49353;<a class="anchor-link" href="#&#47928;&#51088;&#50676;&#51032;-&#44160;&#49353;">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="s2">&quot;To day is the greatest day. I&#39;ve ever known&quot;</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s2">&quot;day&quot;</span><span class="p">)</span>
<span class="s2">&quot;To day is the greatest day. I&#39;ve ever known&quot;</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">&quot;To&quot;</span><span class="p">)</span>
<span class="s2">&quot;To day is the greatest day. I&#39;ve ever known&quot;</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s2">&quot;day&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[67]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="s2">&quot;To day is the greatest day. I&#39;ve ever known&quot;</span><span class="o">.</span><span class="n">rfind</span><span class="p">(</span><span class="s2">&quot;dae&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[67]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>-1</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[64]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="s2">&quot;great&quot;</span> <span class="ow">in</span> <span class="s2">&quot;To day is the greatest day. I&#39;ve ever known&quot;</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[64]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>True</pre>
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
<h2 id="&#47928;&#51088;&#50676;-&#54032;&#48324;">&#47928;&#51088;&#50676; &#54032;&#48324;<a class="anchor-link" href="#&#47928;&#51088;&#50676;-&#54032;&#48324;">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[71]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;12ab&quot;</span><span class="o">.</span><span class="n">isalnum</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;aa&quot;</span><span class="o">.</span><span class="n">isdigit</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;aa bb&quot;</span><span class="o">.</span><span class="n">isspace</span><span class="p">())</span>
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
False
</pre>
</div>
</div>

</div>
</div>

</div>
 

