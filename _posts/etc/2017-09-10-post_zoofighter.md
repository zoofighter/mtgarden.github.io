---
layout: post
title: 'zoofighter'
tags: [etc]
---

## 사용법 1

지킬 사용법 1 페이지는  

https://www.qixiaodong.tk/en/2012/10/11/blogging-with-notebooks-and-jekyll.html
http://fbsight.com/t/jupyter-notebook/85937
http://www.boxnwhis.kr/2015/02/10/blogging_with_python.html
https://adamj.eu/tech/2014/09/21/using-ipython-notebook-to-write-jekyll-blog-posts/

!jupyter nbconvert --to python file_name.ipynb 
!jupyter nbconvert --to python --template basic *test*.ipynb


하지만 내가 원하는 것은 전체 HTML 문서가 아니라 웹사이트 중간에 삽입할 수 있는 HTML 조각(fragment)이다. 다음 명령을 실행하면 단일한 <div> 루트 요소를 갖는 HTML 조각을 얻어낼 수 있다:



> ipython nbconvert --to html --template basic test.ipynb


jupyter nbconvert --to html --template basic test.ipynb

jupyter nbconvert --to html --template basic *.ipynb

[Get *The Fast One* on GitHub](https://github.com/qwtel/hydejack/releases)

[docs]: https://qwtel.com/hydejack/docs/
[gpsi]: https://developers.google.com/speed/pagespeed/insights/?url=http%3A%2F%2Fqwtel.com%2Fhydejack%2F

*[FOUC]: Flash Of Unstyled Content
