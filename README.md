# bilde
You know Cmake? stop using it ...

Bilde is a project management tool that keeps track of what files you added to the project and supports libraries with a simple command line usage (no make file, no IDE needed to understand, everything is simple and clear) WORKS IN TEXT EDITOR (like VS Code or Notepad++).

## commands
`run` compiles the files modified since last time and link every intermediate files and lauches the executable file.<br/>
`comp` compiles the files modified since last time and link every intermediate files.<br/>
`append` adds a file to the project.<br/>
`remove` removes a file from the project.<br/>
`lib` :<br/>
> if used with `-r` removes the library from the project.<br/>
> esle adds it.

## paramiters
all the settings are aviable at the top of the file and the names are explicites

## comman line support
if you want to have a command line tool, coppy Bilde or Bilde.exe to your PATH environement variable (Bilde for Linux and Bilde.exe for Windows)
