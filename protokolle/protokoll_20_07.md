Nächste Woche nicht,  
Per E-Mail ab 2ter Hälfte nächster Woche erreichbar.  

## Zeitplan aufstellen! (s.u.)  
* Juli Klausurenzeit  
* August\Urlaub präferiert  
* September wenig optional  

* Qualitätssicherungsphase: Testszenarien entwerfen und durcharbeiten,
* Normale **Testfälle schon im Laufe der Implementierung einbringen**

**Indigo Abwärtskompatibel?**  
Ggf. Konflikte von Plugins mit der rqt GUI  
  
**Repository Struktur**
Ober-Repository als Top-Level Meta-Paket, einzelne Teile (+ core, s.u.) untergeordnet =: *arni*  
  
Top-Level ist Ordner, wo die einzelnen Pakete drin sind, 1 Ordner tief.  
  
Beide rqt Plugins als ein Paket, damit von beiden auf eine Bibliothek zugegriffen werden kann.
Einen core benutzen, der für verschiedene Komponenten Methoden bereitstellt, u.A. z.B. HostLookup.  
  
Pakete mit Präfix benennen, bspw. halt eben `arni_`  

Readme in *arni*, Readme in Unterordnern vermutlich sinnvoll bie mehreren Komponenten.  
  
Tests als Bestandteil von catkin => Es ist sinnvoll, diese in entsprechender Struktur zu integrieren.  
doc direkt in *arni*?  
Highlevel Dokuemntation (Sphinx Erzeugnis) in eigenem Repo sinnvoll, bspw. `arni_doc`.  
  
Optional z.B. mit jekyll eine Projektseite machen (eigenes Repo -> xy.github.io Seite).  
  
**Code-Stil**  

* main Funktion nicht zu sehr füllen

**Tests**  
Python Unit tests  
catkin unit test command inc  
Ordner `test`, Dateien `test/<testscenario>_test.py` etc.


### Zeitplan ###
* Implementierung bis vorletzte Augustwoche
* Qualitätssicherung bis Do 4.9. **KEIN   T O D E S L I M I T**, Abnahme durch ihn bis 2. Septemberwoche.

* Präsentation nicht vor Mitte September, Woche nach Mitte September