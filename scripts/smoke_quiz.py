from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
d = json.loads((root / 'public/data/quiz.json').read_text(encoding='utf-8'))
assert len(d['modules']) == 10
ids = set()
for m in d['modules']:
    assert len(m['questions']) == 40
    for q in m['questions']:
        assert q['id'] not in ids
        ids.add(q['id'])
        assert q['options'][q['answer']]
        assert q['explanation'] and q['source']
assert len(ids) == 400
print('PASS: 10 modules, 400 questions, unique IDs, answers, explanations and sources.')
