# Constraining the functional form of the Carnot Efficiency

## Disclaimer

I do not take credit for this explanation. A fellow classmate told me this in passing, so I decided to write it up for my own benefit. Unfortunately, I did not catch his name. Additionally, any errors in the presentation should be attributed solely to me. 

## Setup

One can deduce the following constraint about the efficiency of a Carnot engine, $\eta$
$$
1 - \eta(T_1, T_3) = (1 - \eta(T_1, T_2))(1 - \eta(T_2, T_3))
$$
From this, we can conclude that $1 - \eta(T_1, T_2) = \frac{G(T_1)}{G(T_2)}$, for some single-variable function $G$. But how?

## Proof

First of all, let's simplify the problem. I will relabel $T_1, T_2, T_3$ to the familiar $x, y, z$. I will also define another function $f$

 to be $1-\eta$. Thus,
$$
f(x, z) = f(x, y)f(y, z)
$$
Second, let's understand the setup. $x, y,$ and $z$ vary in a certain way, and we are supplying them as inputs to the function. This means that if we choose a particular value of one variable, this constrains the way the functions behave. This becomes more clear once we rearrange the expression. 
$$
\frac{f(x, z)}{f(y, z)} = f(x, y)
$$
All we have done here is divide through by $f(y, z)$. Now, let's consider the variable $z$. The right hand side of the expression does *not* depend on $z$. This is important. This means we can choose a particular value for $z$ ,and nothing will happen to the right hand side. To be more precise, we can define a new function  that takes in three inputs, 
$$
g(x, y, z) \equiv \frac{f(x, z)}{f(y, z)} 
$$
and our expression becomes
$$
g(x, y, z) = f(x, y)
$$
This tells us that $z$ is spurious! No matter what we choose, the function on the right hand side will be the same. That means
$$
g(x, y, 0) = g(x, y, 1) = g(x, y, 2) = f(x, y)
$$
As goes for any number we put in that third slot. Therefore, we might as well just write down
$$
g(x, y) = f(x, y)
$$
And drop that third argument. And we'll do just that, with one small caveat. We cannot *really* drop the second argument from $f(x, z)$, since it is a function of two variables. However, when we choose a particular value of $z$ we can turn it into a single variable function that only depends on $x$. In other words, we are defining
$$
h_z(x) \equiv f(x, z)
$$

Remember that $z$ is a number that we have fixed in advance! Also remember that it might *not* be the case that $h_z(x)$ is the same for all values of $z$. All we know is that the $z$ dependence drops out when we divide them, so it doesn't even matter what we chose $z$ to be in the first place. 
$$
g(x, y, z) = \frac{h_z(x)}{h_z(y)} = f(x, y)
$$
Since the right hand side of this expression, $f(x, y)$ exhibits no $z$ dependence, we might as well drop the $z$ from every other term.
$$
g(x, y) = \frac{h(x)}{h(y)} = f(x, y)
$$
And we are done! Note that the individual function $h(x)$ still *does* depend on $z$, but we might as well leave it out when we write it down as a ratio because it will produce the same function no matter what $z$ was in the first place. 
