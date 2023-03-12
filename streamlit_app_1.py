#STREAMLIT APP 1 !!!!!!!!!!!!!!!!
'''
Usage:
------
Open a socker on port 9999 using netcat

$ nc localhost 9999

Submit the python script

Open a socker on port 9999 using netcat

$ spark-submit firstStreamApp.py localhost 9999

'''
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Begin
if __name__ == "__main__":
        sc = SparkContext(appName="StreamingErrorCount");
        # 2 is the batch interval : 2 seconds
        ssc = StreamingContext(sc, 2)

        # Checkpoint for backups
        ssc.checkpoint("")

        # Define the socket where the system will listen
        # Lines is not a rdd but a sequence of rdd, not static, constantly changing
        lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))


        # Counting errors
        counts = lines.flatMap(lambda line: line.split(" "))\
                    .filter(lambda word:"ERROR" in word)\
                    .map(lambda word : (word, 1))\
                    .reduceByKey(lambda a, b : a + b)
        counts.pprint()
        ssc.start()
        ssc.awaitTermination()
