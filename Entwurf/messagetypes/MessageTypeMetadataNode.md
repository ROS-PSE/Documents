MessageType: /metadata/node/
----

\#ip of the host this node belongs to
string host

\#identifier of this node
string id

\#CPU

float32 node_cpu_temp  
float32 node_cpu_temp_avg
float32 node_cpu_temp_stddev
float32 node_cpu_temp_max

float32 node_cpu_usage  
float32 node_cpu_usage_avg
float32 node_cpu_usage_stddev
float32 node_cpu_usage_max

float32[] node_cpu_usage_core
float32[] node_cpu_usage_core_avg
float32[] node_cpu_usage_core_stddev
float32[] node_cpu_usage_core_max

float32[] node_cpu_temp_core  
float32[] node_cpu_temp_core_avg
float32[] node_cpu_temp_core_stddev
float32[] node_cpu_temp_core_max

\#GPU 

float32[] node_gpu_temp
float32[] node_gpu_temp_avg
float32[] node_gpu_temp_stddev
float32[] node_gpu_temp_max

float32[] node_gpu_usage
float32[] node_gpu_usage_avg
float32[] node_gpu_usage_stddev
float32[] node_gpu_usage_max

\#Network

\# ram  
float32 node_ramusage  
float32 node_ramusage_avg
float32 node_ramusage_stddev
float32 node_ramusage_max
  
\# network load of the host  

int32 node_networkload 
int32 node_networkload_avg
int32 node_networkload_stddev
int32 node_networkload_max
 
int32 node_message_frequency
int32 node_message_frequency_avg
int32 node_message_frequency_stddev
int32 node_message_frequency_max

int32 node_bandwith
int32 node_bandwith_avg
int32 node_bandwith_stddev
int32 node_bandwith_max