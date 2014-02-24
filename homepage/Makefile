.PHONY: all clean

LANG = ru
POT_PATH = messages.pot
BABEL_CONFIG_PATH = babel.cfg
TRANSLATIONS_DIR = translations
PO_PATH = $(TRANSLATIONS_DIR)/$(LANG)/LC_MESSAGES/messages.po
MO_PATH = $(TRANSLATIONS_DIR)/$(LANG)/LC_MESSAGES/messages.mo
TRANSLATION_SOURCES = $(shell find . -name '*.py' && find templates -name '*.html')

build: $(MO_PATH)

clean:
	rm -f $(POT_PATH) $(MO_PATH)

$(MO_PATH): $(PO_PATH)
	pybabel compile -d $(TRANSLATIONS_DIR) -l $(LANG)

$(PO_PATH): $(POT_PATH)
	[ -f $(PO_PATH) ] || { mkdir -p $(TRANSLATIONS_DIR) && pybabel init -i $(POT_PATH) -d $(TRANSLATIONS_DIR) -l $(LANG); }
	pybabel update -i $(POT_PATH) -d $(TRANSLATIONS_DIR) --ignore-obsolete --previous
	sed -i '' '/^#: /d; /^"POT-Creation-Date: /d' $(PO_PATH)

$(POT_PATH): Makefile $(TRANSLATION_SOURCES)
	pybabel extract -F $(BABEL_CONFIG_PATH) -o $(POT_PATH) .
