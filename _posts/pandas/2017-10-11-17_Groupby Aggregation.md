---
layout: post
title: '20_Groupby Aggregation'
tags: [Pandas]
---

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>DataFrameGroupBy# Aggregate</p>
<ul>
<li>Groupby 객체의  Aggregate 메소드 <a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.groupby.DataFrameGroupBy.agg.html">docs</a>
는 그룹함수들을 수집하여 한번에 처리하는 기능으로  DataFrameGroupBy.agg(arg, * args,  kwargs)로 표현된다.<ul>
<li>args에 string, tuple, dicionary, list 를 입력할 수 있다.</li>
</ul>
</li>
<li><p>Agg(Aggregate) 메소드는 다음 용도로 사용된다.</p>
<ul>
<li>count, sum, mean, min, max, first, last같은 그룹함수를 동시에 사용할 경우에 </li>
<li>자신만의 데이터 집계함수를 사용(즉, 사용자 집계함수)</li>
</ul>
</li>
<li><h2 id="Agg&#47484;-&#49324;&#50857;&#54616;&#45716;-&#45824;&#54364;&#51201;&#51064;-&#54364;&#54788;&#51004;&#47196;&#45716;-&#52972;&#47100;&#44284;-&#51201;&#50857;-&#51665;&#44228;&#54632;&#49688;&#47484;-&#46357;&#49492;&#45320;&#47532;&#47196;-&#47564;&#46308;&#44256;-&#44536;-&#46357;&#49492;&#45320;&#47532;&#47484;-&#53916;&#54540;&#47196;-&#47564;&#46308;&#50612;-Agg&#47700;&#49548;&#46300;&#51032;-&#51064;&#51088;&#47196;-&#45347;&#45716;-&#48169;&#48277;&#51060;&#45796;.">Agg&#47484; &#49324;&#50857;&#54616;&#45716; &#45824;&#54364;&#51201;&#51064; &#54364;&#54788;&#51004;&#47196;&#45716; &#52972;&#47100;&#44284; &#51201;&#50857; &#51665;&#44228;&#54632;&#49688;&#47484; &#46357;&#49492;&#45320;&#47532;&#47196; &#47564;&#46308;&#44256; &#44536; &#46357;&#49492;&#45320;&#47532;&#47484; &#53916;&#54540;&#47196; &#47564;&#46308;&#50612; Agg&#47700;&#49548;&#46300;&#51032; &#51064;&#51088;&#47196; &#45347;&#45716; &#48169;&#48277;&#51060;&#45796;.<a class="anchor-link" href="#Agg&#47484;-&#49324;&#50857;&#54616;&#45716;-&#45824;&#54364;&#51201;&#51064;-&#54364;&#54788;&#51004;&#47196;&#45716;-&#52972;&#47100;&#44284;-&#51201;&#50857;-&#51665;&#44228;&#54632;&#49688;&#47484;-&#46357;&#49492;&#45320;&#47532;&#47196;-&#47564;&#46308;&#44256;-&#44536;-&#46357;&#49492;&#45320;&#47532;&#47484;-&#53916;&#54540;&#47196;-&#47564;&#46308;&#50612;-Agg&#47700;&#49548;&#46300;&#51032;-&#51064;&#51088;&#47196;-&#45347;&#45716;-&#48169;&#48277;&#51060;&#45796;.">&#182;</a></h2><ul>
<li>ex) tuple_dic = {2000:['count','mean'], 2001:['max']}</li>
<li>ex) df.groupby(['Team','Season']).agg(tuple_dic)</li>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>

<span class="n">arrays</span> <span class="o">=</span> <span class="p">[[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span><span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">,</span> <span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span><span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>
         <span class="p">,[</span><span class="s1">&#39;First&#39;</span><span class="p">,</span><span class="s1">&#39;First&#39;</span><span class="p">,</span><span class="s1">&#39;First&#39;</span><span class="p">,</span><span class="s1">&#39;First&#39;</span><span class="p">,</span><span class="s1">&#39;Second&#39;</span><span class="p">,</span><span class="s1">&#39;Second&#39;</span><span class="p">,</span><span class="s1">&#39;Second&#39;</span><span class="p">,</span><span class="s1">&#39;Second&#39;</span><span class="p">]]</span>
<span class="n">index</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">MultiIndex</span><span class="o">.</span><span class="n">from_arrays</span><span class="p">(</span><span class="n">arrays</span><span class="p">,</span> <span class="n">names</span><span class="o">=</span><span class="p">(</span><span class="s1">&#39;City&#39;</span><span class="p">,</span><span class="s1">&#39;Season&#39;</span><span class="p">))</span>
<span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2003</span><span class="p">,</span> <span class="mi">2004</span><span class="p">,</span> <span class="mi">2005</span><span class="p">]</span>
<span class="c1">#df = pd.DataFrame(np.random.randn(8, 3), index=index, columns = columns)</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">24</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">((</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">)),</span> <span class="n">index</span><span class="o">=</span><span class="n">index</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>
<span class="n">df</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[1]:</div>


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
      <th></th>
      <th>2003</th>
      <th>2004</th>
      <th>2005</th>
    </tr>
    <tr>
      <th>City</th>
      <th>Season</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arizona</th>
      <th>First</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Boston</th>
      <th>First</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Chicago</th>
      <th>First</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Detroit</th>
      <th>First</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <th>Second</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>Boston</th>
      <th>Second</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <th>Chicago</th>
      <th>Second</th>
      <td>18</td>
      <td>19</td>
      <td>20</td>
    </tr>
    <tr>
      <th>Detroit</th>
      <th>Second</th>
      <td>21</td>
      <td>22</td>
      <td>23</td>
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
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># dictionary의 tuple을 인자로 사용 </span>
<span class="n">tu_dic</span> <span class="o">=</span> <span class="p">{</span><span class="mi">2003</span><span class="p">:[</span><span class="s1">&#39;count&#39;</span><span class="p">,</span><span class="s1">&#39;mean&#39;</span><span class="p">],</span> <span class="mi">2004</span><span class="p">:[</span><span class="s1">&#39;max&#39;</span><span class="p">]}</span>
<span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;Season&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">agg</span><span class="p">(</span><span class="n">tu_dic</span><span class="p">)</span>
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
    <tr>
      <th></th>
      <th colspan="2" halign="left">2003</th>
      <th>2004</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Season</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First</th>
      <td>4</td>
      <td>4.5</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Second</th>
      <td>4</td>
      <td>16.5</td>
      <td>22</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># columns의 값들에 조건을 추가</span>
<span class="n">tu_dic</span> <span class="o">=</span> <span class="p">{</span><span class="mi">2003</span><span class="p">:[</span><span class="s1">&#39;count&#39;</span><span class="p">,</span><span class="s1">&#39;mean&#39;</span><span class="p">],</span> <span class="mi">2004</span><span class="p">:[</span><span class="s1">&#39;max&#39;</span><span class="p">]}</span>
<span class="n">df</span><span class="p">[(</span><span class="n">df</span><span class="p">[</span><span class="mi">2003</span><span class="p">]</span><span class="o">&gt;</span><span class="mi">5</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="mi">2004</span><span class="p">]</span><span class="o">&gt;</span><span class="mi">3</span><span class="p">)]</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;Season&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">agg</span><span class="p">(</span><span class="n">tu_dic</span><span class="p">)</span>
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
    <tr>
      <th></th>
      <th colspan="2" halign="left">2003</th>
      <th>2004</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Season</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First</th>
      <td>2</td>
      <td>7.5</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Second</th>
      <td>4</td>
      <td>16.5</td>
      <td>22</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># reset_index을 사용하여 index를 columns을 변경할 수 있음</span>
<span class="n">tu_dic</span> <span class="o">=</span> <span class="p">{</span><span class="mi">2003</span><span class="p">:[</span><span class="s1">&#39;count&#39;</span><span class="p">,</span><span class="s1">&#39;mean&#39;</span><span class="p">],</span> <span class="mi">2004</span><span class="p">:[</span><span class="s1">&#39;max&#39;</span><span class="p">]}</span>
<span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;Season&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">agg</span><span class="p">(</span><span class="n">tu_dic</span><span class="p">)</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
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
    <tr>
      <th></th>
      <th>Season</th>
      <th colspan="2" halign="left">2003</th>
      <th>2004</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>First</td>
      <td>4</td>
      <td>4.5</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Second</td>
      <td>4</td>
      <td>16.5</td>
      <td>22</td>
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
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Index객체의 속성을 사용하여 컬럼의 이름을 하나로 축약</span>
<span class="n">gpby</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;Season&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">agg</span><span class="p">(</span><span class="n">tu_dic</span><span class="p">)</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
<span class="n">gpby</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Index</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span><span class="o">+</span> <span class="s1">&#39;_&#39;</span><span class="o">+</span> <span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">gpby</span><span class="o">.</span><span class="n">columns</span><span class="o">.</span><span class="n">tolist</span><span class="p">()])</span> 
<span class="n">gpby</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[5]:</div>


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
      <th>Season_</th>
      <th>2003_count</th>
      <th>2003_mean</th>
      <th>2004_max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>First</td>
      <td>4</td>
      <td>4.5</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Second</td>
      <td>4</td>
      <td>16.5</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
 

