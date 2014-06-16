MessageType: /metadata/rated/single
====
\# name of node/host  
string[] id  
\# the metatype that was out of bounds  
string[] metatype  

\# actual value  
string[] actual  

\# expected value  
string[] expected  

\# state of the metadata from the node/host : state ={ 0 = ok ; 1 = warning ; 2 =critical ; 3 = not available }
string[] type
uint8[] state

frage: ist es notwendig topics ohne ihre publisher zu überwachen  
