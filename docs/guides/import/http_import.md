---
layout: docu
title: HTTP Parquet Import
---

To load a Parquet file over HTTP(S), the [`httpfs` extension](../../extensions/httpfs) is required. This can be installed use the `INSTALL` SQL command. This only needs to be run once.

```sql
INSTALL httpfs;
```

To load the `httpfs` extension for usage, use the `LOAD` SQL command:

```sql
LOAD httpfs;
```

After the `httpfs` extension is set up, Parquet files can be read over `http(s)` using the following command:

```sql
SELECT * FROM read_parquet('https://<domain>/path/to/file.parquet');
```
