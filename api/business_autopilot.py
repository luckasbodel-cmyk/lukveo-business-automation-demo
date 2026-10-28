"""LUKVEO Business Autopilot : carnet local, aucune action externe."""
from pathlib import Path
import os, sqlite3, threading
from datetime import datetime, timezone

DB_DIR = Path(os.environ.get('LUKVEO_BUSINESS_DIR', r'C:\JARVIS_DATA\LUKVEO\BUSINESS_AUTOPILOT'))
DB_FILE = DB_DIR / 'business.sqlite3'
LOCK = threading.Lock()
KINDS = {'prospect', 'produit', 'opportunite'}

def _connect():
    DB_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(str(DB_FILE), timeout=10)
    connection.execute('CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, kind TEXT NOT NULL, title TEXT NOT NULL, detail TEXT NOT NULL, status TEXT NOT NULL, created_at TEXT NOT NULL)')
    return connection

def list_entries():
    with LOCK, _connect() as db:
        records = db.execute('SELECT id, kind, title, detail, status, created_at FROM entries ORDER BY id DESC LIMIT 150').fetchall()
    return {'ok': True, 'entries': [dict(zip(('id','kind','title','detail','status','created_at'),row)) for row in records]}

def add_entry(payload):
    kind = payload.get('kind')
    title = payload.get('title')
    detail = payload.get('detail','')
    if kind not in KINDS: raise ValueError('Type inconnu')
    if not isinstance(title,str) or not 2 <= len(title.strip()) <= 140: raise ValueError('Titre requis (2 à 140 caractères)')
    if not isinstance(detail,str) or len(detail) > 2500: raise ValueError('Description trop longue')
    with LOCK, _connect() as db:
        cursor = db.execute('INSERT INTO entries (kind,title,detail,status,created_at) VALUES (?,?,?,?,?)', (kind,title.strip(),detail.strip(),'à étudier',datetime.now(timezone.utc).isoformat(timespec='seconds')))
        db.commit()
        new_id = cursor.lastrowid
    return {'ok':True,'id':new_id,'message':'Fiche enregistrée localement'}
