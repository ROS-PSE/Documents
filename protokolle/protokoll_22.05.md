protokoll treffen 22.05.14


- monitoring knoten publiziert, bewerted und verarbeitet diese (metadaten, abgeglichenen)

- gui: auf den ersten blick wo fehler sind
 pugin auch ros knoten 

- alle knoten publizieren auf /metadaten, übergeben eigenen namen

- von fehler durch einzelschritte (planer) auf lösung zu kommen ist zuviel (aber vllt api für zukünftige?)
- funktion möglich machen automatische aktionen auf bestimmte fehler, dies aber nur als möglichkeit für zukunft (für aufbauenden arbeiten)
- keine popups, da störend -- visuell anzeigen reicht, evtl. hilfestellungen anbieten (z.b. knoten überlastet da host ausgelastet) 
- gui: übersichtlich sehen ob alles ok, und gleichzeitig möglichkeit haben auf einzelne dinge einzugehen
- gui: ohne zuviel fenster aufzumachen alle möglichkeiten zu haben

heartbeat 
- sinvoll
- möglicherweise über metadaten topic (immer metadaten senden, auch wenn "leer"), oder anderes topic für heartbeat

- metadaten mit frequenz unabhängig von traffic (eigener subscriber: extra thread für versendung der metadaten)

- spezialfall nur services: explizit watchdogähnliches einfügen
- für publisher: vllt nur heartbeat

hardwarebeschränkung
- gut nicht auf raspberry
- monitoring nicht performancekritisch, 
- metadatenerfassung sollte resourcensparend sein. (können auf kleinen plattformen liegen), sollte aber eh nicht rechenintensiv sein.

- allgemein 10hz als sendeleistung gute idee
- einfache datentypen nutzen(?)

useabillity
- intuitiv
- ziel sind nicht endanwender sondern entwickler / technisch erfahrene, trotzdem ansprechende intuitive gui
- muss nicht applike sein, ist immer noch technische anwendung
- 100 knoten sollten aber immer noch sinvolle übersicht und details bieten
- nicht schlechter als rqt_gui sein.
- nicht: anzahl klicks usw..

host überwachung (host measurement node)
- psutils für platformunabhängigkeit
- daten über den host selbst sind interessant (cpu,cpu-temp,ram,speicher...)
- zusatz: pro knoten wieviel leistung er verbraucht (knoten <--> prozess könnte unklar sein)
- wenn einfach rauszufinden welche prozesse rosprozesse mit psutils auslesen. interessant zu sehen wieviel auslastung welche knoten selbst verursaucht
- vgl: rqt_gui introspection-> process monitor

- muss feature: pro host auswertung
- optional aber sehr gewünscht: pro knoten welcher verbrauch
  mögliche realisierung: 

- host measurement node: nur für host selbst zuständig
- in den subscriber/watchdog überwachung: für den eigenen knoten herausfinden wieviel cpu, ram, threads der aktuelle knoten besitzt. (bei psutils rausfinden was alles sinvoll ist)
- darauf achten das nur einmal pro knoten prozess infos versenden und nicht pro subscriber

soll spezifikation
- yaml statt xml (besser von hand editbar, platzsparener)
- möglichkeit nur bestimmte teilgraphen zu überwachen (fall nur bei start auswählen welcher teilgraph: parameter genug, oder zur laufzeit hinzufügbar entfernbar)
- beim start reicht wohl soll spezifikation zu übergeben
- entweder mehrere überwachungsknoten für jeden teilgraphen, oder einer für alle
- yaml datei definieren um pro topic, pro host, pro knoten parameter definieren zu können
- immer möglichkeit bereich anzugeben (z.b. von 40 - 70%)
- yaml datei auf parameter server als string, dann mit überwachungsknoten auslesen
- beim entwurf nachdenken: wie parameter zu code verwandeln (pipe, verteilung...) z.b. regeln pro topic sammeln
- yaml dateien pro use case / logische einheit, überlappungen sollen möglich sein (z.b. lower-upper bounds logisch zusammenfügen von verschiedenen use cases für einen bestimmten knoten)
- yaml dateien auf anwenderrechner, werden von monitoring knoten auf parameter server geschrieben werden
- default werde bei config sollen möglich sein, z.b. nur upper bound angeben soll reichen (-> automatisch lower auf 0), damit nicht alles angegeben werden muss


- counter measure knoten: sinvolle ausgaben von fehlern, entscheiden ob wichtig z.b. genaue gradanzahl anzugeben oder nur  cpu zu heiss

- gui: möglichkeit live metadaten plot mit definiertem bereich usw (im rahmen)

--> pflichtenheft nächste woche vorstellen, andreas kommentiert, dann abgabe woche darauf, dabei aber schon parallel mit entwurf anfangen

