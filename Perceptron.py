#Given Expression : [(A+B')(A'.B) (1/-1)]

def change_weights(w0,w1,w2,x1,x2,t,o):
	w0 = w0 + 1*(t-o)
	w1 = w1 + 1*(t-o)*x1
	w2 = w2 + 1*(t-o)*x2
	return [w0,w1,w2]


def evaluation_f(yin):
	if yin > 0:
		return 1
	elif yin == 0:
		return 0
	elif yin < 0:
		return -1

[w0,w1,w2] = [0,0,0]

#inputs as [input1,input2,output]
A_plus_Bbar= [[-1,-1,1],[-1,1,-1],[1,-1,1],[1,1,1]] #[A,B, A+B']
Abar_B = [[-1,-1,-1],[-1,1,1],[1,-1,-1],[1,1,-1]] #[A,B, A'.B]
final_output = [[1,-1,-1],[-1,1,-1],[1,-1,-1],[1,-1,-1]]  # [A+B',A'.B, (A+B').(A'.B)]

#evaluation of final weights
def perceptron(input):
	[w0,w1,w2] = [0,0,0]
	for j in range(2):
		for i in input:
			yin = w0+i[0]*w1+i[1]*w2
			y = evaluation_f(yin)
			if(y == i[2]):
				print("NO need to change the Weights as Target = Output")
			elif(y != i[2]):
				print("Need to change the weights here.Now the updated Weights are  ",end="")
				[w0,w1,w2] = change_weights(w0,w1,w2,i[0],i[1],i[2],y)
				print("w0=",w0,"w1=",w1,"w2=",w2)
	return [w0,w1,w2]

# calculation of weights for perceptrons
print("________________________________________________________________________________")
print("----------------------------------")
print("Evaluation of the Expression(A+B')")
print("----------------------------------")
[w01,w11,w21] = perceptron(A_plus_Bbar)
print("--------------------------------------------------------------------------------")
print("Weights after evaluation of (A+B') perceptron are w0=",w01,"w1=",w11,"w2=",w21)
print("--------------------------------------------------------------------------------")
print("________________________________________________________________________________")
print("----------------------------------")
print("Evaluation of the Expression (A'.B)")
print("----------------------------------")
[w02,w12,w22] = perceptron(Abar_B)
print("--------------------------------------------------------------------------------")
print("Weights after evaluation of (A'.B) perceptron are w0=",w02,"w1=",w12,"w2=",w22)
print("--------------------------------------------------------------------------------")
print("________________________________________________________________________________")
[w03,w13,w23] = perceptron(final_output)
print("--------------------------------------------------------------------------------")
print("Weights of the Hidder layer applied to final linear perceptron are w0=",w03,"w1=",w13,"w2=",w23)
print("--------------------------------------------------------------------------------")
print("________________________________________________________________________________")

# [A,B,Final Output] in final_output variable
final_input=[[1,-1,-1],
            [-1,1,-1],
            [1,-1,-1],
            [1,-1,-1]]



#conversion of -1 and +1 to boolean
def gtb(a):
	if a == -1:
		a = 0
	elif a ==1:
		a = 1
	return a

#comparison of perceptron output to actual output
for i in final_input:
	yin = w01+i[0]*w11+i[1]*w21
	y1 = evaluation_f(yin)
	yin = w02+i[0]*w12+i[2]*w22
	y2 = evaluation_f(yin)
	yin = w03+y1*w13+y2*w23
	y_out = evaluation_f(yin)


	if gtb(y_out)==gtb(i[1]):
		print("The actual and perceptron output is same ",end="")
		print(y_out,i[1])
	else:
		print("The actual and perceptron output is same")
