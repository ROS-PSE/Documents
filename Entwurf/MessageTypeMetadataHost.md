MessageType: /metadata/host/
====
\# ip of the host  
string host

\# cpu  
float32 cpu_temp  
float32 cpu_usage  
float32[] cpu_usage_core  

\# ram  
float32 ram_usage  
  
\# network load of the host  
int32 network_load  
  
\# drive  
string[] drive_name  
int32[] drive_free_space  
  
\# input output operations on a specific drive in the last x seconds  
int32[] drive_read  
int32[] drive_write  
