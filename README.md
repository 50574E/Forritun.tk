Forritun.tk
===========

Vefsíða sem tekur saman þær upplýsingar sem þarf til að koma fólki af stað í forritun auk þess að vera skemmtilegur staður fyrir áhugasama að tala um forritun / forrita. Spjallborðið er eins og er eini parturinn af síðunni sem er kominn í loftið en það má nálgast [hér](http://discourse.forritun.tk).

Liðlagningar
------------
Öll þróunarumræða mun fara fram [þar](http://discourse.forritun.tk) þannig fyrir þá sem hafa áhuga á að taka þátt í þróun á síðunni endilega kíkið á [aðalþráðin](http://discourse.forritun.tk/t/throun-a-vefsidunni/15/2). Aðrar leiðir til að hafa samband eru gegnum github, [facebook](http://www.facebook.com/forritun.tk) eða með því að senda email á forritun.tk@gmail.com.

Uppsetning
==========

1. pip install -r requirements-dev.txt
2. Settu upp Postgresql grunn sem heitir forrituntk með notendanafni forrituntk og lykilorði forrituntk.
Þessu má líka breyta í forrituntk.local.
3. python manage.py syncdb
4. python manage.py runserver

Þá er hægt að opna localhost:8000.
