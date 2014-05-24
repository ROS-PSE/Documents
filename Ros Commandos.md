##Notizen zu den Ros-Kommandos:

- `rqt` --> zum starten der gui
- `killall ‚gzserver‘` --> um gazebo ganz zu beenden
- ``rostopic` --> printing infos about the different topics avaiable
- `roscore` --> startet die Kernkomponente von ros
- `roslaunch ipr_models labor_lwr1.launch` --> zum starten der laborumgebung vom ipr
- `rosrun rqt_gui` --> starten von rqt (GUI) (alternativ: [äquivalent?] rqt
- `rostopic list` --> listet die topics
- `rostopic info /robots/lwr1/state` --> gibt Infos zum Nachrichtentyp des topics
- `rostopic info /robots/lwr1/set_joint`
- `rostopic echo /robots/lwr1/get_joint` --> gib *alle* Nachrichten auf diesem Kanal in der Konsole aus
- `rostopic echo -n 1 /robots/lwr1/get_joint` --> gibt die letzte gesendete Nachricht auf dem Kanal aus
- `rostopic pub /robots/lwr1/direct/set_joint` „message“ --> wenn der richtige nachrichtentyp mit der richtige message (muss die spezifizierten inhalte enthalten) gesendet wird, geht das als normale nachricht über den kanal (z.b. zur manuellen steuerung für knoten)
- `rosparam get /manta/image_raw/compressed/jpeg_quality` --> abrufen von bestimmten gesetzen parameter über rosparam  können auch gesetzt werden mit:
- `rosparam set /manta/image_raw/compressed/jpeg_quality` 90 --> setze einen wert, hier auf 90

