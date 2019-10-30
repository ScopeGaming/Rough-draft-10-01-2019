from tkinter import *

x = 0
HEIGHT=500
WIDTH=600

def optiontrue():

	global x

	x += 1

def instructions():

	instructions = Tk()

	def next1():

		instructions.destroy()	
		Question1()

	topFrame = Frame(instructions)
	topFrame.pack()
	bottomFrame = Frame(instructions)
	bottomFrame.pack()

	Question = Label(topFrame, text="Morilaty Quiz.")
	Question.pack()

	Question2 = Label(topFrame, text="Created by Aiden S.")
	Question2.pack()

	Question3 = Label(topFrame, text="Hi and welcome to my game. It is a test so you will have 10 aituations and you will have 2 choices. At the end you will get a score on how moral you choices are.")
	Question3.pack()


	Choice1 = Button(bottomFrame, text="next", padx=50, bg="black", fg="white", command=next1)
	Choice1.grid(column=3, row=4)

	instructions.mainloop()

def Question1():

	global HEIGHT
	global WIDTH

	questiontxt = ("You are at your sisters wedding an hour before the ceremony is to start. Earlier that day, you came across definitive proof that your sisters husband-to-be is having an affair with the best man")
	questiontxt2 = ("and you catch them sneaking out of a room together looking disheveled. If you tell your sister about the affair, her day will be ruined, but you don't want your sister to marry a cheater.")
	questiontxt3 = ("What do you do?")
	option1txt = ("Tell you Sister and ruin the weding?")
	option2txt = ("Let the wedding continue?")

	question1root = Tk()

	def Option1():

		optiontrue()
		question1root.destroy()
		Question2test()

	def Option2():

		question1root.destroy()
		Question2test()

	topFrame = Frame(question1root)
	topFrame.pack()
	bottomFrame = Frame(question1root)
	bottomFrame.pack()

	Question = Label(topFrame, text=questiontxt)
	Question.pack()

	Question2 = Label(topFrame, text=questiontxt2)
	Question2.pack()

	Question3 = Label(topFrame, text=questiontxt3)
	Question3.pack()

	Choice1 = Button(bottomFrame, text=option1txt, padx=50, bg="black", fg="white", command=Option1)
	Choice1.grid(column=3, row=4)

	Choice2 = Button(bottomFrame, text=option2txt, padx=50, bg="black", fg="white", command=Option2)
	Choice2.grid(column=4, row=4)


	question1root.mainloop()

def Question2test():

	global HEIGHT
	global WIDTH

	questiontxt = ("You are an eyewitness to a crime: A man has robbed a bank, but instead of keeping the money for himself, he donates it to a poor orphanage that can now afford to feed, clothe, and care for its children.")
	questiontxt2 = ("You know who committed the crime. If you go to the authorities with the information, there's a good chance the money will be returned to the bank, leaving a lot of kids in need. What do you do?")
	
	option1txt = ("Turn the robber in to the police?")
	option2txt = ("Say nothing because the money wen tot a good cause?")

	question2root = Tk()


	def Option1():

		question2root.destroy()
		Question3()

	def Option2():

		optiontrue()
		question2root.destroy()
		Question3()

	topFrame = Frame(question2root)
	topFrame.pack()
	bottomFrame = Frame(question2root)
	bottomFrame.pack()

	Question = Label(topFrame, text=questiontxt)
	Question.pack()

	Question2 = Label(topFrame, text=questiontxt2)
	Question2.pack()

	Choice1 = Button(bottomFrame, text=option1txt, padx=50, bg="black", fg="white", command=Option1)
	Choice1.pack(side=LEFT)

	Choice2 = Button(bottomFrame, text=option2txt, padx=50, bg="black", fg="white", command=Option2)
	Choice2.pack(side=RIGHT)


	question2root.mainloop()

def Question3():

	global HEIGHT
	global WIDTH

	questiontxt = ("You have a job as network administrator for a company that also employs your best friend's husband. One day, your best friend's husband sends you a message asking you to release an email from quarantine. This requires you to open the email, at which point you discover that it's correspondence between ")
	questiontxt2 = ("this guy and his secret lover. After releasing the email, you find yourself in a pickle. Your instinct is to tell your best friend about his husband's infidelities, but divulging the contents of company emails is against company policy and you could lose your job. Once it becomes plain that your ")
	questiontxt3 = ("best friend found out about his cheating husband through a company email, all trails will inevitably lead to you as the leak. Do you tell him about the indiscretion? Once it becomes plain that your best friend found out about his cheating husband through a company email, all trails will inevitably ")
	questiontxt4 = ("lead to you as the leak. Do you tell him about the indiscretion?")

	option1txt = ("Yes, Your loyalty to your best friend eclipses any company policy.")
	option2txt = ("No, it sucks that your best friend has a cheating husband, but you can not risk losing your job.")

	question3root = Tk()


	def Option1():

		optiontrue()
		question3root.destroy()
		Question4test()

	def Option2():

		question3root.destroy()
		Question4test()

	topFrame = Frame(question3root)
	topFrame.pack()
	bottomFrame = Frame(question3root)
	bottomFrame.pack()

	Question = Label(topFrame, text=questiontxt)
	Question.pack()

	Question2 = Label(topFrame, text=questiontxt2)
	Question2.pack()

	Question3 = Label(topFrame, text=questiontxt3)
	Question3.pack()

	Question4 = Label(topFrame, text=questiontxt3)
	Question4.pack()

	Choice1 = Button(bottomFrame, text=option1txt, padx=50, bg="black", fg="white", command=Option1)
	Choice1.pack(side=LEFT)

	Choice2 = Button(bottomFrame, text=option2txt, padx=50, bg="black", fg="white", command=Option2)
	Choice2.pack(side=RIGHT)


	question3root.mainloop()

def Question4test():

	global HEIGHT
	global WIDTH

	questiontxt = ("You've been on a cruise for two days when there's an accident that forces everyone on board to abandon ship. During the evacuation, one of the boats is damaged, leaving it with a hole that fills it with water. This should keep the boat from sinking long enough for a rescue team to find you as long as it happens within five hours. You're taking your first brake when you notice your best friend in a")
	questiontxt2 = ("sound lifeboat with only nine people in it and he beckons you to swim over and join them so you won't have to keep bailing out water. You figure that with 10 people in the boat, you can keep the boat afloat by having nine people scoop the filling water out by hand for 10 minutes while the 10th person rests. After that person's 10-minute rest, he or she will get back to work while another person rests, ")
	questiontxt3 = ("and so on. If you leave the people in the sinking boat, they will only be able to stay afloat for two hours instead of five, decreasing their chance of being rescued, but securing yours. What do you do?")

	option1txt = ("Stay in your boat and hope that you are all rescued in five hours time, before the boat sinks and you all drown.")
	option2txt = ("Jump ship and join your friend in his boat and hope that the others are rescued within two hours.")

	question4root = Tk()


	def Option1():

		optiontrue()
		question4root.destroy()
		Question5()

	def Option2():

		optiontrue()
		question4root.destroy()
		Question5()

	topFrame = Frame(question4root)
	topFrame.pack()
	bottomFrame = Frame(question4root)
	bottomFrame.pack()

	Question = Label(topFrame, text=questiontxt)
	Question.pack()

	Question2 = Label(topFrame, text=questiontxt2)
	Question2.pack()

	Question3 = Label(topFrame, text=questiontxt3)
	Question3.pack()

	Choice1 = Button(bottomFrame, text=option1txt, padx=50, bg="black", fg="white", command=Option1)
	Choice1.pack(side=LEFT)

	Choice2 = Button(bottomFrame, text=option2txt, padx=50, bg="black", fg="white", command=Option2)
	Choice2.pack(side=RIGHT)


	question4root.mainloop()

def Question5():

	global HEIGHT
	global WIDTH

	questiontxt = ("You're involved in a two-car crash on your way to work one morning in which you accidentally hit and kill a pedestrian. As you get out of the car, you are intercepted by a tearful woman who seems to think that she hit and killed the pedestrian.")
	questiontxt2 = ("You're not sure why she thinks she hit the person, but she is convinced. There's only you, the woman, and the person you hit on the road; there are no witnesses. You know that whoever is deemed responsible will probably be sent to jail. What do you do?")
	
	option1txt = ("Confess your responsibility; you wouldn't be able to live with the guilt of an innocent person being in jail for a crime you committed.")
	option2txt = ("Let the woman take the blame; the thought of being locked away from your life and family is too much to bear.")

	question5root = Tk()


	def Option1():

		optiontrue()
		question5root.destroy()
		Question6()

	def Option2():

		question5root.destroy()
		Question6()

	topFrame = Frame(question5root)
	topFrame.pack()
	bottomFrame = Frame(question5root)
	bottomFrame.pack()

	Question = Label(topFrame, text=questiontxt)
	Question.pack()

	Question2 = Label(topFrame, text=questiontxt2)
	Question2.pack()

	Choice1 = Button(bottomFrame, text=option1txt, padx=50, bg="black", fg="white", command=Option1)
	Choice1.pack(side=LEFT)

	Choice2 = Button(bottomFrame, text=option2txt, padx=50, bg="black", fg="white", command=Option2)
	Choice2.pack(side=RIGHT)


	question5root.mainloop()

def Question6():

	global HEIGHT
	global WIDTH

	questiontxt = ("Your family is vacationing alone on a private stretch of beach with no lifeguard. Your daughter and your niece, both 7, are best friends and eager to get into the water. You caution them to wait until the water calms some, but they defy you and sneak in anyway.")
	questiontxt2 = (" You soon hear screams of distress and find them both caught in a strong current. You are the only swimmer strong enough to save them, but you can only save one at a time. Your niece is a very poor swimmer and likely won't make it much longer. Your daughter is a stronger swimmer,")
	questiontxt3 = 	("but only has a 50 pecent chance of holding on long enough for you to come back for her. Who do you save first?")

	option1txt = ("Save your daughter first; you know that your niece will probably die, but you can't bear to lose your child.")
	option2txt = ("Save your niece first and hope that your daughter can hold on long enough for you to come back for her.")

	question6root = Tk()


	def Option1():

		question6root.destroy()
		Question7()

	def Option2():

		optiontrue()
		question6root.destroy()
		Question7()

	topFrame = Frame(question6root)
	topFrame.pack()
	bottomFrame = Frame(question6root)
	bottomFrame.pack()

	Question = Label(topFrame, text=questiontxt)
	Question.pack()

	Question2 = Label(topFrame, text=questiontxt2)
	Question2.pack()

	Question3 = Label(topFrame, text=questiontxt3)
	Question3.pack()

	Choice1 = Button(bottomFrame, text=option1txt, padx=50, bg="black", fg="white", command=Option1)
	Choice1.pack(side=LEFT)

	Choice2 = Button(bottomFrame, text=option2txt, padx=50, bg="black", fg="white", command=Option2)
	Choice2.pack(side=RIGHT)


	question6root.mainloop()

def Question7():

	global HEIGHT
	global WIDTH

	questiontxt = ("You are an EMT on the scene of a car crash that involves your spouse and the lover you didn't know s/he had. They are both gravely injured, your spouse's injuries the worst of them.")
	questiontxt2 = ("You can tell it's unlikely s/he will pull through. Meanwhile, his/her lover has a neck wound that will prove fatal if pressure isn't applied soon. Whom do you choose to work on?")

	option1txt = ("Work on your spouse; even though s/he cheated and probably won't pull through, your loyalty lies with them.")
	option2txt = ("Work on his/her lover; they can definitely be saved, and even though you may hate them, saving them is your job.")

	question7root = Tk()


	def Option1():

		question7root.destroy()
		Question8()

	def Option2():

		optiontrue()
		question7root.destroy()
		Question8()

	topFrame = Frame(question7root)
	topFrame.pack()
	bottomFrame = Frame(question7root)
	bottomFrame.pack()

	Question = Label(topFrame, text=questiontxt)
	Question.pack()

	Question2 = Label(topFrame, text=questiontxt2)
	Question2.pack()

	Choice1 = Button(bottomFrame, text=option1txt, padx=50, bg="black", fg="white", command=Option1)
	Choice1.pack(side=LEFT)

	Choice2 = Button(bottomFrame, text=option2txt, padx=50, bg="black", fg="white", command=Option2)
	Choice2.pack(side=RIGHT)


	question7root.mainloop()

def Question8():

	global HEIGHT
	global WIDTH

	questiontxt = ("You and your son are prisoners at a concentration camp. You son tried to escape but was recaptured and sentenced to hang at the gallows. To send a message to all others who may try to escape, the guard orders you to pull the chair out from under your son;")
	questiontxt2 = ("if you refuse, the guard will kill your son and another innocent person in the camp. What do you do?")

	option1txt = ("Tearfully pull the chair out from under your son.")
	option2txt = ("Refuse to pull the chair out from under your son, ensuring both his death and the death of another inmate.")

	question8root = Tk()


	def Option1():

		optiontrue()
		question8root.destroy()
		Question9()

	def Option2():

		question8root.destroy()
		Question9()

	topFrame = Frame(question8root)
	topFrame.pack()
	bottomFrame = Frame(question8root)
	bottomFrame.pack()

	Question = Label(topFrame, text=questiontxt)
	Question.pack()

	Question2 = Label(topFrame, text=questiontxt2)
	Question2.pack()

	Choice1 = Button(bottomFrame, text=option1txt, padx=50, bg="black", fg="white", command=Option1)
	Choice1.pack(side=LEFT)

	Choice2 = Button(bottomFrame, text=option2txt, padx=50, bg="black", fg="white", command=Option2)
	Choice2.pack(side=RIGHT)


	question8root.mainloop()

def Question9():

	global HEIGHT
	global WIDTH

	questiontxt = ("You are a doctor at a top hospital. You have six gravely ill patients, five of whom are in urgent need of organ transplants. You can't help them, though, because there are no available organs that can be used to save their lives.")
	questiontxt2 = ("The sixth patient, however, will die without a particular medicine. If s/he dies, you will be able to save the other five patients by using the organs of patient 6, who is an organ donor. What do you do?")

	option1txt = ("Keep patient 6 comfortable, but do not give him the medical care that could save his life in order to save the other five patients.")
	option2txt = ("Save patient 6 and let the other five die; it's unfortunate, but that's not your call to make.")

	question9root = Tk()


	def Option1():

		question9root.destroy()
		Question10()

	def Option2():

		optiontrue()
		question9root.destroy()
		Question10()

	topFrame = Frame(question9root)
	topFrame.pack()
	bottomFrame = Frame(question9root)
	bottomFrame.pack()

	Question = Label(topFrame, text=questiontxt)
	Question.pack()

	Question2 = Label(topFrame, text=questiontxt2)
	Question2.pack()

	Choice1 = Button(bottomFrame, text=option1txt, padx=50, bg="black", fg="white", command=Option1)
	Choice1.pack(side=LEFT)

	Choice2 = Button(bottomFrame, text=option2txt, padx=50, bg="black", fg="white", command=Option2)
	Choice2.pack(side=RIGHT)


	question9root.mainloop()

def Question10():

	global HEIGHT
	global WIDTH

	questiontxt = ("You and your friend are in Mrs.Ogles room and you have a test tomorrow. She leaves to go make a copy and you see the answer key to the test on her desk.")

	option1txt = ("Do you take a photo of it a cheat.")
	option2txt = ("Do you hold up you intregty and not look at it.")

	question10root = Tk()


	def Option1():

		question10root.destroy()		
		answers()

	def Option2():

		optiontrue()
		question10root.destroy()
		answers()

	topFrame = Frame(question10root)
	topFrame.pack()
	bottomFrame = Frame(question10root)
	bottomFrame.pack()

	Question = Label(topFrame, text=questiontxt)
	Question.pack()

	Choice1 = Button(bottomFrame, text=option1txt, padx=50, bg="black", fg="white", command=Option1)
	Choice1.pack(side=LEFT)

	Choice2 = Button(bottomFrame, text=option2txt, padx=50, bg="black", fg="white", command=Option2)
	Choice2.pack(side=RIGHT)


	question10root.mainloop()
     
def answers():
	global x

	answer1 =('You have a well formed conscious.')
	answer2 =('You have a decently formed conscious but you could form it better.')
	answer3 =('You have a terrible formed conscious.')
	answer4 =('You have no conscious whatsoever.')

	answersroot = Tk()

	topFrame = Frame(answersroot)
	topFrame.pack()
	bottomFrame = Frame(answersroot)
	bottomFrame.pack()

	Question1 = Label(topFrame, text=('You got a ' + str(x*10) + '%!') )
	Question1.pack()

	if x in ([10,9,8]):
		Question1 = Label(topFrame, text=answer1)
		Question1.pack()
	if x in ([7,6,5,4]):
		Question2 = Label(topFrame, text=answer2)
		Question2.pack()
	if x in ([3,2,1]):
		Question3 = Label(topFrame, text=answer3)
		Question3.pack()
	if x == 0:
		Question4 = Label(topFrame, text=answer4)
		Question4.pack()


	end = Button(bottomFrame, text="End", padx=50, bg="black", fg="white", command=answersroot.destroy)
	end.pack(side=LEFT)

	answersroot.mainloop()

def Code():

	instructions()

Code()
