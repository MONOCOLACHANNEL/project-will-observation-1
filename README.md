# Project Will — 観測 #1 データセット（2026-07-21 ロングラン）

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21723921.svg)](https://doi.org/10.5281/zenodo.21723921)

🌐 **English summary: [README_EN.md](README_EN.md)**

実効的な制度（役割の割当て・共有規則・権限・契約の履行機構）を与えずに Minecraft へ放った自律 AI 村人 32 人・約 6 時間の**全記録と全分析**です。動画で提示した全ての主張は、このリポジトリのデータから検証できます。

📺 動画: https://youtu.be/Xn0kTCtqDO0
📄 報告書: [REPORT.md](REPORT.md)
🔎 主張↔データ対応表: [VERIFICATION.md](VERIFICATION.md)
📚 データ辞書: [DATA.md](DATA.md)

## 観測のあらまし

| | |
|---|---|
| 村人 | 32 人スポーン ＋ 10 人出生 − 24 人死亡 ＝ 生存 18 人 |
| 死因 | **24 件すべて村人による殺害**（餓死・事故 0 件）。理由不明の殺人 0 件 |
| 発端 | 17 件が「自宅への侵入」。ただし侵入 59 組のうち殺害は 17 組——**7 割は殺さなかった** |
| 弔い | 誰にも指示されず**墓標 45 件**。うち 8 件は殺した本人が建立。碑文は 5 時間で「争いはもう終わり」から「勝利の記念碑」へ変質 |
| 言葉 | 地名 58 種を自発発明、又聞き 244 件・最大 5 ホップで伝播——しかし**同一地点の呼称は 22 通りが並存し、収束せず** |
| 制度 | 交換レート合意・「管理官」自称・命令は多数発生、**履行・服従は 0 件**（「殺」を含む発言は 9,874 件中 11 件のみ、犯人名の又聞き 0 件） |

## クイックスタート

```bash
# 人物・語句・時間帯でログを横断検索（結果は out.txt に UTF-8 で出力）
python tools/find.py 月島レン --time 00:39 00:45
python tools/find.py 石材16個
python tools/find.py --time 03:22 03:25
```

主要ファイル：`data/events_longrun.jsonl`（構造化イベント 14,969 件）・`data/speech_timeline.txt`（全 9,874 発言）・`data/audit24.txt`（殺人 24 件の動機監査）・`data/epitaphs_final.txt`（墓碑銘 45 件・作者確定）。

時刻表記 `T+HH:MM:SS` は走行開始（epoch **1784565997032** = 2026-07-21 01:46:37 JST）からの経過です。

## システム（要点のみ）

- Minecraft Mod（身体）⇄ Python ブレイン（心）⇄ Gemini 3.1 Flash-Lite
- 9 軸の不満状態（生存・好奇心・共同体）を提示するのみで、行動は一切強制しない
- 記憶は個体別。情報は「見る・話す・看板を読む」でしか伝わらない
- 詳細は [REPORT.md §2](REPORT.md) を参照

## ライセンス / 引用

- データ・文書: **CC BY 4.0** ／ スクリプト: **MIT**（[LICENSE](LICENSE)）
- 引用は [CITATION.cff](CITATION.cff) を参照。DOI: [10.5281/zenodo.21723921](https://doi.org/10.5281/zenodo.21723921)（常に最新版へ解決。初版 v1.0 は [10.5281/zenodo.21723922](https://doi.org/10.5281/zenodo.21723922)）

## 著者

モノコーラ (Monocola) — 質問・指摘は Issue へ。
