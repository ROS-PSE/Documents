##Treffen 17.06.14



- topic als unterkategorie von node, innerhalb topic: connections, sollte in statistics implementiert sein
- (sender, topic, empfänger) tupel
- node-sicht: empfänger: aggregieren, was gehört wo dazu
- topic-sicht: topic, empfänger: n-1
- connections-sicht: tupel: 1-1
- evt. Topic connections als seperate ansicht.
- Topic nur bei subscriber anzeigen
- über anzahl ankommender pakete bei subscriber lässt sich anzahl pakete der publisher bestimmen
- eher: übersichts-widget immer da, 1 auswahl-widget, dass sich updatet, anstatt neue zu öffnen.
- eher: nur eine instanz pro widget
- listen-widget: show topics, show connections hinzufügen
- constraints paralleliesieren mit python threads
- paralleliesieren: beim empfang oder beim verarbeiten der Daten.
- Parallelität: immer thread-bib, nicht multiprozess.
- plotten auch trivial parallel.
- reaktor: statt constraintlevel : countermeasurelevel oder ähnliches.
- eher yaml statt xml. was soll drinnstehen ?

* statt 
  * lock() 
  *	buffer [..] 
  *	unlock() ,
		
* besser: timer() 
  *	lock() 
  *	my.buffer=copy(buffer) 
  *	unlock() 
  *	GUIzeugs.
			
- nächstes Treffen: Do 26.06,  geplante abgabe