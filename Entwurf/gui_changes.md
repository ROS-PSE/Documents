GUI Änderungen

- Item/LogFilterProxy kein Singleton mehr
- + item: selected_item in Selection Widget
- - - host_proxy: rospy.ServiceProxy
- + set_log_item(list<string>) --> adds the given list as a log entry to the model
- eventfilter weg in overview und selection! --> dafür: bool:draw_graphs und on_current_tab_changes(tab:int)
- widgetklassen viele veränderungen!!!


Offene Fragen:
- wie füttere ich den HostLookup
