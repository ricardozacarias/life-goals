# init_neon.py
import os, pathlib, psycopg

DDL = pathlib.Path("schema_pg.sql").read_text(encoding="utf-8")
stmts = [s.strip() for s in DDL.split(";") if s.strip()]  # run statements one by one

url = 'postgresql://neondb_owner:npg_Z3NPBDra1dIu@ep-young-term-ad6r4wbi.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
with psycopg.connect(url) as con:
    with con.cursor() as cur:
        for s in stmts:
            cur.execute(s + ";")
print("Schema applied.")
