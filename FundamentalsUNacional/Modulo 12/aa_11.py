finalfinal = {0:'Hasta luego curso! Turing, puedes estar orgulloso de mi',
1:'Goodbye course! Turing, you can be proud of me'
,2:'Au revoir cours! Turing, tu peux etre fier de moi',3:'Adeus, curso! Turing, pode se orgulhar de mim'
,4:'Auf Wiedersehen! Turing, du kannst stolz auf mich sein'}
xyy = int(input())
while(xyy >= 5): print(finalfinal[xyy%5]) ; xyy //= 5