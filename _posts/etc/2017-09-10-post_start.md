---
layout: post
title: 'jekyll 사용법1'
tags: [etc]

---

## 사용법 1

지킬 사용법 1 페이지는  

https://nolboo.kim/blog/2013/10/15/free-blog-with-github-jekyll/
https://nolboo.kim/blog/2013/10/06/github-for-beginner/

포스트 작성법
http://jekyllrb-ko.github.io/docs/posts/

layout: post
title: 'jekyll 사용법1'
tags: [etc]
description: > description ??

tag 다는 것 섹션 나누는 것

date: 2017-01-07 00:00:00
categories: [blog, jekyll]
author: "Bart Simpson"
meta: "Springfield"
comments: true
description: >
  jekyll description'


The page now scores roughly 90/100 on [Google's PageSpeed Insights][gpsi] (up 

## Major

* HTML, CSS and JS served minified.
* JS downloading starts only after the rest of the page is rendered.
* Critical CSS (above-the-fold) is inlined into the document, the rest is fetched later.

In order to minify the CSS and make it more modular it has been rewritten in SCSS.


## 해결해야 할 것

* about 과 documentation 을 어디로 보내야 함
* tag 다는 것 정확히
* 글 기본형식 올리는 것 폼  
* sublime text for jekyll 사용법
* jupyter for jekyll 
* 구글 킵에 있는 것들.



** 이 내용 들까지는 블로그에 적는다.
* Tabindex for tab navigation
* Social media icons easier tappable with finger


Not strictly part of the release, but the images have been blurred to increase text readability and
help with loading speed as well (burred images get compressed by JPG much better).

***

git init

git remote add origin 저장소URL

git add .

git commit -m "Initialize blog"

git push origin master


***

---

 ipython nbconvert --to html test.ipynb



하지만 내가 원하는 것은 전체 HTML 문서가 아니라 웹사이트 중간에 삽입할 수 있는 HTML 조각(fragment)이다. 다음 명령을 실행하면 단일한 <div> 루트 요소를 갖는 HTML 조각을 얻어낼 수 있다:



> ipython nbconvert --to html --template basic test.ipynb


jupyter nbconvert --to html --template basic test.ipynb

jupyter nbconvert --to html --template basic *.ipynb

[Get *The Fast One* on GitHub](https://github.com/qwtel/hydejack/releases)

[docs]: https://qwtel.com/hydejack/docs/
[gpsi]: https://developers.google.com/speed/pagespeed/insights/?url=http%3A%2F%2Fqwtel.com%2Fhydejack%2F

*[FOUC]: Flash Of Unstyled Content
