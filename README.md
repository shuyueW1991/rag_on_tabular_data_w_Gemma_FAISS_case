# Retrieve never-empty result from a tabular structured data with RAG, Gemma, embedding model, FAISS, Pandas.

- Sometimes we need to retrieve something from a table. If there is corresponding result, that's perfectly good; but if not, we might also need something back because in some situations, people don't care what is exactly in it: 'Just gimme anything, but not too ridiculous, okay?'..
- There are many ways to achieve that, to the knowledge of this repo's author. Even diffuison model has a say in this in terms of tabular data generation.
- This repo, on the other hand, borrowed an existing database but originally not to this purpose --- this repository owes so much to [jaydeepthik/Gemma-RAG](https://github.com/jaydeepthik/Gemma-RAG/blob/main/Gemma_rag_movies.ipynb). Chapeau, jaydeepthik!
- RAG is so light compared against finetuning stuff.
- Gemma has its 2b-it version, which is convenient and beautiful.
- FAISS is also very light and convenient. Its installation avoid systematic sudo apt-get and other things. Usually people of 'just gimme anything' type are also hustlers, who is always impatient, you know what i'm sayin'?
- Pandas is smooth tool for dataset.
- You may now open 'Gemma_rag_procedures_fine_public.ipynb' to take a look. Hope this will inspire you.

