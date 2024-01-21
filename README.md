# Englisch
## **[PandocPrjFilter](https://github.com/PxaMMaxP/PandocPrjFilter)**

The **PandocPrjFilter** can be integrated into Pandoc and removes all code blocks with the `prj` tag.

This means that corresponding code blocks can also be used in documents that are to be converted later with Pandoc.

The `prj` code blocks belong to the **[obsidian-prj](https://github.com/PxaMMaxP/obsidian-prj)** plugin from my hand.

### Installation & usage

- The Python file (`PandocPrjFilter.py`) must be copied to the path `C:\Users\[USERNAME]\AppData\Roaming\pandoc\filters`.
- Pandoc must then be called with the command line option `--filter=PandocPrjFilter.py`.

---
---

# Deutsch
## **[PandocPrjFilter](https://github.com/PxaMMaxP/PandocPrjFilter)**

Der **PandocPrjFilter** kann in Pandoc eingebunden werden und entfernt alle Codeblöcke mit dem `prj`-Tag.

Dadurch können entsprechende Codeblöcke auch in Dokumenten verwendet werden, welche später mit Pandoc konvertiert werden sollen.

Die `prj`-Codeblöcke gehören zum **[obsidian-prj](https://github.com/PxaMMaxP/obsidian-prj)**-Plugin aus meiner Hand.

### Installation & Verwendung

- Die Python Datei (`PandocPrjFilter.py`) muss in den Pfad `C:\Users\[USERNAME]\AppData\Roaming\pandoc\filters` kopiert werden.
- Dann muss Pandoc folgend mit der Kommandozeilenoption `--filter=PandocPrjFilter.py` aufgerufen werden.