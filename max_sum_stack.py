def max_sum(stack1,stack2,stack3):
    sum1=sum(stack1)
    sum2=sum(stack2)
    sum3=sum(stack3)
    top1=top2=top3=0
    while True:
        if top1==len(stack1) or top2==len(stack2) or top3==len(stack3):
            return 0
        if sum1==sum2==sum3:
            return sum1
        if sum1>=sum2 and sum1>=sum3:
            sum1-=stack1[top1]
        elif sum2>=sum1 and sum2>=sum3:
            sum2-=stack2[top2]
        elif sum3>=sum1 and sum3>=sum2:
            sum3-=stack3[top3]

if __name__ == '__main__':
    stack1=[3,2,1,1,1]
    stack2=[4,3,2]
    stack3=[1,1,4,1]
    print("Maximum posiible equal sum:",max_sum(stack1,stack2,stack3))
