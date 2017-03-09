import importlib, os, sys, time, linecache, shutil
path = os.path.dirname( os.path.abspath( __file__ ) )
sys.path.append( path + "\\Lessons" )
os.chdir( path + "\\Lessons" )

def findFiles():
    
    dirfiles = []
    for file in os.listdir():
        if file.endswith( ".py" ):
            dirfiles.append( file.replace( ".py", "" ,1 ) )
    
    total = sum( 1 for line in open( "order.txt" ) ) + 1
    files = []
    for line in range( total ):
        order = linecache.getline( "order.txt", line + 1 ).strip()
        if os.path.exists( order + ".py" ):
            files.append( order )
    newfiles = list( set( dirfiles ) - set( files ) )

    # If there are new files not configured:
    while len( newfiles ) != 0:
        answer = input( "Do you want to add the file, {}, to the list? Inputting 'no' will disable this file".format( newfiles[0] ) + "\n" ).lower()

        if answer == "yes":
            # Add file to order.txt
            with open( "order.txt", "a" ) as f:
                f.write( "\n" + newfiles[0] )
            files.append( newfiles[0] )
            newfiles = newfiles[1:]
            
        elif answer == "no":
            # Disable
            shutil.move( newfiles[0] + ".py", "disabled" )
            newfiles = newfiles[1:]
            
        else:
            print( "Please input 'yes' or 'no'\n" )
        # This only runs if if/elif is completed
        # Removes first file from list
    main( files )
    
def main( topics ):
    errorLn = 1
    error = ""
    
    while True:
        #Detects if in IDLE or command line, and accomodates for both
        newLn = 10 - len( topics )
        if "idlelib.run" in sys.modules:
            newLn = 25 - len( topics )

        print( "\n" + time.strftime( "[%d/%m/%Y %H:%M:%S]" ) + "\n" * newLn )

        print( """
▄▄▌  ▄▄▄ ..▄▄ · .▄▄ ·        ▐ ▄ .▄▄ · 
██•  ▀▄.▀·▐█ ▀. ▐█ ▀. ▪     •█▌▐█▐█ ▀. 
██▪  ▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄ ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄
▐█▌▐▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▌.▐▌██▐█▌▐█▄▪▐█
.▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀▀  ▀█▄▀▪▀▀ █▪ ▀▀▀▀ """ )
        
        print( "\n" + error + "\n" )
        
        print( "Topics:" )
        for num, topic in enumerate( topics ):
            print( str( num+1 ) + ") " + topic )

            
        try:
            userinput = int( input( "\nPick a topic number: " ) )
            if userinput in range( 1, len( topics ) + 1 ):
                print( "\n" * 55 )
                userinput = topics[ userinput - 1 ]
                try:
                    importlib.import_module( userinput )
                    error = ""
                except KeyboardInterrupt:
                    error = "You have quit the current lesson"

            else:
                error = "Please input a number within 1 and " + str( len( topics ) )
        except ValueError:
            error = "That wasn't a full number!"
        except KeyboardInterrupt:
            pass
                
            
if __name__ == "__main__":
    findFiles()
