
## This is a bet dice game website!
It uses eos blockchain to generate dice result.
However, considering the nature of blockchain, it is truely hard to get fully random result.
Notice: 
1. you need  to create a eos account first, named getnumber to make it work!
2. make sure the wallet is unlocked. if locked, it will lead to exceptions.
3. remember to push the contract using: cleos set contract getnumber /your_route_to_contracts/contracts/getnumber -p getnumber@active
4. then use : python3 manager.py runserver 0.0.0.0:8000   to start the server
5. go to <ip addr>:8000/betdiceApp to start!
6. press BET! button to see result and BET AGAIN! button to jump back
