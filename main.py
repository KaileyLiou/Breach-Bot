#Breach Bot Starter Code
breachYear = 2017

#Greets user
print("Hello! I'm Breach Bot. I'm a chatbot that will tell you about a data breach. A data breach is when information has been stolen. Unfortunately, it happens pretty frequently.")
userName = input("What is your name?\n")
print("Nice to meet you, " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the National Health Services Data Breach.")

#Introduces breach
print("Would you like to learn about the National Health Services 2017 Data Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("A ransomware attack using WannaCry encrypted hospital systems across the UK, disrupting healthcare operations but not stealing data. It spread globally through an unpatched Windows vulnerability and affected over 45,000 computers in 74 countries.")
  
  elif topic.lower() == "b":
    print("After the data breach, the NHS acted quickly to manage the incident and coordinated with affected organizations, leading to the cancellation of some non-urgent procedures. Although no specific user guidance was mentioned, general best practices for ransomware situations—including applying security patches and avoiding paying ransoms—were applicable.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("The CIA Triad are the three pillars of Cybersecurity: confidentiality, integrity, and availability. This data breach connects to the availability pillar of the CIA Triad because it disrupted access to essential healthcare systems. Though no data was stolen or changed, hospitals couldn't access important medical records, which interfered with patient care.")
  
  elif topic.lower() == "b":
    print("I agree with the organization's response because they were able to quickly identify the ransomware and were transparent about the situation. They assured the public that their information had not been leaked and maintained efficient communication throughout the incident.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by explaining the risks of ignoring the breach and stress the importance of protecting their personal data. My advice would be to immediately change passwords associated with that hospital account and follow updates from the hospital or NHS.")

  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation
print("\nWould you like to hear some advice on how to better protect yourself?")
giveInfo = input("Type 'yes' or 'no'\n")

if giveInfo.lower() == "yes":
  print("You can check to see if your email has been involved in a data breach! Visit https://haveibeenpwned.com/ to see if your email has been compromised in any data breaches. It's a good way to stay informed and take action if necessary.")
  input("Press enter to continue\n")
  print("If your account was involved in a data breach, you should change your password immediately. Use a strong, unique password for each of your accounts to enhance security. Consider using a password manager to help keep track of them.")
  input("Press enter to continue\n")

print("Thanks for chatting with me, and I hope you learned something new!")