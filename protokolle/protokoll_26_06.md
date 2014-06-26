##Protokoll 6/26/2014 
+ Bildunterschriften sollten in ganzen Sätzen geschrieben werden.
+ Aufzählungen sollten mit Großbuchstaben anfangen und  mit einem Punkt enden
+ Monitoring-Node callback des Subscribers noch einfügen (ohne Rückagbewert und als Parameters statistics)
+ ReactionHandler hat bei reaction einen **";"** statt **":"**
+ psutil.disk_io_counters(boolean perdisk) keine neue Zeile
+ Beziehung zwischen HostStatisticsHandler und ReactionHandler **1:1**, festellen was ist Netzwerkkommunikation und was ist nur auf einem Host
+ Constraint: true_since vll rospy.Time oder rospy.Duration statt int, [Link](wiki.ros.org/rospy/Overview/Time)
+ ReactionDefaultType streichen und mit Klassen handeln
+ gedanken über eine Top-Level-Klasse machen, wo genau ist der Einstiegspunkt in die Klassen
+ GUI-View Klassendiagramm updaten
+ GUI-Modell Pfeile hinzufügen
+ Host-ID: ROS_IP
+ Überprüfen ob Host-Statistics *Network* konsistent ist (genauso wie Bandreite machen)
+ (Enum im MessageType direkt angeben: Ratedstatistics *state*)  
+ RatedStatisticsEntity state einfügen, Name eindimensional
+ NodeRaction *command-line arguments* auf eindimensional umändern
+ aufpassen das Zeit nicht liniear ist, Daten die früher ankommen sind nicht automatisch früher gesendet worden
+ **\\** sollten geändert werden, führt nur zu unnötigen Komplikationen bei Linux
+ GUI_seq auf raceconditions achten


**Note: 1  =)**
===


TODO: [ROS-Tutorials](wiki.ros.org/ROS/Tutorials), die Python-Tutorials mal anschauen
