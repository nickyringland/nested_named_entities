# Create the dataset
The recover_text.py file can be used to combine our annotations with the PTB corpus (download from https://catalog.ldc.upenn.edu/LDC95T7).

~~~~
mkdir Resources/with-text
cd Code
python3 recover_text.py --ptb=/data/dai031/Corpora/PTB/new_wsj --nne_without_text=../Resources/no-text --nne_with_text=../Resources/with-text
~~~~

The train_test_split.sh script can be used to construct train-dev-test split as described in our paper:
~~~~
./train_test_split.sh
~~~~

Sentence instance in the final dataset looks like: 
~~~~
Bell , based in Los Angeles , makes and distributes electronic , computer and building products .
NNP , VBN IN NNP NNP , VBZ CC VBZ JJ , NN CC NN NNS .
0,0 ORGCORP|0,0 NAME|4,5 CITY
~~~~
The first line is tokenized sentence, the second line is its corresponding POS tags, and the third line contain mention annotations.

# Benchmark

The system-output directory contains the output of our flat BiLSTM-CRF models which use either the outermost or the innermost mentions for training.

paper-table.py is the script used to produce BiLSTM-CRF-BOTH (combine the outputs from these two flat models) result in Table 2 of our paper.


## Citing
If you use this dataset, please cite
```bibtex
@InProceedings{Ringland-acl-2019,
  title={NNE: A Dataset for Nested Named Entity Recognition in English Newswire.},
  author={Ringland, Nicky and Dai, Xiang and Hachey, Ben and Karimi, Sarvnaz and Paris, Cecile and Curran, James R.},
  booktitle={ACL},
  year={2019},
  address={Florence, Italy}
}
```
