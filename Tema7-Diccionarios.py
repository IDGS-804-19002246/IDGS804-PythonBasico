myDiccinary = {
    'Matricula':19002246,
    'Apellido':'Escobar'
}
print(myDiccinary['Apellido'])

myDiccinary['Materia'] = 'Desarrollo Web Proficional'
print(myDiccinary)

myDiccinary['Matricula']=123456
print(myDiccinary)
del myDiccinary['Apellido']
print(myDiccinary)
