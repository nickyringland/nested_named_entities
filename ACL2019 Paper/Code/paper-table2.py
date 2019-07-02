OUTERMOST = "../Resources/system-output/innermost/test.pred"
INNERMOST = "../Resources/system-output/outermost/test.pred"


sentences = []
with open(OUTERMOST) as f:
    for line in f:
        sentence = [line.strip()]
        pred = next(f).strip()
        gold = next(f).strip()
        sentence.append(pred)
        sentence.append(gold)
        assert len(next(f).strip()) == 0
        sentences.append(sentence)

sentence_id = 0
with open(INNERMOST) as f:
    for line in f:
        assert line.strip() == sentences[sentence_id][0]
        pred = next(f).strip()
        assert next(f).strip() == sentences[sentence_id][2]
        sentences[sentence_id].append(pred)
        assert len(next(f).strip()) == 0
        sentence_id += 1

TP, FP, FN = 0, 0, 0
for sentence in sentences:
    pred = list(set(sentence[1].split("|") + sentence[3].split("|")))
    gold = sentence[2].split("|")
    for p in pred:
        if len(p) == 0: continue
        if p in gold:
            TP += 1
        else:
            FP += 1
    for g in gold:
        if len(g) > 0 and g not in pred:
            FN += 1

precision = float(TP) / float(TP + FP) if TP + FP > 0 else 0
recall = float(TP) / float(TP + FN) if TP + FN > 0 else 0
f1 = 2. * ((precision * recall) / (precision + recall)) if precision + recall > 0 else 0

print("%.1f & %.1f & %.1f" % (precision * 100, recall * 100, f1 * 100))
