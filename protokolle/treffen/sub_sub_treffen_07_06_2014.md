Entscheidungen
----
Wir nehmen UMLet!  
Namen für bewertete Metadaten: RatedMetaData - RMD 

Zeitplan
----

###Allgemeines Vorgehen
- Architekturentwurf / Nachrichtendaten
- Netzwerkentwurf (Topic Kommunikation sichtbar machen, Datentypen erläutern)
- Klassendiagramm
- Sequenzdiagram

###bis 09.06.:  

* Paper lesen
* In Indigo neue Mechanismen analysieren, ob sie reichen, was man verwenden kann
* Publisher/Subscriber
	+ Klassen anschauen
	+ was ist involviert
	+ anschauen wie wir sie modifizieren können
* PyQT anschauen


###bis 12.06.:  

- **Verlinkte Papers auswerten: Was besteht schon, was wir brauchen**  
- Namen für bewertete Metadaten: RatedMetaData - RMD  
- Architekturentwurf (vgl. Entwurf.pdf 2.1)  
- Schon im Netzwerkdiagramm festhalten  
- nachrichtentypen definieren  
- Klassen identifizieren und mit Klassenkommentar beschreiben  
- Sequenzdiagramm  
- Farbkonvenstionen überlegen und **von Anfang an einhalten!**  




Überlegungen
----
* Trennung in MVC - Wo sind Grenzen sinnvoll?
* Farbliche Unterteilung ist sinnvoll
* Diagramm über verteilte Systeme (wo(auf welchem Host) läuft welche Kompontente, welche Verbindungen bestehen)
* Integration von [psutil][psutil] überlegen
  
* API Schnittstelle für den Monitoringknoten, Für den Abruf durch GUI etc.  
* Speicherung der Daten

###Architektur
Letztlich unterteilt in Erweiterung des Publishers, Monitoring-, Countermeasureknoten und GUI Teil.  

###Nachrichten
**Erweiterter Publisher -> Monitoringknoten & GUI & Datenhaltungsknoten** - topic *"metadata/raw"*  
[Absendezeit, ]Zeitpunkt des letzten pakets, Anzahl ausgegangener nachrichten, Umfang ausgegangener Nachrichten, Knoten UID[, CPU Last und Speicherauslastung durch den Knoten], Host IP oder MAC  
**Hostdaten -> GUI & Datenhaltungsknoten** - topic *"metadata/host"*  
IP Host, MAC Adresse, CPU, HDD, Temperatur, Memory Usage, Network  
**Monitoringknoten -> GUI & Countermeasureknoten** - topic *"metadata/rated"*  
!! Dringend zu klären! Knotenname + Bewertung in < Form hier einfügen>  
**GUI <-> Datenhaltungs- oder Monitoringknoten** ROS Service  

Farbkonventionen
----
* M:
* V:
* C:

Bzgl. Netzwerk/Metadaten: Übersicht über unsere Topics soweit
----
###/metadata/raw/ (rmd1)
alle host und node knoten
vollstöndige node infos

Identifizierung (z.B. IP)
Menge an Ausgehendem traffic
Anzahl ausgehender Nachrichten
optional: CPU-Last, Speicherauslastung vom Knoten

//bewertete Metadaten
###/metadata/rated/ (rmd2)
node
bewertete Metadaten

###/metadata/host/ (hmd)
ip
cpu
speicher
auslaustung festplatte
temperatur :)
Gesamte Netzwerkauslastung
Latenz

TODO: hier noch die Datentypen jeweils erweitern(in Form von structs/primitiven Datentypen, weitere Themen ergänzen, usw.)

Weitere Offene Punkte:
- Kennt der Host seine Nodes?
- Wie erkennnen wir Netzwerkprobleme?
- Wie erkennen wir die Latenz/Last?
- optional: größe der Netzwerkverbindung erkennen?
- immer noch unklar: Speicherung der Daten im Monitoring Knoten (rrd?)


[psutil]:https://github.com/giampaolo/psutil