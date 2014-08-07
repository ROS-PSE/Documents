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
(am besten "erstmal" immer beides hinzuf�gen)  
  
### CMakeLists
catkin_python_setup() aktivieren
  
### setup.py
muss erstellt werden, kann aber vom bsp kopiert werden, packagename anpassen, sonst nichts

im devel ordner (~/catkin_ws/devel/lib/python2.7/dist-packages/*package*) nicht alle dateien, verweis auf aktuelle dateien, damit man nicht immer neu maken muss  
  
neues paket:  
einmal catkin_make, danach nicht unbedingt n�tig  
  
catkin_make -> devel/setup.(zsh|bash) wird ausgef�hrt, erweitert dann pythonpfad auf ros pakete  
  
"paket nicht gefunden" -> source ~/.zshrc (konsole neu initialisieren, pfade neu laden etc.)  

  
### auf indigo release updaten:
```
> sudo apt-get update
> sudo apt-get upgrade
> sudo apt-get dist-upgrade
```

statt `> python *datei*` `> rosrun *paket* *datei*` benutzen (geht auch in anderem dateipfad)  
  
(http://answers.ros.org) oder github issues ruhig benutzen (ggf dann benutze repos auch in der pr�sentation angeben)  
  
auch einen eintrag ins ros wiki, wo dann doku verlinkt ist  
  
###tests:
keine feste konvention, neben "src/" ordner "test/"
zum testen einiger komponenten besser ein eigenes paket mit ausf�hrbarem python script, dass dann mit `rostest` ausgef�hrt werden kann.
  
configs auch f�r topics: w�rde dann f�r alle connections jeweils gelten  
  
�nderungen am Entwurf:
----
entwurfsbezogene �nderungen nicht r�ckw�rts korrigieren, aber in einer datei ablegen, am ende ggf. aufbereiten und nochmal durchsprechen. Als Dokument f�r die Implementierung dann in minimaler Form vielleicht eine Gegen�berstellung vom Entwurf mit diesen Erweiterungen in Kopie des Entwurfsdokumentes. (M��ig wichtig)