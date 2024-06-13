import translation_agent as ta
source_lang, target_lang, country = "English", "Simplified Chinese", "China"
source_text= "It's easy to look sharp when you haven't done anything."
print(f"Source text:\n\n{source_text}\n------------\n")
translation = ta.translate(source_lang, target_lang, source_text, country)
print(f"Translation:\n\n{translation}")