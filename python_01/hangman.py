#��ųʸ��� Ȱ���Ͽ� �������� �Ҵ���� ����� ���� ���Ͽ� �ش� �ܾ ����

#�ش� �ܾ �������� ���� // ���� �ܾ�

# ����� ���� ���ڿ� input //���� ���ڰ� ǥ�õ�  // for (0���� len(words.key[ran]) ����) 
#	input = input + '-' ->  ������ 5���� �̸�  -----

#����� 7���� ���� ����, 
#	chance = 7

#count�� Ȱ���Ͽ� ���� ���� �� ����
	

#����� 0 �� �ǰų�, ������ ���� ������ �ݺ�
#	while �� Ȱ��


#	Ű����� ���� ���� �ϳ��� �Է� �ް�(inputc), 
#	�̸� ����(��ųʸ��� Ű)�� ��_
#	for i=0���� len(words,key[ran]) ���� ��, ���� ��ġ �ϸ� input[i] = inputc
#		for ������ �ݺ�, ���� flag �̿��Ͽ� ��� ���� 
#			_flag �� 1�̸� �ϳ��� ���� ����, 0�̸� chance -=1

import random 

#words = {'funding':0, 'residue':1, 'dungeon':2, 'question':3, 'cohesion':4, 'downfall':5, 'football':6, 'goldfish':7}       #�ܾ���� ��ųʸ��� ����  #���ο��� �б�


#learning 0
#skeleton 2
#mainland 3
#scaffold 4
#bracelet 5
#exercise 6
#bifocals 7                   //d.txt ����


num = 0
words = {}                                                                                                                  #�ܾ ���Ϸ� �޾ƿ���
with open("d.txt") as f:                                                                                                    #f���� Ȱ�� ���� ���� FILE *fp fopen(~~)
    for line in f:                                                                                                          #���κ��� �о����
        (k, v) = line.split()                                                                                               #k = ù �ܾ�  (Ű) v = �ι�° �ܾ� (�� (���))
        words[k] = int(v)        
        num +=1                                                                                           #words �� k Ű�� ������ ���� v �� ��ųʸ� ����
                                                                                                                            #https://www.delftstack.com/ko/howto/python/python-read-file-into-dictionary/ ������.

ran = random.randint(0,num-1)                                                                                                   #0~ �ܾ�� �� ���� ���� ����

ran_word = list(words.keys())[ran]                                                                                                     #���� ������ ���� ������ ��ġ�� �ܾ ���� ����

chance = 7                                                                                                                  #���

count= 0                                                                                                                    #���� ���� ��

flag = 0                                                                                                                    #�ϳ��� �������,,

input_word = []
for i in range(len(ran_word)):
    input_word.append("-")                                                                                    # ����ĭ ����

while chance != 0 and count != len(ran_word):                                                                               #����� 0�̰ų� ��� ���� ��� ���� ����
    flag = 0                                                                                                                #�÷��� �ʱ�ȭ
    print('���� ��� ��: ',chance)                                                                                           #���� ��� �� ���
    print(input_word)                                                                                                            #���� ���� ��Ȳ ���  
    
    inputc=input('���� �ϳ� �Է� : ')                                                                                           #���� �ϳ� �Է¹ޱ�

    for i in range(len(ran_word)):                                                                                          #�Է� ���� �ش� ���� ���� ���鼭 Ȯ��(��ġ�ϴ���)
        if ran_word[i] == inputc:
            count += 1                                                                                                      #��ġ�ϸ� ���� ��(count ++)
            input_word[i] = inputc                                                                                             # -  -> inputc �� �ٲ��ֱ�
            flag = 1                                                                                                        # �������� �÷��� �����

    if flag == 0 :                                                                                                          #�����߸� ��ȸ -1       
        chance -= 1
    
if count == len(ran_word):
    print("�����մϴ�.")
if chance == 0:
    print("����")
