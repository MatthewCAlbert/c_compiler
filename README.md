# C/C++ Compiler/Converter
Compile your code into your predefined definition. Craft retarded code to fit your needs.

## How to use main.py
1. Paste your #define to lib.cpp.
2. Paste your code to raw.cpp, only contain #define (#define can be pasted but not defined at lib.cpp file).
3. Run compiler.py file.
4. The result will be available at out.cpp.

## Notes
View class usage example at main.py
Example files are included.

## Default file location
> Source file : raw.cpp
> 
> Output file : out.cpp
> 
> Library file (#define only) : lib.cpp

## Documentation
### Compiler Class
#### _init_(mode = "", debug = False)
> mode is unused, debug to print output per line to cli.
#### fetchLibrary(library_file_location)
> Store library to class attribute.
#### output(output_file_location)
> Output file to destination from class "out" attribute.
#### addDefinition()
> Append "out" attribute with all library added.
#### compile(source_file_location)
> Rewrite "out" attribute with compiled/converted source file.
#### convertLib(unconverted_code_snippet)
> Return converted code according to added library.
#### convertLine(line)
> Compile/convert a line of code and append it to "out" attribute.