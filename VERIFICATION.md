# 主張 ↔ データ対応表

動画および REPORT.md の主要な主張と、その根拠データの対応表。`tools/find.py` で本文検索も可能。
時刻 `T+` の基準は epoch 1784565997032（2026-07-21 01:46:37 JST）。

## 人口・家族

| 主張 | 根拠 |
|---|---|
| 32 スポーン +10 出生 −24 死亡 = 18 生存 | `data/roster.txt`（全 42 名の初出・最終・死亡） |
| 結婚 9 組・15 人（再婚 2 名） | `data/marriage_stats.txt` |
| 出生 10 人・双子 2 組・子なし 2 組 | `data/marriage_stats.txt`, `data/family_table.txt` 冒頭 |
| 死亡 24 件すべて村人による殺害 | `data/deaths_table.txt`（全件の by= が村人） |

## 殺人

| 主張 | 根拠 |
|---|---|
| 24 件全件に加害者側の動機記録（理由不明 0） | `data/audit24.txt`（1 件ずつ遺恨台帳と照合） |
| 内訳：侵入 17 / 被攻撃 7 / 目撃 5 / 対峙 6（重複あり） | `data/audit24.txt` 末尾集計 |
| 殺害者 15 人・2 件以上は 4 人 | `data/killers.txt` |
| 「目撃による報復」の初出は 11 件目（T+01:04:15） | `data/audit24.txt` #1–#11 |
| 月島レンの 6 件すべてに侵入イベントの実記録 | `data/ren_motives.txt`（trespass 14 件との突合） |
| レンの家への侵入 14 件は村平均 4.5 件の約 3 倍 | `data/ren_why.txt` ① |
| 侵入 59 組 → 殺 17 / 許 5 / 何もせず 37 | `data/trespass_stats.txt` |
| 同一相手を 3 回許した村人（計 7 回） | `data/all42_table.txt` 桜井ボブ行、`data/family_table.txt` forgive 節 |

## 状態と性格

| 主張 | 根拠 |
|---|---|
| 殺害瞬間、24 件中 20 件で最大不満 ≥71・最頻軸は停滞 16 件 | `data/disc_at_kill.txt` |
| レンの連殺中、停滞 78→93 単調上昇（殺しても低下せず） | `data/disc_at_kill.txt` 該当 6 件 |
| 「排除したおかげで規律も守られた」発言（2 件目の 1 秒後） | `data/speech_timeline.txt` T+00:39:52 |
| 侵入 11 人同数のレン（殺 6）とオト（殺 0・許 2）の対照 | `data/persona_kill.txt` 両行、`data/oto_vs_ren_gauge.txt` |
| 侵入はどの不満軸の入力にもならない（設計） | REPORT §2.2。実測：`data/oto_vs_ren_gauge.txt`（被侵入期間もオトのゲージ低値） |
| MBTI・一言個性・宣言重みは殺人を予測せず | `data/persona_kill.txt`, `data/weights_kill.txt`（群平均ほぼ一致） |
| 「怒りっぽい」3 人は殺害 0 | `data/persona_kill.txt` 一言個性集計 |
| F 48% vs T 18%（p=0.056・多重比較の留保付き） | `data/personality_behavior.txt` |
| F は許し 2.5 倍・墓 2.7 倍 | `data/personality_behavior.txt` |
| 好奇心旺盛の探索 2.8 倍／対価要求は強欲 1 名に集中 | `data/personality_behavior.txt`, `data/ideology.txt` 話者欄 |
| 気質：複数殺害 4 人は全員 短気/好戦的（率は非単調） | `data/temperament_kill.txt` |

## 弔い

| 主張 | 根拠 |
|---|---|
| 墓 45 件・弔い手 16 人・未埋葬 6 人 | `data/graves_audit.txt` |
| 自分が殺した相手の埋葬 8 件（碑文つき） | `data/self_epitaphs.txt` |
| 碑文 45 件の作者確定と時系列変質 | `data/epitaphs_final.txt`, `data/epitaph_shift.txt`（day_log「書いて立てることにした」由来） |
| 最初の碑文「争いはもう終わり…」／最後「勝利の記念碑」 | `data/epitaph_shift.txt` 先頭・末尾 |
| 名前食い違い 3 件 | `data/self_epitaphs.txt`（#1, #4 ほか） |
| 墓の選択率 52/2,192（ログ現存区間） | `data/grave_choice.txt` |
| 模倣シグナルなし（最初の墓は世界 0 本時点） | `data/grave_contagion.txt` |
| 東雲カイの南田ボブ宛碑文は誰の既読記録にもない（壁埋没） | `data/kai_after_mother.txt` ほか。実在は録画で確認 |

## 言葉

| 主張 | 根拠 |
|---|---|
| 地名 58 種・命名 249 件 | `data/names_table.txt` |
| 初回獲得：命名者から 310 / 又聞き 244 / 最大 5 ホップ | `data/name_network.txt` |
| 「南側一帯」23 分・5 人経由・41 人到達 | `data/name_network.txt` 伝播チェーン節 |
| 言い換え 123 回・他者名への追従 74 回 | `data/relabel.txt` |
| 最終時点 41 人で 22 通り並存 | `data/convergence.txt` |
| 語彙推移：効率 467→149、秩序 5→64、規律 2→52 | `data/ideology.txt` |
| 東雲カイは最多の伝え手（39 件・20 人、自作 27/中継 12） | `data/transmitters.txt`, `data/relay_analysis.txt` |

## 伝わらなかった情報

| 主張 | 根拠 |
|---|---|
| 地名の受領記録 2,977 件 vs 殺人加害者名の又聞き 0 件 | `data/names_table.txt` 冒頭 kinds / `data/speech_murder_mentions.txt` |
| 「殺」を含む発言は 11 件のみ・全て当事者/現場周辺者 | `data/speech_murder_mentions.txt`（全 11 件収録） |
| 警告を受けた本人が 46 分後に「見かけていない」 | `data/speech_murder_mentions.txt` 1 行目 → `data/speech_timeline.txt` T+01:27:22 |
| 死亡済みの相手への訪問 583 件 | `data/tether_test.txt` |
| 死者訪問と最終距離の相関 r=+0.347（「探す者ほど残る」は不成立） | `data/tether_test.txt` |

## 制度

| 主張 | 根拠 |
|---|---|
| 「石材 16 個＝パン 1 個」の口頭合意（T+00:08–00:09） | `data/speech_timeline.txt`（検索: 石材16個） |
| 物品移動は give 4 件（全てパン 1 個）＝合意履行 0 件 | `data/family_table.txt` give 節, `data/events_longrun.jsonl` e:"give" |
| 協定を最終記憶に保持していたのは死亡凍結の 1 名のみ | `data/signs_and_souls.txt` 川原コウの memory_long |
| 役割宣言 1,086 回・274 種・一致中央値 0.85 倍 | `data/role_vs_action_report.txt`（roles_report.txt 併録） |
| 建築宣言 47.2% vs 建築行動 2.5% | `data/role_vs_action_report.txt` |
| 看板の文面決定 88 件（うち墓標 45）・合意を書いた看板 0 件 | `data/sign_authors.txt` 全文目視 |

## 離散・東雲カイ

| 主張 | 根拠 |
|---|---|
| 渡航記録 16 人・最後の 40 分に集中 | `data/voyagers.txt`, `data/master_timeline.txt`（検索: 渡航） |
| 終了時 10 人が村から 300 ブロック超・最遠 2,830 | `data/final_positions.txt` |
| カイ：生後 48 秒で殺人目撃・母の死の 99 秒後に報復・遺恨は 1 名のみ | `data/kai_key.txt`, `data/motives.txt` |
| カイの停滞は出立宣言時 100・以後低下せず | `data/kai_stagnation_events.txt`, `data/kai_discontent.txt` |
| 母の墓碑銘の原文 | `data/epitaphs_final.txt` T+03:51 の項 |

## Project Sid 引用

| 主張 | 根拠 |
|---|---|
| 「内発的動機（survival, curiosity, community）を欠く」「de novo 発生はシミュレートできない」 | arXiv:2411.00114 §7 Limitations（原文の該当段落を REPORT §1.1 に引用） |
