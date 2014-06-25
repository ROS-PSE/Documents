Sequenzdiagramm...
Namen frei gewählt, bitte noch verbessern. Orientier dich am Sequenzdiagramm vom andren Matthias

OverviewWidgetPlugin ow
--> init
--> ROSMOdel.get_instance()
    model.__init__()
        initialisiert komponenten (hier nur wichtige aufgeschrieben, bitte auhc andere erzeugen)
        (Notiz: root_item wie erzeugen?[vermutlich HostItem dafür nehmen])
        lg = LogFilterProxy()
        lg.setSourceModel(model)
        lg.setDynamicSortFilter(true)
        log_tab_tree_view.setModel(lg)
        log_tab_tree_view.setSortingEnabled(true)
---> startet: Bufferthread(model)
        init(model)
            erzeuge alle Elemente
            zuerst die locks
            dann die subscriber zu den topics via
            rospy.Subscriber('name_des_topics', msg.Statistics, self.add_buffer_item)
--->bufferthread.run()
    [nicht sequentieller Ablauf hier!!!]{
    bufferthread.start()
        proxy = rospy.ServiceProxy('StatisticHistory', storage_server) d.h. Daten vom Service holen 

        proxy(rospy.Time.now()-rospy.Duration(5*60)) // letzte 5 minuten
        Daten umwandeln
        update_model(data, rated_data)
        -->model
            Schleife: transform_data(..)
            ggf new HostItem/TopicItem... (parent)
            und dann auch HostItem.append_child(andres_item)
            sonst item.append_data(data)
        }
--->connect_slots()
    nicht vollständig.. --> nur relevanter slot
    self.model.layoutChanged.connect(self.update)

Signal/Slot
model.layoutChanged() -> ow.update()
    ow setzt Text von QPushButton usw. neu -> siehe OnlineBeschreibung, nehme mal, meistens wird setText() o.Ä. gerufen
    Neue Werte berechnen

    Aktuellen Status berechnen
    z.B. QLabel.setText(current_state)
    QLineEdit.setText(current_state_description)
    ...
