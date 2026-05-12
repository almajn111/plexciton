#To read files absorbance spectra from Cary 3500
def sp_abs(archivo):                                                            #returns a pandas array with the wavelengths(even cols) and intensities (odd cols)
    datos = pd.read_csv(r'AJ_'+str(archivo)+'.csv')                             #the sample name is in the even cols
    datos = datos.iloc[1:, :].dropna(how = "all", axis = 1)
    datos = datos.astype('float64')
    for i in range(len(datos.iloc[:, ::2].columns)):
        ind = 2*i+1
        datos.rename(columns= {'Unnamed: '+str(ind): 'Counts (A. U.)'} ,inplace=True)
    return datos

#To read files from Varian Cary 50 spectrophotometer(absorbance of deposited layers)
def sp_lay(archivo):
    datos = pd.read_csv(r'AJ_'+str(archivo)+'.csv', sep='\;', header=1, skip_blank_lines=True, error_bad_lines=False, engine='python')
    datos = datos.replace(',', '.', regex=True)
    datos = datos.iloc[1:, :].dropna(how = 'all')
    col = datos.iloc[:, 1]
    cols = len(datos.iloc[:, 1::2].columns)*2
    list_ind = []
    for j in range(0, len(col)):
            value = col.iloc[j]
            if type(value)==str:
                index = j
                list_ind.append(index)
    datos = datos.iloc[:list_ind[-1], :cols]
    datos = datos.astype(float)
    return datos

#To read files from Cary Eclipse
def leer(archivo): 
    sample_n = pd.read_csv(r'AJ_'+str(archivo)+'.csv', header=0).dropna(how = "all", axis = 1).columns[::2]
    print(sample_n)
    datos = pd.read_csv(r'AJ_'+str(archivo)+'.csv', header=1, skipfooter=72, engine='python').dropna(how = "all", axis = 1)
    return datos

#To read files from raman
def sp_ram(archivo):
    datos = pd.read_csv(r'AJ_'+str(archivo)+'.txt', delimiter='\t', names=[str(archivo), 'Intensity (Counts)'], header=None)
    return datos

#To read files
