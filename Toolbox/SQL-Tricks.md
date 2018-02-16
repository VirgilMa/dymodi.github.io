---
layout: post
title: SQL Basic
date: Nov. 2, 2017
author: Yi DING
---

[comment]: # "This is the basic operations in SQL"

The basic operations here are from [codecademy SQL course](https://www.codecademy.com/learn/learn-sql)

## Basic Operations
```
SELECT * FROM celebs;
CREATE TABLE celebs (id INTEGER, name TEXT, age INTEGER);
INSERT INTO celebs (id, name, age) VALUES (1, 'Justin Bieber', 21);
UPDATE celebs SET age = 3 WHERE id = 1;
ALTER TABLE celebs ADD COLUMN twitter_handle TEXT;
```


