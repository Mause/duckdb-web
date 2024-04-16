---
title: Time Functions
layout: docu
---

This section describes functions and operators for examining and manipulating `TIME` values.

## Time Operators

The table below shows the available mathematical operators for `TIME` types.

{% duckdb_functions ['+', '-'].include? function['name'] %}

## Time Functions

The table below shows the available scalar functions for `TIME` types.

{% duckdb_functions %w(current_time date_diff date_part date_sub extract make_time).include? function['name'] %}

