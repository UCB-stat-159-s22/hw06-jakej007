#!/bin/bash -i

jupyter-book config sphinx .
sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000

jupyter-book build .

https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html

cd _build/html
python -m http.server