# Modern Cryptology

This repository documents my solutions to a series of cryptographic challenges presented as a multi-level, terminal-based game. Each level required analyzing and breaking a different cipher to extract a password, which was the key to unlocking the next stage of the game.

## Assignment 1: Substitution Cipher
Conducted a **frequency analysis** on the ciphertext to identify it as a simple substitution cipher. Successfully deciphered the message by mapping the most frequent ciphertext characters to their common English language equivalents.

## Assignment 2: Vigenère Cipher
Applied the **Kasiski examination** to identify repeating patterns in the ciphertext, which revealed the length of the encryption key. Subsequently, frequency analysis was performed on the corresponding sub-alphabets to recover the full key and decrypt the message.

## Assignment 3: Substitution-Permutation Network (SPN)
Analyzed repeating sequences and their intervals within the ciphertext to determine the cipher's block size. Following this, **frequency analysis** was employed to deduce the character mappings used in the substitution layer, leading to a successful cryptanalysis of the network.

## Assignment 4: 6-Round Data Encryption Standard (DES)
Executed a **chosen-plaintext attack** using efficient bash scripts to automate the process. The core of the attack involved **differential cryptanalysis**, where high-probability differential characteristics were exploited to systematically recover the subkeys for the 6-round DES variant.

## Assignment 5: Advanced Encryption Standard (AES) Variant
Performed a **chosen-plaintext attack** by encrypting specially crafted plaintexts to probe the cipher's internal structure. This technique revealed a vulnerability, specifically the lower-triangular property of the MixColumns matrix, which was then exploited to efficiently break the encryption. Bash scripts were used to automate the attack.

## Directory Structure

```bash
├── Assignment 1
│   ├── cipher.txt
│   ├── plain.txt
│   └── substitution.ipynb
├── Assignment 2
│   ├── cipher.txt
│   ├── plain.txt
│   └── vigenere.ipynb
├── Assignment 3
│   ├── cipher.txt
│   ├── combined cipher.ipynb
│   └── plain.txt
├── Assignment 4
│   ├── README.md
│   ├── brute_force.ipynb
│   ├── constants.py
│   ├── cryptanalysis.py
│   ├── decode.ipynb
│   ├── des_functions.py
│   ├── letter_pair.ipynb
│   ├── level4.sh
│   ├── supporting_functions.py
│   ├── theirdes_crack631.ipynb
│   └── theirdes_crack632.ipynb
├── Assignment 5
│   ├── README.md
│   ├── constants.py
│   ├── cryptanalysis.py
│   ├── decoding.ipynb
│   ├── find_e_diag.ipynb
│   ├── find_mat.ipynb
│   ├── level5.sh
│   ├── mat_inv.ipynb
│   └── supporting_functions.py
└── README.md
```