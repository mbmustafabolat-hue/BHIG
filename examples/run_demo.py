#!/usr/bin/env python3
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.bhig_wstar_model import demo

result = demo()
print(json.dumps(result, ensure_ascii=False, indent=2))
Path('results').mkdir(exist_ok=True)
Path('results/sample_output.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
