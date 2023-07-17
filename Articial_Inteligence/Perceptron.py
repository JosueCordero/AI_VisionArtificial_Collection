import numpy as np

def perceptron(x,w,d, lr):
    itr = 1
    while(True):

        for n, dn in enumerate(d):
            y = np.sign(w.T @ x[n])

            if ((dn - y) != 0):
                w = w + lr*(dn - y)*x[n]

        yn = np.sign(x @ w)
    
        if(sum(d-yn) == 0):
            print(f"\nAprendizaje realizado en {itr} iteraciones !\n")
            return w 
        itr +=1
            
if __name__ == "__main__":
    #Preparar Data
    x1 = [-1,1,-1,1]
    x2 = [-1,-1,1,1]
    x = np.array([np.ones(len(x1)),x1,x2]).T    

    b = 0.5
    w = np.array([b,1,1])

    d = np.array([-1,-1,-1,1])

    print(f'Los pesos iniciales son: {w}')

    w = perceptron(x,w,d,b)

    y = np.sign(x @ w)
    print(f'Los datos de entrada son: \n {x}')
    print(f'Los pesos actualizados son: {w}')
    print(f'El dato esperado es {d}, y el resultado con el modelo es {y}')
