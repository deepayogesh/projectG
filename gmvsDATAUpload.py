# import Dependancies for Database connection and populating data in table 
import psycopg2
# import sys to get more detailed Python exception info
import sys

# import the connect library for psycopg2
from psycopg2 import connect

# import the error handling libraries for psycopg2
from psycopg2 import OperationalError, errorcodes, errors

# import the psycopg2 library's __version__ string
from psycopg2 import __version__ as psycopg2_version

# define a function that handles and parses psycopg2 exceptions
def print_psycopg2_exception(err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()
    # get the line number when exception occured
    line_num = traceback.tb_lineno
    # print the connect() error
    print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type)

    # psycopg2 extensions.Diagnostics object attribute
    print ("\nextensions.Diagnostics:", err.diag)

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")  
# ENDS function that handles and parses psycopg2 exceptions 

# DEfine function to RDS connection using try  catch 
# Make sure you have config file at proper place
def connectdb():
    from config import db_user,db_host,db_password
    try:
        conn = connect(user= db_user,host =db_host,password =db_password )
    except OperationalError as err:
        # pass exception to function
        print_psycopg2_exception(err)
        # set the connection to 'None' in case of error
        conn = None
    if conn != None:
        # declare a cursor object from the connection
        cursor = conn.cursor()
        #print("Database connected Successfully!")
        #print ("cursor object:", cursor, "\n")
        return (cursor,conn)
    else:
        print_psycopg2_exception(err)
        return  
# ENDS  DEfine function to RDS connection

# Build query statement function
def buildquery(flag,tablename):
    # Build the query for select or delete
    if flag == 'S' or flag =='s':
        query= "SELECT * FROM " +tablename
    else:
        query = "DELETE FROM  "+tablename
    return query
# ENDS here Build query statement function

#  Define function to check table exist
def table_exists(cur, tablename):
    query=buildquery('S',tablename)
    #print("inside table exist query")
    print(query)
    cur.execute(query)
    if cur.rowcount > 0:
         return True
    else:
         return False
# cur.rowcount > 0  # more Pythonic way
#  ENDS HERE Define function to check table exist
# 
#The function below will get used for select and delete
#
def ddl_table(cursor,query,conn):
# SELECT  from table 
    try:
        cursor.execute(query)                
    except Exception as err:
        gVar_Result = "Failuar error occured selecting data from table"
        # pass exception to function
        print_psycopg2_exception(err)
        #print("error")
        # rollback the previous transaction before starting another
        conn.rollback()
# Function ends here

# Define insert from csv function for the table      copy_to(file, table, sep='\t', null='\\N', columns=None)
def fun_insert_rows_from_CSV(cursor,filename,tablename,sep):
    #  Inserrt data from csv 
    try:
        with open(filename, 'r',errors="ignore") as f:
            next(f) # Skip the header row.
            # IF THE FILENAME CONTAINS .TSV  THEN 
            if sep == 'c':
                cursor.copy_from(f, tablename, sep=',')        
                conn.commit()                
            elif sep == 't':
                # another way to import data into table from file
                cursor.copy_expert("COPY "+tablename+" FROM STDIN",f)  # just another way of writing into table
                conn.commit()
            gVar_Result = "Inserted rows sucessfully"
    except Exception as err:
        gVar_Result = "Failuar error occured inserting rows"
        # pass exception to function
        print_psycopg2_exception(err)
        # rollback the previous transaction before starting another
        conn.rollback()   
# ENDS HERE insert from csv function for the table

# Populate data to all table function 
def populate(cursor,tablename,filename,gvar_sep):
        # Check this table EXIST
        vexists = table_exists(cursor,tablename)
        if vexists: 
            print(tablename+"  this Table exist")
            # Delete records before you insert them 
            gquery= buildquery('D',tablename)
            print("Lets delete existing data")
            print(gquery)
            ddl_table(cursor,gquery,conn)
            # Now Populate table data 
            # Assumption : Table already created in the DATABASE and file column and table columns matches 
            try: 
                print(" Now inserting into table from file")
                fun_insert_rows_from_CSV(cursor,filename,tablename,gvar_sep)
                print("Data uploaded ")
                conn.commit()
            except Exception as err:
                #print("Error")
                conn.rollback()
                print_psycopg2_exception(err)
# ENDS HERE Populate data to all table function 
#----------------------------------------------------------------------------------------------------
# Using all functions lets populate data into table from file

# Global variables in use 
gquery = ""
gVar_Result = ""  # this will only display sucess or failuar 
# Assumption = read file stored at same place of this py file. 
# Lets connect to database  # Establish database connection
gcursor,conn = connectdb()
if gcursor !=None:
    # FOR the TABLE and FILE 
    gtablename= 'g_mvs_title_basics2'
    gfilename ='title_basics_non-adult_movies_no_nulls.tsv' 
    gvar_sep = 't'   # setting seperator  for the fiel as comma seperator 
    populate(gcursor,gtablename,gfilename,gvar_sep)
    print(gtablename+" data populated sucessfully") 

    # FOR the TABLE and FILE 
    gtablename= 'g_mvs_us_title_ids2'
    gfilename ='US_title_ids_unq.csv' 
    gvar_sep = 'c'   # setting seperator  for the fiel as comma seperator 
    populate(gcursor,gtablename,gfilename,gvar_sep)
    print(gtablename+" data populated sucessfully")   

    # FOR the TABLE and FILE 
    gtablename= 'g_mvs_title_ratings2'
    gfilename ='title_ratings.csv' 
    gvar_sep = 'c'   # setting seperator  for the fiel as comma seperator 
    populate(gcursor,gtablename,gfilename,gvar_sep)
    print(gtablename+" data populated sucessfully")   
#-------------------------------------------------------------------------------
conn.close()