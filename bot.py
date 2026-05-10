import re
import os

BRAIN_FILE = "chat_memory.txt"

def save_to_memory(text):
    clean_text = text.replace("\n", " ").strip()
    
    russian_laughter = r'^([ахахехыя])+\s*$'
    text_lower = clean_text.lower()
    
    is_laughter = re.search(russian_laughter, text_lower) or \
                  re.search(r'^(h[ae])+h?\s*$', text_lower) or \
                  re.search(r'([а-яa-z])\1{3,}', text_lower)
    
    blacklist = ["lol", "lmao", "xd", "лол", "кек", "ору"]
    
    if text_lower in blacklist or is_laughter:
        return "skipped"  # ← важное изменение, объясню ниже
        
    if clean_text:
        with open(BRAIN_FILE, "a", encoding="utf-8") as f:
            f.write(clean_text + "\n")
        return "saved"  # ← и это тоже