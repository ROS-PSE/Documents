##Kleine Information zum Treffen während der Datenbankübung

- Modellierung der Gui im Model/View Konzept mit Hilfe von Qt Models --> dieses Model wird als Singleton für die unterschiedlichen Widgets zur Verfügung gestellt. Das kein Schreibzugriff bzw. stattfindet, sollte dies kein Problem darstellen.
- Monitoring wird erweitert um die Funktionalität zur Datenspeicherung --> hier fehlt noch eine geeignete Api bzw. wir müssen einen Weg finden hier sinnvoll bidirektional zu kommunizieren (ev. ist das geeignet: [http://wiki.ros.org/actionlib](http://wiki.ros.org/actionlib))
- Das Problem der Erkennung der gestarteten Threads/Prozesse von/durch einen oder mehrere Knoten ist noch nicht geklärt, kann aber vermutlich/hoffentlich mit psutils gelöst werden
- Offene Frage: Kann der roscore jetzt bereits Knoten stoppen o.Ä.? Eher nein.
- Wenn ein Knoten stoppt, stoppt dann auch unser Überwachungsthread? Falls ja, wird in jedem Fall ein Host Prozess benötigt um die falsche Funktionsweise festzustellen (zumindest zum Starten und so).