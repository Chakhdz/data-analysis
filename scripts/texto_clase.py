#!/usr/bin/env python3
"""Añade `texto_clase` a colima-unificado.json/.csv (no modifica ningún otro campo).
Clases:
  inventario      descripción física tipo registro de inventario (todo objeto MNA; textos en mayúsculas; objetos con texto <150 caracteres, salvo MET)
  interpretativo  texto curatorial/interpretativo del museo sobre un objeto
  generico_museo  texto general del museo compartido por varias piezas (texto_tipo = generico)
  cedula_sala     cédula, texto de sala, vitrina o cartel
  catalogo_publicacion  catálogo, folleto, boletín o ficha técnica
  parafrasis      resumen propio (texto_tipo = parafrasis)
  (vacío)         sin texto
Uso: python3 scripts/texto_clase.py   (hace respaldo en LOG/ antes de escribir)"""
import json,csv,re,shutil,datetime,collections
ts=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
for f in ('colima-unificado.json','colima-unificado.csv'): shutil.copy2(f,f'LOG/bak-texto-clase-{ts}-{f}')
d=json.load(open('colima-unificado.json',encoding='utf-8')); o=d['objects']
UP=re.compile(r'^[A-ZÁÉÍÓÚÑ0-9 ,.\-/()]{25,}')
def clase(x):
    t=(x.get('texto_museografico') or '').strip()
    if x.get('texto_tipo')=='parafrasis': return 'parafrasis'
    if not t: return ''
    if x.get('texto_tipo')=='generico': return 'generico_museo'
    tp=x.get('tipo')
    if tp in('cedula','texto_sala','vitrina','cartel','pintura','decoracion'): return 'cedula_sala'
    if tp in('catalogo','folleto','boletin','ficha_tecnica'): return 'catalogo_publicacion'
    if x.get('museo_corto')=='MNA' or UP.match(t): return 'inventario'
    if len(t)<150 and x.get('museo_corto')!='MET': return 'inventario'
    return 'interpretativo'
for x in o: x['texto_clase']=clase(x) or None
if 'texto_clase' not in d['meta']['columnas']: d['meta']['columnas'].append('texto_clase')
d['meta']['nota_texto_clase_2026_11_03']='texto_clase generada por scripts/texto_clase.py (reglas en su docstring).'
json.dump(d,open('colima-unificado.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
rows=list(csv.reader(open('colima-unificado.csv',encoding='utf-8-sig'))); h=rows[0]
if 'texto_clase' not in h: h.append('texto_clase')
ix={c:i for i,c in enumerate(h)}; by={str(x['id_museo']):x for x in o}
for r in rows[1:]:
    r+=['']*(len(h)-len(r)); r[ix['texto_clase']]=by[r[ix['id_museo']]].get('texto_clase') or ''
csv.writer(open('colima-unificado.csv','w',encoding='utf-8-sig',newline='')).writerows(rows)
c=collections.Counter(x['texto_clase'] for x in o if x['texto_clase']); print('clases:',dict(c),'| sin texto:',sum(1 for x in o if not x['texto_clase']))
