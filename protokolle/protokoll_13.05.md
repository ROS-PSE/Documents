Zeitlicher Ablauf
----
Pflichtenheft **Mittwoch, 28.5. 14:00** (Ersatztermin für 29.5.)  
  
Notizen zum Pflichtenheft
----
Inhalte der Metadaten schon als bestandteil des Pflichtenheftes   
-> überlegen, was jeweils möglich ist  
Bandbreite etc. z.B. mitschicken  
  
**GUI Überlegungen (auch schon fürs Pflichtenheft!)**  
vgl. Nagios
  
  
"Technische" Hinweise/Fragestellungen
----
Nachrichten werden an "topic" publiziert, werden am anderen Ende abonniert (n:n)  
Nachrichten sind eigene Datentypen  
  
Zusätzliches *topic* (-> neue Kanten zwischen Knoten) -> vgl. gestrichtelte Linien in Abb. 2 im Lastenheft.  
  
Ziel: Ursprüngliche ROS-Knoten nicht verändern, Mechanismus letztlich in Publisher einbauen  
  
  
Eingehende oder ausgehende Metadaten publishen?  
=> Reicht es, eingehende Kanten zu überwachen?  
  
  
Eingehende überwachen: ROS-core kontaktieren, Daten vervollständigen  
Vorteil: weniger Aufwand im Sendemechanismus  
  
  
Ausgehende überwachen: z.B. Tests möglich, an wie viele Knoten Daten geschickt werden  
(-> beachten, Tests als Bestandteil des Pflichtenheftes)  
  
  
Erweiterung des Systems durch Einfügen oder Vererbung überlegen (allerdings erst im Entwurf relevant) (Kindklassen für Subscriber und Publisher -> Konstruktoren abändern)
