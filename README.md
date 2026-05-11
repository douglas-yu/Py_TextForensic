# 文本取证 · Text Forensics Suite

A PyQt6 desktop application for **Text Forensics**, **Stylometry**, and **Authorship Attribution**.

---

## Features

| Module | Description |
|--------|-------------|
| **01 · Authorship Attribution** | Build author profiles from writing samples, then attribute unknown text to the most likely author |
| **02 · Same Author Detection** | Compare two texts side-by-side and determine if they share the same author |
| **03 · Tampering Detection** | Forensic scan for style discontinuities, encoding anomalies, cryptographic hashes |
| **04 · AI Detection (Deeptext Forensics)** | Heuristic detection of AI-generated content |
| **05 · Style Imitation** | Generate text that imitates the writing style of a source text |

---

## Installation & Launch

```bash
# 1. Install dependency
pip install PyQt6

# 2. Run the app
python main.py
```

---

## How to Use

### Authorship Attribution (Tab 01)
1. Add author names in the left panel
2. Select an author, paste their writing sample, click **BUILD PROFILE**
3. Repeat for all known authors (2–5 recommended)
4. Paste the unknown text in the center panel
5. Click **ANALYZE AUTHORSHIP** — ranked similarity scores appear on the right

### Same Author Detection (Tab 02)
1. Paste Text A and Text B side by side
2. Click **COMPARE AUTHORSHIP**
3. View the overall similarity score and per-category breakdown

### Tampering Detection (Tab 03)
1. Paste or load a text file
2. Click **RUN FORENSIC SCAN**
3. View: cryptographic hashes, style break segments, vocabulary anomalies, encoding issues

### AI Detection (Tab 04)
1. Paste the text to inspect
2. Click **DEEP FORENSIC SCAN**
3. View the AI probability score (0–100) and individual detection signals

### Style Imitation (Tab 05)
1. Paste a source text (200+ words for best results)
2. Click **ANALYZE SOURCE STYLE** to preview the style profile
3. Set target length and number of variations
4. Click **GENERATE TEXT** — variations appear in separate tabs

---

## Technical Notes

### Stylometric Features Extracted
- Type-Token Ratio (TTR) and Hapax Ratio (lexical richness)
- Yule's K (vocabulary diversity)
- Average word length, sentence length, sentence variance
- Punctuation ratios (comma, semicolon, exclamation, question)
- Function word frequency profile (50 function words)
- Word length distribution (1–15+ chars)
- Character bigram/trigram frequencies
- Flesch-Kincaid readability score
- Paragraph statistics
- Uppercase/digit ratios

### Similarity Computation
- Cosine similarity over multi-dimensional feature vectors
- Per-category breakdown: lexical, syntactic, function words, word length profile

### AI Detection Signals
- Vocabulary entropy uniformity
- Sentence length coefficient of variation
- AI cliché phrase detection (30+ patterns)
- Paragraph length uniformity
- Bigram repetition burstiness
- Formal transition word density

### Tampering Detection
- SHA-256 and MD5 hash fingerprints
- Segment-wise style consistency scoring
- Zero-width character detection
- Non-BMP Unicode character detection
- Vocabulary Jaccard discontinuity analysis

---

## Disclaimer

All analyses are heuristic and statistical in nature.
No forensic tool achieves 100% accuracy.
Use results as one signal among many in a broader investigation.
