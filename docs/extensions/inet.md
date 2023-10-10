---
layout: docu
title: INET
selected: Extensions
---

This extension adds a new type (`inet`) to DuckDB, along with cast operators, and primarily exists as a demo of adding new types and operators.

| Function  | Description                                                          | Example                           | Underlying type |
|:----------|:---------------------------------------------------------------------|:----------------------------------|:----------------|
| `inet`    | Format the given `number` per the rules given in the `format_string` | `text(1234567.897, 'h AM/PM')`    | `UTinyInt`      |
| `address` | Alias for `text`.                                                    | `text(1234567.897, 'h:mm AM/PM')` | `HugeInt`       |
| `mask`    | Alias for `text`.                                                    | `text(1234567.897, 'h:mm AM/PM')` | `USmallInt`     |


| Function | Description                                                          | Example                           | Return      |
|:---------|:---------------------------------------------------------------------|:----------------------------------|:------------|
| `host`   | Format the given `number` per the rules given in the `format_string` | `text(1234567.897, 'h AM/PM')`    | `UTinyInt`  |
| `* `-`   | Alias for `text`.                                                    | `text(1234567.897, 'h:mm AM/PM')` | `HugeInt`   |
| `mask`   | Alias for `text`.                                                    | `text(1234567.897, 'h:mm AM/PM')` | `USmallInt` |
