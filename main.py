#!/usr/bin/env python3
"""
文本取证 · Text Forensics Suite
Authorship Attribution, Stylometry, Tampering Detection, AI Detection & Text Generation
"""

import sys
import os
import json
import math
import hashlib
import random
import re
import string
from collections import Counter, defaultdict
from datetime import datetime

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QTabWidget, QSplitter, QFrame,
    QProgressBar, QScrollArea, QGridLayout, QComboBox, QSlider,
    QSpinBox, QCheckBox, QGroupBox, QTableWidget, QTableWidgetItem,
    QHeaderView, QFileDialog, QMessageBox, QSizePolicy, QStackedWidget,
    QLineEdit, QListWidget, QListWidgetItem, QDialog, QDialogButtonBox,
    QRadioButton, QButtonGroup, QToolTip
)
from PyQt6.QtCore import (
    Qt, QThread, pyqtSignal, QTimer, QPropertyAnimation,
    QEasingCurve, QRect, QSize, QPoint, pyqtProperty
)
from PyQt6.QtGui import (
    QFont, QColor, QPalette, QPixmap, QPainter, QLinearGradient,
    QRadialGradient, QPen, QBrush, QFontDatabase, QIcon, QTextCharFormat,
    QSyntaxHighlighter, QTextDocument, QCursor, QGradient, QConicalGradient
)

# ─────────────────────────────────────────────
# STYLE CONSTANTS
# ─────────────────────────────────────────────
DARK_BG      = "#0A0E1A"
PANEL_BG     = "#0F1628"
CARD_BG      = "#141C35"
BORDER_COL   = "#1E2D5A"
ACCENT_CYAN  = "#00D4FF"
ACCENT_BLUE  = "#4A7BFF"
ACCENT_TEAL  = "#00FFB3"
ACCENT_RED   = "#FF3B6B"
ACCENT_AMBER = "#FFB020"
ACCENT_VIOLET= "#A855F7"
TEXT_PRIMARY = "#E8EEFF"
#TEXT_SECONDARY="#8899CC"
TEXT_SECONDARY="#fafbff"
TEXT_MUTED   = "#f0f7f7"
#TEXT_MUTED   = "#4A5680"
GLOW_CYAN    = "rgba(0,212,255,0.15)"

APP_STYLESHEET = f"""
QMainWindow, QWidget {{
    background-color: {DARK_BG};
    color: {TEXT_PRIMARY};
    font-family: 'Courier New', 'Consolas', monospace;
}}
QTabWidget::pane {{
    border: 1px solid {BORDER_COL};
    background: {PANEL_BG};
    border-radius: 4px;
}}
QTabBar::tab {{
    background: {CARD_BG};
    color: {TEXT_SECONDARY};
    padding: 10px 20px;
    border: 1px solid {BORDER_COL};
    border-bottom: none;
    font-size: 13px;
    letter-spacing: 1px;
    text-transform: uppercase;
}}
QTabBar::tab:selected {{
    background: {PANEL_BG};
    color: {ACCENT_CYAN};
    border-top: 2px solid {ACCENT_CYAN};
}}
QTabBar::tab:hover {{
    color: {TEXT_PRIMARY};
    background: {PANEL_BG};
}}
QTextEdit, QLineEdit {{
    background: {CARD_BG};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_COL};
    border-radius: 4px;
    padding: 8px;
    font-family: 'Courier New', monospace;
    font-size: 13px;
    selection-background-color: {ACCENT_BLUE};
}}
QTextEdit:focus, QLineEdit:focus {{
    border: 1px solid {ACCENT_CYAN};
}}
QPushButton {{
    background: transparent;
    color: {ACCENT_CYAN};
    border: 1px solid {ACCENT_CYAN};
    border-radius: 3px;
    padding: 8px 18px;
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-family: 'Courier New', monospace;
}}
QPushButton:hover {{
    background: {GLOW_CYAN};
    color: #ffffff;
}}
QPushButton:pressed {{
    background: rgba(0,212,255,0.3);
}}
QPushButton#danger {{
    color: {ACCENT_RED};
    border-color: {ACCENT_RED};
}}
QPushButton#danger:hover {{
    background: rgba(255,59,107,0.15);
}}
QPushButton#success {{
    color: {ACCENT_TEAL};
    border-color: {ACCENT_TEAL};
}}
QPushButton#success:hover {{
    background: rgba(0,255,179,0.15);
}}
QPushButton#accent {{
    color: {DARK_BG};
    background: {ACCENT_CYAN};
    border-color: {ACCENT_CYAN};
    font-weight: bold;
}}
QPushButton#accent:hover {{
    background: #33DDFF;
}}
QProgressBar {{
    background: {CARD_BG};
    border: 1px solid {BORDER_COL};
    border-radius: 2px;
    height: 6px;
    text-align: center;
    color: transparent;
}}
QProgressBar::chunk {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {ACCENT_BLUE}, stop:1 {ACCENT_CYAN});
    border-radius: 2px;
}}
QComboBox {{
    background: {CARD_BG};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_COL};
    border-radius: 3px;
    padding: 6px 10px;
    font-family: 'Courier New', monospace;
}}
QComboBox::drop-down {{
    border: none;
    padding-right: 8px;
}}
QComboBox QAbstractItemView {{
    background: {PANEL_BG};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_COL};
    selection-background-color: {ACCENT_BLUE};
}}
QSlider::groove:horizontal {{
    background: {CARD_BG};
    height: 4px;
    border-radius: 2px;
}}
QSlider::handle:horizontal {{
    background: {ACCENT_CYAN};
    width: 14px; height: 14px;
    margin: -5px 0;
    border-radius: 7px;
}}
QSlider::sub-page:horizontal {{
    background: {ACCENT_BLUE};
    border-radius: 2px;
}}
QTableWidget {{
    background: {CARD_BG};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_COL};
    gridline-color: {BORDER_COL};
    font-size: 12px;
}}
QTableWidget::item:selected {{
    background: rgba(74,123,255,0.3);
}}
QHeaderView::section {{
    background: {PANEL_BG};
    color: {ACCENT_CYAN};
    border: 1px solid {BORDER_COL};
    padding: 6px;
    font-size: 13px;
    letter-spacing: 1px;
    text-transform: uppercase;
}}
QScrollBar:vertical {{
    background: {DARK_BG};
    width: 6px;
    border: none;
}}
QScrollBar::handle:vertical {{
    background: {BORDER_COL};
    border-radius: 3px;
    min-height: 20px;
}}
QScrollBar::handle:vertical:hover {{
    background: {ACCENT_BLUE};
}}
QScrollBar:horizontal {{
    background: {DARK_BG};
    height: 6px;
    border: none;
}}
QScrollBar::handle:horizontal {{
    background: {BORDER_COL};
    border-radius: 3px;
}}
QGroupBox {{
    color: {ACCENT_CYAN};
    border: 1px solid {BORDER_COL};
    border-radius: 4px;
    margin-top: 12px;
    padding-top: 8px;
    font-size: 13px;
    letter-spacing: 1px;
    text-transform: uppercase;
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    left: 13px;
    padding: 0 4px;
}}
QListWidget {{
    background: {CARD_BG};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_COL};
    border-radius: 3px;
}}
QListWidget::item:selected {{
    background: rgba(74,123,255,0.3);
    color: {ACCENT_CYAN};
}}
QListWidget::item:hover {{
    background: rgba(74,123,255,0.15);
}}
QCheckBox {{
    color: {TEXT_SECONDARY};
    spacing: 8px;
}}
QCheckBox::indicator {{
    width: 14px; height: 14px;
    border: 1px solid {BORDER_COL};
    border-radius: 2px;
    background: {CARD_BG};
}}
QCheckBox::indicator:checked {{
    background: {ACCENT_BLUE};
    border-color: {ACCENT_BLUE};
}}
QSpinBox {{
    background: {CARD_BG};
    color: {TEXT_PRIMARY};
    border: 1px solid {BORDER_COL};
    border-radius: 3px;
    padding: 4px 8px;
}}
QLabel#section_title {{
    color: {ACCENT_CYAN};
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
}}
QLabel#metric_val {{
    color: {ACCENT_TEAL};
    font-size: 22px;
    font-weight: bold;
}}
QLabel#metric_label {{
    color: {TEXT_MUTED};
    font-size: 12px;
    letter-spacing: 1px;
}}
QFrame#separator {{
    color: {BORDER_COL};
}}
QSplitter::handle {{
    background: {BORDER_COL};
    width: 1px;
    height: 1px;
}}
"""

# ─────────────────────────────────────────────
# CORE ANALYSIS ENGINE
# ─────────────────────────────────────────────
class StyleFeatures:
    """Extract stylometric features from text."""

    @staticmethod
    def extract(text: str) -> dict:
        if not text or len(text.strip()) < 10:
            return {}

        words = re.findall(r'\b\w+\b', text.lower())
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 3]
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        chars = list(text)

        # Lexical richness
        unique_words = set(words)
        ttr = len(unique_words) / max(len(words), 1)
        hapax = sum(1 for w, c in Counter(words).items() if c == 1)
        hapax_ratio = hapax / max(len(unique_words), 1)

        # Word lengths
        word_lengths = [len(w) for w in words]
        avg_word_len = sum(word_lengths) / max(len(word_lengths), 1)
        word_len_dist = Counter(min(len(w), 15) for w in words)

        # Sentence lengths
        sent_lengths = [len(re.findall(r'\b\w+\b', s)) for s in sentences]
        avg_sent_len = sum(sent_lengths) / max(len(sent_lengths), 1)
        sent_var = (sum((l - avg_sent_len)**2 for l in sent_lengths) /
                    max(len(sent_lengths), 1)) ** 0.5

        # Punctuation
        punct_count = sum(1 for c in text if c in string.punctuation)
        punct_ratio = punct_count / max(len(text), 1)
        comma_ratio = text.count(',') / max(len(sentences), 1)
        semi_ratio  = text.count(';') / max(len(text), 1)
        exclaim_ratio = text.count('!') / max(len(sentences), 1)
        question_ratio = text.count('?') / max(len(sentences), 1)

        # Function words (style markers)
        function_words = ['the','a','an','and','or','but','in','on','at',
                          'to','of','for','with','by','from','is','was',
                          'are','were','be','been','being','have','has',
                          'had','do','does','did','will','would','could',
                          'should','may','might','must','shall','can',
                          'this','that','these','those','i','you','he',
                          'she','it','we','they','my','your','his','her',
                          'its','our','their','not','so','as','if','but']
        fw_counts = {w: words.count(w) / max(len(words), 1)
                     for w in function_words}

        # Char n-gram frequencies (2-3 grams)
        text_lower = text.lower()
        bigrams  = Counter(text_lower[i:i+2] for i in range(len(text_lower)-1)
                           if text_lower[i:i+2].strip())
        trigrams = Counter(text_lower[i:i+3] for i in range(len(text_lower)-2)
                           if text_lower[i:i+3].strip())

        # Vocabulary richness (Yule's K)
        freq_dist = Counter(words)
        yules_k = StyleFeatures._yules_k(freq_dist)

        # Readability approximation (Flesch-Kincaid)
        syllables = sum(StyleFeatures._count_syllables(w) for w in words)
        fk_score = (0.39 * avg_sent_len +
                    11.8 * (syllables / max(len(words), 1)) - 15.59)

        # Paragraph stats
        avg_para_len = (sum(len(re.findall(r'\b\w+\b', p)) for p in paragraphs) /
                        max(len(paragraphs), 1))

        # Uppercase ratio
        upper_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)

        # Digit ratio
        digit_ratio = sum(1 for c in text if c.isdigit()) / max(len(text), 1)

        return {
            'word_count': len(words),
            'char_count': len(text),
            'sentence_count': len(sentences),
            'paragraph_count': len(paragraphs),
            'ttr': round(ttr, 4),
            'hapax_ratio': round(hapax_ratio, 4),
            'avg_word_len': round(avg_word_len, 4),
            'avg_sent_len': round(avg_sent_len, 4),
            'sent_variance': round(sent_var, 4),
            'punct_ratio': round(punct_ratio, 4),
            'comma_per_sent': round(comma_ratio, 4),
            'semi_ratio': round(semi_ratio, 6),
            'exclaim_ratio': round(exclaim_ratio, 4),
            'question_ratio': round(question_ratio, 4),
            'yules_k': round(yules_k, 4),
            'fk_score': round(fk_score, 2),
            'avg_para_len': round(avg_para_len, 4),
            'upper_ratio': round(upper_ratio, 4),
            'digit_ratio': round(digit_ratio, 4),
            'word_len_dist': dict(word_len_dist),
            'function_words': fw_counts,
            'top_bigrams': dict(bigrams.most_common(20)),
            'top_trigrams': dict(trigrams.most_common(20)),
            'unique_words': len(unique_words),
            'most_common': dict(Counter(words).most_common(20)),
        }

    @staticmethod
    def _count_syllables(word: str) -> int:
        word = word.lower()
        if len(word) <= 3:
            return 1
        vowels = 'aeiouy'
        count = 0
        prev_vowel = False
        for ch in word:
            is_vowel = ch in vowels
            if is_vowel and not prev_vowel:
                count += 1
            prev_vowel = is_vowel
        if word.endswith('e'):
            count -= 1
        return max(1, count)

    @staticmethod
    def _yules_k(freq_dist: Counter) -> float:
        n = sum(freq_dist.values())
        if n == 0:
            return 0
        m2 = sum(v * v for v in freq_dist.values())
        return 10000 * (m2 - n) / max(n * n, 1)


class SimilarityEngine:
    """Compute style similarity between two feature sets."""

    @staticmethod
    def cosine_similarity(vec_a: dict, vec_b: dict) -> float:
        keys = set(vec_a) | set(vec_b)
        a = [vec_a.get(k, 0) for k in keys]
        b = [vec_b.get(k, 0) for k in keys]
        dot = sum(x*y for x,y in zip(a,b))
        mag_a = math.sqrt(sum(x*x for x in a))
        mag_b = math.sqrt(sum(y*y for y in b))
        return dot / max(mag_a * mag_b, 1e-10)

    @staticmethod
    def feature_vector(features: dict) -> dict:
        scalar_keys = [
            'ttr','hapax_ratio','avg_word_len','avg_sent_len',
            'sent_variance','punct_ratio','comma_per_sent','semi_ratio',
            'exclaim_ratio','question_ratio','yules_k','upper_ratio',
            'digit_ratio','avg_para_len'
        ]
        vec = {k: features.get(k, 0) for k in scalar_keys}
        # Add function word weights
        fw = features.get('function_words', {})
        for k, v in fw.items():
            vec[f'fw_{k}'] = v
        # Word length distribution (normalized)
        wld = features.get('word_len_dist', {})
        total = max(sum(wld.values()), 1)
        for l in range(1, 16):
            vec[f'wl_{l}'] = wld.get(l, 0) / total
        return vec

    @staticmethod
    def compare(feat_a: dict, feat_b: dict) -> dict:
        if not feat_a or not feat_b:
            return {'overall': 0, 'details': {}}

        va = SimilarityEngine.feature_vector(feat_a)
        vb = SimilarityEngine.feature_vector(feat_b)
        overall = SimilarityEngine.cosine_similarity(va, vb)

        # Per-category scores
        details = {}

        # Lexical
        lexical_keys = ['ttr','hapax_ratio','yules_k','avg_word_len']
        la = {k: va.get(k,0) for k in lexical_keys}
        lb = {k: vb.get(k,0) for k in lexical_keys}
        details['lexical_richness'] = SimilarityEngine.cosine_similarity(la, lb)

        # Syntactic
        syn_keys = ['avg_sent_len','sent_variance','comma_per_sent',
                    'semi_ratio','punct_ratio']
        sa = {k: va.get(k,0) for k in syn_keys}
        sb = {k: vb.get(k,0) for k in syn_keys}
        details['syntactic_style'] = SimilarityEngine.cosine_similarity(sa, sb)

        # Function words
        fw_keys = [k for k in va if k.startswith('fw_')]
        fa = {k: va[k] for k in fw_keys}
        fb = {k: vb.get(k,0) for k in fw_keys}
        details['function_words'] = SimilarityEngine.cosine_similarity(fa, fb)

        # Word length profile
        wl_keys = [k for k in va if k.startswith('wl_')]
        wla = {k: va[k] for k in wl_keys}
        wlb = {k: vb.get(k,0) for k in wl_keys}
        details['word_length_profile'] = SimilarityEngine.cosine_similarity(wla, wlb)

        return {'overall': round(overall, 4), 'details': details}


class TamperingDetector:
    """Detect potential tampering or inconsistencies in text."""

    @staticmethod
    def analyze(text: str) -> dict:
        results = {
            'anomalies': [],
            'risk_score': 0,
            'segments': [],
            'encoding_issues': [],
            'style_breaks': [],
        }
        if not text or len(text.strip()) < 50:
            return results

        # Split into paragraphs
        paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 20]
        if len(paragraphs) < 2:
            paragraphs = re.split(r'(?<=[.!?])\s+', text)
            paragraphs = [p for p in paragraphs if len(p.split()) > 5]

        # Analyze per-segment features
        seg_features = []
        for para in paragraphs:
            f = StyleFeatures.extract(para)
            if f:
                seg_features.append({'text': para[:80], 'features': f})

        results['segments'] = seg_features

        # Detect style breaks
        if len(seg_features) >= 2:
            global_features = StyleFeatures.extract(text)
            risk = 0
            for i, seg in enumerate(seg_features):
                sim = SimilarityEngine.compare(global_features, seg['features'])
                score = sim['overall']
                if score < 0.7:
                    results['style_breaks'].append({
                        'segment': i + 1,
                        'text_preview': seg['text'],
                        'similarity': round(score, 3),
                        'severity': 'HIGH' if score < 0.5 else 'MEDIUM'
                    })
                    risk += (1 - score) * 30

            # Check for sudden vocabulary shifts
            all_words = [set(re.findall(r'\b\w+\b', s['text'].lower()))
                         for s in seg_features]
            for i in range(1, len(all_words)):
                overlap = len(all_words[i] & all_words[i-1])
                union   = len(all_words[i] | all_words[i-1])
                jaccard = overlap / max(union, 1)
                if jaccard < 0.05 and len(all_words[i]) > 10:
                    results['anomalies'].append(
                        f'Vocabulary discontinuity at segment {i+1} '
                        f'(Jaccard={jaccard:.3f})')
                    risk += 15

            results['risk_score'] = min(100, int(risk))

        # Encoding anomalies
        for i, ch in enumerate(text):
            if ord(ch) > 0xFFFF:
                results['encoding_issues'].append(
                    f'Non-BMP character U+{ord(ch):04X} at position {i}')
            elif 0x200B <= ord(ch) <= 0x200F:
                results['encoding_issues'].append(
                    f'Zero-width/direction marker at position {i}')
            elif 0x2000 <= ord(ch) <= 0x206F and ch not in ' ':
                results['encoding_issues'].append(
                    f'Special unicode space/format char U+{ord(ch):04X} at pos {i}')

        # Hash fingerprint
        results['sha256'] = hashlib.sha256(text.encode()).hexdigest()
        results['md5'] = hashlib.md5(text.encode()).hexdigest()
        results['char_count'] = len(text)
        results['word_count'] = len(re.findall(r'\b\w+\b', text))
        results['line_count'] = text.count('\n') + 1
        results['timestamp'] = datetime.now().isoformat()

        return results


class AIDetector:
    """Heuristic AI-generated text detection."""

    # Common AI writing patterns and signatures
    AI_PHRASES = [
        r'\bin conclusion\b', r'\bto summarize\b', r'\bfurthermore\b',
        r'\bit is worth noting\b', r'\bit is important to note\b',
        r'\bin addition\b', r'\bmoreover\b', r'\bnevertheless\b',
        r'\bsubsequently\b', r'\bconsequently\b', r'\bultimately\b',
        r'\bit\'s crucial to\b', r'\bit\'s essential to\b',
        r'\bwhen it comes to\b', r'\bin today\'s world\b',
        r'\bin the realm of\b', r'\bdelve into\b', r'\btapestry\b',
        r'\bembark on\b', r'\bunlock\b.{0,20}\bpotential\b',
        r'\bshedding light\b', r'\bpioneering\b', r'\blandscape\b',
        r'\bcomprehensive\b', r'\brobust\b', r'\bseamless\b',
    ]

    @staticmethod
    def analyze(text: str) -> dict:
        if not text or len(text.strip()) < 50:
            return {'score': 0, 'verdict': 'INSUFFICIENT_DATA', 'signals': []}

        text_lower = text.lower()
        signals = []
        score = 0

        # 1. Perplexity-like: measure vocabulary uniformity
        words = re.findall(r'\b\w+\b', text_lower)
        if len(words) > 20:
            freq = Counter(words)
            word_probs = [freq[w]/len(words) for w in words]
            entropy = -sum(p * math.log2(p) for p in word_probs if p > 0)
            norm_entropy = entropy / math.log2(max(len(set(words)), 2))
            if norm_entropy > 0.85:
                score += 15
                signals.append({
                    'type': 'vocabulary_uniformity',
                    'desc': 'High entropy vocabulary distribution (AI-typical)',
                    'value': round(norm_entropy, 3), 'weight': 15
                })

        # 2. Sentence length consistency (AI tends to be uniform)
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if len(s.strip().split()) > 3]
        if len(sentences) >= 3:
            sent_lens = [len(s.split()) for s in sentences]
            mean_len = sum(sent_lens) / len(sent_lens)
            variance = sum((l - mean_len)**2 for l in sent_lens) / len(sent_lens)
            cv = math.sqrt(variance) / max(mean_len, 1)
            if cv < 0.25:
                score += 20
                signals.append({
                    'type': 'sentence_uniformity',
                    'desc': 'Very uniform sentence lengths (AI-typical)',
                    'value': round(cv, 3), 'weight': 20
                })

        # 3. AI cliché phrases
        phrase_hits = []
        for pattern in AIDetector.AI_PHRASES:
            matches = re.findall(pattern, text_lower)
            if matches:
                phrase_hits.extend(matches)
        if phrase_hits:
            phrase_score = min(25, len(phrase_hits) * 5)
            score += phrase_score
            signals.append({
                'type': 'ai_phrases',
                'desc': f'AI-typical phrases detected: {phrase_hits[:5]}',
                'value': len(phrase_hits), 'weight': phrase_score
            })

        # 4. Paragraph structure regularity
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        if len(paragraphs) >= 3:
            para_lens = [len(p.split()) for p in paragraphs]
            para_mean = sum(para_lens) / len(para_lens)
            para_var = sum((l - para_mean)**2 for l in para_lens) / len(para_lens)
            para_cv = math.sqrt(para_var) / max(para_mean, 1)
            if para_cv < 0.2:
                score += 15
                signals.append({
                    'type': 'paragraph_uniformity',
                    'desc': 'Suspiciously uniform paragraph lengths',
                    'value': round(para_cv, 3), 'weight': 15
                })

        # 5. Burstiness (human text is more "bursty")
        if len(words) > 50:
            bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
            bigram_freq = Counter(bigrams)
            repeated = sum(1 for _, c in bigram_freq.items() if c > 1)
            bigram_repeat_ratio = repeated / max(len(bigram_freq), 1)
            if bigram_repeat_ratio < 0.05:
                score += 10
                signals.append({
                    'type': 'low_repetition',
                    'desc': 'Low bigram repetition (AI avoids repetition)',
                    'value': round(bigram_repeat_ratio, 3), 'weight': 10
                })

        # 6. Formal transition words
        transitions = ['firstly','secondly','thirdly','finally','additionally',
                       'notably','particularly','specifically','essentially',
                       'fundamentally','inherently','predominantly']
        trans_count = sum(1 for t in transitions if t in text_lower)
        if trans_count >= 3:
            t_score = min(15, trans_count * 3)
            score += t_score
            signals.append({
                'type': 'transition_density',
                'desc': f'High density of formal transitions ({trans_count} found)',
                'value': trans_count, 'weight': t_score
            })

        score = min(100, score)

        if score >= 70:
            verdict = 'LIKELY_AI'
        elif score >= 45:
            verdict = 'POSSIBLY_AI'
        elif score >= 20:
            verdict = 'UNCERTAIN'
        else:
            verdict = 'LIKELY_HUMAN'

        return {
            'score': score,
            'verdict': verdict,
            'signals': signals,
            'analysis_depth': len(signals),
        }


class TextGenerator:
    """Style-imitation text generator based on source text analysis."""

    @staticmethod
    def generate(source_text: str, prompt: str = '', length: int = 200) -> str:
        """Generate text imitating the style of source_text."""
        if not source_text:
            return "[No source text provided for style imitation]"

        words = re.findall(r'\b\w+\b', source_text)
        sentences = re.split(r'(?<=[.!?])\s+', source_text.strip())
        sentences = [s for s in sentences if len(s.split()) > 3]

        if not words or not sentences:
            return "[Insufficient source text for generation]"

        # Build bigram model
        bigrams = defaultdict(list)
        for i in range(len(words) - 1):
            bigrams[words[i].lower()].append(words[i+1])

        # Extract style parameters
        features = StyleFeatures.extract(source_text)
        avg_sent_len = int(features.get('avg_sent_len', 12))
        punct_ratio  = features.get('punct_ratio', 0.05)

        # Starting vocabulary from prompt or random
        prompt_words = re.findall(r'\b\w+\b', prompt.lower()) if prompt else []
        start_words = [w for w in prompt_words if w in bigrams]
        if not start_words:
            # Pick a random noun-like word from source
            candidate_starts = [w for w in words if w[0].isupper() and
                                 w.lower() in bigrams and len(w) > 3]
            if candidate_starts:
                start_words = [random.choice(candidate_starts)]
            else:
                start_words = [random.choice(list(bigrams.keys()))]

        # Generate word-by-word
        current = start_words[-1].lower()
        generated = [start_words[-1].capitalize()]
        word_count = 0
        sent_word_count = 0
        target_sent_len = max(5, int(random.gauss(avg_sent_len, avg_sent_len * 0.3)))

        while word_count < length:
            nexts = bigrams.get(current, [])
            if not nexts:
                # Restart from random
                current = random.choice(list(bigrams.keys()))
                next_word = current.capitalize()
            else:
                next_word = random.choice(nexts)
                current = next_word.lower()

            word_count += 1
            sent_word_count += 1

            # End sentence?
            if sent_word_count >= target_sent_len:
                # Pick appropriate ending from source sentences
                punct = '.' if random.random() > punct_ratio * 5 else \
                        (',' if random.random() > 0.5 else '.')
                generated.append(next_word.rstrip('.,!?;:') + '.')
                generated.append('')  # new sentence marker
                sent_word_count = 0
                target_sent_len = max(5, int(random.gauss(avg_sent_len,
                                                           avg_sent_len * 0.3)))
                current = random.choice(list(bigrams.keys()))
            else:
                generated.append(next_word)

        # Post-process: reconstruct sentences
        result_words = []
        cap_next = False
        for w in generated:
            if w == '':
                cap_next = True
                continue
            if cap_next:
                result_words.append(w.capitalize())
                cap_next = False
            else:
                result_words.append(w)

        text = ' '.join(result_words)
        # Clean up spacing around punctuation
        text = re.sub(r'\s([.,!?;:])', r'\1', text)
        text = re.sub(r'\s+', ' ', text)

        if not text.rstrip().endswith('.'):
            text = text.rstrip() + '.'

        return text


# ─────────────────────────────────────────────
# UI COMPONENTS
# ─────────────────────────────────────────────
class GlowLabel(QLabel):
    def __init__(self, text='', parent=None, color=ACCENT_CYAN):
        super().__init__(text, parent)
        self._color = color

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        super().paintEvent(event)


class MetricCard(QFrame):
    def __init__(self, label: str, value: str = '—',
                 color: str = ACCENT_TEAL, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setStyleSheet(f"""
            QFrame {{
                background: {CARD_BG};
                border: 1px solid {BORDER_COL};
                border-radius: 4px;
                padding: 2px;
            }}
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(4)
        layout.setContentsMargins(12, 10, 12, 10)

        self.val_label = QLabel(value)
        self.val_label.setStyleSheet(f"""
            color: {color};
            font-size: 20px;
            font-weight: bold;
            font-family: 'Courier New', monospace;
        """)
        self.val_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lbl_label = QLabel(label)
        self.lbl_label.setStyleSheet(f"""
            color: {TEXT_MUTED};
            font-size: 12px;
            letter-spacing: 1px;
            text-transform: uppercase;
        """)
        self.lbl_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.val_label)
        layout.addWidget(self.lbl_label)

    def set_value(self, value: str):
        self.val_label.setText(str(value))


class SimilarityBar(QWidget):
    def __init__(self, label: str, value: float = 0, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 3, 0, 3)
        layout.setSpacing(10)

        lbl = QLabel(label)
        lbl.setFixedWidth(160)
        lbl.setStyleSheet(f'color: {TEXT_SECONDARY}; font-size: 11px;')
        layout.addWidget(lbl)

        self.bar = QProgressBar()
        self.bar.setRange(0, 100)
        self.bar.setValue(int(value * 100))
        self.bar.setFixedHeight(8)
        layout.addWidget(self.bar)

        self.val_lbl = QLabel(f'{value:.1%}')
        self.val_lbl.setFixedWidth(50)
        self.val_lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
        color = ACCENT_TEAL if value >= 0.7 else \
                (ACCENT_AMBER if value >= 0.4 else ACCENT_RED)
        self.val_lbl.setStyleSheet(f'color: {color}; font-size: 11px; font-weight: bold;')
        layout.addWidget(self.val_lbl)

    def set_value(self, value: float):
        self.bar.setValue(int(value * 100))
        self.val_lbl.setText(f'{value:.1%}')
        color = ACCENT_TEAL if value >= 0.7 else \
                (ACCENT_AMBER if value >= 0.4 else ACCENT_RED)
        self.val_lbl.setStyleSheet(f'color: {color}; font-size: 11px; font-weight: bold;')


class SectionHeader(QLabel):
    def __init__(self, text: str, parent=None):
        super().__init__(f'▸  {text}', parent)
        self.setStyleSheet(f"""
            color: {ACCENT_CYAN};
            font-size: 12px;
            letter-spacing: 2px;
            text-transform: uppercase;
            padding: 8px 0 4px 0;
            border-bottom: 1px solid {BORDER_COL};
            margin-bottom: 6px;
        """)


class StatusBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(28)
        self.setStyleSheet(f"""
            background: {DARK_BG};
            border-top: 1px solid {BORDER_COL};
        """)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 0, 12, 0)
        layout.setSpacing(20)

        self.status_label = QLabel('READY')
        self.status_label.setStyleSheet(f'color: {ACCENT_TEAL}; font-size: 12px; letter-spacing: 1px;')

        self.info_label = QLabel('文本取证系统 · Text Forensics Suite v1.0')
        self.info_label.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 14px; letter-spacing: 1px;')

        self.time_label = QLabel()
        self.time_label.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 12px;')

        layout.addWidget(self.status_label)
        layout.addWidget(self.info_label)
        layout.addStretch()
        layout.addWidget(self.time_label)

        timer = QTimer(self)
        timer.timeout.connect(self._update_time)
        timer.start(1000)
        self._update_time()

    def _update_time(self):
        self.time_label.setText(datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))

    def set_status(self, text: str, color: str = ACCENT_TEAL):
        self.status_label.setText(text)
        self.status_label.setStyleSheet(f'color: {color}; font-size: 12px; letter-spacing: 1px;')


# ─────────────────────────────────────────────
# TAB: AUTHORSHIP ATTRIBUTION
# ─────────────────────────────────────────────
class AuthorshipTab(QWidget):
    status_update = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
        self.author_profiles = {}

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(splitter)

        # ── LEFT: Author profiles panel ──
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(16, 16, 8, 16)

        left_layout.addWidget(SectionHeader('Author Profiles'))

        # Author list
        self.author_list = QListWidget()
        self.author_list.setFixedHeight(160)
        left_layout.addWidget(self.author_list)

        # Author management
        btn_row = QHBoxLayout()
        self.author_name_input = QLineEdit()
        self.author_name_input.setPlaceholderText('Author name...')
        btn_row.addWidget(self.author_name_input)

        add_btn = QPushButton('+ ADD')
        add_btn.clicked.connect(self._add_author)
        btn_row.addWidget(add_btn)
        left_layout.addLayout(btn_row)

        del_btn = QPushButton('REMOVE SELECTED')
        del_btn.setObjectName('danger')
        del_btn.clicked.connect(self._remove_author)
        left_layout.addWidget(del_btn)

        left_layout.addWidget(SectionHeader('Training Text'))

        self.training_text = QTextEdit()
        self.training_text.setPlaceholderText(
            'Paste sample writing for selected author...\n\n'
            '• At least 200+ words for better accuracy\n'
            '• Multiple samples can be appended\n'
            '• The more text, the better the profile')
        self.training_text.setMinimumHeight(180)
        left_layout.addWidget(self.training_text)

        train_btn = QPushButton('BUILD PROFILE')
        train_btn.setObjectName('accent')
        train_btn.clicked.connect(self._build_profile)
        left_layout.addWidget(train_btn)

        # Profile stats
        self.profile_info = QLabel('No profiles built yet.')
        self.profile_info.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 12px; padding: 4px;')
        self.profile_info.setWordWrap(True)
        left_layout.addWidget(self.profile_info)

        left_layout.addStretch()
        splitter.addWidget(left)

        # ── CENTER: Unknown text ──
        center = QWidget()
        center_layout = QVBoxLayout(center)
        center_layout.setContentsMargins(8, 16, 8, 16)

        center_layout.addWidget(SectionHeader('Unknown Text — To Attribute'))

        self.unknown_text = QTextEdit()
        self.unknown_text.setPlaceholderText(
            'Paste the text of unknown authorship here...\n\n'
            'The system will analyze the writing style and compare '
            'it against all built author profiles to determine the '
            'most likely author.')
        center_layout.addWidget(self.unknown_text)

        btn_row2 = QHBoxLayout()
        analyze_btn = QPushButton('ANALYZE AUTHORSHIP')
        analyze_btn.setObjectName('accent')
        analyze_btn.clicked.connect(self._analyze)
        btn_row2.addWidget(analyze_btn)

        clear_btn = QPushButton('CLEAR')
        clear_btn.clicked.connect(self.unknown_text.clear)
        btn_row2.addWidget(clear_btn)
        center_layout.addLayout(btn_row2)

        splitter.addWidget(center)

        # ── RIGHT: Results ──
        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(8, 16, 16, 16)

        right_layout.addWidget(SectionHeader('Attribution Results'))

        # Verdict box
        self.verdict_label = QLabel('AWAITING ANALYSIS')
        self.verdict_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verdict_label.setStyleSheet(f"""
            background: {CARD_BG};
            border: 2px solid {BORDER_COL};
            border-radius: 6px;
            color: {TEXT_MUTED};
            font-size: 16px;
            font-weight: bold;
            letter-spacing: 3px;
            padding: 20px;
        """)
        right_layout.addWidget(self.verdict_label)

        # Confidence bars
        self.bars_widget = QWidget()
        self.bars_layout = QVBoxLayout(self.bars_widget)
        self.bars_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.addWidget(self.bars_widget)

        # Metrics
        metrics_grid = QGridLayout()
        self.m_words   = MetricCard('WORDS', '—', ACCENT_CYAN)
        self.m_ttr     = MetricCard('TYPE-TOKEN RATIO', '—', ACCENT_VIOLET)
        self.m_sent    = MetricCard('AVG SENT LEN', '—', ACCENT_BLUE)
        self.m_flesch  = MetricCard('READABILITY', '—', ACCENT_AMBER)
        metrics_grid.addWidget(self.m_words, 0, 0)
        metrics_grid.addWidget(self.m_ttr, 0, 1)
        metrics_grid.addWidget(self.m_sent, 1, 0)
        metrics_grid.addWidget(self.m_flesch, 1, 1)
        right_layout.addLayout(metrics_grid)

        # Top words table
        self.words_table = QTableWidget(0, 2)
        self.words_table.setHorizontalHeaderLabels(['WORD', 'FREQUENCY'])
        self.words_table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch)
        self.words_table.setMaximumHeight(200)
        right_layout.addWidget(self.words_table)

        right_layout.addStretch()
        splitter.addWidget(right)
        splitter.setSizes([280, 420, 320])

    def _add_author(self):
        name = self.author_name_input.text().strip()
        if not name:
            return
        if not any(self.author_list.item(i).text() == name
                   for i in range(self.author_list.count())):
            self.author_list.addItem(name)
        self.author_name_input.clear()

    def _remove_author(self):
        row = self.author_list.currentRow()
        if row >= 0:
            name = self.author_list.item(row).text()
            self.author_list.takeItem(row)
            self.author_profiles.pop(name, None)
            self._refresh_profile_info()

    def _build_profile(self):
        selected = self.author_list.currentItem()
        if not selected:
            QMessageBox.warning(self, 'Warning', 'Select an author first.')
            return
        text = self.training_text.toPlainText().strip()
        if len(text.split()) < 50:
            QMessageBox.warning(self, 'Warning', 'Please provide at least 50 words.')
            return
        name = selected.text()
        features = StyleFeatures.extract(text)
        if name in self.author_profiles:
            # Merge features (average)
            old = self.author_profiles[name]['features']
            scalar_keys = ['ttr','hapax_ratio','avg_word_len','avg_sent_len',
                           'sent_variance','punct_ratio','yules_k','fk_score']
            for k in scalar_keys:
                old[k] = (old.get(k,0) + features.get(k,0)) / 2
            self.author_profiles[name]['text'] += ' ' + text
            self.author_profiles[name]['features'] = old
            self.author_profiles[name]['samples'] += 1
        else:
            self.author_profiles[name] = {
                'features': features, 'text': text, 'samples': 1
            }
        self._refresh_profile_info()
        self.training_text.clear()
        self.status_update.emit(f'Profile built for {name}', ACCENT_TEAL)

    def _refresh_profile_info(self):
        if not self.author_profiles:
            self.profile_info.setText('No profiles built yet.')
            return
        lines = []
        for name, data in self.author_profiles.items():
            wc = data['features'].get('word_count', 0)
            lines.append(f'✓ {name}: {wc} words, {data["samples"]} sample(s)')
        self.profile_info.setText('\n'.join(lines))

    def _analyze(self):
        text = self.unknown_text.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, 'Warning', 'Paste unknown text first.')
            return
        if not self.author_profiles:
            QMessageBox.warning(self, 'Warning', 'Build at least one author profile first.')
            return

        features = StyleFeatures.extract(text)
        self.m_words.set_value(str(features.get('word_count', 0)))
        self.m_ttr.set_value(f"{features.get('ttr', 0):.3f}")
        self.m_sent.set_value(f"{features.get('avg_sent_len', 0):.1f}")
        self.m_flesch.set_value(f"{features.get('fk_score', 0):.1f}")

        # Compare against all profiles
        similarities = {}
        for name, data in self.author_profiles.items():
            sim = SimilarityEngine.compare(data['features'], features)
            similarities[name] = sim['overall']

        # Clear bars
        for i in reversed(range(self.bars_layout.count())):
            self.bars_layout.itemAt(i).widget().deleteLater()

        sorted_sims = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        for name, score in sorted_sims:
            bar = SimilarityBar(name, score)
            self.bars_layout.addWidget(bar)

        # Verdict
        best_name, best_score = sorted_sims[0]
        if best_score >= 0.80:
            confidence = 'HIGH CONFIDENCE'
            color = ACCENT_TEAL
        elif best_score >= 0.60:
            confidence = 'MODERATE CONFIDENCE'
            color = ACCENT_AMBER
        else:
            confidence = 'LOW CONFIDENCE'
            color = ACCENT_RED

        self.verdict_label.setText(f'{best_name}')
        self.verdict_label.setStyleSheet(f"""
            background: {CARD_BG};
            border: 2px solid {color};
            border-radius: 6px;
            color: {color};
            font-size: 18px;
            font-weight: bold;
            letter-spacing: 3px;
            padding: 20px;
        """)

        # Top words
        common = features.get('most_common', {})
        self.words_table.setRowCount(0)
        for word, cnt in list(common.items())[:15]:
            row = self.words_table.rowCount()
            self.words_table.insertRow(row)
            self.words_table.setItem(row, 0, QTableWidgetItem(word))
            self.words_table.setItem(row, 1, QTableWidgetItem(str(cnt)))

        self.status_update.emit(f'Attribution: {best_name} ({confidence}, {best_score:.1%})', ACCENT_TEAL)


# ─────────────────────────────────────────────
# TAB: SAME AUTHOR DETECTION
# ─────────────────────────────────────────────
class SameAuthorTab(QWidget):
    status_update = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)

        layout.addWidget(SectionHeader('Same Author Detection — Side-by-Side Comparison'))

        # Two text panels
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Text A
        left = QWidget()
        ll = QVBoxLayout(left)
        ll.setContentsMargins(0, 0, 8, 0)
        lbl_a = QLabel('TEXT  A')
        lbl_a.setStyleSheet(f'color: {ACCENT_BLUE}; font-size: 12px; font-weight: bold; letter-spacing: 2px; padding: 4px;')
        ll.addWidget(lbl_a)
        self.text_a = QTextEdit()
        self.text_a.setPlaceholderText('Paste first text sample here...')
        ll.addWidget(self.text_a)
        splitter.addWidget(left)

        # Text B
        right = QWidget()
        rl = QVBoxLayout(right)
        rl.setContentsMargins(8, 0, 0, 0)
        lbl_b = QLabel('TEXT  B')
        lbl_b.setStyleSheet(f'color: {ACCENT_VIOLET}; font-size: 12px; font-weight: bold; letter-spacing: 2px; padding: 4px;')
        rl.addWidget(lbl_b)
        self.text_b = QTextEdit()
        self.text_b.setPlaceholderText('Paste second text sample here...')
        rl.addWidget(self.text_b)
        splitter.addWidget(right)

        layout.addWidget(splitter)

        # Analyze button
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        analyze_btn = QPushButton('COMPARE AUTHORSHIP')
        analyze_btn.setObjectName('accent')
        analyze_btn.setFixedWidth(200)
        analyze_btn.clicked.connect(self._analyze)
        btn_row.addWidget(analyze_btn)
        clear_btn = QPushButton('CLEAR ALL')
        clear_btn.clicked.connect(self._clear)
        btn_row.addWidget(clear_btn)
        btn_row.addStretch()
        layout.addLayout(btn_row)

        # Results
        results_row = QHBoxLayout()

        # Verdict
        verdict_frame = QFrame()
        verdict_frame.setStyleSheet(f'background: {CARD_BG}; border: 1px solid {BORDER_COL}; border-radius: 4px;')
        verdict_layout = QVBoxLayout(verdict_frame)
        verdict_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verdict_label = QLabel('—')
        self.verdict_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verdict_label.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 28px; font-weight: bold;')
        verdict_layout.addWidget(self.verdict_label)

        self.confidence_label = QLabel('Paste texts and compare')
        self.confidence_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.confidence_label.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 10px; letter-spacing: 1px;')
        verdict_layout.addWidget(self.confidence_label)

        self.similarity_pct = QLabel('')
        self.similarity_pct.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.similarity_pct.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 13px;')
        verdict_layout.addWidget(self.similarity_pct)

        verdict_frame.setFixedWidth(260)
        results_row.addWidget(verdict_frame)

        # Category breakdown
        breakdown_widget = QWidget()
        breakdown_layout = QVBoxLayout(breakdown_widget)
        breakdown_layout.setSpacing(6)
        breakdown_layout.addWidget(SectionHeader('Similarity Breakdown'))

        self.bar_lexical   = SimilarityBar('Lexical Richness', 0)
        self.bar_syntactic = SimilarityBar('Syntactic Style', 0)
        self.bar_function  = SimilarityBar('Function Words', 0)
        self.bar_wordlen   = SimilarityBar('Word Length Profile', 0)
        self.bar_overall   = SimilarityBar('OVERALL SIMILARITY', 0)

        for bar in [self.bar_lexical, self.bar_syntactic,
                    self.bar_function, self.bar_wordlen, self.bar_overall]:
            breakdown_layout.addWidget(bar)

        breakdown_layout.addStretch()
        results_row.addWidget(breakdown_widget)

        # Feature comparison table
        table_widget = QWidget()
        table_layout = QVBoxLayout(table_widget)
        table_layout.addWidget(SectionHeader('Feature Comparison'))

        self.feature_table = QTableWidget(0, 3)
        self.feature_table.setHorizontalHeaderLabels(['FEATURE', 'TEXT A', 'TEXT B'])
        self.feature_table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch)
        table_layout.addWidget(self.feature_table)
        results_row.addWidget(table_widget)

        layout.addLayout(results_row)

    def _clear(self):
        self.text_a.clear()
        self.text_b.clear()
        self.verdict_label.setText('—')
        self.confidence_label.setText('Paste texts and compare')
        self.similarity_pct.setText('')
        for bar in [self.bar_lexical, self.bar_syntactic,
                    self.bar_function, self.bar_wordlen, self.bar_overall]:
            bar.set_value(0)
        self.feature_table.setRowCount(0)

    def _analyze(self):
        text_a = self.text_a.toPlainText().strip()
        text_b = self.text_b.toPlainText().strip()
        if not text_a or not text_b:
            QMessageBox.warning(self, 'Warning', 'Please provide both text samples.')
            return

        feat_a = StyleFeatures.extract(text_a)
        feat_b = StyleFeatures.extract(text_b)
        result = SimilarityEngine.compare(feat_a, feat_b)

        overall = result['overall']
        details = result['details']

        self.bar_overall.set_value(overall)
        self.bar_lexical.set_value(details.get('lexical_richness', 0))
        self.bar_syntactic.set_value(details.get('syntactic_style', 0))
        self.bar_function.set_value(details.get('function_words', 0))
        self.bar_wordlen.set_value(details.get('word_length_profile', 0))

        # Verdict
        if overall >= 0.82:
            verdict = 'SAME AUTHOR'
            color = ACCENT_TEAL
            conf = 'High Confidence'
        elif overall >= 0.65:
            verdict = 'POSSIBLY SAME'
            color = ACCENT_AMBER
            conf = 'Moderate Confidence'
        elif overall >= 0.45:
            verdict = 'UNCERTAIN'
            color = ACCENT_AMBER
            conf = 'Low Confidence'
        else:
            verdict = 'DIFFERENT AUTHORS'
            color = ACCENT_RED
            conf = 'High Confidence'

        self.verdict_label.setText(verdict)
        self.verdict_label.setStyleSheet(f'color: {color}; font-size: 22px; font-weight: bold;')
        self.confidence_label.setText(conf)
        self.confidence_label.setStyleSheet(f'color: {color}; font-size: 10px; letter-spacing: 1px;')
        self.similarity_pct.setText(f'Similarity: {overall:.1%}')

        # Feature table
        compare_features = [
            ('Word Count', 'word_count', '{:.0f}'),
            ('Type-Token Ratio', 'ttr', '{:.4f}'),
            ('Hapax Ratio', 'hapax_ratio', '{:.4f}'),
            ('Avg Word Length', 'avg_word_len', '{:.2f}'),
            ('Avg Sentence Length', 'avg_sent_len', '{:.1f}'),
            ('Sent. Variance', 'sent_variance', '{:.2f}'),
            ('Punct. Ratio', 'punct_ratio', '{:.4f}'),
            ("Yule's K", 'yules_k', '{:.2f}'),
            ('Readability (FK)', 'fk_score', '{:.1f}'),
            ('Unique Words', 'unique_words', '{:.0f}'),
        ]
        self.feature_table.setRowCount(0)
        for label, key, fmt in compare_features:
            va = feat_a.get(key, 0)
            vb = feat_b.get(key, 0)
            row = self.feature_table.rowCount()
            self.feature_table.insertRow(row)
            self.feature_table.setItem(row, 0, QTableWidgetItem(label))
            ia = QTableWidgetItem(fmt.format(va))
            ib = QTableWidgetItem(fmt.format(vb))

            # Color code divergence
            try:
                diff = abs(float(va) - float(vb)) / max(abs(float(va)), abs(float(vb)), 1)
                if diff > 0.3:
                    for item in [ia, ib]:
                        item.setForeground(QColor(ACCENT_RED))
            except:
                pass

            self.feature_table.setItem(row, 1, ia)
            self.feature_table.setItem(row, 2, ib)

        self.status_update.emit(f'Same-author analysis: {verdict} ({overall:.1%})', ACCENT_TEAL)


# ─────────────────────────────────────────────
# TAB: TAMPERING DETECTION
# ─────────────────────────────────────────────
class TamperingTab(QWidget):
    status_update = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(splitter)

        # Left: input
        left = QWidget()
        ll = QVBoxLayout(left)
        ll.setContentsMargins(16, 16, 8, 16)

        ll.addWidget(SectionHeader('Text to Examine'))

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText(
            'Paste text to examine for tampering, inconsistencies, '
            'encoding anomalies, and style breaks...\n\n'
            'The forensic engine will:\n'
            '• Compute cryptographic hashes\n'
            '• Detect style discontinuities\n'
            '• Find encoding anomalies\n'
            '• Identify vocabulary shifts')
        ll.addWidget(self.text_input)

        btn_row = QHBoxLayout()
        analyze_btn = QPushButton('RUN FORENSIC SCAN')
        analyze_btn.setObjectName('accent')
        analyze_btn.clicked.connect(self._analyze)
        btn_row.addWidget(analyze_btn)

        load_btn = QPushButton('LOAD FILE')
        load_btn.clicked.connect(self._load_file)
        btn_row.addWidget(load_btn)
        ll.addLayout(btn_row)

        # Hash display
        hash_group = QGroupBox('Cryptographic Fingerprint')
        hash_layout = QVBoxLayout(hash_group)

        self.sha_label = QLabel('SHA-256: —')
        self.sha_label.setStyleSheet(f'color: {TEXT_SECONDARY}; font-size: 12px; font-family: monospace;')
        self.sha_label.setWordWrap(True)
        hash_layout.addWidget(self.sha_label)

        self.md5_label = QLabel('MD5: —')
        self.md5_label.setStyleSheet(f'color: {TEXT_SECONDARY}; font-size: 12px; font-family: monospace;')
        hash_layout.addWidget(self.md5_label)

        self.stats_label = QLabel('Size: — chars  |  Words: —  |  Lines: —')
        self.stats_label.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 12px;')
        hash_layout.addWidget(self.stats_label)

        ll.addWidget(hash_group)
        ll.addStretch()
        splitter.addWidget(left)

        # Right: results
        right = QWidget()
        rl = QVBoxLayout(right)
        rl.setContentsMargins(8, 16, 16, 16)

        # Risk score
        risk_frame = QFrame()
        risk_frame.setStyleSheet(f'background: {CARD_BG}; border: 1px solid {BORDER_COL}; border-radius: 4px;')
        risk_layout = QHBoxLayout(risk_frame)
        risk_layout.setContentsMargins(16, 12, 16, 12)

        risk_left = QVBoxLayout()
        risk_lbl = QLabel('TAMPERING RISK SCORE')
        risk_lbl.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 12px; letter-spacing: 1px;')
        self.risk_score = QLabel('—')
        self.risk_score.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 36px; font-weight: bold;')
        risk_left.addWidget(risk_lbl)
        risk_left.addWidget(self.risk_score)
        risk_layout.addLayout(risk_left)

        self.risk_bar = QProgressBar()
        self.risk_bar.setRange(0, 100)
        self.risk_bar.setValue(0)
        self.risk_bar.setOrientation(Qt.Orientation.Vertical)
        self.risk_bar.setFixedSize(20, 70)
        risk_layout.addWidget(self.risk_bar)

        rl.addWidget(risk_frame)

        # Style breaks
        rl.addWidget(SectionHeader('Style Discontinuities'))
        self.breaks_table = QTableWidget(0, 3)
        self.breaks_table.setHorizontalHeaderLabels(['SEGMENT', 'SIMILARITY', 'SEVERITY'])
        self.breaks_table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch)
        self.breaks_table.setFixedHeight(160)
        rl.addWidget(self.breaks_table)

        # Anomalies
        rl.addWidget(SectionHeader('Detected Anomalies'))
        self.anomaly_list = QListWidget()
        self.anomaly_list.setFixedHeight(100)
        rl.addWidget(self.anomaly_list)

        # Encoding issues
        rl.addWidget(SectionHeader('Encoding Issues'))
        self.encoding_list = QListWidget()
        self.encoding_list.setFixedHeight(80)
        rl.addWidget(self.encoding_list)

        rl.addStretch()
        splitter.addWidget(right)
        splitter.setSizes([480, 400])

    def _load_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, 'Open Text File', '', 'Text Files (*.txt *.md *.csv *.json *.log);;All Files (*)')
        if path:
            try:
                with open(path, 'r', encoding='utf-8', errors='replace') as f:
                    self.text_input.setPlainText(f.read())
                self.status_update.emit(f'Loaded: {os.path.basename(path)}', ACCENT_CYAN)
            except Exception as e:
                QMessageBox.critical(self, 'Error', str(e))

    def _analyze(self):
        text = self.text_input.toPlainText()
        if not text.strip():
            QMessageBox.warning(self, 'Warning', 'Please provide text to analyze.')
            return

        result = TamperingDetector.analyze(text)

        # Update hashes
        self.sha_label.setText(f'SHA-256: {result.get("sha256", "—")}')
        self.md5_label.setText(f'MD5: {result.get("md5", "—")}')
        self.stats_label.setText(
            f'Size: {result.get("char_count",0):,} chars  |  '
            f'Words: {result.get("word_count",0):,}  |  '
            f'Lines: {result.get("line_count",0):,}')

        # Risk score
        risk = result.get('risk_score', 0)
        self.risk_bar.setValue(risk)
        color = ACCENT_TEAL if risk < 30 else (ACCENT_AMBER if risk < 60 else ACCENT_RED)
        self.risk_score.setText(f'{risk}')
        self.risk_score.setStyleSheet(f'color: {color}; font-size: 36px; font-weight: bold;')
        verdict = 'LOW RISK' if risk < 30 else ('MODERATE RISK' if risk < 60 else 'HIGH RISK')

        # Style breaks
        self.breaks_table.setRowCount(0)
        for sb in result.get('style_breaks', []):
            row = self.breaks_table.rowCount()
            self.breaks_table.insertRow(row)
            preview = sb.get('text_preview', '')[:50] + '...'
            self.breaks_table.setItem(row, 0, QTableWidgetItem(f'§{sb["segment"]} — {preview}'))
            sim_item = QTableWidgetItem(f'{sb["similarity"]:.3f}')
            sev = sb.get('severity', '')
            sev_item = QTableWidgetItem(sev)
            sev_item.setForeground(QColor(ACCENT_RED if sev == 'HIGH' else ACCENT_AMBER))
            self.breaks_table.setItem(row, 1, sim_item)
            self.breaks_table.setItem(row, 2, sev_item)

        # Anomalies
        self.anomaly_list.clear()
        anomalies = result.get('anomalies', [])
        if not anomalies:
            self.anomaly_list.addItem('✓ No vocabulary anomalies detected')
        for a in anomalies:
            item = QListWidgetItem(f'⚠ {a}')
            item.setForeground(QColor(ACCENT_AMBER))
            self.anomaly_list.addItem(item)

        # Encoding issues
        self.encoding_list.clear()
        enc_issues = result.get('encoding_issues', [])
        if not enc_issues:
            self.encoding_list.addItem('✓ No encoding anomalies detected')
        for e in enc_issues:
            item = QListWidgetItem(f'⚠ {e}')
            item.setForeground(QColor(ACCENT_RED))
            self.encoding_list.addItem(item)

        self.status_update.emit(f'Forensic scan: {verdict} (score={risk})', color)


# ─────────────────────────────────────────────
# TAB: AI DETECTION
# ─────────────────────────────────────────────
class AIDetectionTab(QWidget):
    status_update = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(splitter)

        # Left: input
        left = QWidget()
        ll = QVBoxLayout(left)
        ll.setContentsMargins(16, 16, 8, 16)

        ll.addWidget(SectionHeader('Text to Examine'))

        info = QLabel('Analyzes writing patterns to detect AI-generated content. '
                      'Examines sentence uniformity, vocabulary distribution, '
                      'AI phrase patterns, and burstiness.')
        info.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 12px; padding: 4px 0;')
        info.setWordWrap(True)
        ll.addWidget(info)

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText('Paste text to analyze for AI generation...')
        ll.addWidget(self.text_input)

        btn_row = QHBoxLayout()
        analyze_btn = QPushButton('DEEP FORENSIC SCAN')
        analyze_btn.setObjectName('accent')
        analyze_btn.clicked.connect(self._analyze)
        btn_row.addWidget(analyze_btn)
        clear_btn = QPushButton('CLEAR')
        clear_btn.clicked.connect(self.text_input.clear)
        btn_row.addWidget(clear_btn)
        ll.addLayout(btn_row)

        disclaimer = QLabel(
            '⚠ Note: Heuristic detection only. No method achieves 100% accuracy. '
            'Use as one signal among many.')
        disclaimer.setStyleSheet(f'color: {ACCENT_AMBER}; font-size: 12px; padding: 4px 0;')
        disclaimer.setWordWrap(True)
        ll.addWidget(disclaimer)
        ll.addStretch()
        splitter.addWidget(left)

        # Right: results
        right = QWidget()
        rl = QVBoxLayout(right)
        rl.setContentsMargins(8, 16, 16, 16)

        # Verdict
        verdict_frame = QFrame()
        verdict_frame.setStyleSheet(f'background: {CARD_BG}; border: 1px solid {BORDER_COL}; border-radius: 4px;')
        verdict_layout = QVBoxLayout(verdict_frame)
        verdict_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        verdict_layout.setContentsMargins(20, 20, 20, 20)

        self.verdict_label = QLabel('AWAITING SCAN')
        self.verdict_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verdict_label.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 20px; font-weight: bold; letter-spacing: 3px;')
        verdict_layout.addWidget(self.verdict_label)

        self.score_label = QLabel('—')
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_label.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 40px; font-weight: bold;')
        verdict_layout.addWidget(self.score_label)

        score_lbl = QLabel('AI PROBABILITY SCORE (0–100)')
        score_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        score_lbl.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 12px; letter-spacing: 1px;')
        verdict_layout.addWidget(score_lbl)

        self.score_bar = QProgressBar()
        self.score_bar.setRange(0, 100)
        self.score_bar.setValue(0)
        self.score_bar.setFixedHeight(12)
        verdict_layout.addWidget(self.score_bar)

        rl.addWidget(verdict_frame)

        # Signal breakdown
        rl.addWidget(SectionHeader('Detection Signals'))

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet(f'background: {CARD_BG}; border: 1px solid {BORDER_COL};')
        self.signals_widget = QWidget()
        self.signals_layout = QVBoxLayout(self.signals_widget)
        self.signals_layout.setContentsMargins(8, 8, 8, 8)
        scroll.setWidget(self.signals_widget)
        rl.addWidget(scroll)

        rl.addStretch()
        splitter.addWidget(right)
        splitter.setSizes([480, 400])

    def _analyze(self):
        text = self.text_input.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, 'Warning', 'Please paste text to analyze.')
            return

        result = AIDetector.analyze(text)
        score = result['score']
        verdict = result['verdict']

        color = ACCENT_TEAL if verdict == 'LIKELY_HUMAN' else \
                (ACCENT_AMBER if verdict in ('UNCERTAIN','POSSIBLY_AI') else ACCENT_RED)

        label_map = {
            'LIKELY_HUMAN':  'LIKELY HUMAN',
            'UNCERTAIN':     'UNCERTAIN',
            'POSSIBLY_AI':   'POSSIBLY AI',
            'LIKELY_AI':     'LIKELY AI-GENERATED',
            'INSUFFICIENT_DATA': 'INSUFFICIENT DATA',
        }

        self.verdict_label.setText(label_map.get(verdict, verdict))
        self.verdict_label.setStyleSheet(f'color: {color}; font-size: 20px; font-weight: bold; letter-spacing: 2px;')
        self.score_label.setText(str(score))
        self.score_label.setStyleSheet(f'color: {color}; font-size: 40px; font-weight: bold;')
        self.score_bar.setValue(score)
        self.score_bar.setStyleSheet(f"""
            QProgressBar::chunk {{
                background: {color};
            }}
        """)

        # Signals
        for i in reversed(range(self.signals_layout.count())):
            w = self.signals_layout.itemAt(i).widget()
            if w:
                w.deleteLater()

        signals = result.get('signals', [])
        if not signals:
            lbl = QLabel('No significant AI signals detected.')
            lbl.setStyleSheet(f'color: {ACCENT_TEAL}; font-size: 11px; padding: 8px;')
            self.signals_layout.addWidget(lbl)
        else:
            for sig in signals:
                frame = QFrame()
                frame.setStyleSheet(f'background: {PANEL_BG}; border: 1px solid {BORDER_COL}; border-radius: 3px; margin: 2px;')
                frame_layout = QHBoxLayout(frame)
                frame_layout.setContentsMargins(10, 8, 10, 8)

                weight_label = QLabel(f'+{sig["weight"]}')
                weight_label.setStyleSheet(f'color: {ACCENT_RED}; font-size: 14px; font-weight: bold; min-width: 35px;')
                frame_layout.addWidget(weight_label)

                type_label = QLabel(sig['type'].replace('_', ' ').upper())
                type_label.setStyleSheet(f'color: {ACCENT_AMBER}; font-size: 12px; letter-spacing: 1px; min-width: 160px;')
                frame_layout.addWidget(type_label)

                desc_label = QLabel(str(sig.get('desc', '')))
                desc_label.setStyleSheet(f'color: {TEXT_SECONDARY}; font-size: 12px;')
                desc_label.setWordWrap(True)
                frame_layout.addWidget(desc_label)

                self.signals_layout.addWidget(frame)

        self.signals_layout.addStretch()
        self.status_update.emit(f'AI Detection: {label_map.get(verdict, verdict)} (score={score})', color)


# ─────────────────────────────────────────────
# TAB: TEXT GENERATION
# ─────────────────────────────────────────────
class TextGenerationTab(QWidget):
    status_update = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(splitter)

        # Left: config
        left = QWidget()
        ll = QVBoxLayout(left)
        ll.setContentsMargins(16, 16, 8, 16)

        ll.addWidget(SectionHeader('Style Source Text'))

        info = QLabel('Provide a writing sample to extract style from. '
                      'The generator will imitate the vocabulary, sentence '
                      'length, and word patterns of this text.')
        info.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 12px; padding: 4px 0;')
        info.setWordWrap(True)
        ll.addWidget(info)

        self.source_text = QTextEdit()
        self.source_text.setPlaceholderText('Paste style source text here (200+ words recommended)...')
        ll.addWidget(self.source_text)

        ll.addWidget(SectionHeader('Generation Parameters'))

        # Prompt
        prompt_row = QHBoxLayout()
        prompt_row.addWidget(QLabel('Seed / Topic:'))
        self.prompt_input = QLineEdit()
        self.prompt_input.setPlaceholderText('Optional starting words...')
        prompt_row.addWidget(self.prompt_input)
        ll.addLayout(prompt_row)

        # Length
        len_row = QHBoxLayout()
        len_lbl = QLabel('Target Length:')
        len_lbl.setStyleSheet(f'color: {TEXT_SECONDARY}; font-size: 11px;')
        len_row.addWidget(len_lbl)
        self.length_slider = QSlider(Qt.Orientation.Horizontal)
        self.length_slider.setRange(50, 500)
        self.length_slider.setValue(150)
        self.length_val = QLabel('150 words')
        self.length_val.setStyleSheet(f'color: {ACCENT_CYAN}; font-size: 11px; min-width: 65px;')
        self.length_slider.valueChanged.connect(
            lambda v: self.length_val.setText(f'{v} words'))
        len_row.addWidget(self.length_slider)
        len_row.addWidget(self.length_val)
        ll.addLayout(len_row)

        # Num variations
        var_row = QHBoxLayout()
        var_lbl = QLabel('Variations:')
        var_lbl.setStyleSheet(f'color: {TEXT_SECONDARY}; font-size: 11px;')
        var_row.addWidget(var_lbl)
        self.variations_spin = QSpinBox()
        self.variations_spin.setRange(1, 5)
        self.variations_spin.setValue(1)
        var_row.addWidget(self.variations_spin)
        var_row.addStretch()
        ll.addLayout(var_row)

        generate_btn = QPushButton('GENERATE TEXT')
        generate_btn.setObjectName('accent')
        generate_btn.clicked.connect(self._generate)
        ll.addWidget(generate_btn)

        # Style preview
        ll.addWidget(SectionHeader('Source Style Profile'))
        self.style_info = QLabel('Load source text to see style profile.')
        self.style_info.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 12px; padding: 4px;')
        self.style_info.setWordWrap(True)
        ll.addWidget(self.style_info)

        analyze_source_btn = QPushButton('ANALYZE SOURCE STYLE')
        analyze_source_btn.clicked.connect(self._analyze_source)
        ll.addWidget(analyze_source_btn)

        ll.addStretch()
        splitter.addWidget(left)

        # Right: output
        right = QWidget()
        rl = QVBoxLayout(right)
        rl.setContentsMargins(8, 16, 16, 16)

        rl.addWidget(SectionHeader('Generated Text'))

        self.output_tabs = QTabWidget()

        for i in range(5):
            tab = QWidget()
            tab_layout = QVBoxLayout(tab)
            output_text = QTextEdit()
            output_text.setPlaceholderText(f'Variation {i+1} will appear here...')
            output_text.setReadOnly(False)
            tab_layout.addWidget(output_text)

            copy_btn = QPushButton('COPY TO CLIPBOARD')
            copy_btn.clicked.connect(lambda checked, t=output_text:
                                     QApplication.clipboard().setText(t.toPlainText()))
            tab_layout.addWidget(copy_btn)

            self.output_tabs.addTab(tab, f'VAR {i+1}')
            setattr(self, f'output_{i+1}', output_text)

        rl.addWidget(self.output_tabs)

        # Similarity check
        rl.addWidget(SectionHeader('Style Match Verification'))
        self.match_bar = SimilarityBar('Generated vs Source', 0)
        rl.addWidget(self.match_bar)

        splitter.addWidget(right)
        splitter.setSizes([380, 500])

    def _analyze_source(self):
        text = self.source_text.toPlainText().strip()
        if not text:
            return
        f = StyleFeatures.extract(text)
        self.style_info.setText(
            f'Words: {f.get("word_count",0)}  |  '
            f'TTR: {f.get("ttr",0):.3f}  |  '
            f'Avg sent: {f.get("avg_sent_len",0):.1f}\n'
            f'Avg word len: {f.get("avg_word_len",0):.2f}  |  '
            f'Yule\'s K: {f.get("yules_k",0):.2f}\n'
            f'Readability: {f.get("fk_score",0):.1f}  |  '
            f'Unique words: {f.get("unique_words",0)}'
        )
        self.status_update.emit('Source style analyzed', ACCENT_TEAL)

    def _generate(self):
        source = self.source_text.toPlainText().strip()
        if not source:
            QMessageBox.warning(self, 'Warning', 'Provide a source text first.')
            return

        prompt = self.prompt_input.text().strip()
        length = self.length_slider.value()
        num_vars = self.variations_spin.value()

        source_features = StyleFeatures.extract(source)

        for i in range(num_vars):
            generated = TextGenerator.generate(source, prompt, length)
            output = getattr(self, f'output_{i+1}')
            output.setPlainText(generated)

        # Show first variation tab
        self.output_tabs.setCurrentIndex(0)

        # Check similarity
        if num_vars >= 1:
            first_output = self.output_1.toPlainText()
            if first_output:
                gen_features = StyleFeatures.extract(first_output)
                sim = SimilarityEngine.compare(source_features, gen_features)
                self.match_bar.set_value(sim['overall'])

        self._analyze_source()
        self.status_update.emit(f'Generated {num_vars} text variation(s)', ACCENT_TEAL)


# ─────────────────────────────────────────────
# MAIN WINDOW
# ─────────────────────────────────────────────
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('文本取证  ·  Text Forensics Suite')
        self.setMinimumSize(1600, 900)
        self.resize(1440, 860)
        self._setup_ui()
        self._apply_style()

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ── HEADER ──
        header = QWidget()
        header.setFixedHeight(62)
        header.setStyleSheet(f"""
            background: {PANEL_BG};
            border-bottom: 1px solid {BORDER_COL};
        """)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 0, 20, 0)

        logo_label = QLabel('⬡  文本取证')
        logo_label.setStyleSheet(f"""
            color: {ACCENT_CYAN};
            font-size: 20px;
            font-weight: bold;
            letter-spacing: 2px;
            font-family: 'Courier New', monospace;
        """)
        header_layout.addWidget(logo_label)

        subtitle = QLabel('TEXT FORENSICS SUITE  //  Stylometry & Authorship Attribution')
        subtitle.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 14px; letter-spacing: 2px; margin-left: 16px;')
        header_layout.addWidget(subtitle)
        header_layout.addStretch()

        version_label = QLabel('v1.0.0  ·  2024')
        version_label.setStyleSheet(f'color: {TEXT_MUTED}; font-size: 14px; letter-spacing: 1px;')
        header_layout.addWidget(version_label)

        main_layout.addWidget(header)

        # ── TABS ──
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        main_layout.addWidget(self.tabs)

        # Create tabs
        self.authorship_tab = AuthorshipTab()
        self.same_author_tab = SameAuthorTab()
        self.tampering_tab = TamperingTab()
        self.ai_detection_tab = AIDetectionTab()
        self.generation_tab = TextGenerationTab()

        self.tabs.addTab(self.authorship_tab,   '01 · Authorship Attribution')
        self.tabs.addTab(self.same_author_tab,  '02 · Same Author Detection')
        self.tabs.addTab(self.tampering_tab,    '03 · Tampering Detection')
        self.tabs.addTab(self.ai_detection_tab, '04 · AI Detection')
        self.tabs.addTab(self.generation_tab,   '05 · Style Imitation')

        # ── STATUS BAR ──
        self.status_bar = StatusBar()
        main_layout.addWidget(self.status_bar)

        # Connect signals
        for tab in [self.authorship_tab, self.same_author_tab,
                    self.tampering_tab, self.ai_detection_tab,
                    self.generation_tab]:
            tab.status_update.connect(self.status_bar.set_status)

    def _apply_style(self):
        self.setStyleSheet(APP_STYLESHEET)


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Dark palette base
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(DARK_BG))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.ColorRole.Base, QColor(CARD_BG))
    palette.setColor(QPalette.ColorRole.Text, QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.ColorRole.Button, QColor(PANEL_BG))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(ACCENT_BLUE))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor('#ffffff'))
    app.setPalette(palette)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
