def product(a,b): 
	return a*b

def bayes(positive, negative):
	def P(P1, P2): 
		return P1 / (P1 + P2)
	
	def product(a,b): 
		return a*b
	p1 = reduce(product, positive)
	p2 = reduce(product, negative)
	print p1, p2
	return P(p1, p2)

def laplace(query, target, other, k):
	num_msg = (len(target)*1.0) + (len(other)*1.0)
	p_target = (len(target)+k*1.0) / ((num_msg) + k*2)
	p_other = (len(other)+k*1.0) / ((num_msg) + k*2)
	print p_target, p_other

	t = " ".join(target).split(" ")
	o = " ".join(other).split(" ")
	unique = len(set(t + o))
	print("dictionary: " + str(unique))
	query = query.split(" ")

	def lp(word, category, unique, k, name="category"):
		"""occurances of word in category + k / all words in catagory + unique words
		"""
		p1 = category.count(word) + k
		p2 = len(category) + unique
		print(word + " in "+name+": " + str((p1 * 1.0) / (p2 * 1.0)))
		return (p1 * 1.0) / (p2 * 1.0)
	
	q_in_target = reduce(product, [lp(x, t, unique, k, "target") for x in query])
	q_in_other = reduce(product, [lp(x, o, unique, k, "other") for x in query])
	print((q_in_target*p_target) / (q_in_other*p_other+q_in_target*p_target))

def mean(values):
	return (sum(values) * 1.0) / (len(values) * 1.0)

def variance_sq(values):
	return (sum([(x-mean(values))**2 for x in values]) * 1.0) / (len(values) * 1.0)

def maxlikelihood(spam, ham, email):

	spam = " ".join(spam).split(" ")
	ham = " ".join(ham).split(" ")

	p_s = len(spam)/(len(ham+spam)*1.0)
	print "total chance of spam: " + str(p_s)

	p_h = len(ham)/(len(ham+spam)*1.0)
	print "total chance of ham: " + str(p_h)

	def d(word, words): 
		return words.count(x)/(1.0*len(words))
	
	p = [d(x, spam) for x in email.split(" ")]
	p.append(p_s)
	n = [d(x, ham) for x in email.split(" ")]
	n.append(p_h)
	
	print "P1 = " + str(p)
	print "P2 = " + str(n)

	print "result: " + str(bayes(p, n))

def qloss(xs, ys):
	M = len(xs)
	xl = [q**2 for q in xs]
	xy = sum([a * b for a, b in zip(xs,ys)]) #x1*y1 + x2*y2 + ...x_n*y_n

	w1 = ((M * xy - sum(xs)*sum(ys))*1.0) / (((M * sum(xl)) - (sum(xs)**2))*1.0)
	w0 = ((1.0/M) * sum(ys)) - (((w1*1.0)/M)*sum(xs))
	print("w0 = " + str(w0) + " w1 = " + str(w1))
	return w1, w0

spam = ["offer is secret", "click secret link", "secret sports link"]
ham = [
	"play sports today",
	"went play sports",
	"secret sports event",
	"sports is today",
	"sports costs money"
]
email = "today is secret"



# movie = ["a perfect world", "my perfect woman", "pretty woman"]
# song = ["a perfect day", "electric storm", "another rainy day"]
# query = "perfect storm"
# print laplace(query, movie, song, 1)
#print lspamham(movie, 3, song, 3, "perfect" , 1)
#print lspamham(movie, 3, song, 3, "storm" , 1)


