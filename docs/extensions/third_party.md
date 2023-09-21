---
layout: docu
title: Third Party Extensions
---

A number of third party extensions have been written using our [extension template](https://github.com/duckdb/extension-template). The information available on this page is also available at [/data/extensions.json](/data/extensions.json). You can add a new extension to this repository by [submitting a pull request](https://github.com/Mause/duckdb-web/new/third-party-extensions/_data/extensions)

{% assign extensions = site.data.extensions | sort %}
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Install command</th>
</tr>
</thead>
<tbody>

{% for extension_hash in extensions %}
{% if extension_hash[0] != "schema" %}
{% assign extension = extension_hash[1] %}

<tr>
<td>
    <a href="{{extension.git_repository}}">{{extension.name}}</a>
    {% if extension.git_repository %}
    {% assign short_repo = extension.git_repository | split:"https://github.com/" | last %}

    <img src="https://img.shields.io/github/stars/{{ short_repo }}?style=social" style="height: 20px; width: auto; margin: 0" />
    {% endif %}
</td>
<td>{{extension.description}}</td>
<td>
{% if extension.extension_repository %}
{% highlight sql %}
INSTALL {{extension.name}} FROM 'http://{{extension.extension_repository}}';
{% endhighlight %}
{% endif %}
</td>
</tr>

{% endif %}
{% endfor %}
</tbody>
</table>
