# Nested Named Entity Corpus

See [Nested Named Entities, Nicky Ringland](https://ses.library.usyd.edu.au/handle/2123/14558)

The names of people, locations, and organisations play a central role in language, and named entity recognition (NER) has been widely studied, and successfully incorporated, into natural language processing (NLP) applications. The most common variant of NER involves identifying and classifying proper noun mentions of these and miscellaneous entities as linear spans in text.

Unfortunately, this version of NER is no closer to a detailed treatment of named entities than chunking is to a full syntactic analysis. NER, so con- strued, reflects neither the syntactic nor semantic structure of NE mentions, and provides insufficient categorical distinctions to represent that structure.

Representing this nested structure, where a mention may contain mention(s) of other entities, is critical for applications such as coreference resolution. The lack of this structure creates spurious ambiguity in the linear approximation.

Research in NER has been shaped by the size and detail of the available annotated corpora. The existing structured named entity corpora are either small, in specialist domains, or in languages other than English.

This thesis presents our Nested Named Entity (NNE) corpus of named entities and numerical and temporal expressions, taken from the WSJ portion of the Penn Treebank (PTB, Marcus et al., 1993). We use the BBN Pronoun Coreference and Entity Type Corpus (Weischedel and Brunstein, 2005a) as our basis, manu- ally annotating it with a principled, fine-grained, nested annotation scheme and detailed annotation guidelines. The corpus comprises over 279,000 entities over 49,211 sentences (1,173,000 words), including 118,495 top-level entities.

Our annotations were designed using twelve high-level principles that guided the development of the annotation scheme and difficult decisions for annotators. We also monitored the semantic grammar that was being induced during annotation, seeking to identify and reinforce common patterns to main- tain consistent, parsimonious annotations.

The result is a scheme of 118 hierarchical fine-grained entity types and nesting rules, covering all capitalised mentions of entities, and numerical and temporal expressions. Unlike many corpora, we have developed detailed guidelines, including extensive discussion of the edge cases, in an ongoing dia- logue with our annotators which is critical for consistency and reproducibility.

We annotated independently from the PTB bracketing, allowing annotators to choose spans which were inconsistent with the PTB conventions and errors, and only refer back to it to resolve genuine ambiguity consistently.

We merged our NNE with the PTB, requiring some systematic and one-off changes to both annotations. This allows the NNE corpus to complement other PTB resources, such as PropBank, and inform PTB-derived corpora for other formalisms, such as CCG and HPSG. We compare this corpus against BBN.

We consider several approaches to integrating the PTB and NNE annotations, which affect the sparsity of grammar rules and visibility of syntactic and NE structure. We explore their impact on parsing the NNE and merged variants using the Berkeley parser (Petrov et al., 2006), which performs surprisingly well without specialised NER features.

We experiment with flattening the NNE annotations into linear NER variants with stacked categories, and explore the ability of a maximum entropy and a CRF NER system to reproduce them. The CRF performs substantially better, but is infeasible to train on the enormous stacked category sets. The flattened output of the Berkeley parser are almost competitive with the CRF.

Our results demonstrate that the NNE corpus is feasible for statistical models to reproduce. We invite researchers to explore new, richer models of (joint) parsing and NER on this complex and challenging task.

Our nested named entity corpus will improve a wide range of NLP tasks, such as coreference resolution and question answering, allowing automated systems to understand and exploit the true structure of named entities.




