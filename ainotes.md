#	Probability and Bayes theory.

##	Basic probability

1.	Most probability questions can be considered from the following formula:

			target_outcomes / all_possible_outcomes
	
	For example: three flips of a fair coin, what are the chances of getting at least two heads?

			[HHH, HHT, HTH, THH] / [HHH, HHT, HTH, HTT, TTT, TTH, HTH, THH]]
	
	This only works for independent events. If getting heads on the first flip effected all subsequent flips, then the problem is harder.

2.	Combining probabilities means multiplying each instance, when each is independent. 

	Example: five heads in a row with a fair coin = 0.5 * 0.5 * 0.5 * 0.5 * 0.5 = 0.5**5.

3.	Considering many paths to reach a similar conclusion, you can add the combined 		probabilities of each branch. 


##	Bayesian analysis

1.	Given some information, like a test for cancer or the existence trick 2-sided coin, what are the chances the hidden information (actual cancer, which coin you got) is true?

	Example: a bag of 10 coins, one is a trick 2S coin. You pick one randomly, and get five heads. How likely is it that you got the trick coin?


		P(A) = 0.1 			= probability of getting the trick coin
		P(!A) = 0.9 		= probability of getting a normal coin
		P(B) = 	???			= probability of getting 5 heads in a row, regardless of coin
		P(A|B) = ??? 		= given five heads, this is the probability of having gotten the trick coin
		P(B|A) = 1.0 		= probability of getting five heads, given you got the trick coin
		P(B|!A) = 0.03125 	= probability of getting five heads, given a normal coin

		P(B) = P(!A) * P(B|!A) + P(B|A) * P(A)
			= 	probability of getting a normal coin, then getting five heads PLUS the probability of getting the trick coin, then getting five heads
			=	0.9*0.03125 + 1*0.1 = (9/320) / (32/320)
			=	0.12812 = 41/320

	So you have the total space where you get five heads from one coin (around 13% of all outcomes). Some portion of that is from getting really lucky with a normal coin, but a bigger part of it is from getting the trick coin. And that is what we want - how likely is it you got the trick coin?

	Remember that probability is the count of: 
	
		target_outcomes / total_outcomes

	So if we only consider the universe where we got five heads, the total_outcomes is this: 

		P(B) = 0.12812 = P(!A) * P(B|!A) + P(B|A) * P(A)

	And the target_outcomes, where we got the trick coin, the ones we care about, is:

		P(B|A) * P(A) = probability of getting the trick coin, then getting five heads

	So just divide them like you do any target_outcomes / total_outcomes:

		P(A|B) = P(B|A) * P(A) / P(!A) * P(B|!A) + P(B|A) * P(A)

	That is all Bayes rule is. That's the whole formula. So to solve:

		P(A|B)	= P(B|A) * P(A) / P(!A) * P(B|!A) + P(B|A) * P(A)
				= 1.0 * 0.1 / (0.9 * 0.03125 + 1.0 * 0.1)
				= 0.1 / 0.128125
				= 0.780
	
	It's really likely you got the trick coin. And every time you flip and get a heads, it gets more and more likely. Which makes perfect sense. In fact, pretend you got the answer and flipped the coin again, and got heads again.

	The only number that really changes here is the possibility of getting another heads with a normal coin. Instead of 1/32 chance, it is 1/64 or 0.015625.

		P(A|B)	= P(B|A) * P(A) / P(!A) * P(B|!A) + P(B|A) * P(A)
				= 1.0 * 0.1 / (0.9 * 0.015625 + 1.0 * 0.1)
				= 0.1 / 0.1140
				= 0.877
	
	An intelligent agent will likely live in a world of uncertainty. Given some constant information, it needs to make guesses about the real world and reevaluate it's actions whenever it gets new data. Human beings do this all the time without thinking. In theory, the intelligent agent could do better, as it can grasp the nonintuitive conculsions of bayesian analysis.

2.	What about the cancer test? Given a positive result, what is the actual likelihood you have cancer?

		P(A) = 0.01 		chance of having cancer in the general population
		P(B) = ???			POSITIVE test outcome
		P(B|A) = 0.9		NEGATIVE test outcome if DO you have cancer
		P(!B|!A) = 0.8		NEGATIVE result if you DO NOT have cancer
		P(A|B) = ???		Chance of cancer, given a positive test

	We just barely have enough information to solve this. In the total universe where we DO have cancer, in how likely is it we got a positive test? Remember:
		
		target_outcomes / total_outcomes

		cancer_and_positive_test / all_outcomes_with_a_positive_test

		P(A|B) 	= P(B|A) * P(A) / P(!A) * P(B|!A) + P(B|A) * P(A)

	Not all those variables are up there, so we have to think here. Remember that all probabilities for some thing have to equal 100%. Thus we can get the chance of NOT having cancer quite easily:

		P(!A) = 1 - P(A) = 0.99

	P(B|!A) is just "given you don't have cancer, how likely is a positive test?". Essentially, what is the false positive? We have the number for the opposite (a correct negative), so it is again the difference between that and 100%.

		P(B|!A) = 1 - P(!B|!A) = 0.2
	
	That is a big false positive (20%!).

	So, plug the numbers in:

	P(A|B) 	= P(B|A) * P(A) / P(!A) * P(B|!A) + P(B|A) * P(A)
			= 0.9 * 0.01 / ( 0.99 * 0.2 + 0.9 * 0.01 )
			= 0.0437

	You get a positive test and there is only a 4% chance you actually have cancer. Seems wild, but consider the extreme unlikelihood of actually having the cancer (99% of the population DOESN'T have it) and the really high false positive rate. This is why doctors do not rely on just tests, they consider a huge number of variables when making a diagnosis and often repeat the test. 


3.	Lets repeat the test. Suppose you took the test twice and got two positive results. You're doomed huh? Not so fast.

	Remember that the big deal is 
		
		target_outcomes / all_possible_outcomes

	What are the target outcomes? All of the situations where you got two positive tests and have cancer. Or 

		// assume cancer, two positive tests
		P1 	= P(B|A) * P(B|A) * P(A)
			= 0.9 * 0.9 * 0.01
			= 0.0081

	What's P1? They call that the pseudo probability. In this case, it is the pseudo probability if we assume you do have cancer. We can flip it, and assume you don't have cancer (with that lovely 20% false positive scaring the willies out of you)

		// assume no cancer, two positive tests
		P2 	= P(!B|A) * P(!B|A) * P(!A)
			= 0.2 * 0.2 * 0.99
			= 0.03960
	
	These aren't real possibilities mind you. These are more like hypotheticals. Back to the formula, what have we got filled in?

		P(B|A) * P(B|A) * P(A) / ??? + P(B|A) * P(B|A) * P(A)

	The ??? here is "all those other possibilities where you got positive results, but don't really have cancer". Remember, you are comparing the target_outcomes (the top bit, P(B|A) * P(B|A) * P(A)) vs every other situation where the conditionals are the same (aka, where you get the two tests)

	Wait! We just did that, didn't we? When we considered that hypothetical where we didn't have cancer, but did have two positive tests! This thing:

		// assume no cancer, two positive tests
		P2 	= P(!B|A) * P(!B|A) * P(!A)

	That's the missing piece. Full formula for this problem:

		P(A|B&B) = P(B|A) * P(B|A) * P(A) / P(!B|A) * P(!B|A) * P(!A) + P(B|A) * P(B|A) * P(A)

	Just to be 100% clear, I'm going to talk out that whole above equasion:

	"The chance of having cancer after two positive tests is: (P1) The chance of having cancer AND getting two positive tests DIVIDED BY (P2) the chance of getting a pair of false positives and NOT having cancer AND (P1 again) the chance of having cancer AND getting two positive tests"
	
	You can replace "the chance of" with "all of the occurances of" if you like thinking about this stuff as the frequency.

	At the end of the day, you can calculate the psuedo probabilities (P1 and P2 above), pick the thing you are targeting, and divide by their addition:

		P1 / (P1 + P2)

4.	What if I wanted some code for this?

	Okay, here is a simple function for the algorithm.

		def bayes(P_BA, P_A, P_BnA):
		    d = P_BA * P_A
		    n1 = P_BA * P_A
		    n2 = P_BnA * (1-P_A)
		    n = (n1+n2) 
		    print d/n

##	Conditional Dependence

1.	If you originally got a positive test from the example above, how likely are you to get another positive test?

		P(A) = 0.01 	= P(C)
		P(B) = ??? 		= P(+)
		P(B|A) = 0.9 	= P(+|C)
		P(!B|!C) = 0.8 	= P(-|!C)
		P(T2+|T1+) = ???

	Again, target_outcome/total_outcomes. So what are the total_outcomes? First is the possibility where you have cancer, and you get two positive tests, combined with the chance that you have cancer and the first test was positive test.

		P(+2|+1&C) * P(C|+1) 

	Then, naturally, there is the possibility where you DO NOT have cancer, and you get two positive tests, combined with getting a positive test and NOT having cancer.

		P(+2|+1!C) * P(!C|+1)

	Add those together and you get the total probability. It is exactly the same as before, only EVERYTHING is conditions on that first test being positive.

	Now we've seen some of these possibilities before. We know the chances of having cancer and given a positive test (and we know the opposite).

		(??? * 0.043) + (??? * 0.957)

	The other variables you get via the magic of conditional dependence. The first one

		P(+2|+1&C) = probability of a positive second test, given a positive first test and that you have cancer

	Is simple when you consider that if you have cancer, the first test doesn't really add any information. It would only be important if you didn't know if you have cancer, but for the purposes of just this little bit of the equasion, here you are assuming you do.

		P(+2|+1&C) = P(+2|C)

	You can do the same thing for the bit where you assume you don't have cancer.

		P(+2|+1&!C) = P(+2|!C)

	The test is still the test, so both of these equal the generalized values we had above

		P(+2|C) = P(+|C) = P(B|A) = 0.9
		P(+2|!C) = P(+|!C) = P(B|!A) = 0.2
		
	
		P(T2+|T1+) = (0.9 * 0.043) + (0.2 * 0.957)
		= 0.23

2.	Absolute v. Conditional independence

	Absolute independence is coin flips. No one coin flip has an effect on subsequent ones (barring wierdness where you damage the coin).

	Conditional independence is where you have some other variable, which if you take for a given, two other variables are independent. If you have cancer, one the first test has the same chance as the second. But if you didn't know you had cancer, the first test changes the likelihood of the second test being positive or negative.

	If a pair of variables are absolutely independent, this does NOT imply are also conditionally independent. Nor the other way around.

3.	Explaining away

	Suppose two independent variables can cause the same effect. I could be happy because it is a sunny day, or I could be happy if I get a raise, or I could be happy because both occur.

	Given that I am happy AND sunny weather, the sunny weather could "explain away" the cause of happiness. It becomes less likely that I got a raise. 

	On the other hand, if I am happy, and it is rainy, it is more likely that I got a raise than the normal probability of getting a raise would suggest.

	The upshot is that if you observe the effect (I am happy) and some other relevant causal information (sunny, rainy, raise, no raise), then that information can impact the probability of other potential causes. 

	So what is the probability I got a raise, given than I am happy and it is sunny? Also given the following.
		
		P(S) = 0.7
		P(R) = 0.01
		P(H|S,R) = 1
		P(H|!S,R) = 0.9
		P(H|S,!R) = 0.7
		P(H|!S, !R) = 0.1
		
	Well, lets think about the target_outcomes and total_outcomes. What we want is the probability of a raise, given it is sunny and I am happy. Normally, the probability would be just P(R), but it is less now that the happiness can be explained away by the sun.

	With Bayes theorem, you can expand any problem like this. The basics of it is taking the counterfactual and the probability of it happening (the numerator) and dividing that by the total probability of the given variables. The 'A' and 'B' can be anything.

		P(A|B) = P(B|A) * P(A) / P(B)

	So if we plug that in like so

		P(A|B) = P(R|H,S)

	We can fill in the rest

		P(R|H,S) = P(H|R,S) * P(R|S) / P(H|S)

	The chances I am happy GIVEN it is sunny are:

		P(H|S) 	= P(H|S,R) * P(R) + P(H|S,!R) * P(!R)
				= (1 * 0.01) + (0.7 * 0.99)
				= 0.703
	
	Notice you didn't have to also multiply the first two pieces by P(S)? Well the whole problem is based on S as a given! P(H|S).

	R and S are independent, so P(R|S) = P(R). P(H|R,S) = P(H|S,R) = 1, so
	
	P(R|H,S) 	= 1 * 0.01 / 0.703
				= 0.0142

4.	This is it. This is the part where they try to bring their class size from 140K to like 12 diehards. So what is P(R|H) and this is "really complicated"

		P(S) = 0.7
		P(R) = 0.01
		P(H|S,R) = 1
		P(H|!S,R) = 0.9
		P(H|S,!R) = 0.7
		P(H|!S, !R) = 0.1

	Okay, well I got P(H|S) by means of this bit.

		P(H|S) 	= P(H|S,R) * P(R) + P(H|S,!R) * P(!R)
		= (1 * 0.01) + (0.7 * 0.99)
		= 0.703

	It ISN'T just the 1-P(H|S), because it isn't given that P(R|H) is sunny. But we should be able to figure it out in the same fashion. Right? Well, no, but we can get all Bayesian up in this house.

		P(R|H) 	= P(H|R) * P(R) / P(H|R) * P(R) + P(H|!R) * P(!R) 

	Wait, do we have to consider the weather at all? I mean, if it is sunny, it is LESS likely I'm happy because of the raise. Well, turns out just trying to calculate the bottom portion brings that mess in.
		
		P(H|R) 	= P(H|S,R) * P(S) + P(H|!S,R) * P(!S)
				= 1 * 0.7 + 0.9 * 0.3
				= 0.97

		P(H|!R) = P(H|S,!R) * P(S) + P(H|!S,!R) * P(!S)
				= 0.7 * 0.7 + 0.1 * 0.3
				= 0.52

		P(R|H) 	= P(H|R) * P(R) / P(H|R) * P(R) + P(H|!R) * P(!R)
				= 0.97 * 0.01 / (0.97 * 0.01 + 0.52 * 0.99)
				= 0.018
	
	I got this right the first time. Apparently that is pretty impressive, however, it is tempered by the fact I am pretty sure I got everything else in the AI lecture quizzes wrong for this section.

	Last question. What is the probability of getting a raise, given that it is not sunny and I am happy. This tells you the maximum chance of having gotten a raise, given these values.

	P(R|H,!S) 	= P(H|R,!S) * P(R) / (P(H|R,!S) * P(R) +  (P(H|!R,!S) * P(!R))
				= 0.9 * 0.01 / (0.9 * 0.01 + 0.1 * 0.99)
				= 0.083

5.	The takeaway, mindblowing part is that only when we know about the other variable, does it make a difference. When happiness is unknown, the actual chances of say getting a raise is independent of the weather P(R|S) = P(R). S and R become dependent the moment you know the happiness. 

	Independence does not imply conditional independence.

	Conditional independence does not imply absolute independence.

	Thanks to this class, the world is a slightly wierder place.

##	General Bayes Networks

1.	A graph of random variables. 
	
	Each one has a probability assigned to it.

	Each incoming edge defines the dependence of the node's probability.

	A network defined by these edges
		
		A->C
		B->C
		C->D
		C->E

	Has these probabilities for each node

		A = P(A)
		B = P(B)
		C = P(C|A,B)
		D = P(D|C)
		E = P(E|C)

	The joint probability would be 

		P(A,B,C,D,E) = P(A) * P(B) * P(C|A,B) * P(D|C) * P(E|C)

	Rather than using values 2^5-1 to represent this graph (combinatorial approach), we can use 10. Assuming these are binary variables

		P(A) = 1
		P(B) = 1
		P(C|A,B) = 4 [P(C|A,B), P(C|A,!B), P(C|!A,B), P(C|!A,!B)]
		P(D|C) = 2 [P(D|C), P(D|!C)]
		P(E|C) = 2 [P(E|C), P(E|!C)]

2.	How many values are required for this graph?

		A->B->E
		A->C->F
		A->D->F

		A = P(A)
		B = P(B|A), P(B|!A)
		E = P(E|B), P(E|!B)
		C = P(C|A), P(C|!A)
		D = P(D|A), P(D|!A)
		F = P(F|C,D), P(F|C,!D), P(F|!C,D), P(F|!C,!D)

		= 13

	Given binary variables, it is always 2^incoming_edges

##	D-Seperation

1.	Also known as reachability

	Which nodes are dependent and independent of each other.

	All downstream nodes are dependent on their upstream nodes, unless they are given the value of an interceding node.

	Nodes that have a common successor become dependent when their successor is given. The Explain Away effect in action. It doesn't have to be immediate, it could be a known variable much deeper in the graph.

2.	Triplets

	Active = render things dependent.

		A->B->C

	A and C are dependent, if all variables are known.

	Inactive = render things independent.

		A->B->C

	If B is know, but A and C are not, those variables become independent.



##	HW2
1.	Bayes Rule

		P(B) = P(B|A) * P(A) + P(B|!A) * P(!A)
		P(A|B) 	= P(B|A) * P(A) / P(B)
				= P(B|A) * P(A) / P(B|A) * P(A) + P(B|!A) * P(!A)
				= 0.2 * 0.5 / (0.2 * 0.5 + 0.8 * 0.5)
				= 0.2

2.	Simple Bayes Net

	For this graph
		A->X1
		A->X2
		A->X3

	Given these probabilities
		P(A) = 0.5
		For all X, 
		P(Xi|A) = 0.2
		P(Xi|!A) = 0.6

	What is P(A|X1, X2, X3)?

	Multiplication of the preconditions is allowed. Given A, there is conditional independence.

			Prior	X1	X2	!X3	P1		
		A 	0.5 	0.2 0.2 0.8 0.016 	Remember, this is simply the top bit of Bayes rule
		!A 	0.5 	0.6 0.6 0.4 0.072

	Add the P1 together, then divide by P1:
		0.016 + 0.072 = 0.088			And this is just the bottom bit of Bayes rule

		0.016 / 0.088 = 0.181818 <- P(A|X1, X2, X3), the answer
		0.072 / 0.088 = 0.818181

3.	Simple Bayes Net 2

	Same network as above. What is P(X3|X1)?

	Remember Conditional Dependence 1 above. You don't have A, so the X values are conditionally dependent. 

		P(A) = 0.5
		P(X|A) = 0.2
		P(!X|A) = 0.8
		P(X|!A) = 0.6
		P(!X|!A) = 0.4

		P(X3|X1) = P(X1|X3) * P(X3) / P(X1)

	Wow, uh, you don't have any of those values. You gotta bring in A. You also have to bring in the other X (conditional dependence). Remember, target/total. What are the total possible outcomes in this problem? Well consider the situations where A is true and A is false

		P(X1|X3, X2, A) * P(A|X3, X2) + P(X1|X3, X2, !A) * P(!A|X3, X2)

	Given A, we get conditional independence, so we can simplify the first two numbers.

		P(X1|A) * P(A|X3, X2) + P(X1|!A) * P(!A|X3, X2)

	Okay, we have some of these numbers, what do we do about the other ones? Same operation. Add the conditional and expand to take into account the situations where A is true and A is false.

		P(A|X3, X2) = P(X3|A) * P(A|X2) + P(X3|!A) * P(!A|X2)

		P(X1|A) * (P(X3|A) * P(A|X2) + P(X3|!A) * P(!A|X2)) + 
		P(X1|!A) * (P(X3|A) * P(A|X2) + P(X3|!A) * P(!A|X2))

		0.2 * (0.2 * P(A|X2) + 0.6 * P(!A|X2)) + 
		0.6 * (0.2 * P(A|X2) + 0.6 * P(!A|X2))

	That vastly simplifies things. Now we just need to find P(A|X). Bayes to the rescue.

		P(A|X) = P(X|A) * P(A) / P(X)
		P(X) = P(X|A) * P(A) + P(X|!A) * P(!A)
			
		P(A|X) 	= P(X|A) * P(A) / P(X|A) * P(A) + P(X|!A) * P(!A)
				= 0.2 * 0.5 / (0.2 * 0.5 + 0.6 * 0.5)
				= 0.25

	Plug that jazz in

		P(X3|X1) 	= 0.2 * (0.2 * 0.25 + 0.6 * 0.75) + 0.6 * (0.2 * 0.25 + 0.6 * 0.75) / P(X)
					= 0.3999 / P(X)

	Which makes a bit of sense. Independently, the possibility of X given A is 0.2. Given one of the X values as true increases the chance that A is false, which increases the chances of all other X values being true. 

	Think back to the cancer tests - the chance for cancer increased with every positive test (by a little). This is the opposite, every given value of X decreases the likelihood of A, and decreasing the likelihood of A increases the chances for other values of X.

#	Machine Learning

##	Supervised Learning

1.	Goal

	Given some vector of data (x1, x2, x_n) and the result y, predict future y values given any x values.

		f(x_m) = y_m

	The x values might be pixels in a vision learning program, or expert system for choosing mortgage rates, or whatever.

###	Naive Bayes methods, classification

	Using some corpus of test data, you create some function f(x) that determines the likelyhood of x being a class y.

2.	Maximum Likelihood

	Essentially, this just follows the Bayes rule.

		P(A|B) = P(B|A) * P(A) / P(B)
		where P(B) = P(B|A) * P(A) + P(B|!A) * P(!A)

	Given that you have big piles of training data (x1, x2, x_n as above), you will be multiplying probabilities.

		p1 = P(B1|A) * P(B2|A) * P(B_n|A) * P(A)
		p2 = P(B1|!A) * P(B2|!A) * P(B_n|!A) * P(!A)
		= p1 / (p1+p2)

	Problem: any value with a zero probability, aka it doesn't occur in one class, and the whole thing has a zero chance with this formula.

	We are fitting to the data too drastically.

3.	Laplace Smoothing

	One way to avoid this is by adding a dummy value. Here's max likelihood

		p(x) = count(x) / N
		
	where count(x) is the number of occurances of this value in the variable x and N is the total number of occurances of x

	Example:
		
		P(Spam) = count(Spam) / count(Spam & Ham) = 3/8

	Laplace Smoothing adds a variable in there

		p(x) = count(x) + k / N + k|x|

	Where k is some smoothing parameter and |x| is the number of values that thevariable x can be.

	So essentially you add k to the class that you are targeting and then to every single class in the denominator.

	Example:
		
		k=1
		Where data = 1 message, 1 spam 

		P(Spam) 
		= count(Spam)+k / count(Spam)+k + count(ham)+k
		= 1 / 1 + 2
		= 2 / 3

	Where data = 10 message, 6 spam 

		P(Spam) 
		= count(Spam)+k / count(Spam)+k + count(ham)+k
		= 6 / 6 + 4 + 2
		= 0.5833

	Where data = 100 message, 60 spam 

		P(Spam) 
		= count(Spam)+k / (count(Spam) + count(ham)) + 2
		= 60 + 1 / 60 + 40 + 1
		= 0.5986

	You have to be careful about classes. For instance, if you are comparing total messages, then you would have the classes "spam" and "ham". But if your target was the probability of a particular word, then the number of unique classes is 12; the set of unique words.

	Assume the question is asking for the probability of a word in a spam message being "secret" NOT the probability that a spam message contains the word secret.

		k = 1
		vocab = 12

	Messages
		P(Spam) = 
		= three spam messages + k / eight total messages + k*2 (two kinds of messages)
		= 3 + 1 / 8 + 2
		= 4 / 10

		P(Ham) = 1-P(Spam) = 6 / 10

	Words are a little different. You still go back to 
		
		target_outcomes/total_outcomes
	
	But you also add the class normalizer k. In this case, you look at the occurances of a specific word in spam + k, and divide that by occurances of all words in spam and add in every unique kind of word in the whole dataset.

		Number of unique words = 12

		P("today"|Spam)
		= occurances of "today" in spam + k / all words in spam + unique words
		= (spam.count("today") + 1) / (len(spam) + 12)
		= 0.0476

		P("today"|Ham) 
		= (ham.count("today") + 1) / (len(ham) + 12)
		= 3 / 27

	Twelve different words, twelve classes.

	Okay, even harder one. Given M = "today is secret", and k = 1, what is P(spam|M)?

	Well, it should be multiplication, similar to ML with multiple inputs and adding the Laplace value at every step
		
		P("today"|Spam) 	= (spam.count("today")*1.0 + 1) / (len(spam) + 12)
		P("is"|Spam) 		= (spam.count("is")*1.0 + 1) / (len(spam) + 12)
		P("secret"|Spam) 	= (spam.count("secret")*1.0 + 1) / (len(spam) + 12) 
		P(Spam) = total spam messages + 1 / total messages + 2 = 0.4

		p1 	= P("today"|Spam) * P("is"|Spam) * P("secret"|Spam) * P(Spam)
			= 0.0476 * 0.095 * 0.190 * 0.4
			= 0.000345

		p2 	= P("today"|Ham) + P("is"|Ham) * P("secret"|Ham) * P(Ham)
			= 	((ham.count("today")*1.0 + 1.0) / (len(ham) + 12.0)) * ((ham.count("is")*1.0 + 1.0) / (len(ham) + 12.0)) * ((ham.count("secret")*1.0 + 1.0) / (len(ham) + 12.0)) 
				* 0.6
			= 0.000365

		p1 / (p1 + p2) = 0.4857

	3.	Digit recognition

		Input vector (x1, x2, x_n) could be pixels. But absolute pixel methods are not robust - what if the marking is slightly shifted? Another kind of smoothing helps solve this problem; you look at the local neighborhood of pixels.

	4.	Overfitting prevention

		How do you come up with k, anyway? Cross validation is common. This is where you throw some percent of the training data into a crossvalidation set and test set. Train with the to find all your parameters and use various values for k. Then use the CV set to see how well each k does (maximize the utility of k). Then use test to verify the performance of the chosen k.

###	Regression

Dealing with contineous quantities. Like predicting the temperature.

1. 	Definitions
	
	Loss factor = residual error, essentially. Also known as quadratic loss

		sum(trainingdata) * (y_j - prediction)^2

2.	Minimizing loss

	For f(x) = w1*x+w0, you can minimize (find the w values) with these equasions

		M = number of training examples	
		x = the x set
		y = the y set
		xl = [q**2 for q in x]
		xy = sum([a * b for a, b in zip(x,y)]) #x1*y1 + x2*y2 + ...x_n*y_n

		w1 = (M * sum(xy) - sum(x)*sum(y)) / (M * sum(xl)) - (sum(x)**2))

		w0 = (1/M) * sum(y) - (w1/M)*sum(x)
		

	So for example
	
		x = [3, 6, 4, 5]
		y = [0, -3, -1, -2]

		w1 	= ((4 * -32) - (18 * -6)) / ((4 * 86) - 324)
			= -1
		
		w0 	= (1/4) * -6 - (-1 / 4) * 18
			= 3.0
#	Logic

##	Propositional Logic

1.	Based entirely on the truth tables

	P and Q are statements that can be false or true.

		!P is true when P is false
		P || Q is true as long as either P or Q is true
		P && Q is true only when both P and Q are true
		P => Q is false only when P is true and Q is false
		P <=> Q is true when P and Q have the same value (both are true or both are false)

2.	Terminology

	Valid: The statement is true in every possible situation (P, Q, ...n combinations of true or false)
	Satisfiable: True in some universe, but not always true
	Unsatisfiable: Always false, opposite of valid

	So the statement

		P || !P

	Is always true, for whatever value of P. P is either true or not true.

		P && !P

	Has to always be false by the same logic. P cannot be simultaneously true AND false. Now a tougher one

		P || Q || (Q <=> P)

	Break it down. The first half (P || Q) is false ONLY if both are false. Q <=> P is true if they are both false. The inclusive OR between the statements means this whole statement is always true. 

		(P => Q) || (Q => P)

	Makes no sense in English, but in prop logic this statement is always true. The first bit (P => Q) is only false if P is true and Q is false. The second statement is only false if P is false and Q is true. Run the table

		P 	Q 	P=>Q 	Q=>P
		T 	T 	T 	 	T
		T 	F 	F 	 	T
		F 	T 	T 	 	F
		F 	F 	T 	 	T

	Throw an || statement between them and there is no F-F available. Now try three variables

		((F => P) || (D => P)) => ((F && D) => P)

	Break it down again. This combined statement is only false when the first half is true and the second half is false. Lets do the second bit first. Here are the truth tables for every possible F, P, D

		A = F && D 	= [T, T, F, F, F, F, F, F]
		A => D 		= [T, F, T, T, T, T, T, T]

	So only when F and D are true and P is false is the second half false. Given that we only really care about the situation where the first half ((F => P) || (D => P)) is true and the other half ((F && D) => P) is false, lets look at that specific instance in the first half.

		F = True
		D = True
		P = False

		F => P || D => P 

	Well that is false. Whole statement is valid now. Doesn't really matter what the rest of the first half comes out to, the whole thing will always be true unless the first half is true and the second half is false.
		

##	First-Order Logic

1.	How's it work?

	Complex objects, not simple boolean states. Values are called constants, and they can refer to objects. There are also functions. Functions are mappings from objects to objects. 

	There are also relations, which are more or less exactly what you think they are.

	The other significant part is the inclusion of quantifiers. ForAll is an upsidedown A and ThereExists which is an backwards E.

2.	The power

	Otherwise complex or unbounded statements can be created with first order logic. If you wanted to say there was no dirt in the vacuum world, it is a one-liner

		ForAll(d, l) Dirt(d) && Loc(l) => !At(d, l)

	Which roughly translates into "for all variables d and l, if d is dirt and l is a location, there is no d at l". 

	If you want to say the vacuum is in a location with dirt

		ThereExists(l, d), Dirt(d) && Loc(l) && At(V,l) && At(d,l)

	Or, "for some l and d, d is dirt and l is some location and the vacuum is at l and the d is at l".

3.	Examples

		ThereExists(x, y) x=y

	This is always true. Remember that x and y are variables. They might reference the same object. Since they can, and you are asking the question "for all objects", it's always true.

		(ThereExists(x), x=x) => (ForAll(y), ThereExists(z), y=z)

	First bit is always true. If x can mean anything, it can always be itself. Second bit is also always true. ForAll(y) means for every possible value of y. ThereExists(z) means all possible values z could be. The variable z could always be referencing whatever y is referencing.

		ForAll(x), P(x) || !P(x)

	Everything either has to be in the relation of P or not.
	
		ThereExists(x), P(x)

	This isn't necessarily true. There are empty relations, so it is possible that there are no objects x can reference that is a member of P.

4.	English motherf...etc

	A lot of this stuff can be represented in english incorrectly. Here are some examples

		"Sam has two jobs."

		ThereExists(x,y), Job(Sam, x) && Job(Sam, y) && !(x=y)

	Breaking this down. For some x and y, the relation Job includes Sam and x in addition to Sam and y. And x and y are not the same. That seems to work.

	How about set membership? Consider both these statements together.

	ForAll(x,s) Member(x, Add(x,s)) 
	ForAll(x,s) Member(x,s) => (ForAll(y), Member(x, Add(y,s)))

	This doesn't work. It tells you what IS a member of x, but it doesn't tell you what x is not a member of.

	Now checkers. Define adjacency.

	ForAll(x,y) Adj(Sq(x,y)), Sq(+ (x , 1)) && Adj(Sq(x,y), Sq(x, +(y,1)))

	This doesn't work either. It does squares that are above and to the right, but it doesn't define what isn't adjacent to x and y or squares below and to the left. 

	Lesson here? For more complex statements and rules, you are more likely to see the biconditional <=>, as it eliminates the inclusive nature of implications in one direction.