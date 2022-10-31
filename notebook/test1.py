df = spark.read.csv(path='test.csv'
                             , sep=','
                             , header=True
                             , quote='"'
                             , escape='\\'
                             , multiLine=True
                             , lineSep='\n'
                            )
