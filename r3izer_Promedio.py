                ####     PROMEDIO DE NOTAS DE UNA SECCIÓN      ####
                #### CODIGO SENCILLO SIN VALIDACIÓN DE STRING  ####

acum=0
promedio=0.0
j = 0
c = int(input("introduzca la cantidad de alumnos de la sección : "))
if(c<=30 and c>0):
        ###Cantidad de notas que se van a procesar
        while j < c: 
            n= float(input("introduzca las notas definitivas de los alumnos : "))
            ###Validación para numeros positivos y notas en escala de 20
            if(n <=20 and n>0):
                acum = acum + n
                promedio = acum/c
                ###Incremento del indice para que salga del ciclo
                j= j+1 
            else:
                print("Introduzca numeros no negativos entre 1 y 20")           
        print("El promedio de la seccion es : " + str(float(promedio)))
###Salida em caso de exceder el limite de la sección


else:
        ### Caso contrario ciclo para que se repita hasta que se introduzca la cantidad permitida
        while c > 30:
                print("la capacidad maxima de la sección es de 30 persona, por favor intente de nuevo.")
                c = int(input("introduzca la cantidad de alumnos de la sección : "))
                ###Condiciones para calcular el promedio una vez pasada la validación
                if(c<=30 and c >0):
                         while j < c:
                                 n= float(input("introduzca las notas definitivas de los alumnos : "))
                                 if(n <=20 and n>0):
                                         acum = acum + n
                                         promedio = acum/c
                                         j= j+1
                                 else:
                                          print("Introduzca numeros no negativos entre 1 y 20")
                         print("El promedio de la seccion es : " + str(float(promedio)))
                                         
                         
                
        
        
       
                
                        
                        
                                
                                
                                
                        
                               
                
                
                                
        
    
   
            


        
           
    
    
    
