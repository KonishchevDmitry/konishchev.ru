.PHONY: all clean

LANG := ru
POT_PATH := messages.pot
BABEL_CONFIG_PATH := babel.cfg
TRANSLATIONS_PATH := translations
PO_PATH := $(TRANSLATIONS_PATH)/$(LANG)/LC_MESSAGES/messages.po
MO_PATH := $(TRANSLATIONS_PATH)/$(LANG)/LC_MESSAGES/messages.mo
TRANSLATION_SOURCES := $(shell find . -name '*.py' && find templates -name '*.html')

STATIC_PATH := static
LESS := $(wildcard $(STATIC_PATH)/css/*.less)
CSS := $(LESS:%.less=%.css)


build: $(CSS) $(MO_PATH)

clean:
	rm -f $(POT_PATH) $(PO_PATH).orig $(CSS) $(MO_PATH)

%.css: %.less
	lessc --strict-units=on --strict-math=on -O2 $< $@

$(MO_PATH): $(PO_PATH)
	pybabel compile -d $(TRANSLATIONS_PATH) -l $(LANG)

$(PO_PATH): $(POT_PATH)
	[ -f $(PO_PATH) ] || { mkdir -p $(TRANSLATIONS_PATH) && pybabel init -i $(POT_PATH) -d $(TRANSLATIONS_DIR) -l $(LANG); }
	pybabel update -i $(POT_PATH) -d $(TRANSLATIONS_PATH) --ignore-obsolete --previous
	sed -i.orig '/^#: /d; /^"POT-Creation-Date: /d' $(PO_PATH) && rm -f $(PO_PATH).orig

$(POT_PATH): Makefile $(TRANSLATION_SOURCES)
	pybabel extract -F $(BABEL_CONFIG_PATH) -o $(POT_PATH) .
