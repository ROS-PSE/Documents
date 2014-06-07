Entscheidungen
----
Wir nehmen UMLet!  
Namen für bewertete Metadaten: RatedMetaData - RMD 

Zeitplan
----
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

- Kennt der Host seine Nodes?

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


[psutil]:https://github.com/giampaolo/psutil