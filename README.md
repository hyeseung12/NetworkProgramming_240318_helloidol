# helloidol

---

1. startproject helloidol
   1. python -m pip install django~=4.2
      + 4.2 중 최신 버전 설치
   2. django-admin startproject _helloidol_ .
   3. [python manage.py migrate]
   4. python manage.py runserver
2. startapp _playground_
   1. Terminal
      1. python manage.py startapp _playground_
   2. helloidol/settings.py
      1. 'playground', in INSTALLED_APPS
3. playground/
   - 정보 전달: urls -> views -> (models -> )templates
   - 코드 작성: (models ->) views -> templates -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye_html()_
      4. ->templates에 context 전달
   2. urls
      1. _playground/hello/_ -> _say_hello()_
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
      3. _playground/_ -> _bye_html/_ -> _say_bye_html()_
5. startapp 여자친구
   1. Terminal
      1. python manage.py startapp 여자친구
   2. helloidol/settings.py
      1. '여자친구',  in INSTALLED_APPS
6. 여자친구/
   1. views
      1. show_유주()
      2. show_소원()
      3. show_예린()
      4. show_신비()
      5. show_엄지()
      6. show_은하()
      7. -> templates에 context 전달
      8. 정보를 하나로 묶고, 거기에서 꺼내오자
      9. show_멤버()
      10. image link -> image file(static)
      11. show_멤버리스트()
   2. templates/여자친구/
      1. 유주.html
         1. title: 여자친구 - 유주
         2. h1: 여자친구
         3. h2: 유주
         4. img: 유주 프로필 사진
            1. border-radius: 50%
      2. ~~소원.html~~
      3. ~~예린.html~~
      4. ~~신비.html~~
      5. ~~엄지.html~~
      6. ~~은하.html~~
      7. 멤버.html
         1. group_name, name, img_src
         2. `{% load static %} <img src="{% static img_src %}">`
      8. 멤버리스트.html
         1. {% url '앱이름:path이름' %}
         2. {% url '앱이름:path이름' 변수=값 %}
   3. urls
      1. ~~여자친구/ -> 유주/ -> show_유주()~~
      2. ~~여자친구/ -> 소원/ -> show_소원()~~
      3. ~~여자친구/ -> 예린/ -> show_예린()~~
      4. ~~여자친구/ -> 신비/ -> show_신비()~~
      5. ~~여자친구/ -> 엄지/ -> show_엄지()~~
      6. ~~여자친구/ -> 은하/ -> show_은하()~~
      7. `여자친구/ -> <멤버>/ -> show_멤버(멤버)`
      8. 여자친구/ -> 멤버리스트/ -> show_멤버리스트()
   4. static/여자친구/images
      1. 소원.jpeg, 신비.jpeg, 엄지.jpeg, 예린.jpeg, 유주.jpeg, 은하.jpeg