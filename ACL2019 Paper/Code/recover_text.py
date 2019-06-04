import argparse
from collections import defaultdict
from nltk.corpus import treebank
import os


def parse_parameters(parser=None):
    if parser is None: parser = argparse.ArgumentParser()

    # data
    parser.add_argument("--ptb", default="")
    parser.add_argument("--nne_without_text", default="")
    parser.add_argument("--nne_with_text", default="")
    args, _ = parser.parse_known_args()
    return vars(args)


def process_ptb(ptb, folder, filename):
    sentences = []
    parsed_sentences = treebank.parsed_sents(os.path.join(ptb, folder, filename))
    for parsed_sentence in parsed_sentences:
        sentence = {"tokens": [], "pos": []}
        for leaf in parsed_sentence.subtrees(lambda s: s.height() == 2):
            tag = leaf.label()
            token = leaf[0]
            if tag == "-NONE-": continue
            sentence["tokens"].append(token)
            sentence["pos"].append(tag)
        assert len(sentence["tokens"]) == len(sentence["pos"])
        sentences.append(sentence)
    return sentences


if __name__ == "__main__":
    args = parse_parameters()

    all_ptb_files = defaultdict(list)
    for folder in os.listdir(args["ptb"]):
        for filename in os.listdir(os.path.join(args["ptb"], folder)):
            all_ptb_files[folder].append(filename)
    num_folders = len(all_ptb_files)
    num_files = sum([len(v) for v in all_ptb_files.values()])
    print("There are in total %d folders, and %d files in PTB" % (num_folders, num_files))


    all_nne_files = defaultdict(list)
    for folder in os.listdir(args["nne_without_text"]):
        if not folder.isdigit(): continue
        for filename in os.listdir(os.path.join(args["nne_without_text"], folder)):
            all_nne_files[folder].append(filename)
    num_folders = len(all_nne_files)
    num_files = sum([len(v) for v in all_nne_files.values()])
    print("There are in total %d folders, and %d files in NNE" % (num_folders, num_files))

    for folder in all_ptb_files:
        if not os.path.exists(os.path.join(args["nne_with_text"], folder)):
            os.makedirs(os.path.join(args["nne_with_text"], folder), exist_ok=True)

        for filename in all_ptb_files[folder]:
            with open(os.path.join(args["nne_with_text"], folder, filename), "w") as out_f:
                ptb_sentences = process_ptb(args["ptb"], folder, filename)
                with open(os.path.join(args["nne_without_text"], folder, filename)) as in_f:
                    sentence_id = 0
                    for line in in_f:
                        tokens = line.strip().split()
                        assert len(tokens) == len(ptb_sentences[sentence_id]["tokens"])
                        pos = next(in_f).strip()
                        mentions = next(in_f).strip()
                        assert len(next(in_f).strip()) == 0

                        out_f.write("%s\n" % (" ".join(ptb_sentences[sentence_id]["tokens"])))
                        out_f.write("%s\n" % pos)
                        out_f.write("%s\n\n" % mentions)

                        sentence_id += 1

                    assert sentence_id == len(ptb_sentences)