MessageType: /metadata/host/
====
\# ip of the host  
string host

\# cpu  
float32 cpu_temp  
float32 cpu_temp_avg
float32 cpu_temp_stddev
float32 cpu_temp_max

float32 cpu_usage  
float32 cpu_usage_avg
float32 cpu_usage_stddev
float32 cpu_usage_max

float32[] cpu_usage_core
float32[] cpu_usage_core_avg
float32[] cpu_usage_core_stddev
float32[] cpu_usage_core_max

float32[] cpu_temp_core  
float32[] cpu_temp_core_avg
float32[] cpu_temp_core_stddev
float32[] cpu_temp_core_max


\# gpu
float32[] gpu_temp
float32[] gpu_temp_avg
float32[] gpu_temp_stddev
float32[] gpu_temp_max

float32[] gpu_usage
float32[] gpu_usage_avg
float32[] gpu_usage_stddev
float32[] gpu_usage_max
 

\# ram  
float32 ram_usage  
float32 ram_usage_avg
float32 ram_usage_stddev
float32 ram_usage_max
  
\# network load of the host  

int32 network_load 
int32 network_load_avg
int32 network_load_stddev
int32 network_load_max
 
int32 message_frequency
int32 message_frequency_avg
int32 message_frequency_stddev
int32 message_frequency_max

int32 bandwith
int32 bandwith_avg
int32 bandwith_stddev
int32 bandwith_max

time uptime

\# drive  
string[] drive_name  
int32[] drive_free_space  
  
\# input output operations on a specific drive in the last x seconds  
int32[] drive_read  
int32[] drive_write  
