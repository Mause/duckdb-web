---
layout: docu
title: Third Party Extensions
---

{% assign extensions = site.data.extensions | sort %}
<dl>
{% for extension_hash in extensions %}
{% if extension_hash[0] != "schema" %}
{% assign extension = extension_hash[1] %}

<dt>
    <a href="{{extension.git_repository}}">{{extension.name}}</a>
    {% if extension.git_repository %}
    {% assign short_repo = extension.git_repository | split:"https://github.com/" | last %}

    <img src="https://img.shields.io/github/stars/{{ short_repo }}?style=social" style="height: 20px; width: auto; margin: 0" />
    {% else %}
    - closed source
    {% endif %}
</dt>

<dd>
{{extension.description}}

<br/><br/>
</dd>
{% endif %}
{% endfor %}
</dl>
