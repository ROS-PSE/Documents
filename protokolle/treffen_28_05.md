##Treffen 28.05 Protokoll

[TOC]

###Vorstellung des Pflichtenhefts

_Angesprochene Problempunkte:_

- Korrektur der Rechschreibfehler
    - /FA1300/  Parametri`e`sierung
    - /FA1700/  Gege` `maßnahmen 
- /FA1600/ klarstellen, was es für Ergänzung darstellt (ein Monitoring knoten kann mehrere Soll-Spezifikationen "erfüllen")
- /FA1800/ Aufteilung in Pflicht/Soll. Vererbung ist Pflicht, Funktionsaufrufe optional
- /FA2500/ überflüssig
- /NF0800/ ROS großschreiben
- Fehler in GUI Graphiken/Logik beheben
- Bei Tests ergänzen: 
    - Was ist automatisiert testbar? 
    - GUI nicht
    - Netzwerk auch nicht
    - Softwareteile die Daten bekommen und verarbeite ermöglichen relativ gute (automatisierte) Tests, z.B. in dem man der Funktion korrekte/falsche Werte gibt und schaut, ob sie sich korrekt verhält
    - Tests noch ergänzen um weitere sinnvolle Sachen!
- Countermeasure Knoten in den Szenarien noch einbinden
    - Einfaches Szenario: Sollwert Unterschritten --> Countermeasure Knoten gibt Namen des Knoten in Shell aus



####Überlegungen für den Entwurf:
- Obere/Untere Schranken im Entwurf überlegen: Sind nur zahlen notwendig oder auch andere werte? (zur Messung in den Sollspezifikationen)
- Vererbung oder Komposition?
- Python API stellt kein Problem für Vererbung dar
- C++ API falls member private sind, gibts ev. Probleme 
- Pflicht: Vererbung --> ist zumindest für Python bessere Lösung. optional: Utility Klasse für Binärcode o.Ä.
- Wie löst man das Problem des unnötigen Versenden bzw. der Tatsache, dass die Gui nichts auswerten sondern nur anzeigen soll? (z.B. Timer-Thread, der die Gui regelmäßig aktualisiert)
- Nicht einen Nachrichtentyp für jede Abweichung. Die Frage bleibt, wie man die daten zum auswerte übertragen (einen metadatentyp für host/knoten)

__Offenes Problem: Wieviel darf der Monitoring Knoten können?__

- Monitoring gibt zusätzlich zu den Rohdaten noch seine Bewertung an die Gui mit
- Es gibt nicht immer ein Soll-defintion, es kann aber trotzdem gut sein, sich das in der GUI anzuzeigen --> GUI abboniert Rohdaten und die Bewertungen vom Monitoring Knoten ( nur dann anzeigen lassen, wenn auch Monitoring Knoten eingeschaltet ist )
- Monitoring müsste sich zumindest für ein kleines Zeitfenster um eine Datenspeicherung kümmern
- Gui berechnet live-plot nicht über den Monitoring-Ausgang sondern die Gui abboniert auch direkt die Metadaten
- Ampel ausgrauen, falls kein Monitoring Knoten eingeschaltet
- Countermesasure reicht bewertetes Metadaten-Packet
- Monitoring Knoten soll nur so für knapp 5 minuten daten speichern (alles was länger dauert wird mit rosback ermöglicht)
- Monitoring Knoten schreibt optional die Metadaten mit und die Gui ruft sich diese dann ab
- Zu beachten auf jeden Fall: Gui nicht jedes mal aktualisieren (Gui bekommt Metadaten aller Knoten!!! Freqzenz: Frequen pro Knoten (10Hz?) * Knoten!) sondern erst in gewissen abständen --> Sinnvollen timer setzen und nach Ablauf einer Zeiteinheit neu zeichnen
- roslaunch machine tag --> vorhandene funktionalität zum starten/killen ist bereits vorhanden in ROS, Frage wie einfach das zu machen ist. Restart muss man aufpassen, woher man die parameter bekommt, um das Packet beim Starten wieder in seinen alten Zustand zu bekommen


####Gegenstand des Entwurfs
- Übersichts UML Diagramm und Detail UML Diagramm die alle Klassen abbilden zusammen mit Membern und Methoden 
- Sequenz und Zustandsdiagramme, wo sinnvoll  (Sequenz: es reicht Eines, wo alle Bereiche einmal involviert werden) [Klassendiagramme verpflichten]
Klassen zusammen mit Methoden und wichtigen Members. Klassendiagram zusammen mit Beschreibung, was tut die Methode usw soll direkt das Programmieren ermöglichen.
- Nachrichtentypen definieren (Allgemein wenn Netzwerkübertragung Teil ist sollen die Protokollen bzw. übertragbare Datentypen definieren)
- Kommunikationsbeziehungen festlegen
- Automatische Generierung aus Klassen oder selber entwerfen?
    - Software für (manuelles) UML: Umbrello oder Eclipse Plugins oder Microsoft Visio (oder draw.io?)
    - Automatische Generierung: Software, die aus den Klassen die UML Struktur generiert --> doxygen für c++ (Aufgaben: Wie gut ist die Integration mit Python? Was kann doxygen alles?)

Allgemein:

- gute objektorientierte Programmierung anwenden
- ev paralell programmieren und zugleich UML schreiben
- textuelle Beschreibung der Klassen(ev mehr als ein satz), Methoden(ein satz)



####Fristen und Termine

__Nächstes Treffen: *Mittwoch 4. Juni um 14:00*__

__Entwurf abschließen bis: `Ende Juni`__