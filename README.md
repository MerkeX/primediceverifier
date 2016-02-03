# PrimeDice Verifier
A simple tool in python v3 that allows you to verify your PrimeDice bets

This is the guide from the site:
"To create a roll number, Primedice uses a multi-step process to create a roll number 0-99.99. Both client and server seeds and a nonce are combined with hmac-sha512(server_seed, client_seed-nonce) which will generate a hex string. The nonce is the # of bets you made with the current seed pair. First five characters are taken from the hex string to create a roll number that is 0-1,048,575. If the roll number is over 999,999, the process is repeated with the next five characters skipping the previous set. This is done until a number less than 1,000,000 is achieved. In the astronomically unlikely event that all possible 5 character combinations are greater, 99.99 is used as the roll number. The resulting number 0-999,999 is applied a modulus of 10^4, to obtain a roll number 0-9999, and divided by 10^2 to result a 0-99.99 number."
