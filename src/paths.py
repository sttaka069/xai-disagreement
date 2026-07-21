# paths.py : データや図の「保存先」をこの1ファイルに集約するモジュール。
# 他のモジュール（data.py, viz.py など）は保存先を自前で書かず、ここから受け取る。
from pathlib import Path

# --- リポジトリのルートを求める ---
# __file__ はこのファイル自身のパス（例: .../xai-disagreement/src/paths.py）
# .resolve() で絶対パスに変換（相対パスの曖昧さを消す）
# .parents[1] は2つ上の階層 = src/ の親 = リポジトリのルート
#   parents[0]なら src/、parents[1]で xai-disagreement/ を指す
ROOT = Path(__file__).resolve().parents[1]
# --- ルートを基準に、各保存先を定数として定義 ---
# "/" 演算子はパスの連結（Path同士をOSに合った区切りで繋ぐ）。Windowsでも \ に自動対応
DATA_RAM = ROOT / "data" / "raw" # 元データ（ダウンロードやキャッシュの置き場）
DATA_PROC = ROOT / "data" / "processed"# 前処理済みデータ（分割・ラベル反転の結果）
FIG = ROOT / "results" / "figures"# 図（png）の保存先
TAB = ROOT / "results" / "tables"# 数値表（md/csv）の保存先

# --- フォルダが無ければ自動生成 ---
# clone直後などで空フォルダが存在しないケースでも、importした時点で作られるので落ちない
for d in (DATA_RAM,DATA_PROC,FIG,TAB):
    d.mkdir(
        parents = True,# 途中の階層（例: results）も一緒に作る
        exist_ok = True,# 既に存在してもエラーにしない
    )
