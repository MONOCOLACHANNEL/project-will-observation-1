# データ辞書

全ファイル UTF-8。時刻 `T+HH:MM:SS` は走行開始（epoch **1784565997032** = 2026-07-21 01:46:37 JST）からの経過。`epoch` はミリ秒 Unix 時刻。村人名は `姓名#下3桁`（例: 東雲カイ#a50）。

## 一次データ

| ファイル | 内容 |
|---|---|
| `events_longrun.jsonl` | 構造化イベント 14,969 件（1 行 1 JSON）。`e` が種別: death / birth / marry / grave / forgive / trespass / attack / attacked / murder_witness / death_witness / theft_seen / confront / visit / meet / name / settle / far_site / scout ほか |
| `speech_timeline.txt` | 全 9,874 発言。`T+ \| wall \| epoch \| 話者(MBTI/一言個性) -> 相手 \| 本文` |
| `incidents.jsonl` | ダッシュボード事件フィード 329 件（**LLM 生成の要約**。分析には生イベントと併用のこと） |
| `master_timeline.txt` | 主要イベント＋フィードの時系列マージ（1,444 行） |

## 台帳・名簿

| ファイル | 内容 |
|---|---|
| `roster.txt` | 全 42 名の初出・最終・死亡（加害者・座標つき） |
| `all42_table.txt` | 全 42 名：MBTI・一言個性・気質・殺害数・被侵入数・許し・最期（Markdown 表） |
| `vidmap.txt` | 村人名 → 内部 ID(vid) 対応 |
| `firsts.txt` | 村の「初めて」一覧（初侵入・初殺人・初結婚・初墓など） |
| `signs_and_souls.txt` | 42 名の内部状態抜粋（自己規定・遺恨・grief・長期記憶・目標） |
| `motives.txt` | 主要加害者・被害者の遺恨/目撃記録の抜粋 |

## 集計・分析（各ファイル冒頭に算出条件を記載）

- 殺人: `deaths_table.txt`（24 件＋連鎖）, `audit24.txt`（動機監査）, `killers.txt`, `ren_motives.txt`, `ren_why.txt`, `takeru_key.txt`, `bob_vs_io.txt`, `n11_check.txt`, `d08_check.txt`
- 抑制: `trespass_stats.txt`（59 組の帰結）
- 状態: `disc_at_kill.txt`（殺害瞬間の 9 軸・村内順位）, `oto_vs_ren_gauge.txt`, `kai_discontent.txt`, `kai_stagnation_events.txt`, `weights_kill.txt`
- 性格: `persona_kill.txt`, `personality_behavior.txt`（Fisher 検定含む）, `temperament_kill.txt`, `kinship_analysis.txt`
- 弔い: `graves_audit.txt`, `grave_authors.txt`, `epitaphs_final.txt`（碑文 45 件・作者確定）, `epitaph_shift.txt`, `self_epitaphs.txt`, `grave_choice.txt`, `grave_contagion.txt`, `bob_epitaphs.txt`
- 看板: `sign_authors.txt`（文面決定 88 件）, `signs_table.txt`（設置ログ現存分） |
- 言葉: `names_table.txt`, `names_grid.txt`, `name_network.txt`（伝播網・ホップ数）, `relay_analysis.txt`, `transmitters.txt`, `convergence.txt`, `relabel.txt`, `ideology.txt`（30 分毎語彙）
- 伝達: `speech_murder_mentions.txt`（「殺」を含む全 11 発言）, `tether_test.txt`
- 制度: `role_vs_action_report.txt`, `roles_report.txt`, `rolechurn.txt`
- 家族: `marriage_stats.txt`, `family_table.txt`（出生/結婚/墓/許し/対立ほか全件）
- 離散: `voyagers.txt`, `final_positions.txt`, `tracks.txt`
- 内省: `metacognition.txt`（言行不一致の自己記録 127 件）, `mirror_count.txt`
- 人物: `kai_key.txt`, `kai_first_words.txt`, `kai_last_words.txt`, `kai_after_mother.txt`, `pair_mio_sora.txt`, `mio_selfline.txt`, `mio_witness.txt`

## 既知の注意点（正直な但し書き）

1. **brain.log 由来の統計は T+01:17 以降のみ**（それ以前のログは未保存）。`grave_choice.txt` 等に影響
2. `incidents.jsonl` の見出し・理由文は LLM 生成であり、**加害者視点に偏る例がある**（例: 先制攻撃が「攻撃された」と表示される）。事実判定には `events_longrun.jsonl` の attack/attacked 順序を用いること
3. `murder_witness` は死亡ではなく**致命的攻撃の段階で発火**する（目撃時点で被害者が生存している場合がある）
4. 村人の看板既読記録（sign_mem）は**1 人 8 枠の LRU** であり、世界の看板の全量記録ではない
5. 気質・MBTI 等の統計は**探索的**であり、多重比較の補正をしていない
