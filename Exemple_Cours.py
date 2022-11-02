import numpy as np
i_gate= np.array ([[1,0],[0,1]])
h_gate=np.sqrt(0.5)*np.array([[1,1],[1,-1]])
cx_gate=np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
ih_gate=np.kron(i_gate,h_gate)
print(ih_gate)
u_circuit=np.matmul(cx_gate,ih_gate)
print('u_circuit \n',u_circuit)
#Un autre façon, mëme résultat
u_circuit2=cx_gate@ih_gate
print('u_circuit2 \n',u_circuit2)
init_state=np.array([1,0,0,0])
final_state=u_circuit@init_state
print('final_sate=bell state \n',final_state)
probabilites=final_state*np.conjugate(final_state)
print('probabilites \n',probabilites)