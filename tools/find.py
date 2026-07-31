#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""longrun(2026-07-21)の検索ツール。結果は必ずUTF-8のファイルへ書き出す（コンソールはcp932で化けるため）。

使い方（このフォルダで実行）:
  python find.py 月島レン                 # 名前/語句で会話・イベント・看板を横断検索 → out.txt
  python find.py 秩序 --speech            # 会話ログだけ
  python find.py --time 02:10 02:20       # T+の時間帯で全ソース抜き出し
  python find.py 真砂アル --time 03:18 03:30
  python find.py --epoch 1784578165827    # epochの前後3分を抜き出し
出力は out.txt（--out で変更可）。ReplayModジャンプ用のepochが各行に入っている。
"""
import argparse, os, sys, json, datetime

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
START = 1784565997032  # T+00:00:00 = 2026-07-21 01:46:37

SOURCES = [
    ('会話', 'speech_timeline.txt'),
    ('年表', 'master_timeline.txt'),
    ('看板', 'signs_table.txt'),
    ('死', 'deaths_table.txt'),
    ('家族', 'family_table.txt'),
    ('地名', 'names_table.txt'),
]


def tsec(tp):
    """'T+HH:MM:SS' or 'HH:MM' -> 秒"""
    tp = tp.replace('T+', '')
    parts = [int(x) for x in tp.split(':')]
    while len(parts) < 3:
        parts.append(0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def line_tsec(line):
    if not line.startswith('T+'):
        return None
    try:
        return tsec(line[:11].strip())
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('query', nargs='*', help='検索語（複数指定でAND）')
    ap.add_argument('--time', nargs=2, metavar=('FROM', 'TO'), help='T+の範囲 例: --time 02:10 02:20')
    ap.add_argument('--epoch', type=int, help='epoch(ms)の前後3分')
    ap.add_argument('--speech', action='store_true', help='会話ログのみ')
    ap.add_argument('--out', default='out.txt')
    a = ap.parse_args()

    lo = hi = None
    if a.time:
        lo, hi = tsec(a.time[0]), tsec(a.time[1])
    if a.epoch:
        c = (a.epoch - START) // 1000
        lo, hi = c - 180, c + 180

    srcs = [s for s in SOURCES if (not a.speech or s[1] == 'speech_timeline.txt')]
    n = 0
    out_path = os.path.abspath(a.out)
    with open(out_path, 'w', encoding='utf-8') as o:
        o.write('# query=%s time=%s epoch=%s\n' % (a.query, a.time, a.epoch))
        for label, fn in srcs:
            p = os.path.join(HERE, fn)
            if not os.path.exists(p):
                continue
            hits = []
            for line in open(p, encoding='utf-8'):
                line = line.rstrip('\n')
                if a.query and not all(q in line for q in a.query):
                    continue
                if lo is not None:
                    ts = line_tsec(line)
                    if ts is None or not (lo <= ts <= hi):
                        continue
                hits.append(line)
            if hits:
                o.write('\n===== %s (%s) : %d件 =====\n' % (label, fn, len(hits)))
                o.write('\n'.join(hits) + '\n')
                n += len(hits)
    print('hits', n, '->', out_path)


if __name__ == '__main__':
    main()
