def export(fileIn, fileOut):
    import os
    assert os.path.exists(fileIn)

    print("Attempting to read file:");
    print("\t" +fileIn);
    with open(fileIn, "rt") as FInput:
        #Read until start of interested region
        #(exit if EoF found)
        while True:
            line = FInput.readline();
            if line == "":
                return;
            if line.lstrip() == "#region CodeEditor\n":
                break;
        #end while

        #Copy region into fileOut
        #-skip any documentation comments
        #-strip leading two tab characters off
        #-convert tabs into spaces
        #-strip trailing whitespace
        with open(fileOut, "wt", newline='\n') as FOutput:
            while True:
                line = FInput.readline();
                if line == "":
                    break;
                if line.lstrip() == "#endregion\n":
                    break;
                if line.lstrip().startswith("///"):
                    continue;
                line = line.rstrip().replace('\t', '', 2);
                FOutput.write(line.expandtabs(4) +'\n');
            #end while
        #end with open(fileOut)
        assert FOutput.closed
        del FOutput
      
        del line
    #end with open(fileIn)
    assert FInput.closed
    del FInput

#end export


#run interface
if __name__ == "__main__":
    import os;

    print("Finding and exporting scripts...");
    for file in os.listdir():
        if file.endswith(".cs"):
            print();
            export(file, file[:-2] +"txt");
            print("done.");
        #end if
    #end for
    
#end main
