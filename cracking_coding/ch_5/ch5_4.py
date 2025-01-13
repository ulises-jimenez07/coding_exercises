from typing import Optional

def _bit(x: int, i: int)-> int:
    return x & (1<<i)

def next_smaller(x: int) ->int:
    if not x & (x+1):
        return None
    zeros=ones=0
    while _bit(x, i=ones):
        ones+=1
    while not _bit(x, i=ones+zeros):
        zeros +=1
    return x-(1<<ones) - (1<<zeros-1)+1

def next_larger(x:int) -> int:
    zeros=ones=0
    while not _bit(x,i=zeros):
        zeros +=1
    while _bit(x, i=zeros+ones):
        ones +=1
    return x+(1<<zeros)+(1<<ones-1)-1

bin(next_larger(0b10110))
bin(next_smaller(0b10110) )
