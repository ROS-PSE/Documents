struktur
----
```
package/
+- src/
   +- package/
      +- __init__.py
      +- ...
+- test/
+- CMakeLists.txt
+- setup.py
+- package.xml
```

### package.xml
dependencies:  
&lt;build_depend&gt; arni_core  
&lt;run_depend&gt; arni_core  
(am besten "erstmal" immer beides hinzufügen)  
  
### CMakeLists
catkin_python_setup() aktivieren
  
### setup.py
muss erstellt werden, kann aber vom bsp kopiert werden, packagename anpassen, sonst nichts

im devel ordner (~/catkin_ws/devel/lib/python2.7/dist-packages/*package*) nicht alle dateien, verweis auf aktuelle dateien, damit man nicht immer neu maken muss  
  
neues paket:  
einmal catkin_make, danach nicht unbedingt nötig  
  
catkin_make -> devel/setup.(zsh|bash) wird ausgeführt, erweitert dann pythonpfad auf ros pakete  
  
"paket nicht gefunden" -> source ~/.zshrc (konsole neu initialisieren, pfade neu laden etc.)  

  
### auf indigo release updaten:
```
> sudo apt-get update
> sudo apt-get upgrade
> sudo apt-get dist-upgrade
```

statt `> python *datei*` `> rosrun *paket* *datei*` benutzen (geht auch in anderem dateipfad)  
  
(http://answers.ros.org) oder github issues ruhig benutzen (ggf dann benutze repos auch in der präsentation angeben)  
  
auch einen eintrag ins ros wiki, wo dann doku verlinkt ist  
  
###tests:
keine feste konvention, neben "src/" ordner "test/"
zum testen einiger komponenten besser ein eigenes paket mit ausführbarem python script, dass dann mit `rostest` ausgeführt werden kann.
  
configs auch für topics: würde dann für alle connections jeweils gelten  
  
Änderungen am Entwurf:
----
entwurfsbezogene änderungen nicht rückwärts korrigieren, aber in einer datei ablegen, am ende ggf. aufbereiten und nochmal durchsprechen. Als Dokument für die Implementierung dann in minimaler Form vielleicht eine Gegenüberstellung vom Entwurf mit diesen Erweiterungen in Kopie des Entwurfsdokumentes. (Mäßig wichtig)