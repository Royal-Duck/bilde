# bilde
You know Cmake? stop using it ...

Bilde is a project management tool that keeps track of what files you added to the project and supports libraries with a simple command line usage (no make file, no IDE needet to understand, everything is simple and clear).

## commands
`run` compiles the files modified since last time and link every intermediate files and lauches the executable file.
`comp` compiles the files modified since last time and link every intermediate files
`append` adds a file to the project
`remove` removes a file from the project
`lib` :
> if used with `-r` removes the library from the project
> esle adds it

## paramiters
all the settings are aviable at the top of the file and the names are explicites
