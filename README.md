# Retrieve never-empty result from a tabular structured data with RAG, Gemma, embedding model, FAISS, Pandas.

- Sometimes we need to retrieve something from a table. If there is corresponding result, that's perfectly good; but if not, we might also need something back because in some situations, people don't care what is exactly in it: 'Just gimme anything, but not too ridiculous, okay?'..
- There are many ways to achieve that, to the knowledge of this repo's author. Even diffuison model has a say in this in terms of tabular data generation.
- This repo, on the other hand, borrowed an existing database but originally not to this purpose --- this repository owes so much to [jaydeepthik/Gemma-RAG](https://github.com/jaydeepthik/Gemma-RAG/blob/main/Gemma_rag_movies.ipynb). Chapeau, jaydeepthik!
- RAG is so light compared against finetuning stuff.
- Gemma has its 2b-it version, which is convenient and beautiful.
- FAISS is also very light and convenient. Its installation avoid systematic sudo apt-get and other things. Usually people of 'just gimme anything' type are also hustlers, who is always impatient, you know what i'm sayin'?
- Pandas is smooth tool for dataset.
- You may now open 'Gemma_rag_procedures_fine_public.ipynb' to take a look. Hope this will inspire you.
- My approach is basically to find the setup a subdatabase for FAISS that has as few columsn as possible in that I can make similarity of inputting commands with the actually-realted columns in the original database; otherwise, imagine when a simple command is compared to a document with 100 columns...The similarity check is done between them!

P.S. there is also a list of blogs that i gain help from:
- https://medium.com/@lucamassaron/data-science-ai-assistant-with-gemma-2b-it-a-rag-101-25c5445f891e
- https://medium.com/@ashmi_banerjee/mlstory-a-simple-rag-system-using-google-gemma-to-answer-travel-related-queries-4b08b9bde1c6
- https://huggingface.co/learn/cookbook/en/rag_with_hugging_face_gemma_mongodb
- https://colab.research.google.com/drive/14z2yG4JFFGDXQomEg7BQ6tjE1X1P-9Ph?usp=sharing&source=post_page-----f917fc6f753f--------------------------------
- https://medium.com/@mohammed97ashraf/building-a-retrieval-augmented-generation-rag-model-with-gemma-and-langchain-a-step-by-step-f917fc6f753f
- https://www.mongodb.com/developer/products/atlas/gemma-mongodb-huggingface-rag/#step-5--vector-search-index-creation
- - https://blog.superteams.ai/steps-to-build-rag-application-with-gemma-7b-llm-43f7251a36a1
