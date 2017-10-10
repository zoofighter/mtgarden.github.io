---
layout: post
title: '03_DataFrame 메소드'
tags: [Pandas]
---
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="DataFrame-Method">DataFrame Method<a class="anchor-link" href="#DataFrame-Method">&#182;</a></h2><ul>
<li>DataFrame에는 200여개 넘는 Attribute와 Method(메소드)이 존재함 </li>
<li>Attribute와 Method의 간단한 차이를 말하자면 Method는 round brackets인 ()로 표시되고 ,Attribute는 round brackets 로 표시되지 않는다. 앞으로 Attribute도 메소드라 지칭한다.</li>
<li>DataFrame 관련 <a href="https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html">Pandas Docs</a>를 보면 200여개 넘는 메소들이 나열 되어있음</li>
<li><p>대표적인 메소드을 살펴 보면</p>
<ul>
<li>shape: 2차원 행렬의 크기를 반환</li>
<li>T: index와 columns의 위치를 서로 교환</li>
<li>Values:Numpy형으로 변환</li>
<li>head():상위 로우를 반환</li>
<li>Tail():하위 로우를 반환</li>
<li>descibe():기술 통계량을 요약해서 보여줌</li>
<li>rank():axis에 따른 순위를 반환</li>
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
<span class="c1">#data  = np.arange(32).reshape((8, 4))</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randn</span><span class="p">(</span><span class="mi">32</span><span class="p">)</span><span class="o">.</span><span class="n">reshape</span><span class="p">((</span><span class="mi">8</span><span class="p">,</span> <span class="mi">4</span><span class="p">))</span>
<span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;Arizona&#39;</span><span class="p">,</span><span class="s1">&#39;Boston&#39;</span><span class="p">,</span> <span class="s1">&#39;Chicago&#39;</span><span class="p">,</span><span class="s1">&#39;Detroit&#39;</span><span class="p">]</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">columns</span><span class="p">)</span>
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
      <th>Arizona</th>
      <th>Boston</th>
      <th>Chicago</th>
      <th>Detroit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-2.494833</td>
      <td>-1.397416</td>
      <td>-2.573239</td>
      <td>-1.441484</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.475692</td>
      <td>-0.948231</td>
      <td>1.402344</td>
      <td>0.854873</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.869324</td>
      <td>0.592219</td>
      <td>0.076431</td>
      <td>-0.487947</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.108055</td>
      <td>-0.967561</td>
      <td>-0.295529</td>
      <td>-0.112509</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.749410</td>
      <td>-0.780110</td>
      <td>-0.209262</td>
      <td>-0.116538</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-0.947783</td>
      <td>0.148626</td>
      <td>1.373158</td>
      <td>1.640924</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.239441</td>
      <td>-1.890217</td>
      <td>0.682607</td>
      <td>1.641995</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-0.488624</td>
      <td>-0.131904</td>
      <td>1.684033</td>
      <td>-0.920702</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#2차원 행렬의 크기를 반환</span>
<span class="n">df</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[2]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>(8, 4)</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#컬럼과 인덱스의 위치가 교환됨</span>
<span class="n">df</span><span class="o">.</span><span class="n">T</span>
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Arizona</th>
      <td>-2.494833</td>
      <td>0.475692</td>
      <td>0.869324</td>
      <td>0.108055</td>
      <td>-0.749410</td>
      <td>-0.947783</td>
      <td>-0.239441</td>
      <td>-0.488624</td>
    </tr>
    <tr>
      <th>Boston</th>
      <td>-1.397416</td>
      <td>-0.948231</td>
      <td>0.592219</td>
      <td>-0.967561</td>
      <td>-0.780110</td>
      <td>0.148626</td>
      <td>-1.890217</td>
      <td>-0.131904</td>
    </tr>
    <tr>
      <th>Chicago</th>
      <td>-2.573239</td>
      <td>1.402344</td>
      <td>0.076431</td>
      <td>-0.295529</td>
      <td>-0.209262</td>
      <td>1.373158</td>
      <td>0.682607</td>
      <td>1.684033</td>
    </tr>
    <tr>
      <th>Detroit</th>
      <td>-1.441484</td>
      <td>0.854873</td>
      <td>-0.487947</td>
      <td>-0.112509</td>
      <td>-0.116538</td>
      <td>1.640924</td>
      <td>1.641995</td>
      <td>-0.920702</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#numpy 형 array로 반환</span>
<span class="n">df</span><span class="o">.</span><span class="n">values</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[4]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>array([[-2.49483318, -1.39741573, -2.57323916, -1.44148414],
       [ 0.47569211, -0.94823096,  1.40234424,  0.85487322],
       [ 0.86932388,  0.59221938,  0.07643134, -0.48794711],
       [ 0.10805456, -0.96756072, -0.29552902, -0.11250886],
       [-0.74941002, -0.78011002, -0.20926155, -0.11653832],
       [-0.94778329,  0.14862561,  1.37315768,  1.64092446],
       [-0.23944107, -1.89021668,  0.68260669,  1.64199494],
       [-0.48862351, -0.13190406,  1.68403309, -0.92070157]])</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#상위 3 줄 반환</span>
<span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
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
      <th>Arizona</th>
      <th>Boston</th>
      <th>Chicago</th>
      <th>Detroit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-2.494833</td>
      <td>-1.397416</td>
      <td>-2.573239</td>
      <td>-1.441484</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.475692</td>
      <td>-0.948231</td>
      <td>1.402344</td>
      <td>0.854873</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.869324</td>
      <td>0.592219</td>
      <td>0.076431</td>
      <td>-0.487947</td>
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
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#하위 3줄을 반환</span>
<span class="n">df</span><span class="o">.</span><span class="n">tail</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
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
      <th>Arizona</th>
      <th>Boston</th>
      <th>Chicago</th>
      <th>Detroit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>-0.947783</td>
      <td>0.148626</td>
      <td>1.373158</td>
      <td>1.640924</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.239441</td>
      <td>-1.890217</td>
      <td>0.682607</td>
      <td>1.641995</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-0.488624</td>
      <td>-0.131904</td>
      <td>1.684033</td>
      <td>-0.920702</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#요약 통계량을 보여줌</span>
<span class="n">df</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
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
      <th>count</th>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-0.433378</td>
      <td>-0.671824</td>
      <td>0.267568</td>
      <td>0.132327</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.033119</td>
      <td>0.823668</td>
      <td>1.380468</td>
      <td>1.144515</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-2.494833</td>
      <td>-1.890217</td>
      <td>-2.573239</td>
      <td>-1.441484</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.799003</td>
      <td>-1.075024</td>
      <td>-0.230828</td>
      <td>-0.596136</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.364032</td>
      <td>-0.864170</td>
      <td>0.379519</td>
      <td>-0.114524</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.199964</td>
      <td>-0.061772</td>
      <td>1.380454</td>
      <td>1.051386</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.869324</td>
      <td>0.592219</td>
      <td>1.684033</td>
      <td>1.641995</td>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#세로 축으로 순위를 반환</span>
<span class="n">df</span><span class="o">.</span><span class="n">rank</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[8]:</div>


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
      <td>1.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>4.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>2.0</td>
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
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#가로 축으로 순위를 반한</span>
<span class="n">df</span><span class="o">.</span><span class="n">rank</span><span class="p">(</span><span class="n">axis</span><span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[9]:</div>


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
      <td>2.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
 

