# Steps to build an autocorrect tool

1. Word is misspelled if not found in the dictionary, so autocorrect flags that word
2. Find strings that are N-edit-distance away from the misspelled word
Edit distance features include INSERT, DELETE, SWAP, REPLACE
3. Filtering suggested candidates
4. Order filtered candidates based on word probabilities
5. Choose the most-likely candidate