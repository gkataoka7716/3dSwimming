import bpy
import sys
from pathlib import Path

# *************************
# プロジェクトパスを追加
# *************************

PROJECT_DIR = Path(r"C:\Users\chart\OneDrive\ドキュメント\3dSwimming")

POSE_DIR = PROJECT_DIR / "pose"

if str(PROJECT_DIR) not in sys.path:
    sys.path.append(str(PROJECT_DIR))

if str(POSE_DIR) not in sys.path:
    sys.path.append(str(POSE_DIR))


from config import MODEL_PATH

# *************************
# 既存のものを削除
# *************************

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

print("既存のオブジェクトを削除しました")


# *************************
# 3Dモデルの読み込み
# *************************

print(f"モデルを読み込みます: {MODEL_PATH}")

bpy.ops.import_scene.fbx(filepath=str(MODEL_PATH))

print("人型モデルの読み込みが完了しました")


# *************************
# 初期フォームの設定
# *************************

print("")
print("=" * 60)
print("初期フォームを設定します")
print("=" * 60)

from pose.init import create_initial_pose

create_initial_pose()

print("初期フォームの設定が完了しました")

# *************************
# 動かす
# *************************
